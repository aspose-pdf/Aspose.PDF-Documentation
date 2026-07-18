---
title: Agregar imagen a PDF en Node.js
linktitle: Agregar imagen
type: docs
weight: 10
url: /es/nodejs-cpp/add-image-to-pdf/
description: Esta sección describe cómo agregar una imagen a un archivo PDF existente usando Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
---

## Agregar una imagen a un archivo PDF existente

Se cree comúnmente que agregar imágenes a archivos PDF requiere una herramienta especial compleja. Sin embargo, con Aspose.PDF for Node.js puedes agregar rápida y fácilmente las imágenes que necesitas a PDF en un entorno Node.js.

Solo podemos agregar imágenes al final del archivo, por lo tanto, el ejemplo correcto es que tenemos algunas páginas de documentos escaneados y las convertimos en un solo PDF.

En caso de que desees agregar imágenes, puedes utilizar [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) función. 
Por favor, revisa el siguiente fragmento de código para agregar imágenes en el entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF en el que se agregará la imagen.
1. Llamar `AsposePdf` como Promise y realiza la operación para agregar una imagen. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Agregar imagen al final de un PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF en el que se agregará la imagen.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Agregar imagen al final de un PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultAddImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```