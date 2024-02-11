let pageRoot = document.body;
let postShareRoot = document.getElementById("post-share-root");
let postShareModal = document.getElementById("post-share-modal");

pageRoot.addEventListener('click', rootClick);
postShareRoot.addEventListener('click', modalClick);

function rootClick() {

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

}