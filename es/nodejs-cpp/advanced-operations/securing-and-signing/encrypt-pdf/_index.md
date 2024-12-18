---
title:  Encriptar PDF en Node.js
linktitle: Encriptar Archivo PDF
type: docs
weight: 50
url: /es/nodejs-cpp/encrypt-pdf/
description: Encripta un archivo PDF con Aspose.PDF para Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Encriptar Archivo PDF usando Contraseña de Usuario o Propietario

Si estás enviando un correo electrónico a alguien con un archivo PDF adjunto que contiene información confidencial, es posible que desees agregarle algo de seguridad primero para evitar que caiga en las manos incorrectas. La mejor manera de limitar el acceso no autorizado a un documento PDF es protegerlo con una contraseña. Para encriptar documentos de manera fácil y segura, puedes usar Aspose.PDF para Node.js via C++.

>Por favor, especifica diferentes contraseñas de usuario y propietario mientras encriptas el archivo PDF.

- La **contraseña de usuario**, si se establece, es lo que necesitas proporcionar para abrir un PDF. Acrobat/Reader solicitará a un usuario que ingrese la contraseña de usuario. Si no es correcta, el documento no se abrirá.
- La **contraseña de propietario**, si se establece, controla los permisos, como impresión, edición, extracción, comentarios, etc.
 Acrobat/Reader deshabilitará estas cosas basándose en la configuración de permisos. Acrobat requerirá esta contraseña si desea establecer/cambiar permisos.

En caso de que desee cifrar un archivo PDF, puede utilizar la función [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/). Si desea cifrar un archivo PDF, pruebe el siguiente fragmento de código:

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF que será cifrado.
1. Llame a `AsposePdf` como Promise y realice la operación para cifrar el archivo. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. Cifre el archivo PDF con las contraseñas "user" y "owner".
1. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultEncrypt.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encriptar un archivo PDF con las contraseñas "user" y "owner", y guardar el "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Existen diferentes [permisos de encriptación](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent

- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

Hay varios [algoritmos de encriptación](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que cambiará el encriptado.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. Desencripta el archivo PDF con las contraseñas "user" y "owner".

1. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultEncrypt.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encripta un archivo PDF con las contraseñas "user" y "owner", y guarda el "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```