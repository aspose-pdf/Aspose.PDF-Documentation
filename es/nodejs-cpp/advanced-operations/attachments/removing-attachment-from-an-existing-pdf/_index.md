---
title: Eliminando archivos adjuntos de PDF en Node.js
linktitle: Eliminando archivos adjuntos de un PDF existente
type: docs
weight: 10
url: /es/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF puede eliminar archivos adjuntos de tus documentos PDF. Usa el entorno de Node.js para eliminar archivos adjuntos en archivos PDF con Aspose.PDF.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Puede eliminar archivos adjuntos de un archivo PDF usando Aspose.PDF para Node.js a través de C++. En caso de que desee eliminar archivos adjuntos de un PDF, puede usar la función [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/). 
Por favor, consulte el siguiente fragmento de código para eliminar archivos adjuntos de un archivo PDF en el entorno Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF del cual se eliminarán los archivos adjuntos.

1. Llame a `AsposePdf` como Promise y realice la operación para eliminar los adjuntos. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Elimine los adjuntos. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteAttachments.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se contendrá en 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Eliminar adjuntos de un archivo PDF y guardar el "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importar el módulo `asposepdfnodejs`.
1. Especificar el nombre del archivo PDF del cual se eliminarán los adjuntos.
1. Inicializar el módulo AsposePdf. Recibir el objeto si es exitoso.
1. Llamar a la función [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Eliminar adjuntos. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteAttachments.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Eliminar adjuntos de un archivo PDF y guardar en "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```