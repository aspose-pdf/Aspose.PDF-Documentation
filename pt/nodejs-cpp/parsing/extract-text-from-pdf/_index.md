---
title: Extrair texto de PDF em Node.js
linktitle: Extrair texto de PDF
type: docs
weight: 30
url: /pt/nodejs-cpp/extract-text-from-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF for Node.js via C\u002B\u002B.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Documento PDF

Extrair texto do documento PDF é uma tarefa muito comum e útil. 
Extrair texto de PDFs atende a uma variedade de propósitos, desde melhorar a pesquisa e a disponibilidade até permitir a análise e a automação de dados em diversos campos, como negócios, pesquisa e gestão da informação.

Caso você queira extrair texto de um documento PDF, pode usar [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) função. 
Por favor, verifique o trecho de código a seguir para extrair texto de um arquivo PDF usando Node.js via C\u002B\u002B.

Verifique os trechos de código e siga os passos para extrair texto do seu PDF:

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF do qual o texto será extraído.
1. Chamada `AsposePdf` como Promise e execute a operação para extrair texto. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. O texto extraído é armazenado no objeto JSON. Assim, se ‘json.errorCode’ for 0, o texto extraído é exibido usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF do qual o texto será extraído.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. O texto extraído é armazenado no objeto JSON. Assim, se ‘json.errorCode’ for 0, o texto extraído é exibido usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```