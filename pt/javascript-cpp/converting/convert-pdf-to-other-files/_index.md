---
title: Converter PDF para EPUB, TeX, Texto, XPS em JavaScript
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /pt/javascript-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-01"
description: Este tópico mostra como converter arquivo PDF para outros formatos de arquivo como EPUB, LaTeX, Texto, XPS etc usando JavaScript ou JavaScript.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

A operação de conversão depende do número de páginas no documento e pode ser muito demorada. Portanto, recomendamos fortemente o uso de Web Workers.

Este código demonstra uma maneira de descarregar tarefas de conversão de arquivos PDF que exigem muitos recursos para um web worker para evitar bloquear o thread principal da interface do usuário. Ele também oferece uma maneira amigável de baixar o arquivo convertido.

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF para JavaScript apresenta a você o aplicativo online gratuito ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e a qualidade com que trabalha.

[![Aspose.PDF Converção de PDF para EPUB com Aplicativo Gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Converter PDF para EPUB

**<abbr title="Publicação Eletrônica">EPUB</abbr>** é um padrão gratuito e aberto para e-books do Fórum Internacional de Publicação Digital (IDPF). Os arquivos têm a extensão .epub. EPUB é projetado para conteúdo redimensionável, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico. EPUB também suporta conteúdo em layout fixo. O formato é destinado como um único formato que editoras e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/epub+zip", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToEPUB = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Converter um arquivo PDF para ePub e salvar como "ResultPDFtoEPUB.epub" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToEPUB', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub"] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas PDF em arquivos EPUB:

1. Selecione um arquivo PDF para converter.
1. Crie um 'FileReader'.
1. A função [AsposePdfToEPUB](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoepub/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPDFtoEPUB.epub".
1. Em seguida, se o 'json.errorCode' for 0, então seu arquivo de resultado recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileToEPUB = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Converta um arquivo PDF para EPUB e salve como "ResultPDFtoEPUB.epub"*/
        const json = AsposePdfToEPUB(event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Crie um link para baixar o arquivo de resultado*/
        DownloadFile(json.fileNameResult, "application/epub+zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF para JavaScript apresenta a você o aplicativo online gratuito ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode experimentar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para LaTeX/TeX com Aplicativo Gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Converter PDF para TeX

**Aspose.PDF para JavaScript** suporta a conversão de PDF para TeX.
O formato de arquivo LaTeX é um formato de arquivo de texto com marcação especial e é usado em um sistema de preparação de documentos baseado em TeX para composição de alta qualidade.

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/x-tex", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de evento*/
    const ffileToTeX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Converter um arquivo PDF para TeX e salvar como "ResultPDFtoTeX.tex" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTeX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex"] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas PDF em arquivos TEX:

1. Selecione um arquivo PDF para converter.
1. Crie um 'FileReader'.
1. A função [AsposePdfToTeX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotex/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPDFtoTeX.tex".
1. Em seguida, se o 'json.errorCode' for 0, então seu arquivo de resultado recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então informações sobre tal erro serão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileToTeX = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Converta um arquivo PDF para TeX e salve como "ResultPDFtoTeX.tex"*/
        const json = AsposePdfToTeX(event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Faça um link para baixar o arquivo resultante*/
        DownloadFile(json.fileNameResult, "application/x-tex");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**Tente converter PDF para Texto online**

Aspose.PDF para JavaScript apresenta a você um aplicativo online gratuito ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão de PDF para Texto com App Gratuito Aspose.PDF](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Converter PDF para TXT

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "text/plain", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToTxt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Converter um arquivo PDF para Txt e salvar como "ResultPDFtoTxt.txt" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTxt', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt"] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas PDF em arquivos TXT:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfToTxt](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotxt/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPDFtoTxt.txt".
1. Em seguida, se o 'json.errorCode' for 0, então seu arquivo de resultado receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então informações sobre tal erro serão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileToTxt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Converta um arquivo PDF para Txt e salve como "ResultPDFtoTxt.txt"*/
        const json = AsposePdfToTxt(event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Crie um link para baixar o arquivo de resultado*/
        DownloadFile(json.fileNameResult, "text/plain");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF para JavaScript apresenta a você o aplicativo online gratuito ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF PDF para XPS com App Gratuito](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Converter PDF para XPS

O tipo de arquivo XPS é associado principalmente à Especificação de Papel XML pela Microsoft Corporation. A Especificação de Papel XML (XPS), anteriormente codinome Metro e englobando o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos no sistema operacional Windows.

**Aspose.PDF para JavaScript** proporciona a possibilidade de converter arquivos PDF para o formato <abbr title="XML Paper Specification">XPS</abbr>. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com JavaScript.

```js

    /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.ms-xpsdocument", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToXps = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Converter um arquivo PDF para Xps e salvar como "ResultPDFtoXps.xps" - Perguntar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXps', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps"] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas PDF em arquivos XPS:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfToXps](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoxps/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPDFtoXps.xps".
1. Em seguida, se o 'json.errorCode' for 0, então seu arquivo de resultado receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro serão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileToXps = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Converter um arquivo PDF para Xps e salvar como "ResultPDFtoXps.xps"*/
        const json = AsposePdfToXps(event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Criar um link para baixar o arquivo resultante*/
        DownloadFile(json.fileNameResult, "application/vnd.ms-xpsdocument");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Converter PDF para PDF em Tons de Cinza

Converter PDF para preto e branco com Aspose.PDF para JavaScript via o kit de ferramentas Web C++.
Por que devo converter PDF para Tons de Cinza? Se o arquivo PDF contiver muitas imagens coloridas e o tamanho do arquivo for mais importante do que a cor, a conversão economiza espaço. Se você imprimir um arquivo PDF em preto e branco, convertê-lo permitirá verificar visualmente como o resultado final fica.

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileConvertToGrayscale = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*converter um arquivo PDF para tons de cinza e salvar como "ResultConvertToGrayscale.pdf" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToGrayscale', "params": [event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf"] }, [event.target.result]);
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


O exemplo de código JavaScript a seguir mostra um exemplo simples de conversão de páginas de PDF em PDF em escala de cinza:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttograyscale/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultConvertToGrayscale.pdf".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro serão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante no sistema operacional do usuário.

```js

  var ffileConvertToGrayscale = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*converter um arquivo PDF para escala de cinza e salvar como "ResultConvertToGrayscale.pdf"*/
      const json = AsposePdfConvertToGrayscale(event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*criar um link para baixar o arquivo resultante*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```