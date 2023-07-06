const active_button = document.querySelector("#download")
active_button.addEventListener("click", () =>{

    const content = document.querySelector("#content");

    const options = {
        margin:[ 10, 10, 10, 10],
        filename: "arquivo.pdf",
        html2canvas: {scale: 2},
        jsPDF:{unit: "mm", format: "portrait"}
    };

html2pdf().from(content).set(options).save();
})
