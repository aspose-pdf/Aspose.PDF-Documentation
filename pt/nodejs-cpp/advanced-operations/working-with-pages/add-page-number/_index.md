---
title: Adicionar numeração de páginas ao PDF em Node.js
linktitle: Adicionar Número de Página
type: docs
weight: 100
url: /pt/nodejs-cpp/add-page-number/
description: O Aspose.PDF para Node.js via C++ permite adicionar um carimbo de número de página ao seu arquivo PDF usando AsposePdfAddPageNum.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

O número da página facilita para o leitor localizar diferentes partes do documento. Os seguintes trechos de código mostram como adicionar números de página às páginas PDF usando a função [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) em Node.js.

Por favor, verifique o seguinte trecho de código para adicionar números de página em um PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF no qual os números de página serão adicionados.
1. Chame `AsposePdf` como Promise e execute a operação para adicionar números de página. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Adicione número de página a um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultAddPageNum.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Adicione número de página a um arquivo PDF e salve como "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF no qual os números de página serão adicionados.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Adicione número de página a um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultAddPageNum.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Adicione número de página a um arquivo PDF e salve em "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```