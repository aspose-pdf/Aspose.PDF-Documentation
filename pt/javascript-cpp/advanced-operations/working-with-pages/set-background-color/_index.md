---
title: Definir a cor de fundo para PDF com JavaScript via C++
linktitle: Definir cor de fundo
type: docs
weight: 80
url: /pt/javascript-cpp/set-background-color/
description: Defina a cor de fundo para o seu arquivo PDF com JavaScript via C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Os seguintes trechos de código mostram como definir a cor de fundo das páginas de PDF usando a função [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) com JavaScript.

No próximo exemplo, selecionamos o arquivo PDF para manipular.

1. Crie um 'FileReader'.
1. A função [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/) é executada (formato hexadecimal “#RRGGBB”, onde RR-vermelho, GG-verde e BB-azul são inteiros hexadecimais).
1. Defina a cor de fundo para o arquivo PDF e salve como "ResultPdfSetBackgroundColor.pdf"

1. Em seguida, se o 'json.errorCode' for 0, então o seu DownloadFile receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffilePdfSetBackgroundColor = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Define a cor de fundo para o arquivo PDF e salva o "ResultPdfSetBackgroundColor.pdf"*/
        const json = AsposePdfSetBackgroundColor(event.target.result, e.target.files[0].name, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Cria um link para baixar o arquivo resultante*/
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
    const ffilePdfSetBackgroundColor = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const backgroundColor= "#426bf4";
        /*Definir a cor de fundo para o arquivo PDF e salvar "ResultPdfSetBackgroundColor.pdf" - Solicitar Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfSetBackgroundColor', "params": [event.target.result, e.target.files[0].name, backgroundColor, "ResultPdfSetBackgroundColor.pdf"] }, [event.target.result]);
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