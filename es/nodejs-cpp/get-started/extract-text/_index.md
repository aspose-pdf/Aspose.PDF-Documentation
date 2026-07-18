---
title: Extraer texto de PDF en Node.js
linktitle: Extraer texto de PDF
type: docs
weight: 10
url: /es/nodejs-cpp/extract-text/
description: Esta sección describe cómo extraer texto de un documento PDF usando la herramienta Aspose.PDF for Node.js via C\u002B\u002B.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer texto de todas las páginas del documento PDF

Extraer texto de PDF no es fácil. Solo algunos lectores de PDF pueden extraer texto de imágenes PDF o PDFs escaneados. Pero la herramienta **Aspose.PDF for Node.js via C\u002B\u002B** le permite extraer texto fácilmente de cualquier archivo PDF en el entorno Node.js. 

Este código demuestra cómo usar el módulo AsposePDFforNode.js para extraer texto de un archivo PDF especificado y registrar ya sea el texto extraído o los errores encontrados.

Revisa los fragmentos de código y sigue los pasos para extraer texto de tu PDF:

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF del cual se extraerá el texto.
1. Llamar `AsposePdf` como Promise y realiza la operación de extracción de texto. Recibe el objeto si es exitoso.
1. Llame a la función [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. El texto extraído se almacena en el objeto JSON. Por lo tanto, si 'json.errorCode' es 0, el texto extraído se muestra usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF del cual se extraerá el texto.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. El texto extraído se almacena en el objeto JSON. Por lo tanto, si 'json.errorCode' es 0, el texto extraído se muestra usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
