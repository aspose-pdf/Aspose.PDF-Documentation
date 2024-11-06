---
title: Como Mesclar PDF usando JavaScript via C++ 
linktitle: Mesclar arquivos PDF
type: docs
weight: 20
url: pt/javascript-cpp/merge-pdf/
description: Esta página explica como mesclar documentos PDF em um único arquivo PDF com Aspose.PDF para JavaScript via C++ 
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Mesclar ou combinar dois PDFs em um único PDF em JavaScript

Combinar e mesclar arquivos é uma tarefa muito popular ao trabalhar com um grande número de documentos. Às vezes, ao trabalhar com documentos e imagens, quando eles são escaneados, processados e organizados, vários arquivos são criados. Mas e se você precisar armazenar tudo em um único arquivo? Ou você não quer imprimir vários documentos? Concatene dois arquivos PDF com Aspose.PDF para JavaScript via C++.

Esta ferramenta JavaScript permite mesclar dois arquivos PDF em um único documento PDF usando Aspose.PDF para JavaScript via C++. O exemplo é escrito em JavaScript.

1. Selecione arquivos PDF para mesclar.
1. Crie um 'FileReader'.

1. A função [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultMerge.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário. 

O trecho de código a seguir mostra como concatenar arquivos PDF:

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*apenas dois arquivos*/
      if (index >= e.target.files.length || index >= 2) {
        /*mesclar dois arquivos PDF e salvar o "ResultMerge.pdf"*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*criar um link para baixar o arquivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*preparar(salvar) arquivo do BLOB*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```


### Usando Web Workers

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? 
          `Resultado:\n${(evt.data.operation == 'AsposePdfPrepare') ? 
                      fileProcess('AsposePdfMerge2Files', evt.data.json.optdata[0].file, {"fileName2": evt.data.json.fileNameResult}) ?? 'aguarde, por favor...' : 
                      DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0]) /*AsposePdfMerge2Files*/
                    }` :
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de evento. Apenas dois arquivos são mesclados. Se apenas um arquivo for selecionado, use-o. Para o segundo arquivo, você precisa executar AsposePdfPrepare */
    const ffileMerge = evt => fileProcess('AsposePdfPrepare',  evt.target.files[(evt.target.files.length == 1) ? 0 : 1],
                                          [{"operation": 'AsposePdfMerge2Files', "file": evt.target.files[0]}])
    /* Pergunte ao Web Worker */
    const fileProcess = (operation, ffile, optdata) => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        if (operation == 'AsposePdfPrepare')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, "params": [event.target.result, ffile.name, optdata] },
                  [event.target.result]
                );
        else if (operation == 'AsposePdfMerge2Files')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, 
                    "params": [event.target.result, undefined, ffile.name, (optdata === undefined) ? ffile.name : optdata.fileName2,
                                `Resultado${operation}.pdf`] },
                  [event.target.result]
                );
      }
      file_reader.readAsArrayBuffer(ffile);
    }

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