---
title: Limpiar código JavaScript de un archivo PDF
linktitle: Eliminar JavaScripts
type: docs
weight: 50
url: es/javascript-cpp/delete-javascripts/
description: Limpiar macros de JavaScript de un archivo PDF directamente en la Web con Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Eliminar JavaScript en un archivo PDF puede ser necesario por razones de seguridad y privacidad. El JavaScript en archivos PDF a veces puede ser utilizado de manera maliciosa o para funciones no deseadas. Puedes obtener el resultado directamente en tu navegador.

1. Crear un 'FileReader'.
1. Se ejecuta la función [AsposePdfDeleteJavaScripts](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletejavascripts/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPdfDeleteJavaScripts.pdf".

1. A continuación, si el 'json.errorCode' es 0, entonces tu DownloadFile recibe el nombre que especificaste anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

    var ffilePdfDeleteJavaScripts = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Eliminar JavaScripts de un archivo PDF y guardar el "ResultPdfDeleteJavaScripts.pdf"*/
        const json = AsposePdfDeleteJavaScripts(event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf");
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
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffilePdfDeleteJavaScripts = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Eliminar JavaScripts de un archivo PDF y guardar el "ResultPdfDeleteJavaScripts.pdf" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteJavaScripts', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Crear un enlace para descargar el archivo de resultado*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Haga clic aquí para descargar el archivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
        }
```