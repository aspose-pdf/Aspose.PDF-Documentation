---
title: Extrair imagens de PDF em Node.js
linktitle: Extrair imagens de PDF
type: docs
weight: 20
url: /pt/nodejs-cpp/extract-images-from-the-pdf-file/
description: Como extrair uma parte da imagem de um PDF usando Aspose.PDF for Node.js via C++ toolkit.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair imagens de arquivos PDF no ambiente Node.js

Caso você queira extrair imagens de um documento PDF, você pode usar [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) função. 
Devemos passar três argumentos para esta função:  nome do arquivo de entrada e saída e resolução.
Por favor, verifique o trecho de código a seguir para extrair imagens de um arquivo PDF usando Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF do qual a imagem será extraída.
1. Chamada `AsposePdf` como Promise e execute a operação para extrair a imagem. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extraia imagens do arquivo PDF. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultPdfExtractImage{0:D2}.jpg”. Onde {0:D2} representa o número da página no formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF do qual a imagem será extraída.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Extraia imagens do arquivo PDF. Assim, se ‘json.errorCode’ for 0, o resultado da operação será salvo em “ResultPdfExtractImage{0:D2}.jpg”. Onde {0:D2} representa o número da página no formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em ‘json.errorText’.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
