---
title: Eliminar imágenes de un archivo PDF en Node.js
linktitle: Eliminar imágenes
type: docs
weight: 20
url: /es/nodejs-cpp/delete-images-from-pdf-file/
description: Esta sección explica cómo eliminar imágenes de un archivo PDF usando Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
---


Puedes eliminar imágenes de un archivo PDF usando Aspose.PDF for Node.js via C++.

En caso de que quieras eliminar imágenes de PDF, puedes usar [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) función. 
Por favor, revise el siguiente fragmento de código para eliminar imágenes en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF en el que se eliminará la imagen.
1. Llamar `AsposePdf` como Promise y realiza la operación para eliminar imágenes. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Elimine imágenes de un PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteImages.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF en el que se eliminará la imagen.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Elimine imágenes de un PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteImages.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```