---
title: Reparar PDF en Node.js
linktitle: Reparar PDF
type: docs
weight: 10
url: /es/nodejs-cpp/repair-pdf/
description: Este tema describe cómo reparar PDF en el entorno Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js permite una reparación de PDF de alta calidad. El archivo PDF puede no abrirse por cualquier razón, independientemente del programa o navegador. En algunos casos el documento puede ser restaurado, pruebe el siguiente código y compruébelo usted mismo.
En caso de que desee reparar un documento PDF, puede usar [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) función. 
Por favor, revise el siguiente fragmento de código para reparar el archivo PDF en el entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF que se reparará.
1. Llamar `AsposePdf` como Promise y realiza la operación para reparar el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repare el archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfRepair.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF que se reparará.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repare el archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfRepair.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```