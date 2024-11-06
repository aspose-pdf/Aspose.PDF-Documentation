---
title: Otimizar PDF usando Aspose.PDF para JavaScript via C++
linktitle: Otimizar Arquivo PDF
type: docs
weight: 10
url: pt/javascript-cpp/optimize-pdf/
description: Otimize e comprima arquivos PDF para visualização rápida na web usando a ferramenta JavaScript.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Otimizar Documento PDF

O Toolkit da Aspose.PDF para JavaScript via C++ permite otimizar o conteúdo de um PDF para a Web.

A otimização, ou linearização para a Web, refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador da web. Para otimizar um arquivo para exibição na web:

1. Selecione um arquivo PDF para otimização.
1. Crie um 'FileReader'.
1. A função [AsposePdfOptimize](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfoptimize/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultOptimize.pdf".

1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

O trecho de código a seguir mostra como otimizar um documento PDF.

```js

  var ffileOptimize = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*otimizar um arquivo PDF e salvar como "ResultOptimize.pdf"*/
      const json = AsposePdfOptimize(event.target.result, e.target.files[0].name, "ResultOptimize.pdf");
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
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de evento*/
    const ffileOptimize = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Otimizar um arquivo PDF e salvar como "ResultOptimize.pdf" - Solicitar Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfOptimize', "params": [event.target.result, e.target.files[0].name, "ResultOptimize.pdf"] },
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