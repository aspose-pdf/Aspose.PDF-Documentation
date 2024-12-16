---
title: Otimizar Recursos PDF usando JavaScript via C++ 
linktitle: Otimizar Recursos PDF
type: docs
weight: 15
url: /pt/javascript-cpp/optimize-pdf-resources/
description: Otimizar Recursos de arquivos PDF para visualização rápida na web usando ferramenta JavaScript.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Otimizar Recursos PDF

Otimizar recursos no documento:

  1. Recursos que não são usados nas páginas do documento são removidos
  1. Recursos iguais são unidos em um único objeto
  1. Objetos não utilizados são deletados

1. Selecione um arquivo PDF para otimizar.
1. Crie um 'FileReader'.
1. A função [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfoptimizeresource/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfOptimizeResource.pdf".

1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.  
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.  

O trecho de código a seguir mostra como otimizar um documento PDF.

```js

    var ffilePdfOptimizeResource = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Otimizar recursos de um arquivo PDF e salvar como "ResultPdfOptimizeResource.pdf"*/
        const json = AsposePdfOptimizeResource(event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Criar um link para baixar o arquivo de resultado*/
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
    const ffilePdfOptimizeResource = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Otimizar recursos de um arquivo PDF e salvar como "ResultPdfOptimizeResource.pdf" - Solicitar Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfOptimizeResource', "params": [event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf"] }, [event.target.result]);
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