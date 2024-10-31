---
title: Añadir Encabezado y Pie de Página a PDF en Node.js
linktitle: Añadir Encabezado y Pie de Página a PDF
type: docs
weight: 70
url: /nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para Node.js a través de C++ le permite añadir encabezados y pies de página a su archivo PDF usando AsposePdfAddTextHeaderFooter.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF para Node.js a través de C++** le permite añadir encabezado y pie de página en su archivo PDF existente.

En caso de que desee añadir encabezado y pie de página, puede usar la función [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).

Por favor, revise el siguiente fragmento de código para añadir encabezado y pie de página a un archivo PDF en el entorno de Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF en el que se añadirán el encabezado y el pie de página.

1. Llama a `AsposePdf` como Promesa y realiza la operación para agregar encabezado y pie de página. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Agrega texto en el Encabezado y Pie de página de un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddHeaderFooter.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Agregar texto en el Encabezado/Pie de página de un archivo PDF y guardar el "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF en el cual se agregarán el encabezado y el pie de página.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Agrega texto en el Encabezado y Pie de página de un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddHeaderFooter.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Agregar texto en Encabezado/Pie de página de un archivo PDF y guardar en "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```