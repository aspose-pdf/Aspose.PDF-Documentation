---
title: Excluir página em PDF no Node.js
linktitle: Excluir páginas de PDF
type: docs
weight: 30
url: /pt/nodejs-cpp/delete-pages/
description: Você pode excluir páginas do seu arquivo PDF usando Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Caso você queira excluir páginas de PDF, pode usar [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) função. 

Um recurso desta função é que ela pode aceitar vários tipos como parâmetro numPages:

- string: neste caso, podemos mencionar um conjunto de páginas usando páginas específicas ou intervalos. Por exemplo, string "7, 20, 30-32, 34" significa que queremos remover as páginas 7, 20, de 30 a 32 e 34.
- array: neste caso, podemos mencionar apenas páginas. Array [3,7] significa que queremos remover as páginas 3 e 7.
- int: um número de página único.

Por favor, verifique o trecho de código a seguir para excluir páginas de PDF no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF do qual as páginas serão excluídas.
1. Chamada `AsposePdf` como Promise e execute a operação para remover páginas. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. Remove as páginas específicas do arquivo PDF. Portanto, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultDeletePages.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF do qual as páginas serão excluídas.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Esta função ajuda a remover as páginas especificadas do arquivo PDF. A operação é determinada pela variável numPages, que pode ser uma string com intervalos de páginas (por exemplo, \"7, 20, 22, 30-32, 33, 36-40, 46\"), um array de números de página ou um único número de página.
1. Remove as páginas específicas do arquivo PDF. Portanto, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultDeletePages.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```