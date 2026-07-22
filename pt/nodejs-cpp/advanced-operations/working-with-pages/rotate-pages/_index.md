---
title: Girar Páginas PDF no Node.js
linktitle: Girar Páginas PDF
type: docs
weight: 50
url: /pt/nodejs-cpp/rotate-pages/
description: Este tópico descreve como girar a orientação da página em um arquivo PDF existente de forma programática no ambiente Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Esta seção descreve como girar páginas em um arquivo PDF existente usando Aspose.PDF for Node.js via C++.

Caso você queira girar páginas PDF, pode usar [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) função. Esta função usa um parâmetro especial 'AsposePdfModule.Rotation' para o valor de rotação. Com ele você pode definir quantos graus precisa girar o PDF. Existem as variantes: None, 90, 180 ou 270 graus.

Por favor, verifique o trecho de código a seguir para girar páginas PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF a ser girado.
1. Chamada `AsposePdf` como Promise e execute a operação para girar páginas. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Gire todos os arquivos PDF. A rotação está definida para 270 graus (on270). Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultRotation.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF a ser girado.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Gire todos os arquivos PDF. A rotação está definida para 270 graus (on270). Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultRotation.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```