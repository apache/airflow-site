export const showAllCommiters = (initialChildrenCount) => {
    const container = window.document.getElementById("commiters-container");
    const button = window.document.getElementById("show-all-commiters");

    if (container.childElementCount <= initialChildrenCount) return;

    button.style.display = "block";
    const hiddenChildren = Array.from(container.children)
        .slice(initialChildrenCount, container.childElementCount)
        .map(child => {
            child.style.display = "none";
            return child;
        });

    button.addEventListener("click", () => {
        hiddenChildren.forEach(child => child.style.display = "flex");
        button.style.display = "none";
    });
};
