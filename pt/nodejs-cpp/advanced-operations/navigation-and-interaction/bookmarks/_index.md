---
title: Marcadores em PDF no Node.js
linktitle: Marcadores em PDF
type: docs
weight: 10
url: /pt/nodejs-cpp/bookmark/
description: Você pode adicionar ou excluir marcadores em um documento PDF no ambiente Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Excluir um Marcador Específico de um Documento PDF

Você pode excluir marcadores de um arquivo PDF usando Aspose.PDF for Node.js via C\u002B\u002B. Caso queira excluir marcadores de um PDF, você pode usar [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) função. 
Por favor, verifique o trecho de código a seguir para excluir marcadores de um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF do qual os marcadores serão removidos.
1. Chamada `AsposePdf` como Promise e execute a operação para remover o marcador. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Excluir marcadores. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultPdfDeleteBookmarks.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

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

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF do qual os marcadores serão removidos.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Excluir marcadores. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultPdfDeleteBookmarks.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```