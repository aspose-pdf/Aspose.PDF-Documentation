---
title: Dividir PDF no Node.js
linktitle: Dividir arquivos PDF
type: docs
weight: 30
url: /nodejs-cpp/split-pdf/
description: Este tópico mostra como dividir páginas de PDF em arquivos PDF individuais com Aspose.PDF para Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dividir PDF em dois arquivos usando Node.js

Caso você queira dividir um único PDF em partes, você pode usar a função [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
Por favor, verifique o trecho de código a seguir para dividir dois PDFs no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome dos arquivos PDF que serão divididos.
1. Chame `AsposePdf` como Promise e realize a operação para dividir o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).

1. Divida dois arquivos PDF. Ele define a variável pageToSplit para 1, indicando que o arquivo PDF será dividido na página 1.
1. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultSplit1.pdf" e "ResultSplit2.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Defina o número de páginas para dividir*/
      const pageToSplit = 1;
      /*Divida em dois arquivos PDF e salve "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.

1. Especifique o nome dos arquivos PDF que serão divididos.
1. Inicialize o módulo AsposePdf. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Divida dois arquivos PDF. Define a variável pageToSplit para 1, indicando que o arquivo PDF será dividido na página 1.
1. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultSplit1.pdf" e "ResultSplit2.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Defina o número de uma página para dividir*/
  const pageToSplit = 1;
  /*Divida em dois arquivos PDF e salve "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```