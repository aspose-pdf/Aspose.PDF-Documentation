---
title: Extrair Texto de PDF em Node.js
linktitle: Extrair Texto de PDF
type: docs
weight: 10
url: pt/nodejs-cpp/extract-text/
description: Esta seção descreve como extrair texto de documentos PDF usando o Aspose.PDF para Node.js via toolkit C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Todas as Páginas do Documento PDF

Extrair texto de PDF não é fácil. Apenas alguns leitores de PDF podem extrair texto de imagens em PDF ou PDFs digitalizados. Mas a ferramenta **Aspose.PDF para Node.js via C++** permite que você extraia facilmente texto de todo o arquivo PDF no ambiente Node.js.

Este código demonstra como usar o módulo AsposePDFforNode.js para extrair texto de um arquivo PDF especificado e registrar o texto extraído ou erros encontrados.

Confira os trechos de código e siga os passos para extrair texto do seu PDF:

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.

1. Especifique o nome do arquivo PDF do qual o texto será extraído.
1. Chame `AsposePdf` como Promise e execute a operação para extrair o texto. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. O texto extraído é armazenado no objeto JSON. Assim, se 'json.errorCode' for 0, o texto extraído é exibido usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

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
1. O texto extraído é armazenado no objeto JSON. Assim, se 'json.errorCode' for 0, o texto extraído é exibido usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extrair texto de um arquivo PDF*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```