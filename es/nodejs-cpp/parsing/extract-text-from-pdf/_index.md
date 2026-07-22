---
title: Analizar texto de PDF en Node.js
linktitle: Analizar texto de PDF
type: docs
weight: 30
url: /es/nodejs-cpp/extract-text-from-pdf/
description: Este artículo describe varias formas de analizar texto de documentos PDF usando Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Analizar texto de documento PDF

Analizar texto del documento PDF es una tarea muy común y útil. 
Extraer texto de PDFs sirve para una variedad de propósitos, desde mejorar la búsqueda y la disponibilidad hasta habilitar el análisis y la automatización de datos en diversos campos como los negocios, la investigación y la gestión de la información.

En caso de que desees extraer texto de un documento PDF, puedes usar [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) función. 
Por favor, revisa el siguiente fragmento de código para extraer texto de un archivo PDF usando Node.js vía C++.

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