// Icons
const sunIcons = document.querySelectorAll(".sun");
const moonIcons = document.querySelectorAll(".moon");
const darkModeButtons = document.querySelectorAll(".dark-mode-button");

const mobileMenuBtn = document.querySelector("button.mobile-menu-button");
const mobileMenu = document.querySelector(".mobile-menu");

// Theme Vars
const userTheme = localStorage.getItem("theme");
const systemTheme = window.matchMedia("(prefers-color-scheme: dark)").matches;

// Icon Toggling
const iconToggle = () => {
    for (let icon of moonIcons) {
        icon.classList.toggle("display-none");
    }
    for (let icon of sunIcons) {
        icon.classList.toggle("display-none");
    }
};

// Initial Theme Check
const themeCheck = () => {
    if(userTheme === "dark" || (!userTheme && systemTheme)) {
        document.documentElement.classList.add("dark");
        for (let icon of moonIcons) {
            icon.classList.add("display-none");
        }
        return;
    }

    for (let icon of sunIcons) {
        icon.classList.add('display-none');
    }
};

// Manual Theme Switch
const themeSwitch = () => {
    if (document.documentElement.classList.contains("dark")) {
        document.documentElement.classList.remove("dark");
        localStorage.setItem("theme", "light");
        iconToggle();
        return;
    }

    document.documentElement.classList.add("dark");
    localStorage.setItem("theme", "dark");
    iconToggle();
};

// call theme switch on clicking buttons
darkModeButtons.forEach(function(button) {
    button.addEventListener("click", () => {
        themeSwitch();
    });
});

// invoke theme check on initial load
themeCheck();

mobileMenuBtn.addEventListener("click", () => {
    let h = mobileMenu.style.maxHeight;
    if(h == "0px") {
        showMobileMenu();
    }
    else {
        hideMobileMenu();
    }
    
});

function hideMobileMenu() {
    mobileMenu.style.maxHeight = "0px";
    mobileMenu.style.borderWidth = "0px";
}

function showMobileMenu() {
    mobileMenu.style.maxHeight = "400px";
    mobileMenu.style.borderWidth = "1px";
}