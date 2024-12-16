---
title: Convertir PDF a documentos de Word en JavaScript
linktitle: Convertir PDF a Word
type: docs
weight: 10
url: /es/javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: Aprende cómo escribir código JavaScript para convertir PDF a DOC(DOCX) directamente en la Web.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

La operación de conversión depende del número de páginas en el documento y puede ser muy lenta. Por lo tanto, recomendamos encarecidamente usar Web Workers.

Este código demuestra una manera de descargar tareas de conversión de archivos PDF que consumen muchos recursos a un trabajador web para evitar bloquear el hilo principal de la interfaz de usuario. También ofrece una forma fácil de usar para descargar el archivo convertido.

Para editar el contenido de un archivo PDF en Microsoft Word u otros procesadores de texto que soportan los formatos DOC y DOCX. Los archivos PDF son editables, pero los archivos DOC y DOCX son más flexibles y personalizables.

{{% alert color="success" %}}
**Intenta convertir PDF a DOC en línea**

Aspose.PDF para JavaScript te presenta la aplicación gratuita en línea ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Convertir PDF a DOC](/pdf/es/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF a DOC

```js

  /*Crear Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Error desde Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '¡cargado!' :
      (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

  /*Manejador de eventos*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Convertir un archivo PDF a Doc y guardar como "ResultPDFtoDoc.doc" - Pedir a Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
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


El siguiente fragmento de código JavaScript muestra un ejemplo simple de conversión de páginas PDF a archivos DOC:

1. Seleccione un archivo PDF para convertir.
1. Cree un 'FileReader'.
1. Se ejecuta la función [AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPDFtoDoc.doc".
1. A continuación, si el 'json.errorCode' es 0, entonces su archivo resultante recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error se contendrá en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Convertir un archivo PDF a Doc y guardar el "ResultPDFtoDoc.doc"*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Crear un enlace para descargar el archivo resultante*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


{{% alert color="warning" %}}
**Intente convertir PDF a DOCX en línea**

Aspose.PDF para JavaScript te presenta la aplicación en línea gratuita ["PDF a Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), donde puedes probar e investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/es/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Convertir PDF a DOCX

La API Aspose.PDF para JavaScript te permite leer y convertir documentos PDF a DOCX. DOCX es un formato bien conocido para documentos de Microsoft Word cuya estructura cambió de binario simple a una combinación de archivos XML y binarios. Los archivos Docx pueden abrirse con Word 2007 y versiones posteriores, pero no con las versiones anteriores de MS Word que soportan extensiones de archivo DOC.

```js

  /*Crear un Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*convertir un archivo PDF a DocX y guardar como "ResultPDFtoDocX.docx" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Fragmento de código]

    /*crear un enlace para descargar el archivo resultado*/
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


El siguiente fragmento de código JavaScript muestra un ejemplo simple de cómo convertir páginas PDF en archivos DOCX:

1. Seleccionar un archivo PDF para convertir.
1. Crear un 'FileReader'.
1. Se ejecuta la función [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPDFtoDocX.docx".
1. A continuación, si el 'json.errorCode' es 0, entonces su archivo de resultado recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convertir un archivo PDF a DocX y guardar el "ResultPDFtoDocX.docx"*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*crear un enlace para descargar el archivo de resultado*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```