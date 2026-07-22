---
title: Otimizar recursos de PDF no Node.js
linktitle: Otimizar recursos de PDF
type: docs
weight: 15
url: /pt/nodejs-cpp/optimize-pdf-resources/
description: Otimizar recursos de arquivos PDF para visualização rápida na web usando a ferramenta Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Otimizar recursos de PDF

Otimizar recursos no documento:

1. Recursos que não são usados nas páginas do documento são removidos
1. Recursos iguais são unidos em um único objeto
1. Objetos não utilizados são excluídos
 

Caso você queira otimizar recursos de PDF, pode usar [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) função. 
Por favor, verifique o trecho de código a seguir para otimizar recursos de PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF cujos recursos serão otimizados.
1. Chamada `AsposePdf` como Promise e execute a operação para otimizar o arquivo. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Otimizar recursos de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfOptimizeResource.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF cujos recursos serão otimizados.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Otimizar recursos de um PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfOptimizeResource.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```