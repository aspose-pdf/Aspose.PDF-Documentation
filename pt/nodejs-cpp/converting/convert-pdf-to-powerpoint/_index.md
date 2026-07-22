---
title: Converter PDF para PPTX em Node.js
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: /pt/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-18"
description: Aspose.PDF permite que você converta PDF para o formato PPTX usando Node.js diretamente no ambiente Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF para PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para PPTX com aplicativo gratuito](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Converter PDF para PPTX

Caso queira converter um documento PDF, você pode usar [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoPptX.pptx". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoPptX.pptx". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```