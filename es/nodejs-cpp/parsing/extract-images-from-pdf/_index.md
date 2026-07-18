---
title: Extraer imágenes de PDF en Node.js
linktitle: Extraer imágenes de PDF
type: docs
weight: 20
url: /es/nodejs-cpp/extract-images-from-the-pdf-file/
description: Cómo extraer una parte de la imagen de un PDF usando Aspose.PDF for Node.js via C++ toolkit.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer imágenes de archivos PDF en el entorno Node.js

En caso de que desee extraer imágenes de un documento PDF, puede usar [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) función. 
Debemos pasar tres argumentos a esta función: el nombre del archivo de entrada y salida y la resolución.
Por favor, revise el siguiente fragmento de código para extraer imágenes de un archivo PDF usando Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF del cual se extraerá la imagen.
1. Llamar `AsposePdf` como Promise y realizar la operación para extraer la imagen. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extraiga imágenes del archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfExtractImage{0:D2}.jpg". Donde {0:D2} representa el número de página con formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF del cual se extraerá la imagen.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extraiga imágenes del archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfExtractImage{0:D2}.jpg". Donde {0:D2} representa el número de página con formato de dos dígitos. Las imágenes se guardan con una resolución de 150 DPI. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
