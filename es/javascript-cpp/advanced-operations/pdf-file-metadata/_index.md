---
title: Trabajando con Metadatos de Archivos PDF usando JavaScript a través de C++
linktitle: Metadatos de Archivos PDF
type: docs
weight: 130
url: es/javascript-cpp/pdf-file-metadata/
description: Esta sección explica cómo obtener información de archivos PDF, cómo obtener metadatos de un archivo PDF, establecer Información de Archivos PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Información de Archivos PDF

1. Crear un 'FileReader'.
1. Se ejecuta la función [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/).
1. Metadatos de PDF que se pueden obtener:
- title - título
- creator - creador
- author - autor
- subject - asunto
- keywords - palabras clave
- creation - fecha de creación
- mod - fecha de modificación
1. A continuación, si el 'json.errorCode' es 0, entonces puedes obtener la lista de Información del archivo PDF. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Obtener información (metadatos) del archivo PDF.*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
      title - título
      creator - creador
      author - autor
      subject - asunto
      keywords - palabras clave
      format - formato PDF
      version - versión PDF
      ispdfa - PDF es PDF/A
      ispdfua - PDF es PDF/UA
      islinearized - PDF es linealizado
      isencrypted - PDF está encriptado
      permission - permiso PDF
      size - tamaño de página PDF
      pagecount - Recuento de páginas
      сreation Date: json.creation
      modify Date:   json.mod
      annotationcount - Recuento de anotaciones
      bookmarkcount - Recuento de marcadores
      attachmentcount - Recuento de adjuntos
      metadatacount - Recuento de metadatos
      javascriptcount - Recuento de JavaScript
      imagecount - Recuento de imágenes
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


### Uso de Web Workers

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ?
          `info:\n${JSON.stringify(evt.data.json, null, 4)}` :
          `Error: ${evt.data.json.errorText}`; 

    /*Manejador de eventos*/
    const ffilePdfGetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Obtener información (metadatos) de un archivo PDF - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetInfo', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Obtener Todas las Fuentes

Obtener fuentes de un archivo PDF puede ser una forma útil de reutilizar fuentes en otros documentos o aplicaciones.
 
En caso de que desees obtener todas las fuentes de un documento PDF, puedes usar [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/). 
Por favor, revisa el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente usando JavaScript a través de C++.

1. Crea un 'FileReader'.
1. Se ejecuta la función [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/).
1. A continuación, si el 'json.errorCode' es 0, entonces puedes obtener la lista de fuentes del archivo PDF. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*obtener lista de fuentes del archivo PDF.*/
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## Usando Web Workers

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error desde el Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ?
          `fuentes:\n${JSON.stringify(evt.data.json.fonts, null, 4)}` :
          `Error: ${evt.data.json.errorText}`; 

    /*Manejador de eventos*/
    const ffilePdfGetAllFonts = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Obtener lista de fuentes de un archivo PDF - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetAllFonts', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```
## Establecer Información del Archivo PDF

Aspose.PDF para JavaScript a través de C++ te permite establecer información específica del archivo para un PDF, como autor, fecha de creación, asunto y título.
 Para configurar esta información:

1. Cree un 'FileReader'.
1. Si no necesita establecer un valor, use undefined o "" (cadena vacía).
1. Se ejecuta la función [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultSetInfo.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error se encontrará en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

```js

    var ffilePdfSetInfo = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Establecer información del PDF: título, creador, autor, tema, palabras clave, creación (fecha), mod (fecha de modificación)*/
        /*Si no necesita establecer un valor, use undefined o "" (cadena vacía)*/
        /*Establecer información (metadatos) en un archivo PDF y guardar el "ResultSetInfo.pdf"*/
        const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "Configuración de Información del Documento PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 11:55 PM", "ResultSetInfo.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Crear un enlace para descargar el archivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

### Usando Web Workers

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffilePdfSetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Información del PDF: título, creador, autor, asunto, palabras clave, creación (fecha), modificación (fecha de modificación)*/
        const title = 'Estableciendo Información del Documento PDF';
        const creator = ''; /*si no es necesario establecer un valor, use: undefined o ""/'' (cadena vacía)*/
        const author = 'Aspose';
        const subject = undefined;
        const keywords = 'Aspose.Pdf, DOM, API';
        const creation = undefined; /*fecha de creación*/
        const mod = '16/02/2023 11:55 PM'; /*fecha de modificación*/
        /*Establecer información (metadatos) en un archivo PDF y guardar el "ResultSetInfo.pdf" - Pedir al Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSetInfo',
            "params": [event.target.result, e.target.files[0].name, title, creator, author, subject, keywords, creation, mod, "ResultSetInfo.pdf"] },
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


## Eliminar Información del Archivo PDF

Aspose.PDF para JavaScript a través de C++ te permite eliminar los metadatos del archivo PDF:

1. Crear un 'FileReader'.
1. Se ejecuta la función [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/javascript-cpp/metadata/asposepdfremovemetadata/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPdfRemoveMetadata.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces tu DownloadFile recibirá el nombre que especificaste anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre dicho error se encontrará en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

    var ffilePdfRemoveMetadata = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Eliminar metadatos de un archivo PDF y guardar el "ResultPdfRemoveMetadata.pdf"*/
        const json = AsposePdfRemoveMetadata(event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Crear un enlace para descargar el archivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### Uso de Web Workers

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffilePdfRemoveMetadata = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Quitar metadatos de un archivo PDF y guardar el "ResultPdfRemoveMetadata.pdf" - Solicitar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRemoveMetadata', "params": [event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Fragmento de código]

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