---

title: Trabalhando com Metadados de Arquivos PDF no Node.js  
linktitle: Metadados de Arquivo PDF  
type: docs  
weight: 130  
url: /nodejs-cpp/pdf-file-metadata/  
description: Esta seção explica como obter informações de arquivos PDF, como obter metadados de um arquivo PDF, definir informações de arquivos PDF no Node.js.  
lastmod: "2023-11-16"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  

---

## Obter Informações do Arquivo PDF

Caso você queira obter informações de um arquivo PDF, você pode usar a função [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).  
Por favor, verifique o trecho de código a seguir para obter informações de um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como a variável `AsposePdf`.  
1. Especifique o nome do arquivo PDF do qual as informações serão extraídas.  
1. Chame `AsposePdf` como Promise e execute a operação para extrair informações. Receba o objeto se for bem-sucedido.  

1. Chame a função [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Os metadados extraídos são armazenados no objeto JSON. Assim, se 'json.errorCode' for 0, os metadados extraídos são exibidos usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Obter informações (metadados) de um arquivo PDF*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Título             : json.title
        Criador            : json.creator
        Autor              : json.author
        Assunto            : json.subject
        Palavras-chave     : json.keywords
        Data de criação    : json.creation
        Data de modificação: json.mod
        Formato do PDF     : json.format
        Versão do PDF      : json.version
        PDF é PDF/A        : json.ispdfa
        PDF é PDF/UA       : json.ispdfua
        PDF é linearizado  : json.islinearized
        PDF é criptografado: json.isencrypted
        Permissão do PDF   : json.permission
        Tamanho da página  : json.size
        Contagem de páginas: json.pagecount
        Contagem de anotações: json.annotationcount
        Contagem de marcadores: json.bookmarkcount
        Contagem de anexos : json.attachmentcount
        Contagem de metadados: json.metadatacount
        Contagem de JavaScript: json.javascriptcount
        Contagem de imagens: json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Título: ' + json.title : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual as informações serão extraídas.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Os metadados extraídos são armazenados no objeto JSON. Assim, se 'json.errorCode' for 0, os metadados extraídos são exibidos usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Obter informações (metadados) de um arquivo PDF*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Title             : json.title
      Creator           : json.creator
      Author            : json.author
      Subject           : json.subject
      Keywords          : json.keywords
      Creation Date     : json.creation
      Modify Date       : json.mod
      PDF format        : json.format
      PDF version       : json.version
      PDF is PDF/A      : json.ispdfa
      PDF is PDF/UA     : json.ispdfua
      PDF is linearized : json.islinearized
      PDF is encrypted  : json.isencrypted
      PDF permission    : json.permission
      PDF page size     : json.size
      Page count        : json.pagecount
      Annotation count  : json.annotationcount
      Bookmark count    : json.bookmarkcount
      Attachment count  : json.attachmentcount
      Metadata count    : json.metadatacount
      JavaScript count  : json.javascriptcount
      Image count       : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```


## Obter Todas as Fontes

Obter fontes de um arquivo PDF pode ser uma maneira útil de reutilizar fontes em outros documentos ou aplicativos.

Caso você queira obter fontes de um arquivo PDF, você pode usar a função [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/). 
Por favor, verifique o seguinte exemplo de código para obter fontes de um arquivo PDF no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF do qual as fontes serão extraídas.
1. Chame `AsposePdf` como Promise e execute a operação para extrair fontes. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).

1. As fontes extraídas são armazenadas no objeto JSON. Assim, se 'json.errorCode' for 0, ele exibe um array de detalhes da fonte, incluindo o nome da fonte, se está incorporada e seu status de acessibilidade usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Obter lista de fontes de um arquivo PDF*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array de fontes: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual as fontes serão extraídas.

1. Inicialize o módulo AsposePdf. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. As fontes extraídas são armazenadas no objeto JSON. Assim, se 'json.errorCode' for 0, ele exibe uma matriz de detalhes da fonte, incluindo o nome da fonte, se está incorporada e seu status de acessibilidade usando console.log. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Obter lista de fontes de um arquivo PDF*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array de fontes: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Definir Informações do Arquivo PDF


Aspose.PDF para Node.js via C++ permite que você defina informações específicas de arquivo para um PDF, informações como autor, data de criação, assunto e título. Para definir essas informações:

Caso você queira definir informações específicas de arquivo, você pode usar a função [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/). Por favor, verifique o seguinte trecho de código para definir informações de arquivo no ambiente Node.js.

Possível definir:
- título
- criador
- autor
- assunto
- listar palavras-chave
- data de criação
- data de modificação
- nome do arquivo de resultado

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF onde as informações serão definidas.
1. Chame `AsposePdf` como Promise e realize a operação. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).

1. Defina as informações do arquivo PDF. Informações como título, criador, autor, assunto, palavras-chave, data de criação e data de modificação são fornecidas como parâmetros. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultSetInfo.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Defina as informações do PDF: título, criador, autor, assunto, palavras-chave, criação (data), mod (data de modificação)*/
      /*Se não precisar definir o valor, use undefined ou "" (string vazia)*/
      /*Defina informações (metadados) em um arquivo PDF e salve em "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Definindo Informações do Documento PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF onde a informação será definida.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Defina as informações do arquivo PDF. Informações como título, criador, autor, assunto, palavras-chave, data de criação e data de modificação são fornecidas como parâmetros. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultSetInfo.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Definir informações do PDF: título, criador, autor, assunto, palavras-chave, criação (data), mod (data de modificação)*/
  /*Se não precisar definir valor, use undefined ou "" (string vazia)*/
  /*Definir informações (metadados) em um arquivo PDF e salvar em "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Definindo Informações do Documento PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


## Remover Informações do Arquivo PDF

Aspose.PDF para Node.js via C++ permite que você remova os Metadados de um arquivo PDF:

Caso você queira remover metadados de um PDF, você pode usar a função [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/). 
Por favor, verifique o seguinte trecho de código para remover metadados de um PDF no ambiente Node.js.

**CommonJS:**

1. Requerer o módulo AsposePDFforNode.js.
1. Especificar o nome do arquivo PDF do qual as informações serão removidas.
1. Inicializar o módulo AsposePdf. Receber o objeto se for bem-sucedido.
1. Chamar a função [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Excluir informações do arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfRemoveMetadata.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, a informação do erro estará contida em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remover metadados de um arquivo PDF e salvar em "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF do qual a informação será removida.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Exclua as informações do arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfRemoveMetadata.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações de erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Remover metadados de um arquivo PDF e salvar como "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```