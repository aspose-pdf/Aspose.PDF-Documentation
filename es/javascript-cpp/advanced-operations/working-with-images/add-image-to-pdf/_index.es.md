---
title: Agregar Imagen a PDF usando JavaScript a través de C++
linktitle: Agregar Imagen
type: docs
weight: 10
url: /javascript-cpp/add-image-to-pdf/
description: Esta sección describe cómo agregar una imagen a un archivo PDF existente usando Aspose.PDF para JavaScript a través de C++.
lastmod: "2023-12-15"
---

## Agregar Imagen en un Archivo PDF Existente

¿Necesitas adjuntar una imagen a un PDF? ¿Quieres mejorar la legibilidad de tu PDF? Agrega imágenes a tu PDF y tu presentación o currículum se verá más presentable.

Se cree comúnmente que agregar imágenes a archivos PDF requiere una herramienta especial compleja. Sin embargo, con Aspose.PDF para JavaScript puedes añadir rápidamente y fácilmente las imágenes que necesitas a PDF usando JavaScript directamente en tu navegador.

Para agregar una imagen a un archivo PDF existente:

1. Establece el nombre de archivo de imagen predeterminado.
2. Crea un 'FileReader'.
3. Establece el nombre de archivo de imagen.
4. Prepara el archivo de imagen desde BLOB.
5. Se ejecuta la función [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/).

1. Agregue el archivo de imagen al final de un archivo PDF y guarde el "ResultImage.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, habrá un error en su archivo, entonces la información sobre dicho error se contendrá en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

El siguiente fragmento de código muestra cómo agregar la imagen en un documento PDF.

```js

  /*establecer el nombre de archivo de imagen predeterminado*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*establecer el nombre de archivo de imagen*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*preparar(guardar) el archivo de imagen desde BLOB*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

En el siguiente ejemplo, seleccionamos la imagen para manejar:

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*agregar el archivo de imagen al final de un archivo PDF y guardar el "ResultImage.pdf"*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
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
          `Resultado:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '¡imagen preparada!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Establecer el nombre de archivo de imagen por defecto: 'Aspose.jpg' ya cargado, ver configuraciones en 'settings.json'*/
    var fileImage = "Aspose.jpg";

    /*Manejador de eventos*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Agregar imagen al final de un archivo PDF y guardar el "ResultImage.pdf" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Establecer el nombre del archivo de imagen*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Guardar el BLOB en el FS de Memoria para su procesamiento*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
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