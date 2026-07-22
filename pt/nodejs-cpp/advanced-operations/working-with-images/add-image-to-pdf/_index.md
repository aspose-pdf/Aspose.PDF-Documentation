---
title: Adicionar imagem ao PDF em Node.js
linktitle: Adicionar imagem
type: docs
weight: 10
url: /pt/nodejs-cpp/add-image-to-pdf/
description: Esta seção descreve como adicionar imagem a um arquivo PDF existente usando Aspose.PDF for Node.js via C\u002B\u002B.
lastmod: "2026-07-18"
---

## Adicionar uma imagem a um arquivo PDF existente

É comumente acreditado que adicionar imagens a arquivos PDF requer uma ferramenta especial complexa. No entanto, com Aspose.PDF for Node.js você pode rapidamente e facilmente adicionar as imagens necessárias ao PDF no ambiente Node.js.

Podemos adicionar imagens apenas ao final do arquivo, portanto o exemplo correto é que temos algumas páginas de documentos escaneados e as convertemos em um único PDF.

Caso você queira adicionar imagens, pode usar [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) função. 
Por favor, verifique o trecho de código a seguir para adicionar imagens no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF no qual a imagem será adicionada.
1. Chamada `AsposePdf` como Promise e execute a operação para adicionar imagem. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Adicione a imagem ao final de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultAddImage.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF no qual a imagem será adicionada.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Adicione a imagem ao final de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultAddImage.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```