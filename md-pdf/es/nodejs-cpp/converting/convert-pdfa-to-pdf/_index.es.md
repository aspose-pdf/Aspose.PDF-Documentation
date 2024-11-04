---
title: Convertir PDF/A a formato PDF en Node.js
linktitle: Convertir PDF/A a formato PDF
type: docs
weight: 110
url: /nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-16"
description: Este tema le muestra cómo Aspose.PDF permite convertir un archivo PDF/A a un documento PDF en el entorno de Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF/A a formato PDF

En caso de que desee convertir un documento PDF, puede usar la función [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/). 
Por favor, revise el siguiente fragmento de código para realizar la conversión en el entorno de Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF que se convertirá.
1. Llame a `AsposePdf` como Promise y realice la operación para convertir el archivo. Reciba el objeto si es exitoso.

1. Llama a la función [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultConvertToPDF.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se contendrá en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convierte un archivo PDF/A a PDF y guarda el "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF/A que será convertido.

1. Inicialice el módulo AsposePdf. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Convierta el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultConvertToPDF.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convertir un archivo PDF/A a PDF y guardar el "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```