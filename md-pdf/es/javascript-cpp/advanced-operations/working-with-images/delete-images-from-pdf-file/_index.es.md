---
title: Eliminar Imágenes del Archivo PDF a través de JavaScript
linktitle: Eliminar Imágenes
type: docs
weight: 20
url: /javascript-cpp/delete-images-from-pdf-file/
description: Esta sección explica cómo eliminar Imágenes del Archivo PDF usando Aspose.PDF para JavaScript.
lastmod: "2022-02-17"
---

Puede eliminar imágenes de un archivo PDF usando Aspose.PDF para JavaScript a través de C++. Puede obtener el resultado directamente en su navegador.

1. Cree un 'FileReader'.
1. Se ejecuta la función [AsposePdfDeleteImages](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteimages/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPdfDeleteImages.pdf".
1. A continuación, si 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre tal error estará contenida en el archivo 'json.errorText'.

1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

    var ffilePdfDeleteImages = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Eliminar imágenes de un archivo PDF y guardar el "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfDeleteImages(event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Crear un enlace para descargar el archivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Usando Web Workers

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error from Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffilePdfDeleteImages = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Eliminar imágenes de un archivo PDF y guardar el "ResultPdfDeleteImages.pdf" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteImages', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Crear un enlace para descargar el archivo resultante*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Haz clic aquí para descargar el archivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
        }
```