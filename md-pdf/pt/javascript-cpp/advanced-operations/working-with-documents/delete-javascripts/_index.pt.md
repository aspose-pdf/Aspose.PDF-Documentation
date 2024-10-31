---
title: Limpar código JavaScript de um arquivo PDF
linktitle: Excluir JavaScripts
type: docs
weight: 50
url: /javascript-cpp/delete-javascripts/
description: Limpar macros JavaScript de um arquivo PDF diretamente na Web com Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Remover JavaScript em um arquivo PDF pode ser necessário por razões de segurança e privacidade. JavaScript em arquivos PDF pode, às vezes, ser usado maliciosamente ou para funções indesejadas. Você pode obter o resultado diretamente no seu navegador.

1. Crie um 'FileReader'.
1. A função [AsposePdfDeleteJavaScripts](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletejavascripts/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfDeleteJavaScripts.pdf".

1. Em seguida, se o 'json.errorCode' for 0, então o seu DownloadFile receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffilePdfDeleteJavaScripts = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Excluir JavaScripts de um arquivo PDF e salvar como "ResultPdfDeleteJavaScripts.pdf"*/
        const json = AsposePdfDeleteJavaScripts(event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf");
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
    const ffilePdfDeleteJavaScripts = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Excluir JavaScripts de um arquivo PDF e salvar como "ResultPdfDeleteJavaScripts.pdf" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteJavaScripts', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf"] }, [event.target.result]);
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