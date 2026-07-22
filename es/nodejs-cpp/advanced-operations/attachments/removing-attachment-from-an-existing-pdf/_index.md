---
title: Eliminar adjuntos de PDF en Node.js
linktitle: Eliminar adjunto de un PDF existente
type: docs
weight: 10
url: /es/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF puede eliminar adjuntos de sus documentos PDF. Utilice el entorno Node.js para eliminar adjuntos en archivos PDF mediante Aspose.PDF.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Puede eliminar adjuntos de un archivo PDF utilizando Aspose.PDF for Node.js via C++. En caso de que desee eliminar adjuntos de un PDF, puede usar [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) función. 
Por favor, revise el siguiente fragmento de código para eliminar adjuntos de un archivo PDF en el entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF del cual se eliminarán los adjuntos.
1. Llamar `AsposePdf` como Promise y ejecutar la operación para eliminar los archivos adjuntos. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Elimine los adjuntos. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteAttachments.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF del cual se eliminarán los adjuntos.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Elimine los adjuntos. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteAttachments.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```