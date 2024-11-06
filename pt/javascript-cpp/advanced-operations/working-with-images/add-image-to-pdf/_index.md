---
title: Adicionar Imagem ao PDF usando JavaScript via C++ 
linktitle: Adicionar Imagem
type: docs
weight: 10
url: pt/javascript-cpp/add-image-to-pdf/
description: Esta seção descreve como adicionar imagem a um arquivo PDF existente usando Aspose.PDF para JavaScript via C++.
lastmod: "2023-12-15"
---

## Adicionar Imagem em um Arquivo PDF Existente

Você precisa anexar uma imagem a um PDF? Quer melhorar a legibilidade do seu PDF? Adicione imagens ao seu PDF e sua apresentação ou currículo parecerá mais apresentável.

É comumente acreditado que adicionar imagens a arquivos PDF requer uma ferramenta especial complexa. No entanto, com o Aspose.PDF para JavaScript, você pode rápida e facilmente adicionar as imagens que precisa ao PDF usando JavaScript diretamente no seu navegador.

Para adicionar uma imagem a um arquivo PDF existente:

1. Defina o nome de arquivo padrão da imagem.
1. Crie um 'FileReader'.
1. Defina o nome do arquivo da imagem.
1. Prepare o arquivo de imagem a partir do BLOB.
1. A função [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/) é executada.

1. Adicione o arquivo de imagem ao final de um arquivo PDF e salve como "ResultImage.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

O trecho de código a seguir mostra como adicionar a imagem em um documento PDF.

```js

  /*definir o nome do arquivo de imagem padrão*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*definir o nome do arquivo de imagem*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*preparar(salvar) o arquivo de imagem a partir do BLOB*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

No próximo exemplo, selecionamos a imagem para manipular:

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*adicionar o arquivo de imagem ao final de um arquivo PDF e salvar o "ResultImage.pdf"*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*criar um link para baixar o arquivo resultante*/
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

    /*Definir o nome padrão do arquivo de imagem: 'Aspose.jpg' já carregado, veja as configurações em 'settings.json'*/
    var fileImage = "Aspose.jpg";

    /*Manipulador de eventos*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Adicionar imagem ao final de um arquivo PDF e salvar o "ResultImage.pdf" - Perguntar ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Definir o nome do arquivo de imagem*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Salvar o BLOB na FS de Memória para processamento*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Criar um link para baixar o arquivo resultante*/
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