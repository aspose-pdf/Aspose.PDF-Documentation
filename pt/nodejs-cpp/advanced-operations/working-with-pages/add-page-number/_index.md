---
title: Adicionar numeração de página ao PDF em Node.js
linktitle: Adicionar número de página
type: docs
weight: 100
url: /pt/nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++ permite que você adicione um carimbo de número de página ao seu arquivo PDF usando AsposePdfAddPageNum.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

O número da página facilita ao leitor localizar diferentes partes do documento. O trecho de código a seguir mostra como adicionar números de página às páginas PDF usando o [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) função em Node.js.

Por favor, verifique o trecho de código a seguir para adicionar números de página ao PDF em um ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF no qual os números de página serão adicionados.
1. Chamada `AsposePdf` como Promise e execute a operação para adicionar numeração de páginas. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Adicione número de página a um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em \"ResultAddPageNum.pdf\". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add page number to a PDF-file save the "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF no qual os números de página serão adicionados.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Adicione número de página a um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em \"ResultAddPageNum.pdf\". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add page number to a PDF-file and save the "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```