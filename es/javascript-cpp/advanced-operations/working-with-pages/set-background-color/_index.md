---
title: Establecer el color de fondo para PDF con JavaScript a través de C++
linktitle: Establecer color de fondo 
type: docs
weight: 80
url: es/javascript-cpp/set-background-color/
description: Establecer el color de fondo para tu archivo PDF con JavaScript a través de C++. 
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los siguientes fragmentos de código muestran cómo establecer el color de fondo de las páginas PDF usando la función [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) con JavaScript.

En el siguiente ejemplo, seleccionamos el archivo PDF para manejar.

1. Crear un 'FileReader'.
1. Se ejecuta la función [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) (formato hexadecimal “#RRGGBB”, donde RR-rojo, GG-verde y BB-azul son enteros hexadecimales).
1. Establecer el color de fondo para el archivo PDF y guardar como "ResultPdfSetBackgroundColor.pdf".

1. A continuación, si el 'json.errorCode' es 0, entonces tu DownloadFile recibirá el nombre que especificaste anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre tal error estará contenida en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

  var ffilePdfSetBackgroundColor = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Establece el color de fondo para el archivo PDF y guarda el "ResultPdfSetBackgroundColor.pdf"*/
        const json = AsposePdfSetBackgroundColor(event.target.result, e.target.files[0].name, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Crea un enlace para descargar el archivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
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
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffilePdfSetBackgroundColor = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const backgroundColor= "#426bf4";
        /*Establecer el color de fondo para el archivo PDF y guardar "ResultPdfSetBackgroundColor.pdf" - Pedir al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfSetBackgroundColor', "params": [event.target.result, e.target.files[0].name, backgroundColor, "ResultPdfSetBackgroundColor.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

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