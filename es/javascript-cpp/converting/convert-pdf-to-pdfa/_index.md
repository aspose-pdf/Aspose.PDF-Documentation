---
title: Convertir PDF a formatos PDF/A 
linktitle: Convertir PDF a formatos PDF/A
type: docs
weight: 100
url: /es/javascript-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-01"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF a un archivo PDF compatible con PDF/A. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para JavaScript** te permite convertir un archivo PDF a un archivo PDF compatible con <abbr title="Formato de Documento Portátil / A">PDF/A</abbr>. 

La operación de conversión depende del número de páginas en el documento y puede consumir mucho tiempo. Por lo tanto, recomendamos encarecidamente usar Web Workers. 

Este código demuestra una manera de descargar tareas de conversión de archivos PDF que consumen muchos recursos a un web worker para evitar bloquear el hilo principal de la interfaz de usuario. También ofrece una forma amigable para el usuario de descargar el archivo convertido.

{{% alert color="success" %}}
**Intenta convertir PDF a PDF/A en línea**

Aspose.PDF para JavaScript te presenta una aplicación en línea gratuita ["PDF a PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a PDF/A con Aplicación Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Convertir PDF a formato PDF/A

```js

  /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}\n${DownloadFile(evt.data.json.fileNameLogResult, "application/xml", evt.data.params[1])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffilePdfConvertToPDFA = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pdfFormat = 'Module.PdfFormat.PDF_A_1A';
        /*convertir un archivo PDF a PDF/A(1A) y guardar el "ResultConvertToPDFA.pdf"*/
        /*durante el proceso de conversión, también se realiza la validación, "ResultConvertToPDFA.xml"- Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToPDFA', "params": [event.target.result, e.target.files[0].name, pdfFormat, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Fragmento de código]

    /*crear un enlace para descargar el archivo de resultado*/
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


El siguiente fragmento de código JavaScript muestra un ejemplo simple de conversión de archivos PDF a PDF/A:

1. Seleccione un archivo PDF para convertir.
1. Cree un 'FileReader'.
1. Se ejecuta la función [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultConvertToPDFA.pdf". Durante el proceso de conversión, también se realiza la validación, "ResultConvertToPDFA.xml".
1. A continuación, si el 'json.errorCode' es 0, entonces su DownloadFile recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre dicho error se encontrará en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante, y un enlace para descargar el archivo de Log (xml) al sistema operativo del usuario.

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convertir un archivo PDF a PDF/A(1A) y guardar "ResultConvertToPDFA.pdf"*/
      /*durante el proceso de conversión, también se realiza la validación, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\nArchivo de Log (formato xml): " + json.fileNameLogResult;
        /*crear un enlace para descargar el archivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\nArchivo de Log (formato xml): " + json.fileNameLogResult;
      /*crear un enlace para descargar el Log (xml)*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```