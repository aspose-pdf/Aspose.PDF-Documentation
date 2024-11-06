---
title: Eliminar Anotación usando JavaScript
linktitle: Eliminar Anotación
type: docs
weight: 10
url: es/javascript-cpp/delete-annotation/
description: Con Aspose.PDF para JavaScript puedes eliminar anotaciones de tu archivo PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Puedes eliminar anotaciones de un archivo PDF usando Aspose.PDF para JavaScript a través de C++. Puedes obtener el resultado directamente en tu navegador.

1. Crea un 'FileReader'.
1. Se ejecuta la función [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteannotations/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPdfDeleteAnnotations.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces tu DownloadFile recibe el nombre que especificaste anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.

1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

    var ffilePdfDeleteAnnotations = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Eliminar anotaciones de un archivo PDF y guardar el "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfDeleteAnnotations(event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf");
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
    AsposePDFWebWorker.onerror = evt => console.log(`Error desde Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffilePdfDeleteAnnotations = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Eliminar anotaciones de un archivo PDF y guardar el "ResultPdfDeleteAnnotations.pdf" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAnnotations', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf"] }, [event.target.result]);
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