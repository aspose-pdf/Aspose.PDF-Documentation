---
title: Rotacionar Páginas de PDF com JavaScript via C++
linktitle: Rotacionar Páginas de PDF
type: docs
weight: 50
url: /javascript-cpp/rotate-pages/
description: Este tópico descreve como rotacionar a orientação da página em um arquivo PDF existente programaticamente via JavaScript via C++
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Esta seção descreve como alterar a orientação da página de paisagem para retrato e vice-versa em um arquivo PDF existente usando JavaScript via C++.

1. Crie um 'FileReader'.
1. A função [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfrotateallpages/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultRotation.pdf".

1. Em seguida, se o 'json.errorCode' for 0, então o seu DownloadFile receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre esse erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileRotateAllPages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*girar todas as páginas do arquivo PDF e salvar como "ResultRotation.pdf"*/
      const json = AsposePdfRotateAllPages(event.target.result, e.target.files[0].name, Module.Rotation.on270, "ResultRotation.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*criar um link para baixar o arquivo resultante*/
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
        (evt.data.json.errorCode == 0) ?
          `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileRotateAllPages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const rotation = 'Module.Rotation.on270';
        /*Girar páginas do PDF e salvar o "ResultRotation.pdf" - Solicitar Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfRotateAllPages',
            "params": [event.target.result, e.target.files[0].name, rotation, "ResultRotation.pdf"] },
          [event.target.result]
        );
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