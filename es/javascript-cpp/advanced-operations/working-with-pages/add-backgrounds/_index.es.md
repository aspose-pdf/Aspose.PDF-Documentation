---
title: Añadir fondo a PDF con JavaScript a través de C++
linktitle: Añadir fondos
type: docs
weight: 10
url: /javascript-cpp/add-backgrounds/
description: Añade una imagen de fondo a tu archivo PDF con JavaScript a través de C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los siguientes fragmentos de código muestran cómo agregar una imagen de fondo a las páginas de un PDF utilizando la función [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) con JavaScript.

En el siguiente fragmento de código, cargamos la imagen para trabajar con ella en el sistema de archivos interno:

1. Crear un 'FileReader'.
1. Establecer el nombre del archivo de imagen.
1. Preparar el archivo de imagen desde BLOB.

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*establecer el nombre del archivo de imagen*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*preparar(guardar) el archivo de imagen desde BLOB*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


In the next example, we select the PDF file to handle.  
1. Cree un 'FileReader'.  
1. Se ejecuta la función [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/).  
1. Agregue el archivo de imagen al PDF y guarde el "ResultBackgroundImage.pdf".  
1. A continuación, si el 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error se encontrará en el archivo 'json.errorText'.  
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

```js

  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*agregar un archivo de imagen de fondo al PDF y guardar el "ResultBackgroundImage.pdf"*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*crear un enlace para descargar el archivo resultado*/
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
          `Resultado:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '¡imagen preparada!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Establecer el nombre de archivo de imagen predeterminado: 'Aspose.jpg' ya cargado, ver configuraciones en 'settings.json'*/
    var fileBackgroundImage = "Aspose.jpg";

    /*Manejador de eventos*/
    const ffileAddBackgroundImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Agregar imagen de fondo a un archivo PDF y guardar el "ResultBackgroundImage.pdf" - Preguntar a Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddBackgroundImage',
            "params": [event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Establecer el nombre de archivo de imagen*/
      fileBackgroundImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Guardar el BLOB en la memoria FS para su procesamiento*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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