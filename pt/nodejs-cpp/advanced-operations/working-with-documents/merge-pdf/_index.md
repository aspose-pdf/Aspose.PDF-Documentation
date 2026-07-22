---
title: Como Mesclar PDF no Node.js
linktitle: Mesclar arquivos PDF
type: docs
weight: 20
url: /pt/nodejs-cpp/merge-pdf/
description: Esta página explica como mesclar documentos PDF em um único arquivo PDF com Aspose.PDF for Node.js via C\u002B\u002B.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Mesclar ou combinar dois PDFs em um único PDF no Node.js

Combinar e mesclar arquivos é uma tarefa muito popular ao trabalhar com um grande número de documentos. Às vezes, ao lidar com documentos e imagens, quando são escaneados, processados e organizados, vários arquivos são criados.
Mas e se você precisar armazenar tudo em um único arquivo? Ou você não quer imprimir vários documentos? Concatenar dois arquivos PDF com Aspose.PDF for Node.js via C\u002B\u002B.

Caso você queira mesclar dois PDFs, pode usar [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) função. 
Por favor, verifique o trecho de código a seguir para mesclar dois arquivos PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome dos arquivos PDF que serão mesclados.
1. Chamada `AsposePdf` como Promise e execute a operação de mesclagem. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Mescle dois arquivos PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultMerge.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome dos arquivos PDF que serão mesclados.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Mescle dois arquivos PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultMerge.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```