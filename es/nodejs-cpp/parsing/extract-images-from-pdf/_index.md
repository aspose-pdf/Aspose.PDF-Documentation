---
title: Extraer Imágenes de PDF en Node.js
linktitle: Extraer Imágenes de PDF
type: docs
weight: 20
url: es/nodejs-cpp/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen de un PDF usando Aspose.PDF para Node.js via C++ toolkit.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer imágenes de archivos PDF en el entorno de Node.js

En caso de que desees extraer imágenes de un documento PDF, puedes usar la función [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/). 
Debemos pasar tres argumentos a esta función: nombre del archivo de entrada, nombre del archivo de salida y resolución.
Por favor, consulta el siguiente fragmento de código para extraer imágenes de un archivo PDF usando Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF del cual se extraerá la imagen.

1. Llama a `AsposePdf` como Promesa y realiza la operación para extraer la imagen. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extrae imágenes del archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfExtractImage{0:D2}.jpg". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se contendrá en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extraer imagen de un archivo PDF con la plantilla "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guardar*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF del cual se extraerá la imagen.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extrae imágenes del archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfExtractImage{0:D2}.jpg". Donde {0:D2} representa el número de página con un formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extraer imagen de un archivo PDF con la plantilla "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolución 150 DPI y guardar*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```