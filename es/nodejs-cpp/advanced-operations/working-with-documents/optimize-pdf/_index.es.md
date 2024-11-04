---
title: Optimizar PDF usando Aspose.PDF para Node.js a través de C++
linktitle: Optimizar Archivo PDF
type: docs
weight: 10
url: /nodejs-cpp/optimize-pdf/
description: Optimizar y comprimir archivos PDF para una vista web rápida usando el entorno Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimizar Documento PDF

El conjunto de herramientas de Aspose.PDF para Node.js a través de C++ te permite optimizar el contenido del PDF para el entorno de Node.js.

La optimización, o linealización, se refiere al proceso de hacer que un archivo PDF sea adecuado para la navegación en línea utilizando un navegador web.

En caso de que desees optimizar un PDF, puedes usar la función [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/). Por favor, revisa el siguiente fragmento de código para optimizar archivos PDF en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que será optimizado.

1. Llamar a `AsposePdf` como Promesa y realizar la operación para optimizar el archivo. Recibir el objeto si es exitoso.
1. Llamar a la función [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimizar un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultOptimize.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimizar un archivo PDF y guardar el "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el módulo `asposepdfnodejs`.
1. Especificar el nombre del archivo PDF que será optimizado.

1. Inicializar el módulo AsposePdf. Recibir el objeto si es exitoso.
1. Llamar a la función [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimizar un archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultOptimize.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimizar un archivo PDF y guardar el "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```