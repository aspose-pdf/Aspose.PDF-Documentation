---
title: Adicionar cabeçalho e rodapé ao PDF em Node.js
linktitle: Adicionar cabeçalho e rodapé ao PDF
type: docs
weight: 70
url: /pt/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Node.js via C++ permite que você adicione cabeçalhos e rodapés ao seu arquivo PDF usando AsposePdfAddTextHeaderFooter.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js via C++** permite que você adicione cabeçalho e rodapé no seu arquivo PDF existente. 

Caso você queira adicionar cabeçalho e rodapé, pode usar [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/) função. 

Por favor, verifique o trecho de código a seguir para adicionar cabeçalho e rodapé a um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF no qual o cabeçalho e o rodapé serão adicionados.
1. Chamada `AsposePdf` como Promise e execute a operação para adicionar cabeçalho e rodapé. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Adicione texto no Cabeçalho e no Rodapé de um arquivo PDF. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultAddHeaderFooter.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF no qual o cabeçalho e o rodapé serão adicionados.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Adicione texto no Cabeçalho e no Rodapé de um arquivo PDF. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultAddHeaderFooter.pdf”. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```