---
title: Extrair Tabelas de PDF em Node.js
linktitle: Extrair Tabelas de PDF
type: docs
weight: 10
url: pt/nodejs-cpp/extract-tables-from-the-pdf-file/
description: Como converter PDF para CSV usando Aspose.PDF para Node.js via ferramenta C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair tabelas ao converter arquivos PDF para CSV

### Converter PDF para CSV

Se houver tabelas no PDF, elas serão salvas em arquivos CSV separados. Caso você queira converter um documento PDF, você pode usar a função [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/). 
Por favor, verifique o seguinte trecho de código para converter arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chame `AsposePdf` como Promise e execute a operação para converter o arquivo. Receba o objeto se for bem-sucedido.

1. Chame a função [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPDFtoXlsX.xlsx". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Converte um arquivo PDF para CSV (extrai tabelas) com o modelo "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... formato número de página), TAB como delimitador e salva*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.

1. Especifique o nome do arquivo PDF que será convertido.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoXlsX.xlsx". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Converter um arquivo PDF para CSV (extrair tabelas) com o modelo "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... formato número da página), TAB como delimitador e salvar*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```