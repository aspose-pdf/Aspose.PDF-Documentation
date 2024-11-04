---
title: Adicionar fundo ao PDF com JavaScript via C++
linktitle: Adicionar fundos
type: docs
weight: 10
url: /javascript-cpp/add-backgrounds/
description: Adicione uma imagem de fundo ao seu arquivo PDF com JavaScript via C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Os trechos de código a seguir mostram como adicionar uma imagem de fundo às páginas do PDF usando a função [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) com JavaScript.

No próximo trecho de código, carregamos a imagem para trabalhos futuros no sistema de arquivos interno:

1. Crie um 'FileReader'.
1. Defina o nome do arquivo da imagem.
1. Prepare o arquivo de imagem a partir do BLOB.

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*defina o nome do arquivo da imagem*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*prepare(salve) o arquivo de imagem a partir do BLOB*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


In the next example, we select the PDF file to handle.
1. Crie um 'FileReader'.
1. A função [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) é executada.
1. Adicione o arquivo de imagem no PDF e salve como "ResultBackgroundImage.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*adicione um arquivo de imagem de fundo no PDF e salve como "ResultBackgroundImage.pdf"*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*crie um link para baixar o arquivo resultante*/
      DownloadFile(json.fileNameResult, "application/pdf");
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
          `Resultado:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'imagem preparada!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erro: ${evt.data.json.errorText}`;

    /*Definir o nome de arquivo de imagem padrão: 'Aspose.jpg' já carregado, veja as configurações em 'settings.json'*/
    var fileBackgroundImage = "Aspose.jpg";

    /*Manipulador de evento*/
    const ffileAddBackgroundImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Adicionar imagem de fundo a um arquivo PDF e salvar como "ResultBackgroundImage.pdf" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddBackgroundImage',
            "params": [event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Definir o nome do arquivo de imagem*/
      fileBackgroundImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Salvar o BLOB na memória FS para processamento*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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