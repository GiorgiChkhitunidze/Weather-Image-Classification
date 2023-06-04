let fileInput = document.getElementById("file");
let imageContainer = document.getElementById("images");
let numOfFiles = document.getElementById("num-of-files");
let predictButton = document.getElementById("L2");
let mainContainer = document.getElementById('container');

function preview(){
    imageContainer.innerHTML = "";
    numOfFiles.textContent = ``;
    numOfFiles.style.margin = '0';
    predictButton.style.display = 'block';
    mainContainer.style.top = '10%';

    let reader = new FileReader();
    let figure = document.createElement("figure");
    let figCap = document.createElement("figcaption");
    figure.appendChild(figCap);
    reader.onload=()=>{
        let img = document.createElement("img");
        img.setAttribute("src",reader.result);
        figure.insertBefore(img,figCap);
    }
    imageContainer.appendChild(figure);
    reader.readAsDataURL(fileInput.files[0]);
}