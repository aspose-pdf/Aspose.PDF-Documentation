---
title: Extraer Texto de PDF en Node.js
linktitle: Extraer Texto de PDF
type: docs
weight: 10
url: /nodejs-cpp/extract-text/
description: Esta sección describe cómo extraer texto de un documento PDF usando Aspose.PDF para Node.js a través del kit de herramientas C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Texto de Todas las Páginas de un Documento PDF

Extraer texto de un PDF no es fácil. Solo unos pocos lectores de PDF pueden extraer texto de imágenes PDF o PDFs escaneados. Pero la herramienta **Aspose.PDF para Node.js a través de C++** te permite extraer fácilmente texto de todo el archivo PDF en el entorno Node.js.

Este código demuestra cómo usar el módulo AsposePDFforNode.js para extraer texto de un archivo PDF especificado y registrar ya sea el texto extraído o los errores encontrados.

Consulta los fragmentos de código y sigue los pasos para extraer texto de tu PDF:

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como la variable `AsposePdf`.

1. Especifique el nombre del archivo PDF del cual se extraerá el texto.
1. Llame a `AsposePdf` como una Promesa y realice la operación para extraer texto. Reciba el objeto si es exitoso.
1. Llame a la función [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. El texto extraído se almacena en el objeto JSON. Así, si 'json.errorCode' es 0, el texto extraído se muestra usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extraer texto de un archivo PDF*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe el módulo `asposepdfnodejs`.

1. Especifique el nombre del archivo PDF del cual se extraerá el texto.
1. Inicialice el módulo AsposePdf. Reciba el objeto si es exitoso.
1. Llame a la función [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. El texto extraído se almacena en el objeto JSON. Por lo tanto, si 'json.errorCode' es 0, el texto extraído se muestra usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extraer texto de un archivo PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```