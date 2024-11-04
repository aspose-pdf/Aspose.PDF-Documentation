---
title: Extrair Texto de PDF usando JavaScript
linktitle: Extrair texto de PDF
type: docs
weight: 30
url: /javascript-cpp/extract-text-from-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF para JavaScript.
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Documento PDF

Extrair texto do documento PDF é uma tarefa muito comum e útil.
Extrair texto de PDFs serve a uma variedade de propósitos, desde melhorar a pesquisa e disponibilidade até possibilitar a análise e automação de dados em vários campos, como negócios, pesquisa e gerenciamento de informações.

Caso você queira extrair texto de um documento PDF, você pode usar a função [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/).
Por favor, verifique o seguinte trecho de código para extrair texto de um arquivo PDF usando JavaScript via C++.

1. Crie um 'FileReader'.

1. A função [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) é executada.
1. Em seguida, se o 'json.errorCode' for 0, você pode obter links para os arquivos de resultado. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.

```js

    var ffileExtract = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Extrair texto de um arquivo PDF*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
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
            evt.data.json.extractText :
            `Erro: ${evt.data.json.errorText}`; 

    /*Manipulador de eventos*/
    const ffileExtract = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Extrair texto de um arquivo PDF - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```