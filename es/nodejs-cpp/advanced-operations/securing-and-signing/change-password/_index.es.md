---
title: Cambiar contraseña de un archivo PDF en Node.js
linktitle: Cambiar contraseña
type: docs
weight: 50
url: /nodejs-cpp/change-password-pdf/
description: Cambiar contraseña de un archivo PDF con Aspose.PDF para Node.js vía C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Cambiar contraseña de un archivo PDF

En caso de que desees cambiar la contraseña de un PDF, puedes usar la función [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/). Cambia la contraseña de usuario y la contraseña de propietario mediante la contraseña de propietario, manteniendo la configuración de seguridad original. Si deseas cambiar la contraseña de un archivo PDF de "owner" a "newowner" o "newuser", prueba el siguiente fragmento de código:

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como la variable `AsposePdf`.
2. Especifica el nombre del archivo PDF que cambiará la contraseña.
3. Llama a `AsposePdf` como Promesa y realiza la operación para cambiar la contraseña. Recibe el objeto si tiene éxito.

1. Llama a la función [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Cambiar contraseña. La contraseña de propietario existente está configurada como "owner" y se cambia a "newowner" con la nueva contraseña de usuario "newuser".
1. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfChangePassword.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se contendrá en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Cambiar las contraseñas del archivo PDF de "owner" a "newowner" y guardar el "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


Tenga en cuenta que si la contraseña está vacía:

1. Si la contraseña del usuario está vacía, el PDF se abre sin pedir una contraseña (pero aún está cifrado).
1. Si la contraseña del propietario está vacía, el PDF se abre con una solicitud de contraseña de usuario.
1. Si ambas están vacías, el PDF se abre sin pedir una contraseña (pero aún está cifrado).

**ECMAScript/ES6:**

1. Importe el módulo `asposepdfnodejs`.
1. Especifique el nombre del archivo PDF que cambiará la contraseña.
1. Inicialice el módulo AsposePdf. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Cambie la contraseña. La contraseña existente del propietario se establece en "owner" y se cambia a "newowner" con la nueva contraseña de usuario "newuser".

1. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfChangePassword.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Cambiar las contraseñas del archivo PDF de "owner" a "newowner" y guardar en "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```