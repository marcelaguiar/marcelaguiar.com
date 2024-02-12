let pageRoot = document.body;
let postShareRoot = document.getElementById("post-share-root");
let postShareModal = document.getElementById("post-share-modal");

pageRoot.addEventListener('click', closeShareModal);
postShareRoot.addEventListener('click', modalClick);

function closeShareModal() {
    postShareModal.classList.remove("post-share-modal-active");
    postShareModal.classList.remove("border");
}

function openShareModal() {
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


    // Close modal
    closeShareModal();
}