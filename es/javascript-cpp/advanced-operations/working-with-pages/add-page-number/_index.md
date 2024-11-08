---
title: Agregar Número de Página al PDF con JavaScript via C++ 
linktitle: Agregar Número de Página
type: docs
weight: 100
url: /es/javascript-cpp/add-page-number/
description: Aspose.PDF para JavaScript via C++ te permite agregar un Sello de Número de Página a tu archivo PDF usando AsposePdfAddPageNum.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Todos los documentos deben tener números de página en ellos. El número de página facilita al lector localizar diferentes partes del documento.

**Aspose.PDF para JavaScript via C++** te permite agregar números de página con [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/).

1. Crear un 'FileReader'.
1. Se ejecuta la función [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultAddPageNum.pdf".

1. A continuación, si el 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

```js
  var ffileAddPageNum = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*agregar número de página a un archivo PDF y guardar el "ResultAddPageNum.pdf"*/
      const json = AsposePdfAddPageNum(event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf");
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
    const ffileAddPageNum = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Agregar número de página a un archivo PDF y guardar el "ResultAddPageNum.pdf" - Pedir a Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddPageNum', "params": [event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf"] },
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
        link.innerHTML = "Haz clic aquí para descargar el archivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```