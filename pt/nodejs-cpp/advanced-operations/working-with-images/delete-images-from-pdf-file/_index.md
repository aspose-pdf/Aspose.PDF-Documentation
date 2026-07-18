---
title: Excluir Imagens de Arquivo PDF em Node.js
linktitle: Excluir Imagens
type: docs
weight: 20
url: /pt/nodejs-cpp/delete-images-from-pdf-file/
description: Esta seção explica como excluir Imagens de Arquivo PDF usando Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
---


Você pode excluir imagens de um arquivo PDF usando Aspose.PDF for Node.js via C++.

Caso você queira excluir imagens de PDF, pode usar [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) função. 
Por favor, verifique o trecho de código a seguir para excluir imagens no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF no qual a imagem será removida.
1. Chamada `AsposePdf` como Promise e execute a operação para remover imagens. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Exclua imagens de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfDeleteImages.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF no qual a imagem será removida.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Exclua imagens de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfDeleteImages.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```