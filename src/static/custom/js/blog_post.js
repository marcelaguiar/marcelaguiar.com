let pageRoot = document.body;
let postShareRoot = document.getElementById("post-share-root");
let postShareModal = document.getElementById("post-share-modal");

pageRoot.addEventListener('click', closeShareModal);
postShareRoot.addEventListener('click', modalClick);

let copyButton = document.getElementById("share-copy-button");
let copyConfirmation = document.getElementById("copy-confirmation");
let copyContainer = document.getElementById("copy-container");

let timeoutId = 0;

function closeShareModal() {
    postShareModal.classList.remove("post-share-modal-active");
    postShareModal.classList.remove("border");
    clearTimeout(timeoutId);
}

function openShareModal() {
    switchToCopyButton();
    postShareModal.classList.add("border");
    postShareModal.classList.add("post-share-modal-active");
}

function modalClick(e) {
    e.preventDefault();
    e.stopPropagation();
    e.stopImmediatePropagation();
    return false;
}

function copyURL() {
    // Copy to clipboard
    const copyText = document.getElementById("post-url").value;

    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText);

    // Success message
    toggleCopy();
    timeoutId = setTimeout(function() { toggleCopy(); }, 3000);
}

function toggleCopy() {
    if(copyButton.style.display == "none") {
        switchToCopyButton();
    }
    else {
        switchToCopySuccessIcon();
    }    
}

function switchToCopyButton() {
    copyConfirmation.style.display = "none";
    copyContainer.classList.remove("justify-center");
    copyContainer.classList.add("justify-end");
    copyButton.style.display = "block";
}

function switchToCopySuccessIcon() {
    copyButton.style.display = "none";
    copyContainer.classList.remove("justify-end");
    copyContainer.classList.add("justify-center");
    copyConfirmation.style.display = "block";
}