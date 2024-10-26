let selectedFiles = [];
const fileInput = document.getElementById("fileInput");
const imagePreview = document.getElementById("imagePreview");
const uploadSuccess = document.getElementById("uploadSuccess");
const uploadError = document.getElementById("uploadError");
const loadingIndicator = document.getElementById("loading");
const uploadButton = document.getElementById("uploadButton");

fileInput.addEventListener("change", (event) => {
    const files = event.target.files;
    selectedFiles = [];

    // Clear previous images and messages
    imagePreview.innerHTML = "";
    uploadSuccess.style.display = "none";
    uploadError.style.display = "none";

    for (const file of files) {
        selectedFiles.push(file);
        const reader = new FileReader();
        reader.onload = (e) => {
            const imgElement = document.createElement("img");
            imgElement.src = e.target.result;
            imgElement.style.width = "500px";
            imgElement.style.height = "auto";
            imgElement.style.marginTop = "10px";
            imgElement.style.border = "2px solid #ccc";
            imgElement.style.borderRadius = "8px";
            imagePreview.appendChild(imgElement);
        };
        reader.readAsDataURL(file);
    }
});

uploadButton.addEventListener("click", () => {
    if (selectedFiles.length === 0) {
        uploadError.innerText = "Please select at least one image.";
        uploadError.style.display = "block";
        return;
    }

    const formData = new FormData();
    for (const file of selectedFiles) {
        formData.append("images", file);
    }

    loadingIndicator.style.display = "block";

    fetch("http://127.0.0.1:8080/upload", {
        method: "POST",
        body: formData,
    })
    .then((response) => {
        loadingIndicator.style.display = "none";
        if (!response.ok) {
            throw new Error("Upload failed");
        }
        return response.blob();
    })
    .then((blob) => {
        fileInput.value = "";
        selectedFiles = [];
        imagePreview.innerHTML = "";

        const imageUrl = URL.createObjectURL(blob);
        const imgElement = document.createElement("img");
        imgElement.src = imageUrl;
        imgElement.style.width = "1000px";
        imgElement.style.height = "auto";
        imgElement.style.marginTop = "10px";
        imgElement.style.border = "2px solid #ccc";
        imgElement.style.borderRadius = "8px";
        imagePreview.appendChild(imgElement);
        uploadSuccess.style.display = "block";
    })
    .catch((error) => {
        loadingIndicator.style.display = "none";
        uploadError.innerText = "Error uploading images: " + error.message;
        uploadError.style.display = "block";
    });
});
