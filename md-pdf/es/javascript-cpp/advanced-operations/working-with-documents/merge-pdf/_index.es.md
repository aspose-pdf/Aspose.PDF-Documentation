---
title: Cómo Fusionar PDF usando JavaScript a través de C++
linktitle: Fusionar archivos PDF
type: docs
weight: 20
url: /javascript-cpp/merge-pdf/
description: Esta página explica cómo fusionar documentos PDF en un solo archivo PDF con Aspose.PDF para JavaScript a través de C++
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Fusionar o combinar dos PDF en un solo PDF en JavaScript

Combinar y fusionar archivos es una tarea muy popular al trabajar con una gran cantidad de documentos. A veces, al trabajar con documentos e imágenes, cuando se escanean, procesan y organizan, se crean varios archivos. Pero, ¿qué pasa si necesitas almacenar todo en un solo archivo? ¿O no quieres imprimir varios documentos? Concatenar dos archivos PDF con Aspose.PDF para JavaScript a través de C++.

Esta herramienta de JavaScript permite fusionar dos archivos PDF en un solo documento PDF usando Aspose.PDF para JavaScript a través de C++. El ejemplo está escrito en JavaScript.

1. Selecciona archivos PDF para fusionar.
1. Crea un 'FileReader'.

1. Se ejecuta la función [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultMerge.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error se encontrará en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

El siguiente fragmento de código muestra cómo concatenar archivos PDF:

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*solo dos archivos*/
      if (index >= e.target.files.length || index >= 2) {
        /*fusionar dos archivos PDF y guardar el "ResultMerge.pdf"*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*crear un enlace para descargar el archivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*preparar(guardar) archivo desde BLOB*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```


### Usando Web Workers

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error desde Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'cargado!' :
        (evt.data.json.errorCode == 0) ? 
          `Resultado:\n${(evt.data.operation == 'AsposePdfPrepare') ? 
                      fileProcess('AsposePdfMerge2Files', evt.data.json.optdata[0].file, {"fileName2": evt.data.json.fileNameResult}) ?? 'espere por favor...' : 
                      DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0]) /*AsposePdfMerge2Files*/
                    }` :
          `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos. Solo se fusionan dos archivos. Si solo se selecciona un archivo, entonces úselo. Para el segundo archivo, necesita realizar AsposePdfPrepare */
    const ffileMerge = evt => fileProcess('AsposePdfPrepare',  evt.target.files[(evt.target.files.length == 1) ? 0 : 1],
                                          [{"operation": 'AsposePdfMerge2Files', "file": evt.target.files[0]}])
    /* Preguntar a Web Worker */
    const fileProcess = (operation, ffile, optdata) => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        if (operation == 'AsposePdfPrepare')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, "params": [event.target.result, ffile.name, optdata] },
                  [event.target.result]
                );
        else if (operation == 'AsposePdfMerge2Files')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, 
                    "params": [event.target.result, undefined, ffile.name, (optdata === undefined) ? ffile.name : optdata.fileName2,
                                `Result${operation}.pdf`] },
                  [event.target.result]
                );
      }
      file_reader.readAsArrayBuffer(ffile);
    }

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