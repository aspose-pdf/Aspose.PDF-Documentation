---
title: Adicionar Imagem ao PDF em Node.js 
linktitle: Adicionar Imagem
type: docs
weight: 10
url: pt/nodejs-cpp/add-image-to-pdf/
description: Esta seção descreve como adicionar imagem a um arquivo PDF existente usando Aspose.PDF para Node.js via C++.
lastmod: "2023-11-16"
---

## Adicionar uma imagem a um arquivo PDF existente

Acredita-se comumente que adicionar imagens a arquivos PDF requer uma ferramenta especial complexa. No entanto, com Aspose.PDF para Node.js você pode rápida e facilmente adicionar as imagens que precisa ao PDF no ambiente Node.js.

Podemos adicionar imagens apenas ao final do arquivo, portanto, o exemplo correto é termos algumas páginas de documentos digitalizados e convertê-las em um único PDF.

Caso você queira adicionar imagens, você pode usar a função [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/). 
Por favor, verifique o trecho de código a seguir para adicionar imagens no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.

1. Especifique o nome do arquivo PDF no qual a imagem será adicionada.
1. Chame `AsposePdf` como Promise e execute a operação para adicionar imagem. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Adicione a imagem ao final de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultAddImage.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro serão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Adicione uma imagem ao final de um arquivo PDF e salve no "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF no qual a imagem será adicionada.
1. Inicialize o módulo AsposePdf. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Adicione a imagem ao final de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultAddImage.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Adicione uma imagem ao final de um arquivo PDF e salve em "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```