---
title: Dividir PDF en Node.js
linktitle: Dividir archivos PDF
type: docs
weight: 30
url: /es/nodejs-cpp/split-pdf/
description: Este tema muestra cómo dividir páginas PDF en archivos PDF individuales con Aspose.PDF for Node.js via C++ .
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dividir PDF en dos archivos usando Node.js

En caso de que desee dividir un PDF único en partes, puede usar [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) función. 
Por favor, revise el siguiente fragmento de código para dividir dos PDFs en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre de los archivos PDF que se dividirán.
1. Llamar `AsposePdf` como Promise y realiza la operación para dividir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Divida dos archivos PDF. Establece la variable pageToSplit a 1, indicando que el archivo PDF se dividirá en la página 1. 
1. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSplit1.pdf" y "ResultSplit2.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre de los archivos PDF que se dividirán.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Divida dos archivos PDF. Establece la variable pageToSplit a 1, indicando que el archivo PDF se dividirá en la página 1. 
1. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultSplit1.pdf" y "ResultSplit2.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```