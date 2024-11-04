---
title: Otimizar Recursos de PDF em Node.js
linktitle: Otimizar Recursos de PDF
type: docs
weight: 15
url: /nodejs-cpp/optimize-pdf-resources/
description: Otimize recursos de arquivos PDF para visualização rápida na web usando a ferramenta Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Otimizar Recursos de PDF

Otimizar recursos no documento:

1. Recursos que não são usados nas páginas do documento são removidos
1. Recursos iguais são unidos em um único objeto
1. Objetos não utilizados são deletados

Caso você queira otimizar recursos de PDF, você pode usar a função [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/). 
Por favor, verifique o seguinte trecho de código para otimizar recursos de PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF para o qual os recursos serão otimizados.

1. Chame `AsposePdf` como Promise e execute a operação para otimizar o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Otimize os recursos de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfOptimizeResource.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Otimizar recursos do arquivo PDF e salvar em "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF para o qual os recursos serão otimizados.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Otimize os recursos de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfOptimizeResource.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Otimize os recursos do arquivo PDF e salve o "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```