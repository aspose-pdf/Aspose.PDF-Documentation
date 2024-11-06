---
title: Añadir numeración de página a PDF en Node.js
linktitle: Añadir Número de Página
type: docs
weight: 100
url: es/nodejs-cpp/add-page-number/
description: Aspose.PDF para Node.js vía C++ te permite añadir un sello de número de página a tu archivo PDF usando AsposePdfAddPageNum.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El número de página facilita al lector localizar diferentes partes del documento. Los siguientes fragmentos de código muestran cómo añadir números de página a las páginas de un PDF usando la función [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) en Node.js.

Por favor, revisa el siguiente fragmento de código para añadir números de página en PDF en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especifica el nombre del archivo PDF al que se le añadirán los números de página.
1. Llama a `AsposePdf` como Promise y realiza la operación para añadir números de página. Recibe el objeto si tiene éxito.

1. Llama a la función [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Agrega el número de página a un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddPageNum.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Agregar número de página a un archivo PDF y guardar en "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF al que se agregarán los números de página.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.

1. Llama a la función [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Añadir número de página a un archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddPageNum.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Añadir número de página a un archivo PDF y guardar el "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```