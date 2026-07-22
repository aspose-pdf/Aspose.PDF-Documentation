---
title: Reparar PDF em Node.js
linktitle: Reparar PDF
type: docs
weight: 10
url: /pt/nodejs-cpp/repair-pdf/
description: Este tópico descreve como Reparar PDF no ambiente Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js permite reparo de PDF de alta qualidade. O arquivo PDF pode não abrir por qualquer motivo, independentemente do programa ou navegador. Em alguns casos, o documento pode ser restaurado; experimente o código a seguir e veja por si mesmo.
Caso você queira reparar um documento PDF, pode usar [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) função. 
Por favor, verifique o trecho de código a seguir para reparar o arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será reparado.
1. Chamada `AsposePdf` como Promise e execute a operação para reparar o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repare o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfRepair.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será reparado.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repare o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfRepair.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```