---
title: Eliminar páginas de PDF con JavaScript a través de C++
linktitle: Eliminar páginas de PDF
type: docs
weight: 30
url: /es/javascript-cpp/delete-pages/
description: Puede eliminar páginas de su archivo PDF usando Aspose.PDF para JavaScript a través de C++.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Puede eliminar páginas de un archivo PDF usando Aspose.PDF para JavaScript a través de C++. Puede obtener el resultado directamente en su navegador.

1. Crear un 'FileReader'.
1. Especificar números de página para eliminar.
1. Se ejecuta la función [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultDeletePages.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, habrá un error en su archivo, entonces la información sobre dicho error se contendrá en el archivo 'json.errorText'.

1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*cadena, incluye número de páginas con intervalo: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*array, array de números de páginas*/
      /*const numPages = [1,3];*/
      /*número, número de página*/
      /*const numPages = 1;*/
      /*elimina las páginas 1-3 de un archivo PDF y guarda el "ResultOptimize.pdf"*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
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
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*cadena, incluir número de páginas con intervalo: "7, 20, 22, 30-32, 33, 36-40, 46"*/
        const numPages = "1-3";
        /*array, array de números de páginas*/
        /*const numPages = [1,3];*/
        /*número, número de página*/
        /*const numPages = 1;*/
        /*Eliminar páginas de un archivo PDF y guardar como "ResultDeletePages.pdf - Ask Web Worker"*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Crear un enlace para descargar el archivo resultado*/
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