---
title: Cómo fusionar PDF en Node.js
linktitle: Fusionar archivos PDF
type: docs
weight: 20
url: /es/nodejs-cpp/merge-pdf/
description: Esta página explica cómo fusionar documentos PDF en un solo archivo PDF con Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Fusiona o combina dos PDF en un solo PDF en Node.js

Combinar y fusionar archivos es una tarea muy popular al trabajar con una gran cantidad de documentos. A veces, al trabajar con documentos e imágenes, cuando se escanean, procesan y organizan, se crean varios archivos.
Pero, ¿qué pasa si necesitas almacenar todo en un solo archivo? ¿O no quieres imprimir varios documentos? Concatenar dos archivos PDF con Aspose.PDF for Node.js via C++.

En caso de que quieras fusionar dos PDFs, puedes usar [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) función. 
Por favor, revisa el siguiente fragmento de código para fusionar dos archivos PDFs en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre de los archivos PDF que se fusionarán.
1. Llamar `AsposePdf` como Promise y realiza la operación para fusionar. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Fusiona dos archivos PDF. Por lo tanto, si \u0027json.errorCode\u0027 es 0, el resultado de la operación se guarda en \u0022ResultMerge.pdf\u0022. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en \u0027json.errorText\u0027.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre de los archivos PDF que se fusionarán.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Fusiona dos archivos PDF. Por lo tanto, si \u0027json.errorCode\u0027 es 0, el resultado de la operación se guarda en \u0022ResultMerge.pdf\u0022. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en \u0027json.errorText\u0027.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```