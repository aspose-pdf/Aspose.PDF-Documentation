---
title: Rotar Páginas PDF en Node.js
linktitle: Rotar Páginas PDF
type: docs
weight: 50
url: /es/nodejs-cpp/rotate-pages/
description: Este tema describe cómo rotar la orientación de la página en un archivo PDF existente programáticamente en el entorno de Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Esta sección describe cómo rotar páginas en un archivo PDF existente usando Aspose.PDF para Node.js a través de C++.

En caso de que desee rotar páginas PDF, puede usar la función [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). Esta función utiliza un parámetro especial 'AsposePdfModule.Rotation' para el valor de rotación. Con el cual puede establecer cuántos grados necesita rotar el PDF. Hay variantes: Ninguno, 90, 180 o 270 grados.

Por favor, revise el siguiente fragmento de código para rotar páginas PDF en el entorno de Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.

1. Especifica el nombre del archivo PDF para rotar.
1. Llama a `AsposePdf` como Promesa y realiza la operación para rotar páginas. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
1. Rota todos los archivos PDF. La rotación se establece a 270 grados (on270). Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultRotation.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotar páginas de PDF y guardar en "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF a rotar.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Rota todos los archivos PDF. La rotación se establece a 270 grados (on270). Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultRotation.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rota las páginas del PDF y guarda el "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```