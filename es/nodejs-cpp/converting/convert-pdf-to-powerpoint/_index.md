---
title: Convertir PDF a PPTX en Node.js
linktitle: Convertir PDF a PowerPoint
type: docs
weight: 30
url: /es/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-16"
description: Aspose.PDF le permite convertir PDF a formato PPTX usando Node.js directamente en el entorno de Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**Intenta convertir PDF a PowerPoint en línea**

Aspose.PDF para Node.js le presenta la aplicación gratuita en línea ["PDF a PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), donde puede intentar investigar la funcionalidad y la calidad con la que funciona.

[![Aspose.PDF Conversión PDF a PPTX con App Gratuita](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Convertir PDF a PPTX

En caso de que desee convertir un documento PDF, puede usar la función [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).

Por favor, revise el siguiente fragmento de código para convertir en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llama a `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoPptX.pptx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convierte un archivo PDF a PptX y guarda en "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que se convertirá.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoPptX.pptx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un archivo PDF a PptX y guardar en "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```