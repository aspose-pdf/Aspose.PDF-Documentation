---
title: Adicionar Carimbos de Imagem em PDF usando JavaScript via C++
linktitle: Carimbos de Imagem em Arquivo PDF
type: docs
weight: 60
url: pt/javascript-cpp/stamping/
description: Adicione o Carimbo de Imagem ao seu documento PDF usando a função AsposePdfAddStamp com o toolkit JavaScript.
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Carimbo de Imagem em Arquivo PDF

Carimbar um documento PDF é semelhante a carimbar um documento em papel. Um carimbo em um arquivo PDF fornece informações adicionais ao arquivo PDF, como proteger o arquivo PDF para outros usarem e confirmar a segurança do conteúdo do arquivo PDF.
Você pode usar a função [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) para adicionar um carimbo de imagem a um arquivo PDF usando JavaScript.

Para adicionar um carimbo de imagem:

1. Defina o nome de arquivo de imagem padrão.
1. Crie um 'FileReader'.
1. Defina o nome do arquivo de imagem.
1. Prepare o arquivo de carimbo a partir do BLOB.

O trecho de código a seguir mostra como adicionar um carimbo de imagem no arquivo PDF.

```js

  /*defina o nome de arquivo de carimbo padrão*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*defina o nome do arquivo de carimbo*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*prepare(salve) o arquivo de carimbo a partir do BLOB*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


1. Crie um 'FileReader'.
1. A função [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) é executada.
1. Adicione o arquivo de imagem ao final de um arquivo PDF e salve como "ResultImage.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*insira o arquivo de carimbo em um arquivo PDF e salve como "ResultImage.pdf"*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
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

    /*Defina o nome do arquivo de selo padrão: 'Aspose.jpg' já carregado, veja as configurações em 'settings.json'*/
    var fileStamp = "Aspose.jpg";

    /*Manipulador de eventos*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*Adicione selo a um arquivo PDF e salve o "ResultStamp.pdf" - Pergunte ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddStamp',
            "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_,
                      setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*Defina o nome do arquivo de selo*/
      fileStamp = e.target.files[0].name;
      file_reader.onload = event => {
        /*Salve o BLOB no FS de memória para processamento*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Crie um link para baixar o arquivo de resultado*/
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