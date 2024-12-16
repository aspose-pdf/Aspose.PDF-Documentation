---
title: Extraer Texto de PDF en Node.js
linktitle: Extraer texto de PDF
type: docs
weight: 30
url: /es/nodejs-cpp/extract-text-from-pdf/
description: Este artículo describe varias formas de extraer texto de documentos PDF usando Aspose.PDF para Node.js a través de C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Texto del Documento PDF

Extraer texto del documento PDF es una tarea muy común y útil. Extraer texto de los PDFs sirve para una variedad de propósitos, desde mejorar la búsqueda y la disponibilidad hasta permitir el análisis y la automatización de datos en varios campos como negocios, investigación y gestión de información.

En caso de que quiera extraer texto de un documento PDF, puede usar la función [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/). Por favor revise el siguiente fragmento de código para extraer texto de un archivo PDF usando Node.js a través de C++.

Revise los fragmentos de código y siga los pasos para extraer texto de su PDF:


**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especifica el nombre del archivo PDF del cual se extraerá el texto.
1. Llama a `AsposePdf` como Promesa y realiza la operación para extraer texto. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. El texto extraído se almacena en el objeto JSON. Así, si 'json.errorCode' es 0, el texto extraído se muestra usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

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

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF del cual se extraerá el texto.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. El texto extraído se almacena en el objeto JSON. Por lo tanto, si 'json.errorCode' es 0, el texto extraído se muestra usando console.log. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extraer texto de un archivo PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```