---
title:  Encriptar PDF usando JavaScript
linktitle: Encriptar Archivo PDF
type: docs
weight: 50
url: /es/javascript-cpp/encrypt-pdf/
description: Encriptar Archivo PDF con Aspose.PDF para JavaScript vía C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Encriptar Archivo PDF usando Contraseña de Usuario o Propietario

Si estás enviando un correo electrónico a alguien con un archivo PDF adjunto que contiene información confidencial, es posible que desees añadirle algo de seguridad primero para evitar que caiga en manos incorrectas. La mejor manera de limitar el acceso no autorizado a un documento PDF es protegerlo con una contraseña. Para encriptar documentos de manera fácil y segura, puedes usar Aspose.PDF para JavaScript vía C++.

>Especifique diferentes contraseñas de usuario y propietario al encriptar el archivo PDF.

- La **contraseña de usuario**, si se establece, es lo que necesitas proporcionar para abrir un PDF. Acrobat/Reader solicitará al usuario que ingrese la contraseña de usuario. Si no es correcta, el documento no se abrirá.
- La **contraseña de propietario**, si se establece, controla los permisos, como impresión, edición, extracción, comentarios, etc.
 Acrobat/Reader deshabilitará estas cosas basadas en la configuración de permisos. Acrobat requerirá esta contraseña si deseas establecer/cambiar permisos.

El siguiente fragmento de código te muestra cómo cifrar archivos PDF.

1. Selecciona un archivo PDF para cifrar.
1. Crea un 'FileReader'.
1. Se ejecuta la función [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/).
1. Se establece el nombre del archivo resultante, en este ejemplo "ResultEncrypt.pdf".
1. A continuación, si el 'json.errorCode' es 0, entonces tu DownloadFile recibe el nombre que especificaste anteriormente. Si el parámetro 'json.errorCode' no es igual a 0 y, por consiguiente, hay un error en tu archivo, entonces la información sobre dicho error estará contenida en el archivo 'json.errorText'.
1. Como resultado, la función [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) genera un enlace y te permite descargar el archivo resultante al sistema operativo del usuario.

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*cifra un archivo PDF con las contraseñas "user" y "owner", y guarda el "ResultDecrypt.pdf"*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*crea un enlace para descargar el archivo resultante*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## Usando Web Workers

```js

    /*Crear Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error desde el Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '¡cargado!' :
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Manejador de eventos*/
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'user';
        const password_owner = 'owner';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /*Encriptar un archivo PDF con contraseñas "user" y "owner", y guardar el "ResultEncrypt.pdf" - Preguntar al Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
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
        link.innerHTML = "Haz clic aquí para descargar el archivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```