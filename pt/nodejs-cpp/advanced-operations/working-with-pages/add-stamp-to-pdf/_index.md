---
title: Adicionar carimbos de imagem ao PDF em Node.js
linktitle: Carimbos de imagem em arquivo PDF
type: docs
weight: 60
url: /pt/nodejs-cpp/stamping/
description: Adicione o carimbo de imagem ao seu documento PDF usando AsposePdfAddStamp com a ferramenta Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar carimbo de imagem em arquivo PDF

Carimbar um documento PDF é semelhante a carimbar um documento de papel. Um carimbo em um arquivo PDF fornece informações adicionais ao arquivo PDF, como proteger o arquivo PDF para que outros o utilizem e confirmar a segurança do conteúdo do arquivo PDF.
Você pode usar o [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) função para adicionar um carimbo de imagem a um arquivo PDF usando Node.js.

Por favor, verifique o trecho de código a seguir para adicionar um carimbo de imagem a um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF no qual o carimbo de imagem será adicionado.
1. Chamada `AsposePdf` como Promise e execute a operação para adicionar o selo de imagem. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Adicione um carimbo a um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultImage.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF no qual o carimbo de imagem será adicionado.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Adicione um carimbo a um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultImage.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```