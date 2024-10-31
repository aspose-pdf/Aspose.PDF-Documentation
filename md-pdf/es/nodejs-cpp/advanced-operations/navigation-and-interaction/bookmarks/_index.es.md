---
title: Marcadores en PDF en Node.js
linktitle: Marcadores en PDF
type: docs
weight: 10
url: /nodejs-cpp/bookmark/
description: Puede agregar o eliminar marcadores en un documento PDF en el entorno de Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Eliminar un Marcador Particular de un Documento PDF

Puede eliminar marcadores de un archivo PDF utilizando Aspose.PDF para Node.js a través de C++. En caso de que desee eliminar marcadores de un PDF, puede usar la función [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/). 
Por favor, consulte el siguiente fragmento de código para eliminar marcadores de un archivo PDF en el entorno de Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF del cual se eliminarán los marcadores.
1. Llame a `AsposePdf` como Promise y realice la operación para eliminar el marcador. Reciba el objeto si tiene éxito.

1. Llama a la función [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Elimina los marcadores. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteBookmarks.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error se contendrá en 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Eliminar marcadores de un archivo PDF y guardar en el "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF del cual se eliminarán los marcadores.

1. Inicializar el módulo AsposePdf. Recibir el objeto si tiene éxito.  
1. Llamar a la función [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).  
1. Eliminar marcadores. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteBookmarks.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se contendrá en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Eliminar marcadores de un archivo PDF y guardar en "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```