---
title: Deletar Anotação usando JavaScript
linktitle: Deletar Anotação
type: docs
weight: 10
url: pt/javascript-cpp/delete-annotation/
description: Com Aspose.PDF para JavaScript você pode deletar anotações do seu arquivo PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Você pode deletar anotações de um arquivo PDF usando Aspose.PDF para JavaScript via C++. Você pode obter o resultado diretamente no seu navegador.

1. Crie um 'FileReader'.
1. A função [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteannotations/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfDeleteAnnotations.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então o seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre esse erro estarão contidas no arquivo 'json.errorText'.

1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffilePdfDeleteAnnotations = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Excluir anotações de um arquivo PDF e salvar como "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfDeleteAnnotations(event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf");
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

    /*Manipulador de evento*/
    const ffilePdfDeleteAnnotations = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Excluir anotações de um arquivo PDF e salvar como "ResultPdfDeleteAnnotations.pdf" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAnnotations', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf"] }, [event.target.result]);
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