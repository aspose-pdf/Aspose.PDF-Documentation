---
title: Trabalhando com Metadados de Arquivo PDF usando JavaScript via C++
linktitle: Metadados de Arquivo PDF
type: docs
weight: 130
url: pt/javascript-cpp/pdf-file-metadata/
description: Esta seção explica como obter informações de arquivo PDF, como obter metadados de um arquivo PDF, definir Informações de Arquivo PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Informações de Arquivo PDF

1. Crie um 'FileReader'.
1. A função [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/) é executada.
1. Metadados de PDF que podem ser obtidos:
- title - título
- creator - criador
- author - autor
- subject - assunto
- keywords - palavras-chave
- creation - data de criação
- mod - data de modificação
1. Em seguida, se o 'json.errorCode' for 0, você pode obter a lista de Informações do arquivo PDF. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então a informação sobre tal erro estará contida no arquivo 'json.errorText'.

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Obter informações (metadados) do arquivo PDF.*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
      title - título
      creator - criador
      author - autor
      subject - assunto
      keywords - palavras-chave
      format - formato PDF
      version - versão PDF
      ispdfa - PDF é PDF/A
      ispdfua - PDF é PDF/UA
      islinearized - PDF é linearizado
      isencrypted - PDF é criptografado
      permission - permissão PDF
      size - tamanho da página PDF
      pagecount - Contagem de páginas
      Data de criação: json.creation
      Data de modificação: json.mod
      annotationcount - Contagem de anotações
      bookmarkcount - Contagem de marcadores
      attachmentcount - Contagem de anexos
      metadatacount - Contagem de metadados
      javascriptcount - Contagem de JavaScript
      imagecount - Contagem de imagens
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


### Usando Web Workers

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ?
          `info:\n${JSON.stringify(evt.data.json, null, 4)}` :
          `Erro: ${evt.data.json.errorText}`; 

    /*Manipulador de evento*/
    const ffilePdfGetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Obter informações (metadados) de um arquivo PDF - Perguntar ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetInfo', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Obter Todas as Fontes

Obter fontes de um arquivo PDF pode ser uma maneira útil de reutilizar fontes em outros documentos ou aplicativos.
 
No caso de você querer obter todas as fontes de um documento PDF, você pode usar [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/). 
Por favor, verifique o seguinte trecho de código para obter todas as fontes de um documento PDF existente usando JavaScript via C++.

1. Crie um 'FileReader'.
1. A função [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/) é executada.
1. Em seguida, se o 'json.errorCode' for 0, então você pode obter a lista de fontes do arquivo PDF. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*obter lista de fontes do arquivo PDF.*/
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## Usando Web Workers

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ?
          `fontes:\n${JSON.stringify(evt.data.json.fonts, null, 4)}` :
          `Erro: ${evt.data.json.errorText}`; 

    /*Manipulador de evento*/
    const ffilePdfGetAllFonts = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Obter lista de fontes de um arquivo PDF - Perguntar ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetAllFonts', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```
## Definir Informações do Arquivo PDF

Aspose.PDF para JavaScript via C++ permite que você defina informações específicas do arquivo para um PDF, como autor, data de criação, assunto e título.
 Para definir esta informação:

1. Crie um 'FileReader'.
1. Se não for necessário definir um valor, use undefined ou "" (string vazia).
1. A função [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultSetInfo.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffilePdfSetInfo = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Definir informações do PDF: título, criador, autor, assunto, palavras-chave, criação (data), mod (data de modificação)*/
        /*Se não for necessário definir um valor, use undefined ou "" (string vazia)*/
        /*Definir informações (metadados) em um arquivo PDF e salvar como "ResultSetInfo.pdf"*/
        const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "Definindo Informações do Documento PDF", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 11:55 PM", "ResultSetInfo.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Criar um link para baixar o arquivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

### Usando Web Workers

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de evento*/
    const ffilePdfSetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Informações do PDF: título, criador, autor, assunto, palavras-chave, criação (data), mod (data de modificação)*/
        const title = 'Definindo Informações do Documento PDF';
        const creator = ''; /*se não precisar definir valor, use: undefined ou ""/'' (string vazia)*/
        const author = 'Aspose';
        const subject = undefined;
        const keywords = 'Aspose.Pdf, DOM, API';
        const creation = undefined; /*data de criação*/
        const mod = '16/02/2023 11:55 PM'; /*data de modificação*/
        /*Defina informações (metadados) em um arquivo PDF e salve como "ResultSetInfo.pdf" - Pergunte ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSetInfo',
            "params": [event.target.result, e.target.files[0].name, title, creator, author, subject, keywords, creation, mod, "ResultSetInfo.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Criar um link para baixar o arquivo de resultado*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Clique aqui para baixar o arquivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


## Remover Informações do Arquivo PDF

Aspose.PDF para JavaScript via C++ permite que você remova os Metadados do arquivo PDF:

1. Crie um 'FileReader'.
1. A função [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/javascript-cpp/metadata/asposepdfremovemetadata/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo, "ResultPdfRemoveMetadata.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile é dado o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffilePdfRemoveMetadata = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Remover metadados de um arquivo PDF e salvar como "ResultPdfRemoveMetadata.pdf"*/
        const json = AsposePdfRemoveMetadata(event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Criar um link para baixar o arquivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### Usando Web Workers

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de evento*/
    const ffilePdfRemoveMetadata = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Remover metadados de um arquivo PDF e salvar como "ResultPdfRemoveMetadata.pdf" - Pedir ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRemoveMetadata', "params": [event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Trecho de código]

    /*Criar um link para baixar o arquivo de resultado*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Clique aqui para baixar o arquivo " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```