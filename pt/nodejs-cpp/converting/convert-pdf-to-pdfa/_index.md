---
title: Converter formatos PDF para PDF/A em Node.js 
linktitle: Converter formatos PDF para PDF/A
type: docs
weight: 100
url: pt/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-16"
description: Este tópico mostra como o Aspose.PDF permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A no ambiente Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para Node.js** permite que você converta um arquivo PDF em um arquivo PDF compatível com <abbr title="Formato de Documento Portátil para Arquivamento de documentos eletrônicos">PDF/A</abbr>.

{{% alert color="success" %}}
**Tente converter PDF para PDF/A online**

Aspose.PDF para Node.js apresenta a você o aplicativo gratuito online ["PDF para PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), onde você pode experimentar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão de PDF para PDF/A com Aplicativo Gratuito](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## Converter PDF para formato PDF/A

Caso você queira converter um documento PDF, você pode usar a função [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
 
Por favor, verifique o seguinte trecho de código para converter no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chame `AsposePdf` como Promise e execute a operação para converter o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Repare o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultConvertToPDFA.pdf". Durante o processo de conversão, a validação é realizada, e os resultados da validação são salvos como "ResultConvertToPDFALog.xml." Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Converter um arquivo PDF para PDF/A(1A) e salvar como "ResultConvertToPDFA.pdf"*/
      /*Durante o processo de conversão, a validação também é realizada, "ResultConvertToPDFALog.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF que será convertido.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Repare o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultConvertToPDFA.pdf". Durante o processo de conversão, a validação é realizada, e os resultados da validação são salvos como "ResultConvertToPDFALog.xml." Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Converter um arquivo PDF para PDF/A(1A) e salvar como "ResultConvertToPDFA.pdf"*/
  /*Durante o processo de conversão, a validação também é realizada, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```