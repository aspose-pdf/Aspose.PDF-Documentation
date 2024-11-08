---
title: Optimizar PDF usando Aspose.PDF para JavaScript vía C++
linktitle: Optimizar Archivo PDF
type: docs
weight: 10
url: /es/javascript-cpp/optimize-pdf/
description: Optimizar y comprimir archivos PDF para una visualización web rápida usando la herramienta JavaScript.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimizar Documento PDF

El kit de herramientas de Aspose.PDF para JavaScript vía C++ te permite optimizar el contenido de un PDF para la Web.

La optimización, o linealización para la Web, se refiere al proceso de hacer que un archivo PDF sea adecuado para la navegación en línea usando un navegador web. Para optimizar un archivo para su visualización en la web:

1. Selecciona un archivo PDF para optimizar.
1. Crea un 'FileReader'.
1. Se ejecuta la función [AsposePdfOptimize](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfoptimize/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultOptimize.pdf".

1. A continuación, si el 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error se encontrará en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

El siguiente fragmento de código muestra cómo optimizar un documento PDF.

```js

  var ffileOptimize = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*optimizar un archivo PDF y guardar el "ResultOptimize.pdf"*/
      const json = AsposePdfOptimize(event.target.result, e.target.files[0].name, "ResultOptimize.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*crear un enlace para descargar el archivo resultante*/
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
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffileOptimize = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Optimizar un archivo PDF y guardar el "ResultOptimize.pdf" - Pedir al Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfOptimize', "params": [event.target.result, e.target.files[0].name, "ResultOptimize.pdf"] },
          [event.target.result]
        );
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