---
title: Extrair Texto de PDF usando JavaScript
linktitle: Extrair Texto de PDF
type: docs
weight: 10
url: /javascript-cpp/extract-text/
description: Esta seção descreve como extrair texto de um documento PDF usando o kit de ferramentas JavaScript.
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Texto de Todas as Páginas do Documento PDF

Extrair texto de PDF não é fácil. Poucos leitores de PDF conseguem extrair texto de imagens PDF ou PDFs digitalizados. Mas a ferramenta **Aspose.PDF para JavaScript via C++** permite que você extraia texto facilmente de qualquer arquivo PDF.

Confira o trecho de código e siga os passos para extrair texto do seu PDF:

1. Selecione um arquivo PDF para extrair texto.
1. Crie um 'FileReader' para ler o texto.
1. A função [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/) é executada.

1. Em seguida, se o 'json.errorCode' for 0, então o 'json.extractText' conterá o conteúdo extraído. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, seu arquivo tiver um erro, então as informações sobre esse erro serão contidas no 'json.errorText'.
1. Como resultado, você receberá uma string com o texto extraído do seu PDF.

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

    /*Manipulador de evento*/
    const ffileExtract = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Extrair texto de um arquivo PDF - Pedir ao Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```