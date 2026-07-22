---
title: Optimizar PDF usando Aspose.PDF for Node.js via C++
linktitle: Optimizar archivo PDF
type: docs
weight: 10
url: /es/nodejs-cpp/optimize-pdf/
description: Optimizar y comprimir archivos PDF para una visualización web rápida usando el entorno Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimizar documento PDF

El kit de herramientas de Aspose.PDF for Node.js via C++ le permite optimizar el contenido PDF para el entorno Node.js. 

La optimización, o linealización, se refiere al proceso de hacer que un archivo PDF sea adecuado para la navegación en línea mediante un navegador web.

En caso de que desees optimizar PDF, puedes usar [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) función. 
Por favor, revisa el siguiente fragmento de código para optimizar archivos PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será optimizado.
1. Llamar `AsposePdf` como Promise y realiza la operación para optimizar el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimiza un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultOptimize.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF que será optimizado.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimiza un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultOptimize.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```