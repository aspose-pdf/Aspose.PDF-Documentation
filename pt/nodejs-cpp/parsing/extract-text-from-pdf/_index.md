---
title: Extrair Texto de PDF em Node.js
linktitle: Extrair texto de PDF
type: docs
weight: 30
url: pt/nodejs-cpp/extract-text-from-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF para Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Documento PDF

Extrair texto de um documento PDF é uma tarefa muito comum e útil.
Extrair texto de PDFs serve para uma variedade de propósitos, desde melhorar a busca e disponibilidade até permitir a análise e automação de dados em vários campos, como negócios, pesquisa e gestão da informação.

Caso você queira extrair texto de um documento PDF, você pode usar a função [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
Por favor, verifique o trecho de código a seguir para extrair texto de um arquivo PDF usando Node.js via C++.

Confira os trechos de código e siga os passos para extrair texto do seu PDF:

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF do qual o texto será extraído.
1. Chame `AsposePdf` como Promise e execute a operação para extrair texto. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. O texto extraído é armazenado no objeto JSON. Assim, se 'json.errorCode' for 0, o texto extraído é exibido usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extrair texto de um arquivo PDF*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual o texto será extraído.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. O texto extraído é armazenado no objeto JSON. Assim, se 'json.errorCode' for 0, o texto extraído será exibido usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro serão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extrair texto de um arquivo PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```