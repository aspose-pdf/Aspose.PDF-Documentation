---
title: Reparar PDF em Node.js 
linktitle: Reparar PDF
type: docs
weight: 10
url: /nodejs-cpp/repair-pdf/
description: Este tópico descreve como reparar PDF no ambiente Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF para Node.js permite reparo de PDF de alta qualidade. O arquivo PDF pode não abrir por qualquer motivo, independentemente do programa ou navegador. Em alguns casos, o documento pode ser restaurado, tente o código a seguir e veja por si mesmo.
Caso você queira reparar um documento PDF, você pode usar a função [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/). 
Por favor, verifique o trecho de código a seguir para reparar arquivos PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como a variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será reparado.
1. Chame `AsposePdf` como Promise e execute a operação para reparar o arquivo. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repare o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfRepair.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repare um arquivo PDF e salve como "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF que será reparado.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repare o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfRepair.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações sobre o erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Reparar um arquivo PDF e salvar em "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```