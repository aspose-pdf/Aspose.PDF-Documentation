---
title: Convertir PDF/A a formato PDF 
linktitle: Convertir PDF/A a formato PDF
type: docs
weight: 110
url: /es/javascript-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-01"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF/A a un documento PDF con JavaScript. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF/A a formato PDF

```js

  /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error desde Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffilePdfAConvertToPDF = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*convertir un archivo PDF/A a PDF y guardar como "ResultConvertToPDF.pdf" - Solicitar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAConvertToPDF', "params": [event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Fragmento de código]

    /*crear un enlace para descargar el archivo resultante*/
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


El siguiente fragmento de código en JavaScript muestra un ejemplo simple de conversión de PDF/A a PDF:

1. Selecciona un archivo PDF para convertir.
2. Crea un 'FileReader'.
3. Se ejecuta la función [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaconverttopdf/).
4. Se establece el nombre del archivo resultante, en este ejemplo "ResultConvertToPDFA.pdf".
5. A continuación, si 'json.errorCode' es 0, entonces tu DownloadFile se le da el nombre que especificaste anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, habrá un error en tu archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.
6. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

    var ffilePdfAConvertToPDF = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*convierte un archivo PDF/A a PDF y guarda el "ResultConvertToPDF.pdf"*/
        const json = AsposePdfAConvertToPDF(event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*crear un enlace para descargar el archivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

```