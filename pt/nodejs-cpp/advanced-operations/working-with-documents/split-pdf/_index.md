---
title: Dividir PDF em Node.js
linktitle: Dividir arquivos PDF
type: docs
weight: 30
url: /pt/nodejs-cpp/split-pdf/
description: Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais com Aspose.PDF for Node.js via C\u002B\u002B .
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dividir PDF em dois arquivos usando Node.js

Caso você queira dividir um único PDF em partes, você pode usar [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) função. 
Por favor, verifique o trecho de código a seguir para dividir dois PDFs em um ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome dos arquivos PDF que serão divididos.
1. Chamada `AsposePdf` como Promise e execute a operação de divisão de arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Divida dois arquivos PDF. Ele define a variável pageToSplit como 1, indicando que o arquivo PDF será dividido na página 1. 
1. Assim, se ‘json.errorCode’ for 0, o resultado da operação é salvo em “ResultSplit1.pdf” e “ResultSplit2.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome dos arquivos PDF que serão divididos.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Divida dois arquivos PDF. Ele define a variável pageToSplit como 1, indicando que o arquivo PDF será dividido na página 1. 
1. Assim, se ‘json.errorCode’ for 0, o resultado da operação é salvo em “ResultSplit1.pdf” e “ResultSplit2.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```