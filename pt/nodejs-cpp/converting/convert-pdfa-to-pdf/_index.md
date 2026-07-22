---
title: Converter PDF/A para formato PDF no Node.js
linktitle: Converter PDF/A para formato PDF
type: docs
weight: 110
url: /pt/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2026-07-18"
description: Este tópico mostra como o Aspose.PDF permite converter um arquivo PDF/A para um documento PDF no ambiente Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Converter PDF/A para formato PDF

Caso queira converter um documento PDF, você pode usar [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Converter arquivo PDF. Assim, se \u0027json.errorCode\u0027 for 0, o resultado da operação será salvo em \u0022ResultConvertToPDF.pdf\u0022. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro estarão contidas em \u0027json.errorText\u0027.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF/A que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Converter arquivo PDF. Assim, se \u0027json.errorCode\u0027 for 0, o resultado da operação será salvo em \u0022ResultConvertToPDF.pdf\u0022. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro estarão contidas em \u0027json.errorText\u0027.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```