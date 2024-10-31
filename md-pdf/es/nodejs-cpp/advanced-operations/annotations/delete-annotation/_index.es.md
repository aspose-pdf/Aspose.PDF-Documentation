---
title: Eliminar Anotación en Node.js
linktitle: Eliminar Anotación
type: docs
weight: 10
url: /nodejs-cpp/delete-annotation/
description: Con Aspose.PDF para Node.js puedes eliminar anotaciones de tu archivo PDF.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Puedes eliminar anotaciones de un archivo PDF usando Aspose.PDF para Node.js vía C++. En caso de que quieras eliminar anotaciones de un PDF, puedes usar la función [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/). 
Por favor, revisa el siguiente fragmento de código para eliminar anotaciones de un archivo PDF en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifica el nombre del archivo PDF del cual se eliminará la anotación.
1. Llama a `AsposePdf` como Promise y realiza la operación para eliminar anotaciones. Recibe el objeto si es exitoso.

1. Llame a la función [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Eliminar anotaciones. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteAnnotations.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Eliminar anotaciones de un archivo PDF y guardar en "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importe el módulo `asposepdfnodejs`.
1. Especifique el nombre del archivo PDF del cual se eliminará la anotación.

1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Eliminar anotaciones. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPdfDeleteAnnotations.pdf". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Eliminar anotaciones de un archivo PDF y guardar en "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```