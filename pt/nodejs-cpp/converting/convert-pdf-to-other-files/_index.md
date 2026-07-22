---
title: Converter PDF para EPUB, TeX, Texto, XPS em Node.js
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /pt/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-18"
description: Este tópico mostra como converter arquivos PDF para outros formatos de arquivo, como EPUB, LaTeX, Texto, XPS etc., no ambiente Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão de PDF para EPUB com Aspose.PDF e aplicativo gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Converter PDF para EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** é um padrão de e-book livre e aberto do International Digital Publishing Forum (IDPF). Os arquivos têm a extensão .epub.
O EPUB foi projetado para conteúdo refluível, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico. O EPUB também suporta conteúdo de layout fixo. O formato foi concebido como um formato único que editores e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

Caso queira converter um documento PDF, você pode usar [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Converter o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoEPUB.epub". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. Converter o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoEPUB.epub". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para LaTeX/TeX com aplicativo gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Converter PDF para TeX

**Aspose.PDF for Node.js** suporta a conversão de PDF para TeX.
Caso queira converter um documento PDF, você pode usar [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da opera\u00e7\u00e3o ser\u00e1 salvo em \"ResultPDFtoTeX.tex\". Se o par\u00e2metro json.errorCode n\u00e3o for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informa\u00e7\u00f5es do erro estar\u00e3o contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da opera\u00e7\u00e3o ser\u00e1 salvo em \"ResultPDFtoTeX.tex\". Se o par\u00e2metro json.errorCode n\u00e3o for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informa\u00e7\u00f5es do erro estar\u00e3o contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Tente converter PDF para Texto online**

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para Texto com Aplicativo Gratuito](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Converter PDF para TXT

Caso queira converter um documento PDF, você pode usar [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoTxt.txt". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoTxt.txt". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para XPS com App Gratuito](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Converter PDF para XPS

O tipo de arquivo XPS está principalmente associado à XML Paper Specification da Microsoft Corporation. A XML Paper Specification (XPS), anteriormente com o nome de código Metro e incorporando o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos ao sistema operacional Windows.

**Aspose.PDF for Node.js** oferece a possibilidade de converter arquivos PDF para <abbr title="XML Paper Specification">XPS</abbr> formato. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com Node.js.

Caso queira converter um documento PDF, você pode usar [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoXps.xps". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoXps.xps". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Converter PDF para PDF em tons de cinza

Converter PDF para preto e branco com o Aspose.PDF for Node.js via C++ toolkit. 
Por que devo converter PDF para tons de cinza? Se o arquivo PDF contém muitas imagens coloridas e o tamanho do arquivo é importante em vez da cor, a conversão economiza espaço. Se você imprimir um arquivo PDF em preto e branco, convertê-lo permitirá que você verifique visualmente como ficará o resultado final. 

Caso queira converter um documento PDF, você pode usar [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultConvertToGrayscale.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultConvertToGrayscale.pdf". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```






