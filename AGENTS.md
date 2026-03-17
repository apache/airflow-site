<!-- SPDX-License-Identifier: Apache-2.0
      https://www.apache.org/licenses/LICENSE-2.0 -->

# AGENTS instructions

## Environment Setup

- Install prek: `uv tool install prek`
- Enable commit hooks: `prek install`

## Commands

- **Run static checks:** `prek run --from-ref <target_branch> --stage pre-commit`
- **Run manual (slower) checks:** `prek run --from-ref <target_branch> --stage manual`
- **Run all checks on all files:** `prek run --all-files`
- **Build the site:** `./site.sh build-site`
- **Prepare theme:** `./site.sh prepare-theme`
- **Install node dependencies:** `./site.sh install-node-deps`

## Repository Structure

- `landing-pages/` — Hugo-based landing pages (HTML, SCSS, JS)
  - `site/themes/docsy/` — Docsy theme (npm dependencies)
- `sphinx_airflow_theme/` — Sphinx theme package for Airflow documentation
  - `demo/` — theme demo site
- `.github/workflows/` — CI workflows (build, dependabot)
- `site.sh` — main build script for the website
- `license-templates/` — Apache License templates for prek hooks

## Coding Standards

- Apache License header on all new files (prek enforces this).

## Commits and PRs

Write commit messages focused on user impact, not implementation details.

- NEVER add Co-Authored-By with yourself as co-author of the commit. Agents cannot be authors, humans can be, Agents are assistants.

### Creating Pull Requests

**Always push to the user's fork**, not to the upstream `apache/airflow-site` repo. Never push
directly to `main`.

Before pushing, determine the fork remote. Check `git remote -v` — if `origin` does **not**
point to `apache/airflow-site`, use `origin` (it's the user's fork). If `origin` points to
`apache/airflow-site`, look for another remote that points to the user's fork. If no fork remote
exists, create one:

```bash
gh repo fork apache/airflow-site --remote --remote-name fork
```

Before pushing, perform a self-review of your changes:

1. Review the full diff (`git diff main...HEAD`) and verify every change is intentional and
   related to the task — remove any unrelated changes.
2. Run static checks (`prek run --from-ref <target_branch> --stage pre-commit`) and fix any failures.
3. Check for security issues — no secrets, no injection vulnerabilities, no unsafe patterns.

Before pushing, always rebase your branch onto the latest target branch (usually `main`)
to avoid merge conflicts and ensure CI runs against up-to-date code:

```bash
git fetch <upstream-remote> <target_branch>
git rebase <upstream-remote>/<target_branch>
```

If there are conflicts, resolve them and continue the rebase. If the rebase is too complex,
ask the user for guidance.

Then push the branch to the fork remote and open the PR:

```bash
git push -u <fork-remote> <branch-name>
gh pr create --web --title "Short title (under 70 chars)" --body "$(cat <<'EOF'
Brief description of the changes.

closes: #ISSUE  (if applicable)

---

##### Was generative AI tooling used to co-author this PR?

- [X] Yes — <Agent Name and Version>

Generated-by: <Agent Name and Version>

EOF
)"
```

Remind the user to:

1. Review the PR title — keep it short (under 70 chars) and focused on user impact.
2. Add a brief description of the changes at the top of the body.
3. Reference related issues when applicable (`closes: #ISSUE` or `related: #ISSUE`).

## Boundaries

- **Ask first**
  - Large refactors.
  - New dependencies with broad impact.
- **Never**
  - Commit secrets, credentials, or tokens.
  - Edit generated files by hand when a generation workflow exists.
  - Use destructive git operations unless explicitly requested.
