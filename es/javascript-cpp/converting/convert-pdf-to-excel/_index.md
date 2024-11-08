---
title: Convertir PDF a Excel en JavaScript
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/javascript-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-01"
keywords: convertir PDF a Excel usando javascript, convertir PDF a XLSX, convertir PDF a CSV.
description: Aspose.PDF para JavaScript te permite convertir PDF a XLSX y formatos CSV.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Crear hojas de cálculo desde PDF usando JavaScript

**Aspose.PDF para JavaScript** soporta la función de convertir archivos PDF a formatos Excel y CSV.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF para JavaScript te presenta una aplicación gratuita en línea ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes probar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a Excel con Aplicación Gratuita](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

La operación de conversión depende del número de páginas en el documento y puede ser muy lenta.
 Por lo tanto, recomendamos encarecidamente usar Web Workers.

Este código demuestra una manera de delegar tareas de conversión de archivos PDF que consumen muchos recursos a un trabajador web para evitar bloquear el hilo principal de la interfaz de usuario. También ofrece una forma fácil de usar para descargar el archivo convertido.

## Convertir PDF a XLSX

```js

  /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffileToXlsX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*convertir un archivo PDF a XlsX y guardar como "ResultPDFtoXlsX.xlsx" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXlsX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx"] }, [event.target.result]);
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
        link.innerHTML = "Haz clic aquí para descargar el archivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

El siguiente fragmento de código JavaScript muestra un ejemplo simple de convertir páginas PDF en archivos XlsX:

1. Seleccione un archivo PDF para convertir.
1. Cree un 'FileReader'.
1. Se ejecuta la función [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPDFtoXlsX.xlsx".
1. A continuación, si el 'json.errorCode' es 0, entonces su archivo resultado recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en su archivo, entonces la información sobre tal error se contendrá en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convertir un archivo PDF a XlsX y guardar el "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*crear un enlace para descargar el archivo resultante*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


## Convertir PDF a CSV

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error del Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ? 
          `Número de archivos(tablas): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "text/csv", element) ) ?? ""}` : 
          `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffileToCSV = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Convertir un archivo PDF a CSV (extraer tablas) con la plantilla "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... formato de número de página), TAB como delimitador y guardar - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfTablesToCSV', "params": [event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Crear un enlace para descargar el archivo resultante*/
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


El siguiente fragmento de código JavaScript muestra un ejemplo simple de convertir PDF en CSV:

1. Seleccione un archivo PDF para convertir.
1. Cree un 'FileReader'.
1. Se ejecuta la función [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPdfTablesToCSV{0:D2}.csv".
1. A continuación, si el 'json.errorCode' es 0, entonces su archivo de resultado recibe el nombre que especificó anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, habrá un error en su archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y le permite descargar el archivo resultante al sistema operativo del usuario.

```js

  var ffileToCSV = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Convierta un archivo PDF a CSV (extraiga tablas) con la plantilla "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... formato número de página), TAB como delimitador*/
        const json = AsposePdfTablesToCSV(event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Conteo de archivos(tablas): " + json.filesCount.toString();
          /*Crear enlaces a los archivos de resultado*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "text/csv");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```