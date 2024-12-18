---
title: Extrair Imagens de PDF em Node.js
linktitle: Extrair Imagens de PDF
type: docs
weight: 20
url: /pt/nodejs-cpp/extract-images-from-the-pdf-file/
description: Como extrair uma parte da imagem do PDF usando o Aspose.PDF para Node.js via toolkit C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair imagens de arquivos PDF no ambiente Node.js

Caso você queira extrair imagens de um documento PDF, você pode usar a função [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/). Devemos passar três argumentos para esta função: nome do arquivo de entrada e saída e resolução. Por favor, verifique o seguinte trecho de código para extrair imagens de um arquivo PDF usando Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF do qual a imagem será extraída.

1. Chame `AsposePdf` como Promise e execute a operação para extrair imagem. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extraia imagens do arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfExtractImage{0:D2}.jpg". Onde {0:D2} representa o número da página com um formato de dois dígitos. As imagens são salvas com uma resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro serão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extrair imagem de um arquivo PDF com o modelo "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato de número de página), resolução 150 DPI e salvar*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual a imagem será extraída.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extraia imagens do arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfExtractImage{0:D2}.jpg". Onde {0:D2} representa o número da página com um formato de dois dígitos. As imagens são salvas com uma resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extrair imagem de um arquivo PDF com o modelo "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato número de página), resolução 150 DPI e salvar*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```