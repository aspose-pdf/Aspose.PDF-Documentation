---
title: Extrair Imagens de PDF JavaScript
linktitle: Extrair Imagens de PDF
type: docs
weight: 20
url: pt/javascript-cpp/extract-images-from-the-pdf-file/
description: Como extrair uma parte da imagem do PDF usando a ferramenta Aspose.PDF para JavaScript.
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

A ferramenta web do Aspose.PDF permite que você extraia facilmente imagens de arquivos PDF.

Caso você queira extrair imagens de um documento PDF, você pode usar a função [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/). 
Por favor, verifique o seguinte trecho de código para extrair imagens de um arquivo PDF usando JavaScript através de C++.

1. Crie um 'FileReader'.
1. A função [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfExtractImage{0:D2}.jpg".

1. Em seguida, se o 'json.errorCode' for 0, você poderá obter links para os arquivos de resultado. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*Extrair imagem de um arquivo PDF com o modelo "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formatar número da página), resolução de 150 DPI e salvar*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Contagem de arquivos(imagens): " + json.filesCount.toString();
        /*Criar links para os arquivos de resultado*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Usando Web Workers

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? 
          `Contagem de arquivos(imagens): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Extrair imagem de um arquivo PDF com o modelo "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato do número da página), resolução 150 DPI e salvar*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
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