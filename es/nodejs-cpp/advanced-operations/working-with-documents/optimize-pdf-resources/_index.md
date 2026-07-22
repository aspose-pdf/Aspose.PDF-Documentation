---
title: Optimizar recursos PDF en Node.js
linktitle: Optimizar recursos PDF
type: docs
weight: 15
url: /es/nodejs-cpp/optimize-pdf-resources/
description: Optimizar recursos de archivos PDF para visualización web rápida usando la herramienta Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimizar recursos PDF

Optimizar recursos en el documento:

1. Los recursos que no se usan en las páginas del documento se eliminan
1. Los recursos iguales se combinan en un solo objeto
1. Los objetos no utilizados son eliminados
 

En caso de que desee optimizar los recursos PDF, puede usar [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) función. 
Por favor, revise el siguiente fragmento de código para optimizar los recursos PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF para el cual se optimizarán los recursos.
1. Llamar `AsposePdf` como Promise y realiza la operación para optimizar el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimizar los recursos de un PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfOptimizeResource.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF para el cual se optimizarán los recursos.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimizar los recursos de un PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfOptimizeResource.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```