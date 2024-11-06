---
title: Reparar PDF com JavaScript via C++ 
linktitle: Reparar PDF
type: docs
weight: 10
url: pt/javascript-cpp/repair-pdf/
description: Este tópico descreve como Reparar PDF via JavaScript via C++ 
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF para JavaScript permite reparo de PDF de alta qualidade. O arquivo PDF pode não abrir por qualquer motivo, independentemente do programa ou navegador. Em alguns casos, o documento pode ser restaurado, tente o código a seguir e veja por si mesmo.

1. Crie um 'FileReader'.
1. A função [AsposePdfRepair](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfrepair/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfRepair.pdf".
1. Em seguida, se o 'json.errorCode' for 0, você pode obter links para os arquivos de resultado. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.

1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffilePdfRepair = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Reparar um arquivo PDF e salvar como "ResultPdfRepair.pdf"*/
        const json = AsposePdfRepair(event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Criar um link para baixar o arquivo resultante*/
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
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffilePdfRepair = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Reparar um arquivo PDF e salvar como "ResultPdfRepair.pdf" - Solicitar Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRepair', "params": [event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Trecho de código]

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