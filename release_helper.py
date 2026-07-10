import subprocess
import os
import sys
from datetime import date

def run(cmd_list):
    print(f"   -> Running: {' '.join(cmd_list)}", flush=True)
    env = os.environ.copy()
    env["GIT_PAGER"] = "cat"
    env["GIT_TERMINAL_PROMPT"] = "0"
    print(f"   -> Env set, calling subprocess...", flush=True)
    result = subprocess.run(
        ' '.join(cmd_list),
        shell=True,
        capture_output=True,
        text=True,
        env=env,
        timeout=60
    )
    print(f"   -> Subprocess done. Return code: {result.returncode}", flush=True)
    return result.stdout.strip(), result.stderr.strip()

def ask(question):
    print(question, end="", flush=True)
    return sys.stdin.readline().strip().lower()

def main():
    print("Step 1: Starting script...", flush=True)
    
    source_branch = "main"
    target_branch = "staging"
    team_files_path = "team_files.txt"

    print("Step 2: Reading team_files.txt...", flush=True)
    with open(team_files_path) as f:
        team_files = [line.strip() for line in f if line.strip()]
    print(f"Step 2 done: {team_files}", flush=True)

    print("Step 3: Running git diff...", flush=True)
    diff_output, diff_err = run(["git", "diff", target_branch, source_branch, "--name-only"])
    print(f"Step 3 done: {len(diff_output.splitlines())} files differ", flush=True)

    print("Step 4: Checking which team files have differences...", flush=True)
    changed_files = diff_output.splitlines()
    files_to_release = []
    for f in team_files:
        if f in changed_files:
            print(f"Step 4: File has differences: {f}", flush=True)
            answer = ask("   Include in release? (y/n): ")
            if answer == "y":
                files_to_release.append(f)
        else:
            print(f"Step 4: No differences for: {f} - skipping", flush=True)
    print(f"Step 4 done: selected files: {files_to_release}", flush=True)

    if not files_to_release:
        print("No files selected. Exiting.", flush=True)
        return

    print("Step 5: Finding merge base...", flush=True)
    merge_base, err = run(["git", "merge-base", target_branch, source_branch])
    print(f"Step 5 done: merge base = {merge_base}", flush=True)

    print("Step 6: Finding commits for each file...", flush=True)
    commits_to_pick = []
    for f in files_to_release:
        print(f"Step 6: Looking for commits for file: {f}", flush=True)
        log, log_err = run(["git", "log", f"{merge_base}..{source_branch}", "--oneline", "--", f])
        print(f"Step 6 done for {f}: log = {log}", flush=True)
        if not log:
            print("   No commits found for this file.", flush=True)
            continue
        commits = [line.split()[0] for line in log.splitlines()]
        print(f"   Commits found: {commits}", flush=True)
        commits_to_pick.extend(commits)

    if not commits_to_pick:
        print("No commits to cherry-pick. Exiting.", flush=True)
        return

    print("Step 7: Removing duplicate commits...", flush=True)
    seen = set()
    unique_commits = []
    for c in reversed(commits_to_pick):
        if c not in seen:
            seen.add(c)
            unique_commits.append(c)
    print(f"Step 7 done: unique commits = {unique_commits}", flush=True)

    print(f"\nCommits to cherry-pick ({len(unique_commits)} total):", flush=True)
    for c in unique_commits:
        print(f"   {c}", flush=True)

    confirm = ask("\nProceed with cherry-picking? (y/n): ")
    if confirm != "y":
        print("Aborted.", flush=True)
        return

    print("Step 8: Starting cherry-pick...", flush=True)
    success = 0
    failed = 0
    for commit in unique_commits:
        print(f"Step 8: Cherry-picking {commit}...", flush=True)
        out, err = run(["git", "cherry-pick", commit])
        print(f"Step 8: Result - out: {out}, err: {err}", flush=True)
        if "conflict" in err.lower() or "conflict" in out.lower():
            print(f"WARNING: Conflict on {commit}! Resolve manually then press Enter...", flush=True)
            sys.stdin.readline()
            failed += 1
        elif err and "error" in err.lower():
            print(f"ERROR: {err}", flush=True)
            failed += 1
        else:
            print(f"   Done!", flush=True)
            success += 1

    print(f"\n----------------------------------", flush=True)
    print(f"Release branch is ready!", flush=True)
    print(f"Successfully cherry-picked: {success} commits", flush=True)
    if failed > 0:
        print(f"Commits with conflicts: {failed}", flush=True)
    print(f"----------------------------------", flush=True)
    print("\nNext steps:", flush=True)
    print("   1. Review your changes: git diff staging", flush=True)
    print("   2. Push your branch: git push origin release-" + str(date.today()), flush=True)
    print("   3. Open a Pull Request into staging", flush=True)

if __name__ == "__main__":
    main()