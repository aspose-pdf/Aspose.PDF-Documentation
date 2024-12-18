---
title: Converter PDF para Excel em JavaScript
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/javascript-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-01"
description: Aspose.PDF para JavaScript permite converter PDF para XLSX, e formatos CSV.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Criando planilhas a partir de PDF usando JavaScript

**Aspose.PDF para JavaScript** suporta a funcionalidade de converter arquivos PDF para os formatos Excel e CSV.

{{% alert color="success" %}}
**Tente converter PDF para Excel online**

Aspose.PDF para JavaScript apresenta a você o aplicativo online gratuito ["PDF para XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Convertion PDF para Excel com Aplicativo Gratuito](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

A operação de conversão depende do número de páginas no documento e pode ser muito demorada.
 Portanto, recomendamos fortemente o uso de Web Workers.

Este código demonstra uma maneira de descarregar tarefas de conversão de arquivos PDF que consomem muitos recursos para um web worker, para evitar bloquear a thread principal da UI. Ele também oferece uma maneira amigável para o usuário baixar o arquivo convertido.

## Converter PDF para XLSX

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToXlsX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*converter um arquivo PDF para XlsX e salvar como "ResultPDFtoXlsX.xlsx" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXlsX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Trecho de código]

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

O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas de PDF em arquivos XlsX:

1. Selecione um arquivo PDF para converter.
1. Crie um 'FileReader'.
1. A função [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPDFtoXlsX.xlsx".
1. Em seguida, se o 'json.errorCode' for 0, seu arquivo de resultado receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre tal erro serão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*converter um arquivo PDF para XlsX e salvar como "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*criar um link para baixar o arquivo resultante*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


## Converter PDF para CSV

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? 
          `Contagem de arquivos(tabelas): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "text/csv", element) ) ?? ""}` : 
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToCSV = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Converter um arquivo PDF para CSV (extrair tabelas) com o modelo "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... formato número de página), TAB como delimitador e salvar - Pedir ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfTablesToCSV', "params": [event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t"] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de converter PDF em CSV:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfTablesToCSV{0:D2}.csv".
1. Em seguida, se o 'json.errorCode' for 0, então o seu arquivo de resultado recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileToCSV = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Converter um arquivo PDF para CSV (extrair tabelas) com o modelo "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... formato do número da página), TAB como delimitador*/
        const json = AsposePdfTablesToCSV(event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Contagem de arquivos(tabelas): " + json.filesCount.toString();
          /*Fazer links para os arquivos de resultado*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "text/csv");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```