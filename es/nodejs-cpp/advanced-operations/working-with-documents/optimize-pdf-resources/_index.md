---
title: Optimizar Recursos PDF en Node.js
linktitle: Optimizar Recursos PDF
type: docs
weight: 15
url: es/nodejs-cpp/optimize-pdf-resources/
description: Optimizar Recursos de archivos PDF para una rápida visualización web usando la herramienta Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimizar Recursos PDF

Optimizar recursos en el documento:

1. Los recursos que no se utilizan en las páginas del documento se eliminan
1. Los recursos iguales se combinan en un solo objeto
1. Se eliminan los objetos no utilizados
 

En caso de que desee optimizar los recursos PDF, puede utilizar la función [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/). 
Por favor, consulte el siguiente fragmento de código para optimizar recursos PDF en entorno Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF para el cual se optimizarán los recursos.

1. Llama a `AsposePdf` como Promise y realiza la operación para optimizar el archivo. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimiza los recursos de un PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfOptimizeResource.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimizar los recursos del archivo PDF y guardar en "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF cuyos recursos serán optimizados.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimiza los recursos de un PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfOptimizeResource.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimiza los recursos del archivo PDF y guarda el "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```