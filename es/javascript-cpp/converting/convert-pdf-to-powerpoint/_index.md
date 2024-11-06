---
title: Convertir PDF a PPTX en JavaScript
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: es/javascript-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-01"
description: Aspose.PDF le permite convertir PDF a formato PPTX usando JavaScript directamente en la web.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La operación de conversión depende del número de páginas en el documento y puede ser muy lenta. Por lo tanto, recomendamos encarecidamente usar Web Workers.

Este código demuestra una forma de descargar tareas de conversión de archivos PDF que consumen muchos recursos a un trabajador web para evitar bloquear el subproceso principal de la interfaz de usuario. También ofrece una forma fácil de usar para descargar el archivo convertido.

{{% alert color="success" %}}
**Intente convertir PDF a PowerPoint en línea**

Aspose.PDF para JavaScript le presenta la aplicación gratuita en línea ["PDF a PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puede intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Convertir PDF a PPTX

```js

  /*Crear Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Error desde Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '¡cargado!' :
      (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

  /*Manejador de eventos*/
  const ffileToPptX = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Convertir un archivo PDF a PptX y guardar como "ResultPDFtoPptX.pptx" - Solicitar a Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToPptX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx"] }, [event.target.result]);
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


El siguiente fragmento de código JavaScript muestra un ejemplo simple de conversión de archivos PDF a PPTX:

1. Seleccione un archivo PDF para convertir.
1. Cree un 'FileReader'.
1. Se ejecuta la función [AsposePdfToPptX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftopptx/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPDFtoPptX.pptx".
1. A continuación, si el 'json.errorCode' es 0, entonces su archivo de resultado recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

```js

  var ffileToPptX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Convertir un archivo PDF a PptX y guardar como "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfToPptX(event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Crear un enlace para descargar el archivo resultante*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```