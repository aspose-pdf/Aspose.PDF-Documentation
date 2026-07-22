---
title: Agregar marcas de imagen a PDF en Node.js
linktitle: Marcas de imagen en archivo PDF
type: docs
weight: 60
url: /es/nodejs-cpp/stamping/
description: Agregue la marca de imagen a su documento PDF usando AsposePdfAddStamp con la herramienta Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Agregar marca de imagen en archivo PDF

Estampar un documento PDF es similar a estampar un documento en papel. Una estampilla en un archivo PDF proporciona información adicional al archivo PDF, como proteger el archivo PDF para que otros lo usen y confirmar la seguridad del contenido del archivo PDF.
Puede usar el [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) función para agregar una marca de imagen a un archivo PDF usando Node.js.

Por favor, revise el siguiente fragmento de código para agregar una marca de imagen a un archivo PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF en el que se agregará la marca de imagen.
1. Llamar `AsposePdf` como Promise y realizar la operación para agregar una marca de imagen. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Agregue una marca a un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF en el que se agregará la marca de imagen.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Agregue una marca a un archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultImage.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```