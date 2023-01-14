const selectTrigger = document.getElementById("selectTrigger");

selectTrigger.addEventListener("click", async function () {

    const result = await eel.getImages('select')();
    
    if (result.error !== undefined) {
        console.error(result.error.message);
        return
    }

    loadImages(result.images);

});

const folderTrigger = document.getElementById("folderTrigger");

folderTrigger.addEventListener("click", async function () {

    const result = await eel.getImages("folder")();

    if (result.error !== undefined) {
        console.error(result.error.message);
        return
    }

    loadImages(result.images);

});

const clearImages = () => {
    const images = document.querySelectorAll(".imageContainer");
    for(const image of images){
        image.remove();
    }
};

const loadImages = images => {

    const imgArea = document.getElementById("images");
    const documentFragment = document.createDocumentFragment();

    console.log()

    images.source.forEach((image, index) => {
        let container = document.createElement("div");
        container.classList.add("imageContainer");
        let card = document.createElement("div");
        card.classList.add("card", "flex");
        let img = document.createElement("img");
        img.src = "./_temp/" + image;
        card.appendChild(img);
        container.appendChild(card);
        console.log(container);
        documentFragment.appendChild(container);
    });

    clearImages();
    imgArea.appendChild(documentFragment);

};

eel.expose(getResult);