---
title: Agregar firma digital en PDF en Node.js
linktitle: Firmar PDF digitalmente
type: docs
weight: 70
url: /es/nodejs-cpp/sign-pdf/
description: Firmar documentos PDF digitalmente en el entorno Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


Una firma digital en un documento PDF es una forma de verificar la autenticidad e integridad del documento. Este es el proceso de la firma electrónica de un documento PDF usando una clave privada y un certificado digital. Esta firma garantiza al titular que el documento no ha sido alterado o modificado desde la firma y que el firmante es quien lo aprueba. Para firmar PDF con Node.js, use la herramienta Aspose.PDF.

En caso de que desee firmar un archivo PDF, puede usar [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) función.

Es posible usar **parámetros** relacionados con la firma:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- establecerSangríaY
- establecerAltura
- establecerAncho
- razón
- contacto
- ubicación
- isVisible
- signatureAppearance
- fileNameResult 

Este fragmento de código utiliza el módulo AsposePDFforNode.js en un entorno Node.js para firmar digitalmente un archivo PDF usando la firma PKCS7.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF a firmar, el archivo de clave PKCS7 y el archivo de imagen de apariencia de la firma. El certificado y la imagen pueden colocarse en cualquier lugar de su sistema de archivos desde donde los cargue para la firma de PDF.
1. Llamar `AsposePdf` como Promise y realiza la operación para firmar el archivo. Recibe el objeto si tiene éxito.
1. Llama al [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) función. 
1. Firmar un archivo PDF con firmas digitales. Parámetros relacionados con la firma (como el archivo de clave, la contraseña, coordenadas, razón, contacto, ubicación, etc). 
1. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSignPKCS7.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Key PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Signature appearance*/
      const sign_img_file = 'Aspose.jpg';
      /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se va a firmar, el archivo de clave PKCS7 y el archivo de imagen de apariencia de la firma.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama al [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) función. 
1. Firmar un archivo PDF con firmas digitales. Parámetros relacionados con la firma (como el archivo de clave, la contraseña, coordenadas, razón, contacto, ubicación, etc). 
1. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSignPKCS7.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Key PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Signature appearance*/
  const sign_img_file = 'Aspose.jpg';
  /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```