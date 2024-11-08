---
title: Extraer Texto de PDF usando JavaScript
linktitle: Extraer texto de PDF
type: docs
weight: 30
url: /es/javascript-cpp/extract-text-from-pdf/
description: Este artículo describe varias formas de extraer texto de documentos PDF usando Aspose.PDF para JavaScript.
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Texto del Documento PDF

Extraer texto del documento PDF es una tarea muy común y útil. 
Extraer texto de PDFs sirve para una variedad de propósitos, desde mejorar la búsqueda y disponibilidad hasta habilitar el análisis y la automatización de datos en diversos campos como los negocios, la investigación y la gestión de información.

En caso de que desee extraer texto de un documento PDF, puede utilizar la función [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/). 
Por favor, consulte el siguiente fragmento de código para extraer texto de un archivo PDF usando JavaScript a través de C++.

1. Crear un 'FileReader'.

1. Se ejecuta la función [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/).
1. A continuación, si el 'json.errorCode' es 0, entonces puedes obtener enlaces a los archivos resultantes. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre dicho error se contendrá en el archivo 'json.errorText'.

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