---
title: Adicionar plano de fundo ao PDF em Node.js
linktitle: Adicionar plano de fundo
type: docs
weight: 10
url: /pt/nodejs-cpp/add-background/
description: Adicionar uma imagem de plano de fundo ao seu arquivo PDF em Node.js
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Os trechos de código a seguir mostram como adicionar uma imagem de plano de fundo às páginas PDF usando o [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) função em Node.js.

Por favor, verifique o trecho de código a seguir para adicionar uma imagem de plano de fundo no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF no qual a imagem de plano de fundo será adicionada.
1. Chamada `AsposePdf` como Promise e execute a operação de adição de imagem de fundo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. Adicione uma imagem de plano de fundo a um arquivo PDF. Portanto, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultAddBackgroundImage.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro em seu arquivo, a informação do erro estará contida em ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF no qual a imagem de plano de fundo será adicionada.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. Adicione uma imagem de plano de fundo a um arquivo PDF. Portanto, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultAddBackgroundImage.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro em seu arquivo, a informação do erro estará contida em ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```