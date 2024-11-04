---
title: Converter PDF para PPTX em JavaScript
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: /javascript-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-01"
description: Aspose.PDF permite que você converta PDF para o formato PPTX usando JavaScript diretamente na web.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A operação de conversão depende do número de páginas no documento e pode ser muito demorada. Portanto, recomendamos fortemente o uso de Web Workers.

Este código demonstra uma maneira de transferir tarefas de conversão de arquivos PDF que consomem muitos recursos para um web worker, a fim de evitar o bloqueio da thread principal da interface do usuário. Ele também oferece uma maneira amigável de baixar o arquivo convertido.

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF para JavaScript apresenta a você o aplicativo online gratuito ["PDF para PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode investigar a funcionalidade e a qualidade com que ele funciona.


[![Aspose.PDF Conversão de PDF para PPTX com Aplicativo Gratuito](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Converter PDF para PPTX

```js

  /*Criar Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'carregado!' :
      (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

  /*Manipulador de eventos*/
  const ffileToPptX = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Converter um arquivo PDF para PptX e salvar como "ResultPDFtoPptX.pptx" - Pedir ao Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToPptX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx"] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de arquivos PDF para PPTX:

1. Selecione um arquivo PDF para converter.
1. Crie um 'FileReader'.
1. A função [AsposePdfToPptX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftopptx/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPDFtoPptX.pptx".
1. Em seguida, se 'json.errorCode' for 0, então seu arquivo de resultado recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileToPptX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Converte um arquivo PDF para PptX e salva o "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfToPptX(event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Cria um link para baixar o arquivo resultante*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```