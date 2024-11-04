---
title: Converter PDF para Formatos de Imagem em JavaScript
linktitle: Converter PDF para Imagens
type: docs
weight: 70
url: /javascript-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-01"
description: Este tópico mostra como usar Aspose.PDF para converter PDF para vários formatos de imagens, por exemplo, TIFF, BMP, JPEG, PNG, SVG com algumas linhas de código.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## JavaScript Converter PDF para Imagem

Neste artigo, mostraremos as opções para converter PDF para formatos de imagem.

Documentos previamente digitalizados são frequentemente salvos no formato de arquivo PDF. No entanto, você precisa editá-lo em um editor gráfico ou enviá-lo em formato de imagem? Temos uma ferramenta universal para você converter PDF em imagens usando
A tarefa mais comum é quando você precisa salvar um documento PDF inteiro ou algumas páginas específicas de um documento como um conjunto de imagens. **Aspose for JavaScript via C++** permite que você converta PDF para os formatos JPG e PNG para simplificar as etapas necessárias para obter suas imagens de um arquivo PDF específico.

**Aspose.PDF for JavaScript via C++** suporta várias conversões de formatos de imagem para PDF.
 Por favor, confira a seção [Formatos de Arquivo Suportados pelo Aspose.PDF](https://docs.aspose.com/pdf/javascript-cpp/supported-file-formats/).

A operação de conversão depende do número de páginas no documento e pode ser muito demorada. Portanto, recomendamos fortemente o uso de Web Workers.

Este código demonstra uma maneira de transferir tarefas de conversão de arquivos PDF que consomem muitos recursos para um web worker para evitar o bloqueio do thread principal da UI. Ele também oferece uma maneira amigável de baixar o arquivo convertido.

{{% alert color="success" %}}
**Tente converter PDF para JPEG online**

Aspose.PDF para JavaScript apresenta a você o aplicativo online gratuito ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão de PDF para JPEG com Aplicativo Gratuito Aspose.PDF](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Converter PDF para JPEG

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? 
          `Contagem de arquivos(páginas): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToJpg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*converter um arquivo PDF para arquivos jpg com o template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formatar número da página), resolução 150 DPI e salvar - Pedir ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToJpg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Trecho de código]

    /*criar um link para baixar o arquivo resultante*/
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

O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas PDF em arquivos Jpeg:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestojpg/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfToJpg{0:D2}.jpg".
1. Em seguida, se o 'json.errorCode' for 0, então seu arquivo de resultado receberá o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre esse erro serão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileToJpg = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*converter um arquivo PDF para arquivos jpg com o modelo "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... formato do número da página), resolução 150 DPI e salvar*/
      const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Contagem de arquivos(páginas): " + json.filesCount.toString();
        /*criar links para os arquivos resultantes*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**Tente converter PDF para TIFF online**

Aspose.PDF para JavaScript apresenta a você o aplicativo online gratuito ["PDF para TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode tentar investigar a funcionalidade e a qualidade com que ele funciona.

[![Conversão Aspose.PDF de PDF para TIFF com aplicativo gratuito](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Converter PDF para TIFF

```js

  /*Cria Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? 
          `Contagem de arquivos(páginas): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/tiff", element) ) ?? ""}` : 
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToTiff = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Converte um arquivo PDF para TIFF com o modelo "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... número de página no formato), resolução de 150 DPI e salva - Solicita ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToTiff', "params": [event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Cria um link para baixar o arquivo resultante*/
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas de PDF em arquivos Tiff:

1. Selecione um arquivo PDF para converter.
1. Crie um 'FileReader'.
1. A função [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestotiff/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfToTiff{0:D2}.tiff".
1. Em seguida, se o 'json.errorCode' é 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então a informação sobre tal erro será contida no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileToTiff = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Converta um arquivo PDF para TIFF com o modelo "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... formato do número da página), resolução 150 DPI e salve*/
        const json = AsposePdfPagesToTiff(event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Contagem de arquivos(páginas): " + json.filesCount.toString();
          /*Crie links para os arquivos resultantes*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/tiff");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como um exemplo de como nossas aplicações gratuitas funcionam, por favor, confira o próximo recurso.

Aspose.PDF para JavaScript apresenta a você a aplicação online gratuita ["PDF para PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode tentar investigar a funcionalidade e a qualidade com que ela funciona.

[![Como converter PDF para PNG usando Aplicativo Gratuito](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF para PNG

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? 
          `Contagem de arquivos(páginas): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/png", element) ) ?? ""}` : 
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToPng = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'proprietário';
        /*converter um arquivo PDF em arquivos png com o modelo "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... formato número da página), resolução 150 DPI e salvar - Pedir ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToPng', "params": [event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas de PDF em arquivos PNG:

1. Selecione um arquivo PDF para converter.
1. Crie um 'FileReader'.
1. A função [AsposePdfPagesToPng](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestopng/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfToPng{0:D2}.png".
1. Em seguida, se o 'json.errorCode' for 0, então o seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro serão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você faça o download do arquivo resultante para o sistema operacional do usuário.

```js

  var ffileToPng = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*converter um arquivo PDF em arquivos png com o modelo "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... formatar número da página), resolução 150 DPI e salvar*/
      const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Contagem de arquivos(páginas): " + json.filesCount.toString();
        /*criar links para arquivos de resultado*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/png");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF para JavaScript apresenta a você a aplicação online gratuita ["PDF para SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para SVG com Aplicativo Gratuito](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Gráficos Vetoriais Escaláveis (SVG)** é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

## Converter PDF para SVG

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? 
          `Contagem de arquivos(páginas): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/svg", element) ) ?? ""}` : 
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToSvg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Converter um arquivo PDF para SVG - Perguntar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg"] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas PDF em arquivos SVG:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvg/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfToSvg.svg".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileToSvg = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Converta um arquivo PDF para SVG*/
        const json = AsposePdfPagesToSvg(event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Quantidade de arquivos(páginas): " + json.filesCount.toString();
          /*Crie links para os arquivos resultantes*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/svg");
        }
        else document.getElementById('output').textContent = json.errorText;
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


### Converter PDF para SVG compactado

```js

  /*Criar Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? `Resultado:\n${DownloadFile(evt.data.json.fileNameResult, "application/zip", evt.data.params[0])}` : `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de eventos*/
    const ffileToSvgZip = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Converter um arquivo PDF para SVG(zip) e salvar o "ResultPdfToSvgZip.zip" - Solicitar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvgZip', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip"] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas PDF em arquivos SVG(zip):

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvgzip/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfToSvgZip.zip".
1. Em seguida, se o 'json.errorCode' for 0, então o seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileToSvgZip = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Converta um arquivo PDF para SVG(zip) e salve como "ResultPdfToSvgZip.zip"*/
        const json = AsposePdfPagesToSvgZip(event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Crie um link para baixar o arquivo resultante*/
        DownloadFile(json.fileNameResult, "application/zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Converter PDF para DICOM

```js

  /*Criar Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'carregado!' :
      (evt.data.json.errorCode == 0) ?
        `Contagem de arquivos(páginas): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
          (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "application/dicom", element) ) ?? ""}` :
        `Erro: ${evt.data.json.errorText}`;

  /*Manipulador de eventos*/
  const ffileToDICOM = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Converter um arquivo PDF para DICOM com o modelo "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... formato número de página), resolução 150 DPI e salvar - Solicitar ao Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToDICOM', "params": [event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150] }, [event.target.result]);
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


O seguinte trecho de código JavaScript mostra um exemplo simples de conversão de páginas PDF em arquivos DICOM:

1. Selecione um arquivo PDF para converter.
2. Crie um 'FileReader'.
3. A função [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestodicom/) é executada.
4. O nome do arquivo resultante é definido, neste exemplo "ResultPdfToDICOM{0:D2}.dcm".
5. Em seguida, se o 'json.errorCode' for 0, então o seu arquivo de resultado recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro no seu arquivo, então as informações sobre tal erro estarão contidas no arquivo 'json.errorText'.
6. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

  var ffileToDICOM = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Converte um arquivo PDF para DICOM com o template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... número da página no formato), resolução de 150 DPI e salva*/
      const json = AsposePdfPagesToDICOM(event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Contagem de arquivos(páginas): " + json.filesCount.toString();
        /*Cria links para os arquivos de resultado*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "application/dicom");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Converter PDF para BMP

```js

    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Erro do Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'carregado!' :
        (evt.data.json.errorCode == 0) ? 
          `Contagem de arquivos(páginas): ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/bmp", element) ) ?? ""}` : 
          `Erro: ${evt.data.json.errorText}`;

    /*Manipulador de evento*/
    const ffileToBmp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Converter um arquivo PDF para BMP com o modelo "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... formatar número da página), resolução 150 DPI e salvar - Perguntar ao Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToBmp', "params": [event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150] }, [event.target.result]);
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


The following JavaScript code snippet shows simple example of coverting PDF pages into BMP files:

1. Selecione um arquivo PDF para conversão.
1. Crie um 'FileReader'.
1. A função [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestobmp/) é executada.
1. O nome do arquivo resultante é definido, neste exemplo "ResultPdfToBmp{0:D2}.bmp".
1. Em seguida, se o 'json.errorCode' for 0, então seu DownloadFile recebe o nome que você especificou anteriormente. Se o parâmetro 'json.errorCode' não for igual a 0 e, consequentemente, houver um erro em seu arquivo, então as informações sobre esse erro estarão contidas no arquivo 'json.errorText'.
1. Como resultado, a função [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) gera um link e permite que você baixe o arquivo resultante para o sistema operacional do usuário.

```js

    var ffileToBmp = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Converta um arquivo PDF para BMP com o modelo "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... formato do número da página), resolução 150 DPI e salve*/
        const json = AsposePdfPagesToBmp(event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "Contagem de arquivos (páginas): " + json.filesCount.toString();
          /*Crie links para os arquivos resultantes*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/bmp");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```