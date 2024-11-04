---
title: Extraer Texto de PDF usando JavaScript
linktitle: Extraer Texto de PDF
type: docs
weight: 10
url: /javascript-cpp/extract-text/
description: Esta sección describe cómo extraer texto de un documento PDF usando el kit de herramientas de JavaScript.
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Texto de todas las Páginas del Documento PDF

Extraer texto de PDF no es fácil. No muchos lectores de PDF pueden extraer texto de imágenes PDF o PDFs escaneados. Pero la herramienta **Aspose.PDF para JavaScript vía C++** te permite extraer fácilmente texto de cualquier archivo PDF.

Consulta el fragmento de código y sigue los pasos para extraer texto de tu PDF:

1. Selecciona un archivo PDF para extraer texto.
2. Crea un 'FileReader' para leer el texto.
3. Se ejecuta la función [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/).

1. A continuación, si el 'json.errorCode' es 0, entonces el 'json.extractText' contendrá el contenido extraído. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, su archivo tendrá un error, entonces la información sobre dicho error se contendrá en el 'json.errorText'.
1. Como resultado, recibirá una cadena con el texto extraído de su PDF.

```js

    var ffileExtract = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Extraer texto de un archivo PDF*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
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
        (evt.data.json.errorCode == 0) ?
          evt.data.json.extractText :
          `Error: ${evt.data.json.errorText}`; 

    /*Manejador de eventos*/
    const ffileExtract = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Extraer texto de un archivo PDF - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```