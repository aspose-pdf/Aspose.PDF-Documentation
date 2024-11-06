---
title: Definir a cor de fundo para PDF em Node.js
linktitle: Definir cor de fundo
type: docs
weight: 80
url: pt/nodejs-cpp/set-background-color/
description: Defina a cor de fundo para o seu arquivo PDF com Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Caso você queira definir a cor de fundo de um PDF, você pode usar a função [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).

Por favor, verifique o seguinte trecho de código para definir a cor de fundo do PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF cuja cor de fundo você deseja definir.
1. Chame `AsposePdf` como Promise e realize a operação para definir a cor de fundo. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
1. Defina a cor de fundo para o arquivo PDF. Você precisa passar 3 argumentos para esta função: um nome de arquivo de entrada, uma cor desejada em forma hexadecimal e um nome de arquivo de saída. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultRotation.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Defina a cor de fundo para o arquivo PDF e salve como "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF cujo fundo você deseja definir.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
1. Defina a cor de fundo para o arquivo PDF. A cor de fundo é definida como "#426bf4", que é um código de cor hexadecimal representando um tom de azul. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultRotation.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Defina a cor de fundo para o arquivo PDF e salve o "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```