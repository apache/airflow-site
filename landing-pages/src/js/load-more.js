export const loadMore = (containerId, loadButtonId, initialChildrenCount) => {
    const container = window.document.getElementById(containerId);
    const button = window.document.getElementById(loadButtonId);

    const hiddenChildren = Array.from(container.children)
        .slice(initialChildrenCount, container.childElementCount)
        .forEach(child => child.style.display = "none");

    button.addEventListener("click", () => hiddenChildren.forEach(child => child.style.display = "block"))

};
