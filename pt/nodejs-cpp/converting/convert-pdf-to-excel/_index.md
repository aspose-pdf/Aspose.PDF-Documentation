---
title: Converter PDF para Excel em Node.js
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-18"
description: Aspose.PDF for Node.js permite converter PDF para o formato XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criando planilhas a partir de PDF usando Node.js 

**Aspose.PDF for Node.js via C++** suporta o recurso de converter arquivos PDF para arquivo Excel.

{{% alert color="success" %}}
**Tente converter PDF para Excel online**

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Excel com Aplicativo Gratuito](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Converter PDF para XLSX

Caso queira converter um documento PDF, você pode usar [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPDFtoXlsX.xlsx". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPDFtoXlsX.xlsx". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

