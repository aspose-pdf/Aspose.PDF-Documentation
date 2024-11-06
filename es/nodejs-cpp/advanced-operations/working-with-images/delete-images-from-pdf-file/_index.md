---
title: Eliminar Imágenes de un Archivo PDF en Node.js
linktitle: Eliminar Imágenes
type: docs
weight: 20
url: es/nodejs-cpp/delete-images-from-pdf-file/
description: Esta sección explica cómo eliminar imágenes de un archivo PDF usando Aspose.PDF para Node.js a través de C++.
lastmod: "2023-11-16"
---

Puedes eliminar imágenes de un archivo PDF usando Aspose.PDF para Node.js a través de C++.

En caso de que desees eliminar imágenes de un PDF, puedes usar la función [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
Por favor, revisa el siguiente fragmento de código para eliminar imágenes en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF del cual se eliminará la imagen.
1. Llama a `AsposePdf` como Promesa y realiza la operación para eliminar imágenes. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).

1. Eliminar imágenes de un PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteImages.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se contendrá en 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Eliminar imágenes de un archivo PDF y guardar en "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importar el módulo `asposepdfnodejs`.
1. Especificar el nombre del archivo PDF en el cual se eliminará la imagen.
1. Inicializar el módulo AsposePdf. Recibir el objeto si es exitoso.

1. Llama a la función [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Elimina imágenes de un PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteImages.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Eliminar imágenes de un archivo PDF y guardar en "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```