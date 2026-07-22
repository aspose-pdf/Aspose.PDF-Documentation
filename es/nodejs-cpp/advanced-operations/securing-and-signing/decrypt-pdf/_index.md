---
title: Descifrar PDF en Node.js
linktitle: Descifrar archivo PDF
type: docs
weight: 40
url: /es/nodejs-cpp/decrypt-pdf/
description: Descifrar archivo PDF con Aspose.PDF para Node.js vía C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Descifrar archivo PDF usando la contraseña del propietario

Recientemente, cada vez más usuarios intercambian documentos cifrados para no convertirse en víctimas de fraudes en internet y proteger sus documentos.
En este sentido, se vuelve necesario acceder al archivo PDF cifrado, ya que dicho acceso solo puede ser obtenido por un usuario autorizado. Además, la gente busca diversas soluciones para descifrar archivos PDF. 

En caso de que desees descifrar un archivo PDF, puedes usar [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) función. 
Si deseas descifrar un archivo PDF, prueba el siguiente fragmento de código:

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que cambiará el descifrado.
1. Llamar `AsposePdf` como Promise y realizar la operación para descifrar el archivo. Reciba el objeto si tiene éxito.
1. Llama al [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) función.
1. Descifrar archivo PDF con la contraseña es "owner".
1. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultDecrypt.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF que cambiará el descifrado.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama al [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) función.
1. Descifrar archivo PDF con la contraseña es "owner".
1. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultDecrypt.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```