---
title: Reparar PDF en Node.js 
linktitle: Reparar PDF
type: docs
weight: 10
url: es/nodejs-cpp/repair-pdf/
description: Este tema describe cómo reparar PDF en el entorno de Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF para Node.js permite una reparación de PDF de alta calidad. El archivo PDF puede no abrirse por cualquier razón, independientemente del programa o navegador. En algunos casos, el documento puede ser restaurado, prueba el siguiente código y compruébalo por ti mismo.
En caso de que desees reparar un documento PDF, puedes usar la función [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/). 
Por favor, revisa el siguiente fragmento de código para reparar archivos PDF en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que será reparado.
1. Llama a `AsposePdf` como Promesa y realiza la operación para reparar el archivo. Recibe el objeto si es exitoso.

1. Llama a la función [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repara el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfRepair.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repara un archivo PDF y guarda el "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que será reparado.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.

1. Llama a la función [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repara el archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfRepair.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Reparar un archivo PDF y guardar el "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```