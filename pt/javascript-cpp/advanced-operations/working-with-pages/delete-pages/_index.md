---
title: Excluir Páginas de PDF com JavaScript via C++
linktitle: Excluir Páginas de PDF
type: docs
weight: 30
url: pt/javascript-cpp/delete-pages/
description: Você pode excluir páginas do seu arquivo PDF usando Aspose.PDF para JavaScript via C++.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Você pode excluir páginas de um arquivo PDF usando Aspose.PDF para JavaScript via C++. Você pode obter o resultado diretamente no seu navegador.

1. Crie um 'FileReader'.
1. Especifique os números das páginas a serem excluídas.
1. A função [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultDeletePages.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então informações sobre tal erro serão contidas no arquivo 'json.errorText'.

1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*string, incluir número de páginas com intervalo: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*array, array de números de páginas*/
      /*const numPages = [1,3];*/
      /*número, número da página*/
      /*const numPages = 1;*/
      /*excluir páginas 1-3 de um arquivo PDF e salvar como "ResultOptimize.pdf"*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
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

    /*Manejador de evento*/
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*string, incluir número de páginas com intervalo: "7, 20, 22, 30-32, 33, 36-40, 46"*/
        const numPages = "1-3";
        /*array, matriz de números de páginas*/
        /*const numPages = [1,3];*/
        /*número, número de página*/
        /*const numPages = 1;*/
        /*Excluir páginas de um arquivo PDF e salvar o "ResultDeletePages.pdf - Perguntar ao Web Worker"*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
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