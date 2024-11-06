---
title: Añadir Imagen a PDF en Node.js
linktitle: Añadir Imagen
type: docs
weight: 10
url: es/nodejs-cpp/add-image-to-pdf/
description: Esta sección describe cómo añadir una imagen a un archivo PDF existente usando Aspose.PDF para Node.js vía C++.
lastmod: "2023-11-16"
---

## Añadir una imagen a un archivo PDF existente

Comúnmente se cree que agregar imágenes a archivos PDF requiere una herramienta especial compleja. Sin embargo, con Aspose.PDF para Node.js puedes rápida y fácilmente añadir las imágenes que necesitas al PDF en el entorno de Node.js.

Podemos agregar imágenes solo al final del archivo, por lo tanto, el ejemplo correcto es tener algunas páginas de documentos escaneados y convertirlas en un solo PDF.

En caso de que quieras añadir imágenes, puedes usar la función [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
Por favor, revisa el siguiente fragmento de código para añadir imágenes en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.

1. Especifique el nombre del archivo PDF en el cual se añadirá la imagen.
1. Llame a `AsposePdf` como Promesa y realice la operación para agregar la imagen. Reciba el objeto si es exitoso.
1. Llame a la función [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Añadir imagen al final de un PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Añadir una imagen al final de un archivo PDF y guardar el "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF en el que se añadirá la imagen.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Añade una imagen al final de un PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Añadir una imagen al final de un archivo PDF y guardar en "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```