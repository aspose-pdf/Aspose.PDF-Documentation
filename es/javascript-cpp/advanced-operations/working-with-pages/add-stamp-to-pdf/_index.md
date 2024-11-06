---
title: Añadir sellos de imagen en PDF usando JavaScript a través de C++
linktitle: Sellos de imagen en archivo PDF
type: docs
weight: 60
url: es/javascript-cpp/stamping/
description: Añada el sello de imagen a su documento PDF usando la función AsposePdfAddStamp con el kit de herramientas JavaScript.
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir sello de imagen en archivo PDF

Sellar un documento PDF es similar a sellar un documento en papel. Un sello en un archivo PDF proporciona información adicional al archivo PDF, como proteger el archivo PDF para que otros lo usen y confirmar la seguridad del contenido del archivo PDF.
Puede usar la función [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) para añadir un sello de imagen a un archivo PDF usando JavaScript.

Para añadir un sello de imagen:

1. Establezca el nombre de archivo de imagen predeterminado.
1. Cree un 'FileReader'.
1. Establezca el nombre de archivo de imagen.
1. Prepare el archivo de sello desde BLOB.

El siguiente fragmento de código muestra cómo añadir un sello de imagen en el archivo PDF.

```js

  /*establecer el nombre de archivo de sello predeterminado*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*establecer el nombre de archivo de sello*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*preparar(guardar) el archivo de sello desde BLOB*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


1. Crear un 'FileReader'.
1. Se ejecuta la función [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/).
1. Agregar el archivo de imagen al final de un archivo PDF y guardar el "ResultImage.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*insertar el archivo de sello en un archivo PDF y guardar el "ResultImage.pdf"*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
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

    /*Establecer el nombre de archivo de sello predeterminado: 'Aspose.jpg' ya cargado, ver configuraciones en 'settings.json'*/
    var fileStamp = "Aspose.jpg";

    /*Manejador de eventos*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*Agregar sello a un archivo PDF y guardar el "ResultStamp.pdf" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddStamp',
            "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_,
                      setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*Establecer el nombre de archivo del sello*/
      fileStamp = e.target.files[0].name;
      file_reader.onload = event => {
        /*Guardar el BLOB en la memoria FS para su procesamiento*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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