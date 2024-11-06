---
title: Otimizar PDF usando Aspose.PDF para Node.js via C++
linktitle: Otimizar Arquivo PDF
type: docs
weight: 10
url: pt/nodejs-cpp/optimize-pdf/
description: Otimizar e comprimir arquivos PDF para visualização rápida na web usando o ambiente Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Otimizar Documento PDF

O toolkit Aspose.PDF para Node.js via C++ permite que você otimize o conteúdo do PDF para o ambiente Node.js.

Otimização, ou linearização, refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador web.

Caso você queira otimizar o PDF, você pode usar a função [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
Por favor, confira o trecho de código a seguir para otimizar arquivos PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será otimizado.

1. Chame `AsposePdf` como Promise e execute a operação para otimizar o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Otimize um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultOptimize.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro serão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Otimize um arquivo PDF e salve como "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF que será otimizado.

1. Inicialize o módulo AsposePdf. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Otimize um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultOptimize.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Otimize um arquivo PDF e salve em "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```