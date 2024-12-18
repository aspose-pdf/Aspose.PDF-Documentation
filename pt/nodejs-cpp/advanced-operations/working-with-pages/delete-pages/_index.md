```javascript
// Este exemplo de código mostra como deletar páginas de um arquivo PDF usando o Aspose.PDF para Node.js via C++ no ambiente CommonJS.

const asposepdf = require("asposepdf");
const pdfApi = new asposepdf.PdfApi("client_credentials", "client_secret");

pdfApi.deletePages("sample.pdf", "7, 20, 30-32, 34")
    .then((result) => {
        console.log("Páginas deletadas com sucesso!");
    })
    .catch((error) => {
        console.log("Erro ao deletar páginas:", error);
    });
```

**ES6:**

```javascript
// Este exemplo de código mostra como deletar páginas de um arquivo PDF usando o Aspose.PDF para Node.js via C++ no ambiente ES6.

import asposepdf from "asposepdf";
const pdfApi = new asposepdf.PdfApi("client_credentials", "client_secret");

pdfApi.deletePages("sample.pdf", "7, 20, 30-32, 34")
    .then((result) => {
        console.log("Páginas deletadas com sucesso!");
    })
    .catch((error) => {
        console.log("Erro ao deletar páginas:", error);
    });
```

Além disso, você pode usar outros valores do parâmetro numPages, como uma matriz ou um número inteiro, conforme explicado anteriormente.

1. Chame `require` e importe o módulo `asposepdfnodejs` como a variável `AsposePdf`.
1. Especifique o nome do arquivo PDF do qual as páginas serão excluídas.
1. Chame `AsposePdf` como Promise e execute a operação para remover páginas. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).
1. Remove as páginas específicas do arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultDeletePages.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, incluir números de páginas com intervalo: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, matriz de números de páginas*/
      /*const numPages = [1,3];*/
      /*número, número da página*/
      const numPages = 1;
      /*Excluir páginas de um arquivo PDF e salvar como "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual as páginas serão excluídas.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Esta função ajuda a remover as páginas especificadas do arquivo PDF. A operação é determinada pela variável numPages, que pode ser uma string com intervalos de páginas (por exemplo, "7, 20, 22, 30-32, 33, 36-40, 46"), um array de números de páginas ou um único número de página.
1. Remove as páginas específicas do arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultDeletePages.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro serão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, incluir número de páginas com intervalo: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array de números de páginas*/
  /*const numPages = [1,3];*/
  /*número, número da página*/
  const numPages = 1;
  /*Excluir páginas de um arquivo PDF e salvar em "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```