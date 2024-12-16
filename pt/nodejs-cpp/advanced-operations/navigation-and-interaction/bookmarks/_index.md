---
title: Marcadores em PDF no Node.js
linktitle: Marcadores em PDF
type: docs
weight: 10
url: /pt/nodejs-cpp/bookmark/
description: Você pode adicionar ou deletar marcadores em um documento PDF no ambiente Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Deletar um Marcador Específico de um Documento PDF

Você pode deletar marcadores de um arquivo PDF usando Aspose.PDF para Node.js via C++. Caso você queira deletar marcadores de um PDF, você pode usar a função [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/). 
Por favor, verifique o seguinte trecho de código para deletar marcadores de um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF do qual os marcadores serão removidos.
1. Chame `AsposePdf` como Promise e execute a operação para remover o marcador. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Exclua os marcadores. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfDeleteBookmarks.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Excluir marcadores de um arquivo PDF e salvar como "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual os marcadores serão removidos.

1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Exclua os marcadores. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfDeleteBookmarks.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro serão contidas em 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Excluir marcadores de um arquivo PDF e salvar em "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```