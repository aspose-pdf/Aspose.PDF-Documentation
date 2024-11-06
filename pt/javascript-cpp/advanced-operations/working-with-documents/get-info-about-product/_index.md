---
title: Obter informações sobre o Produto usando JavaScript
linktitle: Obter informações sobre o Produto
type: docs
weight: 70
url: pt/javascript-cpp/get-info-about-product/
description: Este tópico mostra como obter informações sobre o Produto com Aspose.PDF para JavaScript via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Este tópico explica como obter informações sobre o Produto usando JavaScript.

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode !== 0) ? `Erro: ${evt.data.json.errorText}` :
                          "Produto       : " + evt.data.json.product
                      + "\nFamília      : " + evt.data.json.family
                      + "\nVersão       : " + evt.data.json.version
                      + "\nData de lançamento : " + evt.data.json.releasedate
                      + "\nProdutor     : " + evt.data.json.producer
                      + "\nEstá licenciado  : " + evt.data.json.islicensed;

    /*Manipulador de evento*/
    const onAsposePdfAbout = e => {
      /*Obter informações sobre o Produto - Perguntar ao Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAbout', "params": [] }, []);
    };
```


O seguinte trecho de código JavaScript mostra um exemplo simples de como obter informações sobre o Produto:

1. A função [AsposePdfAbout](https://reference.aspose.com/pdf/javascript-cpp/misc/asposepdfabout/) é executada.
1. Informações do Produto que podem ser obtidas:
- Nome do produto
- Família do produto
- Versão do produto
- Data de lançamento
- Nome completo/produtor
- Produto está licenciado
1. Em seguida, se o 'json.errorCode' for 0, você pode obter informações sobre o Produto. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.

```js

  var onAsposePdfAbout = function () {
    /*Obter informações sobre o Produto*/
    const json = AsposePdfAbout();
    /* JSON
    Nome do produto      : json.product
    Família do produto   : json.family
    Versão do produto    : json.version
    Data de lançamento   : json.releasedate
    Nome completo/produtor: json.producer
    Produto está licenciado: json.islicensed
    */
    if (json.errorCode == 0) document.getElementById('output').textContent = 
                    "Produto       : " + json.product
                + "\nFamília       : " + json.family
                + "\nVersão        : " + json.version
                + "\nData de lançamento: " + json.releasedate
                + "\nProdutor      : " + json.producer
                + "\nEstá licenciado: " + json.islicensed;
    else document.getElementById('output').textContent = json.errorText;
  }
```