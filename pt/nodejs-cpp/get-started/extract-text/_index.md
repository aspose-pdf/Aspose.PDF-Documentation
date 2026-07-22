---
title: Extrair texto de PDF no Node.js
linktitle: Extrair texto de PDF
type: docs
weight: 10
url: /pt/nodejs-cpp/extract-text/
description: Esta seção descreve como extrair texto de um documento PDF usando o Aspose.PDF for Node.js via C++ toolkit.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair texto de todas as páginas do documento PDF

Extrair texto de PDF não é fácil. Apenas alguns leitores de PDF podem extrair texto de imagens PDF ou PDFs escaneados. Mas a ferramenta **Aspose.PDF for Node.js via C++** permite que você extraia texto facilmente de todos os arquivos PDF no ambiente Node.js. 

Este código demonstra como usar o módulo AsposePDFforNode.js para extrair texto de um arquivo PDF especificado e registrar tanto o texto extraído quanto os erros encontrados.

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
