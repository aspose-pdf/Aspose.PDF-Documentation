---
title: Adicionar Cabeçalho e Rodapé ao PDF em Node.js
linktitle: Adicionar Cabeçalho e Rodapé ao PDF
type: docs
weight: 70
url: /nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para Node.js via C++ permite que você adicione cabeçalhos e rodapés ao seu arquivo PDF usando AsposePdfAddTextHeaderFooter.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF para Node.js via C++** permite que você adicione cabeçalho e rodapé em seu arquivo PDF existente.

Caso você queira adicionar cabeçalho e rodapé, você pode usar a função [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).

Por favor, verifique o seguinte trecho de código para adicionar cabeçalho e rodapé a um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF no qual o cabeçalho e o rodapé serão adicionados.

1. Chame `AsposePdf` como Promise e execute a operação para adicionar cabeçalho e rodapé. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Adicione texto no Cabeçalho e Rodapé de um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultAddHeaderFooter.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro serão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Adicione texto no Cabeçalho/Rodapé de um arquivo PDF e salve o "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF no qual o cabeçalho e o rodapé serão adicionados.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Adicione texto no Cabeçalho e Rodapé de um arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultAddHeaderFooter.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Adicione texto no Cabeçalho/Rodapé de um arquivo PDF e salve o "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```