---
title: Definir a cor de fundo para PDF em Node.js
linktitle: Definir cor de fundo
type: docs
weight: 80
url: /pt/nodejs-cpp/set-background-color/
description: Definir cor de fundo para o seu arquivo PDF com Node.js via C\u002B\u002B.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Caso você queira definir a cor de fundo de um PDF, você pode usar [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) função. 

Por favor, verifique o seguinte trecho de código para definir a cor de fundo de um PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF cuja cor de fundo você deseja definir.
1. Chamada `AsposePdf` como Promise e execute a operação para definir a cor de fundo. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Defina a cor de fundo para o arquivo PDF. Você precisa passar 3 argumentos para esta função: um nome de arquivo de entrada, uma cor desejada em formato hexadecimal e um nome de arquivo de saída. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultRotation.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF cuja cor de fundo você deseja definir.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Defina a cor de fundo para o arquivo PDF. A cor de fundo é definida como "#426bf4," que é um código de cor hexadecimal representando um tom de azul. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultRotation.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```