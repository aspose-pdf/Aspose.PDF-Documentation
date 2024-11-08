---
title: Cambiar Contraseña de un Archivo PDF
linktitle: Cambiar Contraseña
type: docs
weight: 50
url: /es/javascript-cpp/change-password-pdf/
description: Cambiar Contraseña de un Archivo PDF con Aspose.PDF para JavaScript vía C++.
lastmod: "2023-09-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Cambiar Contraseña de un Archivo PDF

Si deseas cambiar la contraseña de un archivo PDF de "owner" a "newowner" prueba el siguiente fragmento de código:

1. Selecciona un archivo PDF.
1. Crea un 'FileReader'.
1. Se ejecuta la función [AsposePdfChangePassword](https://reference.aspose.com/pdf/javascript-cpp/security/asposepdfchangepassword/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultPdfChangePassword.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces tu DownloadFile recibe el nombre que especificaste anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, en consecuencia, hay un error en tu archivo, entonces la información sobre dicho error se encontrará en el archivo 'json.errorText'.

1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

    var ffilePdfChangePassword = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Cambiar contraseñas de un archivo PDF de "owner" a "newowner" y guardar el "ResultPdfChangePassword.pdf"*/
        const json = AsposePdfChangePassword(event.target.result, e.target.files[0].name, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
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
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffilePdfChangePassword = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const ownerPassword = 'owner'; /*Contraseña del propietario*/
        const newUserPassword = "newuser"; /*Nueva contraseña de usuario*/
        const newOwnerPassword = "newowner"; /*Nueva contraseña del propietario*/
        /*Cambiar contraseñas de un archivo PDF de "owner" a "newowner" y guardar el "ResultPdfChangePassword.pdf" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfChangePassword', "params": [event.target.result, e.target.files[0].name, ownerPassword, newUserPassword, newOwnerPassword, "ResultPdfChangePassword.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Fragmento de código]

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