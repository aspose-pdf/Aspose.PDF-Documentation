---
title: Removendo anexos de PDF no Node.js
linktitle: Removendo anexo de um PDF existente
type: docs
weight: 10
url: /pt/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF pode remover anexos dos seus documentos PDF. Use o ambiente Node.js para remover anexos em arquivos PDF pelo Aspose.PDF.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Você pode excluir anexos de um arquivo PDF usando Aspose.PDF for Node.js via C++. Caso deseje excluir anexos de um PDF, você pode usar [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) função. 
Por favor, verifique o trecho de código a seguir para excluir anexos de um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF do qual os anexos serão removidos.
1. Chamada `AsposePdf` como Promise e execute a operação de remoção de anexos. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Exclua os anexos. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfDeleteAttachments.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro ficarão contidas em 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF do qual os anexos serão removidos.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Exclua os anexos. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfDeleteAttachments.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro ficarão contidas em 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```