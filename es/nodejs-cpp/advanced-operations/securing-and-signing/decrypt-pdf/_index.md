---
title: Decrypt PDF en Node.js
linktitle: Desencriptar archivo PDF
type: docs
weight: 40
url: es/nodejs-cpp/decrypt-pdf/
description: Desencriptar archivo PDF con Aspose.PDF para Node.js vía C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Desencriptar archivo PDF usando contraseña de propietario

Recientemente, más y más usuarios intercambian documentos encriptados para no convertirse en víctimas del fraude en Internet y proteger sus documentos.
En este sentido, se hace necesario acceder al archivo PDF encriptado, ya que dicho acceso solo puede ser obtenido por un usuario autorizado. Además, las personas buscan diversas soluciones para desencriptar archivos PDF.

En caso de que desees desencriptar un archivo PDF, puedes usar la función [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
Si deseas desencriptar un archivo PDF, prueba el siguiente fragmento de código:

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que cambiará el desencriptado.

1. Llama a `AsposePdf` como Promise y realiza la operación para desencriptar el archivo. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Desencripta el archivo PDF con la contraseña "owner".
1. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultDecrypt.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Desencriptar un archivo PDF con la contraseña "owner" y guardar en "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que cambiará el descifrado.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Descifra el archivo PDF con la contraseña "owner".
1. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultDecrypt.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Descifrar un archivo PDF con la contraseña "owner" y guardar en "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```