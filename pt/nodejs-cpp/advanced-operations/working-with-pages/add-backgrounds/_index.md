---
title: Adicionar fundo ao PDF em Node.js
linktitle: Adicionar fundo
type: docs
weight: 10
url: pt/nodejs-cpp/add-background/
description: Adicione uma imagem de fundo ao seu arquivo PDF em Node.js
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Os seguintes trechos de código mostram como adicionar uma imagem de fundo a páginas PDF usando a função [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) em Node.js.

Confira o seguinte trecho de código para adicionar uma imagem de fundo no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF no qual a imagem de fundo será adicionada.
1. Chame `AsposePdf` como Promise e realize a operação para adicionar a imagem de fundo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).

1. Adicione uma imagem de fundo a um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultAddBackgroundImage.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações sobre o erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Adicione uma imagem de fundo a um arquivo PDF e salve como "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF no qual a imagem de fundo será adicionada.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. Adicione imagem de fundo a um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultAddBackgroundImage.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Adicione imagem de fundo a um arquivo PDF e salve como "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```