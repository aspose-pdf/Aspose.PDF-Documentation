---
title: Extraer Imágenes de PDF JavaScript
linktitle: Extraer Imágenes de PDF
type: docs
weight: 20
url: /javascript-cpp/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen de un PDF utilizando el kit de herramientas Aspose.PDF para JavaScript.
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El kit de herramientas web de Aspose.PDF te permite extraer fácilmente imágenes de archivos PDF.

En caso de que desees extraer imágenes de un documento PDF, puedes usar la función [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/). 
Por favor, revisa el siguiente fragmento de código para extraer imágenes de un archivo PDF usando JavaScript a través de C++.

1. Crear un 'FileReader'.
1. Se ejecuta la función [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPdfExtractImage{0:D2}.jpg".

1. A continuación, si el 'json.errorCode' es 0, entonces puedes obtener enlaces a los archivos de resultado. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, habrá un error en tu archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*Extraer imagen de un archivo PDF con la plantilla "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guardar*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Cantidad de archivos(imágenes): " + json.filesCount.toString();
        /*Crear enlaces a los archivos de resultado*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Usando Web Workers

```js

  /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ? 
          `Cantidad de archivos(imágenes): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Extraer imagen de un archivo PDF con la plantilla "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guardar*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Crear un enlace para descargar el archivo resultante*/
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