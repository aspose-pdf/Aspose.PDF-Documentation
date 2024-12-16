---
title: Converter PDF/A para formato PDF em Node.js
linktitle: Converter PDF/A para formato PDF
type: docs
weight: 110
url: /pt/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-16"
description: Este tópico mostra como a Aspose.PDF permite converter um arquivo PDF/A em um documento PDF no ambiente Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter PDF/A para formato PDF

Caso você queira converter um documento PDF, você pode usar a função [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/). 
Por favor, verifique o seguinte trecho de código para converter no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chame `AsposePdf` como Promise e execute a operação para converter o arquivo. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultConvertToPDF.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Converter um arquivo PDF/A para PDF e salvar o "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF/A que será convertido.

1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultConvertToPDF.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Converta um arquivo PDF/A para PDF e salve em "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```