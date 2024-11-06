---
title: Removendo anexos de PDF em Node.js
linktitle: Removendo anexo de um PDF existente
type: docs
weight: 10
url: pt/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF pode remover anexos de seus documentos PDF. Use o ambiente Node.js para remover anexos em arquivos PDF com Aspose.PDF.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Você pode excluir anexos de um arquivo PDF usando o Aspose.PDF para Node.js via C++. Caso você queira excluir anexos de um PDF, você pode usar a função [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/). 
Por favor, verifique o seguinte trecho de código para excluir anexos de um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como a variável `AsposePdf`.
1. Especifique o nome do arquivo PDF do qual os anexos serão removidos.

1. Chame `AsposePdf` como Promise e execute a operação para remover anexos. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Exclua os anexos. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfDeleteAttachments.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações de erro estarão contidas em 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Excluir anexos de um arquivo PDF e salvar o "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual os anexos serão removidos.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Exclua os anexos. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfDeleteAttachments.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Excluir anexos de um arquivo PDF e salvar o "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```