---
title: Converter PDF para formatos PDF/A
linktitle: Converter PDF para formatos PDF/A
type: docs
weight: 100
url: /javascript-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-01"
description: Este tópico mostra como o Aspose.PDF permite converter um arquivo PDF em um arquivo PDF compatível com PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para JavaScript** permite converter um arquivo PDF em um arquivo PDF compatível com <abbr title="Portable Document Format / A">PDF/A</abbr>.

A operação de conversão depende do número de páginas no documento e pode ser muito demorada. Portanto, recomendamos fortemente o uso de Web Workers.

Este código demonstra uma maneira de transferir tarefas de conversão de arquivos PDF que exigem muitos recursos para um web worker para evitar o bloqueio do thread principal da interface do usuário. Ele também oferece uma maneira amigável de baixar o arquivo convertido.

{{% alert color="success" %}}
**Tente converter PDF para PDF/A online**

Aspose.PDF para JavaScript apresenta a você o aplicativo online gratuito ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), onde você pode tentar investigar a funcionalidade e qualidade do funcionamento.

[![Aspose.PDF Conversão PDF para PDF/A com Aplicativo Gratuito](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Converter PDF para formato PDF/A

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}\n${DownloadFile(evt.data.json.fileNameLogResult, "application/xml", evt.data.params[1])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffilePdfConvertToPDFA = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pdfFormat = 'Module.PdfFormat.PDF_A_1A';
        /*converter um arquivo PDF para PDF/A(1A) e salvar como "ResultConvertToPDFA.pdf"*/
        /*durante o processo de conversão, a validação também é realizada, "ResultConvertToPDFA.xml"- Pergunte ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToPDFA', "params": [event.target.result, e.target.files[0].name, pdfFormat, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Código]

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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de arquivos PDF para PDF/A:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultConvertToPDFA.pdf". Durante o processo de conversão, a validação também é realizada, "ResultConvertToPDFA.xml".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante, e um link para baixar o arquivo de Log (xml) para o sistema operacional do usuário.

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*converter um arquivo PDF para PDF/A(1A) e salvar como "ResultConvertToPDFA.pdf"*/
      /*durante o processo de conversão, a validação também é realizada, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\nArquivo de Log (formato xml): " + json.fileNameLogResult;
        /*criar um link para baixar o arquivo resultante*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\nArquivo de Log (formato xml): " + json.fileNameLogResult;
      /*criar um link para baixar o Log (xml)*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```