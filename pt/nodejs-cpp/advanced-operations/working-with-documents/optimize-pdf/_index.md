---
title: Otimizar PDF usando Aspose.PDF for Node.js via C++
linktitle: Otimizar arquivo PDF
type: docs
weight: 10
url: /pt/nodejs-cpp/optimize-pdf/
description: Otimizar e compactar arquivos PDF para visualização web rápida usando o ambiente Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Otimizar documento PDF

O Toolkit da Aspose.PDF for Node.js via C++ permite otimizar o conteúdo PDF para o ambiente Node.js. 

Otimização, ou linearização, refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador web.

Caso você queira otimizar PDF, pode usar [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) função. 
Por favor, verifique o trecho de código a seguir para otimizar arquivos PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será otimizado.
1. Chamada `AsposePdf` como Promise e execute a operação para otimizar o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Otimize um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultOptimize.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será otimizado.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Otimize um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultOptimize.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```