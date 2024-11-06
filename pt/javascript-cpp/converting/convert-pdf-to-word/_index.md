---
title: Converter PDF para documentos Word em JavaScript
linktitle: Converter PDF para Word
type: docs
weight: 10
url: pt/javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: Aprenda a escrever código JavaScript para conversão de PDF para DOC(DOCX) diretamente na Web.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A operação de conversão depende do número de páginas no documento e pode ser muito demorada. Portanto, recomendamos fortemente o uso de Web Workers.

Este código demonstra uma maneira de transferir tarefas de conversão de arquivos PDF que consomem muitos recursos para um web worker para evitar o bloqueio do thread principal da interface do usuário. Ele também oferece uma maneira fácil de baixar o arquivo convertido.

Para editar o conteúdo de um arquivo PDF no Microsoft Word ou outros processadores de texto que suportam formatos DOC e DOCX. Os arquivos PDF são editáveis, mas os arquivos DOC e DOCX são mais flexíveis e personalizáveis.

{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF para JavaScript apresenta a você o aplicativo online gratuito ["PDF para DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode experimentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Converter PDF para DOC](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter PDF para DOC

```js

  /*Criar Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'carregado!' :
      (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

  /*Manipulador de evento*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Converter um arquivo PDF para Doc e salvar como "ResultPDFtoDoc.doc" - Perguntar ao Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas PDF em arquivos DOC:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPDFtoDoc.doc".
1. Em seguida, se o 'json.errorCode' for 0, então seu arquivo de resultado receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Converter um arquivo PDF para Doc e salvar como "ResultPDFtoDoc.doc"*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Criar um link para baixar o arquivo resultante*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF para JavaScript apresenta a você a aplicação online gratuita ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Converter PDF para DOCX

A API Aspose.PDF para JavaScript permite que você leia e converta documentos PDF para DOCX. DOCX é um formato conhecido para documentos do Microsoft Word, cuja estrutura foi alterada de binário simples para uma combinação de arquivos XML e binários. Arquivos Docx podem ser abertos com o Word 2007 e versões posteriores, mas não com as versões anteriores do MS Word que suportam extensões de arquivo DOC.

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*converter um arquivo PDF para DocX e salvar como "ResultPDFtoDocX.docx" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Fragmento de código]

    /*criar um link para baixar o arquivo de resultado*/
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


O trecho de código JavaScript a seguir mostra um exemplo simples de conversão de páginas PDF em arquivos DOCX:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPDFtoDocX.docx".
1. Em seguida, se 'json.errorCode' for 0, então seu arquivo de resultado receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre esse erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*converter um arquivo PDF para DocX e salvar como "ResultPDFtoDocX.docx"*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*criar um link para baixar o arquivo de resultado*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```