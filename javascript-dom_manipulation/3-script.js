document.getElementById("toggle_header").addEventListener("click", function () {
    // document.querySelector("header").classList.add("red")
    const currentClass = document.querySelector("header").className;
    if (currentClass === "red") {
        document.querySelector("header").classList.remove("red");
        document.querySelector("header").classList.add("green");
    }
    else {
        document.querySelector("header").classList.remove("green");
        document.querySelector("header").classList.add("red");
    }
});