---
title: Añadir firma digital en PDF en Node.js
linktitle: Firmar PDF digitalmente
type: docs
weight: 70
url: /nodejs-cpp/sign-pdf/
description: Firmar digitalmente documentos PDF en el entorno de Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Una firma digital en un documento PDF es una forma de verificar la autenticidad e integridad del documento. Este es el proceso de firma electrónica de un documento PDF utilizando una clave privada y un certificado digital. Esta firma garantiza al poseedor que el documento no ha sido alterado o modificado desde la firma y que el firmante es quien lo aprueba. Para firmar un PDF con Node.js, utiliza la herramienta Aspose.PDF.

En caso de que desees firmar un archivo PDF, puedes utilizar la función [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).

Es posible utilizar **parámetros** relacionados con la firma:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- reason

- contact
- ubicación
- esVisible
- aparienciaDeFirma
- nombreDeArchivoResultado

Este fragmento de código utiliza el módulo AsposePDFforNode.js en un entorno Node.js para firmar digitalmente un archivo PDF utilizando la firma PKCS7.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especifique el nombre del archivo PDF que se va a firmar, el archivo de clave PKCS7 y el archivo de imagen de apariencia de la firma. El certificado y la imagen pueden colocarse en cualquier lugar de su sistema de archivos desde donde los cargue para la firma del PDF.
1. Llame a `AsposePdf` como Promise y realice la operación para firmar el archivo. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Firme un archivo PDF con firmas digitales. Parámetros relacionados con la firma (como el archivo de clave, contraseña, coordenadas, razón, contacto, ubicación, etc.).

1. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSignPKCS7.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Clave PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Apariencia de la firma*/
      const sign_img_file = 'Aspose.jpg';
      /*Firmar un archivo PDF con firmas digitales y guardar el "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.

1. Especifique el nombre del archivo PDF que se firmará, el archivo de clave PKCS7 y el archivo de imagen de apariencia de firma.
1. Inicialice el módulo AsposePdf. Reciba el objeto si es exitoso.
1. Llame a la función [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Firme un archivo PDF con firmas digitales. Parámetros relacionados con la firma (como el archivo de clave, contraseña, coordenadas, razón, contacto, ubicación, etc.).
1. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSignPKCS7.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se contendrá en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Clave PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Apariencia de la firma*/
  const sign_img_file = 'Aspose.jpg';
  /*Firmar un archivo PDF con firmas digitales y guardar en "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```