---
title: Excluir Imagens de Arquivo PDF via JavaScript
linktitle: Excluir Imagens
type: docs
weight: 20
url: /javascript-cpp/delete-images-from-pdf-file/
description: Esta seção explica como excluir imagens de um arquivo PDF usando Aspose.PDF para JavaScript.
lastmod: "2022-02-17"
---

Você pode excluir imagens de um arquivo PDF usando Aspose.PDF para JavaScript via C++. Você pode obter o resultado diretamente em seu navegador.

1. Crie um 'FileReader'.
1. A função [AsposePdfDeleteImages](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteimages/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfDeleteImages.pdf".
1. Em seguida, se o 'json.errorCode' for 0, seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então informações sobre tal erro serão contidas no arquivo 'json.errorText'.

1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffilePdfDeleteImages = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Excluir imagens de um arquivo PDF e salvar o "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfDeleteImages(event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf");
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
    const ffilePdfDeleteImages = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Excluir imagens de um arquivo PDF e salvar o "ResultPdfDeleteImages.pdf" - Perguntar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteImages', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf"] }, [event.target.result]);
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