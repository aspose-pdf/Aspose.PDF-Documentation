---
title: Excluir Imagens de Arquivo PDF em Node.js
linktitle: Excluir Imagens
type: docs
weight: 20
url: pt/nodejs-cpp/delete-images-from-pdf-file/
description: Esta seção explica como excluir imagens de um arquivo PDF usando Aspose.PDF para Node.js via C++.
lastmod: "2023-11-16"
---

Você pode excluir imagens de um arquivo PDF usando Aspose.PDF para Node.js via C++.

Caso você queira excluir imagens de um PDF, você pode usar a função [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/). 
Por favor, verifique o seguinte trecho de código para excluir imagens no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF no qual a imagem será removida.
1. Chame `AsposePdf` como Promise e execute a operação para remover imagens. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).

1. Excluir imagens de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfDeleteImages.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro em seu arquivo, as informações sobre o erro estarão contidas em 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Excluir imagens de um arquivo PDF e salvar como "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual a imagem será removida.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Delete imagens de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfDeleteImages.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro serão contidas em 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Exclua imagens de um arquivo PDF e salve em "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```