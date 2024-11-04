---

title: Girar Páginas de PDF em Node.js  
linktitle: Girar Páginas de PDF  
type: docs  
weight: 50  
url: /nodejs-cpp/rotate-pages/  
description: Este tópico descreve como girar a orientação da página em um arquivo PDF existente programaticamente no ambiente Node.js.  
lastmod: "2023-11-16"  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  

---

Esta seção descreve como girar páginas em um arquivo PDF existente usando Aspose.PDF para Node.js via C++.

Caso você queira girar páginas de PDF, você pode usar a função [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). Esta função usa um parâmetro especial 'AsposePdfModule.Rotation' para o valor de rotação. Com isso, você pode definir quantos graus você precisa girar o PDF. Existem variantes: Nenhum, 90, 180 ou 270 graus.

Por favor, verifique o seguinte trecho de código para girar páginas de PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.

1. Especifique o nome do arquivo PDF a ser rotacionado.  
1. Chame `AsposePdf` como Promise e execute a operação para rotacionar as páginas. Receba o objeto se for bem-sucedido.  
1. Chame a função [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).  
1. Rotacione todos os arquivos PDF. A rotação é definida para 270 graus (on270). Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultRotation.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotacionar páginas PDF e salvar em "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF a ser rotacionado.
1. Inicialize o módulo AsposePdf. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
1. Rotacione todos os arquivos PDF. A rotação é configurada para 270 graus (on270). Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultRotation.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotacione páginas PDF e salve o "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```