---
title: Cambiar la contraseña de un archivo PDF en Node.js
linktitle: Cambiar contraseña
type: docs
weight: 50
url: /es/nodejs-cpp/change-password-pdf/
description: Cambiar la contraseña de un archivo PDF con Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Cambiar la contraseña de un archivo PDF

En caso de que quieras cambiar la contraseña del PDF, puedes usar [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) función. Cambia la contraseña de usuario y la contraseña de propietario mediante la contraseña de propietario, manteniendo la configuración de seguridad original.
Si desea cambiar la contraseña de un archivo PDF de “owner” a “newowner” o “newuser”, pruebe el siguiente fragmento de código:

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF cuya contraseña se cambiará.
1. Llamar `AsposePdf` como Promise y realizar la operación para cambiar la contraseña. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Cambiar contraseña. La contraseña de propietario existente está establecida en “owner”, y se cambia a “newowner” con la nueva contraseña de usuario “newuser”.
1. Así, si ‘json.errorCode’ es 0, el resultado de la operación se guarda en “ResultPdfChangePassword.pdf”. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Tenga en cuenta que si la contraseña es una cadena vacía:

1. Si la contraseña de usuario está vacía, el PDF se abre sin solicitar una contraseña (pero sigue estando cifrado).
1. Si la contraseña del propietario está vacía, el PDF se abre con una solicitud de contraseña de usuario.
1. Si ambos están vacíos  - el PDF se abre sin solicitar una contraseña (pero sigue estando encriptado).


**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF cuya contraseña se cambiará.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Cambiar contraseña. La contraseña de propietario existente está establecida en “owner”, y se cambia a “newowner” con la nueva contraseña de usuario “newuser”.
1. Así, si ‘json.errorCode’ es 0, el resultado de la operación se guarda en “ResultPdfChangePassword.pdf”. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```