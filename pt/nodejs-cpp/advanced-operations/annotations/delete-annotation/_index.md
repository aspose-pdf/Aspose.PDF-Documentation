---
title: Excluir Anotação no Node.js
linktitle: Excluir Anotação
type: docs
weight: 10
url: pt/nodejs-cpp/delete-annotation/
description: Com Aspose.PDF para Node.js, você pode excluir anotações do seu arquivo PDF.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Você pode excluir anotações de um arquivo PDF usando o Aspose.PDF para Node.js via C++. Caso você queira excluir anotações de um PDF, você pode usar a função [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/). Por favor, verifique o trecho de código a seguir para excluir anotações de um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF do qual a anotação será removida.
1. Chame `AsposePdf` como Promise e realize a operação para remover anotações. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Exclua as anotações. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfDeleteAnnotations.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Excluir anotações de um arquivo PDF e salvar em "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual a anotação será removida.

1. Inicialize o módulo AsposePdf. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Exclua as anotações. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfDeleteAnnotations.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Excluir anotações de um arquivo PDF e salvar como "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```