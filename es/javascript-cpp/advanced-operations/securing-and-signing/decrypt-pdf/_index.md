---
title: Desencriptar PDF usando JavaScript
linktitle: Desencriptar Archivo PDF
type: docs
weight: 40
url: es/javascript-cpp/decrypt-pdf/
description: Desencriptar Archivo PDF con Aspose.PDF para JavaScript vía C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Desencriptar Archivo PDF usando Contraseña de Propietario

Recientemente, cada vez más usuarios intercambian documentos encriptados para no ser víctimas de fraudes en Internet y proteger sus documentos. En este sentido, se vuelve necesario acceder al archivo PDF encriptado, ya que dicho acceso solo puede ser obtenido por un usuario autorizado. Además, las personas buscan diversas soluciones para desencriptar archivos PDF.

Es mejor resolver este problema una vez utilizando Aspose.PDF para JavaScript vía C++ directamente en su navegador web. El siguiente fragmento de código le muestra cómo desencriptar archivos PDF.

1. Seleccione un archivo PDF para desencriptar.
1. Cree un 'FileReader'.
1. Se ejecuta la función [AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/).

1. El nombre del archivo resultante se establece, en este ejemplo "ResultDecrypt.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces tu DownloadFile recibe el nombre que especificaste anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, la información sobre dicho error se encontrará en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

    var ffileDecrypt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Desencriptar un archivo PDF con la contraseña "owner" y guardar el "ResultDecrypt.pdf"*/
        const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Crear un enlace para descargar el archivo resultante*/
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
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffileDecrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*Desencriptar un archivo PDF con la contraseña "owner" y guardar como "ResultDecrypt.pdf" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDecrypt',
            "params": [event.target.result, e.target.files[0].name, password, "ResultDecrypt.pdf"] }, 
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