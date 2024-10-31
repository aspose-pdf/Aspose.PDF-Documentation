---
title: Converter PDF para Excel em Node.js
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-16"
keywords: converter PDF para Excel usando node.js, converter PDF para XLSX.
description: Aspose.PDF para Node.js permite converter PDF para o formato XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criando planilhas a partir de PDF usando Node.js 

**Aspose.PDF para Node.js via C++** suporta a funcionalidade de converter arquivos PDF para arquivos Excel.

{{% alert color="success" %}}
**Tente converter PDF para Excel online**

Aspose.PDF para Node.js apresenta a você o aplicativo online gratuito ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para Excel com Aplicativo Gratuito](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Converter PDF para XLSX

Caso você queira converter um documento PDF, você pode usar a função [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chame `AsposePdf` como Promise e execute a operação para converter o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPDFtoXlsX.xlsx". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Converter um arquivo PDF para XlsX e salvar como "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF que será convertido.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPDFtoXlsX.xlsx". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Converter um arquivo PDF para XlsX e salvar como "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```