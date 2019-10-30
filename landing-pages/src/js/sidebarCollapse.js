const handleClick = (section) => {
  const subsection = section.querySelector(".collapse");
  if (subsection.classList.contains("show")) {
    subsection.classList.remove("show");
    // section.classList.remove("arrow-down");
  } else {
    subsection.classList.add("show");
    // section.classList.add("arrow-down");
  }
};

const handleCollapse = () => {
  const root = window.document.querySelector(".roadmap");
  if (!root) {
    return;
  }

  const arrows = root.querySelectorAll(".td-sidebar-nav > .td-sidebar-nav__section .td-sidebar-nav__section");
  arrows.forEach(section => section.addEventListener("click", () => handleClick(section)));
};

handleCollapse();
