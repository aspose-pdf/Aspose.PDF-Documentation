---
title: Añadir firma digital o firmar digitalmente PDF en JavaScript a través de C++
linktitle: Firmar PDF digitalmente
type: docs
weight: 70
url: /javascript-cpp/sign-pdf/
description: Firmar digitalmente documentos PDF usando JavaScript a través de C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Una firma digital en un documento PDF es una forma de verificar la autenticidad e integridad del documento. Este es el proceso de la firma electrónica de un documento PDF utilizando una clave privada y un certificado digital. Esta firma garantiza al titular que el documento no ha sido alterado o modificado desde la firma y que el firmante es quien lo aprueba. Para firmar PDF con JavaScript, use la herramienta Aspose.PDF.

Aspose.PDF para JavaScript a través de C++ admite la característica de firmar digitalmente los archivos PDF utilizando el [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/).

## Firmar PDF con firmas digitales

```js

    /*Establecer el nombre de archivo PKCS7 predeterminado*/
    var fileSign = "/test.pfx";

    var ffileSign = function (e) {
      const file_reader = new FileReader();
      /*Establecer el nombre de archivo PKCS7*/
      fileImage = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Guardar el BLOB en la memoria FS para su procesamiento*/
        AsposePdfPrepare(event.target.result, fileSign);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Establecer el nombre de archivo de imagen (Apariencia de la Firma) predeterminado*/
    var signatureAppearance = "/Aspose.jpg";

    var ffileImage = function (e) {
      const file_reader = new FileReader();
      /*Establecer el nombre de archivo de imagen*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*Guardar el BLOB en la memoria FS para su procesamiento*/
        AsposePdfPrepare(event.target.result, signatureAppearance);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    var ffileSignPKCS7 = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        let pswSign = document.getElementById("passwordSign").value;
        /*Firmar un archivo PDF con firmas digitales y guardar el "ResultSignPKCS7.pdf"*/
        const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Crear un enlace para descargar el archivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### Usando Web Workers

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error desde Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '¡archivo preparado!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Establecer el nombre de archivo PKCS7 predeterminado*/
    var fileSign = "test.pfx";
    /*Establecer el nombre de archivo de imagen predeterminado (Apariencia de Firma): 'Aspose.jpg' ya cargado, ver configuraciones en 'settings.json'*/
    var signatureAppearance = "Aspose.jpg";

    /*Manejador de eventos*/
    const ffileSignPKCS7 = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pageNum = 1;
        const pswSign = document.getElementById("passwordSign").value;
        const setXIndent = 100;
        const setYIndent = 100;
        const setHeight = 200;
        const setWidth = 100;
        const reason = 'Razón';
        const contact = 'contact@test.com';
        const location = 'Ubicación';
        const isVisible = 1;
        /*Firmar un archivo PDF con firmas digitales y guardar "ResultSignPKCS7.pdf" - Solicitar a Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSignPKCS7',
            "params": [event.target.result, e.target.files[0].name, pageNum, fileSign, pswSign, setXIndent, setYIndent,
                      setHeight, setWidth, reason, contact, location, isVisible, signatureAppearance, "ResultSignPKCS7.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileSign = e => {
      const file_reader = new FileReader();
      /*Establecer el nombre de archivo PKCS7*/
      fileSign = e.target.files[0].name;
      file_reader.onload = event => {
        /*Guardar el BLOB en la memoria FS para su procesamiento*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, fileSign] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Establecer el nombre de archivo de imagen*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = event => {
        /*Guardar el BLOB en la memoria FS para su procesamiento*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, signatureAppearance] },
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
        link.innerHTML = "Haga clic aquí para descargar el archivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```