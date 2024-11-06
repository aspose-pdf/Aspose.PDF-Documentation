---
title: Dividir PDF en Node.js
linktitle: Dividir archivos PDF
type: docs
weight: 30
url: es/nodejs-cpp/split-pdf/
description: Este tema muestra cómo dividir páginas PDF en archivos PDF individuales con Aspose.PDF para Node.js vía C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dividir un PDF en dos archivos usando Node.js

En caso de que desee dividir un solo PDF en partes, puede usar la función [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/). 
Por favor, revise el siguiente fragmento de código para dividir dos PDF en el entorno de Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre de los archivos PDF que se dividirán.
1. Llame a `AsposePdf` como Promise y realice la operación para dividir el archivo. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).

1. Dividir dos archivos PDF. Establece la variable pageToSplit en 1, indicando que el archivo PDF se dividirá en la página 1.
1. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSplit1.pdf" y "ResultSplit2.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Establecer el número de página para dividir*/
      const pageToSplit = 1;
      /*Dividir en dos archivos PDF y guardar "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el módulo `asposepdfnodejs`.

1. Especifique el nombre de los archivos PDF que se dividirán.
1. Inicialice el módulo AsposePdf. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Divida dos archivos PDF. Establece la variable pageToSplit en 1, indicando que el archivo PDF se dividirá en la página 1.
1. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSplit1.pdf" y "ResultSplit2.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Establecer el número de página para dividir*/
  const pageToSplit = 1;
  /*Dividir en dos archivos PDF y guardar "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```