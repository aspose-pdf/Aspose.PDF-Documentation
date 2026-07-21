---
title:  Cifrar PDF en Node.js
linktitle: Cifrar archivo PDF
type: docs
weight: 50
url: /es/nodejs-cpp/encrypt-pdf/
description: Cifrar archivo PDF con Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Cifrar archivo PDF usando la contraseña de usuario o de propietario

Si estás enviando un correo electrónico a alguien con un archivo adjunto PDF que contiene información confidencial, puede que desees añadirle seguridad primero para evitar que caiga en manos equivocadas. La mejor manera de limitar el acceso no autorizado a un documento PDF es protegerlo con una contraseña. Para cifrar documentos de forma fácil y segura, puedes usar Aspose.PDF for Node.js via C++.

>Por favor, especifica diferentes contraseñas de usuario y de propietario al cifrar el archivo PDF.

- La **contraseña de usuario**, si está establecida, es lo que necesita proporcionar para abrir un PDF. Acrobat/Reader solicitará al usuario que ingrese la contraseña de usuario. Si no es correcta, el documento no se abrirá.
- La **contraseña de propietario**, si está establecida, controla los permisos, como imprimir, editar, extraer, comentar, etc. Acrobat/Reader prohibirá estas acciones según la configuración de permisos. Acrobat requerirá esta contraseña si desea establecer/cambiar permisos.

En caso de que desee cifrar un archivo PDF, puede usar [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) función. 
Si desea cifrar un archivo PDF, pruebe el siguiente fragmento de código:

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF que será cifrado.
1. Llamar `AsposePdf` como Promise y realiza la operación de cifrado del archivo. Recibe el objeto si es exitoso.
1. Llama al [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) función. 
1. Encripte el archivo PDF con las contraseñas "user" y "owner".
1. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultEncrypt.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Hay diferentes [permisos de cifrado](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent
- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

Hay varios [algoritmos de cifrado](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF cuyo cifrado será cambiado.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama al [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) función. 
1. Descifre el archivo PDF con las contraseñas "user" y "owner".
1. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultEncrypt.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```