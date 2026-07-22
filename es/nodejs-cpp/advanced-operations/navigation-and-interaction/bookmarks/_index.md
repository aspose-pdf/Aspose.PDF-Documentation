---
title: Marcadores en PDF en Node.js
linktitle: Marcadores en PDF
type: docs
weight: 10
url: /es/nodejs-cpp/bookmark/
description: Puede agregar o eliminar marcadores en un documento PDF en el entorno Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Eliminar un marcador específico de un documento PDF

Puede eliminar marcadores de un archivo PDF usando Aspose.PDF for Node.js via C++. En caso de que quiera eliminar marcadores de un PDF, puede usar [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) función. 
Por favor, revise el siguiente fragmento de código para eliminar marcadores de un archivo PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifique el nombre del archivo PDF del cual se eliminarán los marcadores.
1. Llamar `AsposePdf` como Promise y ejecutar la operación para eliminar el marcador. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Eliminar marcadores. Por lo tanto, si ‘json.errorCode’ es 0, el resultado de la operación se guarda en “ResultPdfDeleteBookmarks.pdf”. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en ‘json.errorText’.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifique el nombre del archivo PDF del cual se eliminarán los marcadores.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Eliminar marcadores. Por lo tanto, si ‘json.errorCode’ es 0, el resultado de la operación se guarda en “ResultPdfDeleteBookmarks.pdf”. Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en ‘json.errorText’.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```