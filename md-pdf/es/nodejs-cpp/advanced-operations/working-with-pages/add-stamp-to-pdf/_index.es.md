---
title: Añadir sellos de imagen a PDF en Node.js
linktitle: Sellos de imagen en archivo PDF
type: docs
weight: 60
url: /nodejs-cpp/stamping/
description: Añadir el sello de imagen en su documento PDF utilizando AsposePdfAddStamp con la herramienta Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir sello de imagen en archivo PDF

Estampar un documento PDF es similar a estampar un documento de papel. Un sello en un archivo PDF proporciona información adicional al archivo PDF, como proteger el archivo PDF para que otros lo usen y confirmar la seguridad del contenido del archivo PDF.
Puede usar la función [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) para agregar un sello de imagen a un archivo PDF usando Node.js.

Por favor, revise el siguiente fragmento de código para agregar un sello de imagen a un archivo PDF en el entorno de Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como la variable `AsposePdf`.

1. Especifique el nombre del archivo PDF en el que se añadirá el sello de imagen.
1. Llame a `AsposePdf` como Promesa y realice la operación para agregar el sello de imagen. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Agregue el sello a un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js
  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Añadir sello a un archivo PDF y guardar el "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
2. Especifica el nombre del archivo PDF en el que se añadirá el sello de imagen.
3. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
4. Llama a la función [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
5. Añade un sello a un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Añadir un sello a un archivo PDF y guardar en "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```