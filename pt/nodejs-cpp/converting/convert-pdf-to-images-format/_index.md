---
title: Converter PDF para formatos de imagem em Node.js
linktitle: Converter PDF para imagens
type: docs
weight: 70
url: /pt/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-18"
description: Este tópico mostra como usar o Aspose.PDF para converter PDF em vários formatos de imagem, por exemplo, TIFF, BMP, JPEG, PNG, SVG, com algumas linhas de código no ambiente Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js Converter PDF para Imagem

Neste artigo, mostraremos as opções para converter PDF para formatos de imagem.

Documentos escaneados anteriormente são frequentemente salvos no formato de arquivo PDF. No entanto, você precisa editá-lo em um editor gráfico ou enviá-lo posteriormente em formato de imagem? Temos uma ferramenta universal para você converter PDF em imagens usando 
A tarefa mais comum é quando você precisa salvar um documento PDF inteiro ou algumas páginas específicas de um documento como um conjunto de imagens. **Aspose for Node.js via C++** permite converter PDF para formatos JPG e PNG para simplificar as etapas necessárias para obter suas imagens de um arquivo PDF específico.

**Aspose.PDF for Node.js via C++** suporta várias conversões de PDF para formatos de imagem. Por favor, verifique a seção [Aspose.PDF Formatos de Arquivo Suportados](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/).

{{% alert color="success" %}}
**Tente converter PDF para JPEG online**

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF para JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para JPEG com aplicativo gratuito](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Converter PDF para JPEG

Caso queira converter um documento PDF, você pode usar [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToJpg{0:D2}.jpg". Onde {0:D2} representa o número da página no formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToJpg{0:D2}.jpg". Onde {0:D2} representa o número da página no formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to JPG with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Tente converter PDF para TIFF online**

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF para TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Conversão Aspose.PDF de PDF para TIFF com App Gratuito](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Converter PDF para TIFF

Caso queira converter um documento PDF, você pode usar [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToTiff{0:D2}.tiff". Onde {0:D2} representa o número da página com formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToTiff{0:D2}.tiff". Onde {0:D2} representa o número da página com formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, ocorrer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TIFF with template "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Tente converter PDF para PNG online**

Como exemplo de como nossas aplicações gratuitas funcionam, verifique o próximo recurso.

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF para PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Como converter PDF para PNG usando aplicativo gratuito](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Converter PDF para PNG

Caso queira converter um documento PDF, você pode usar [AsposePdfPagesParaPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfPagesParaPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToPng{0:D2}.png". Onde {0:D2} representa o número da página com formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfPagesParaPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToPng{0:D2}.png". Onde {0:D2} representa o número da página com formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PNG with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

{{% alert color="success" %}}
**Tente converter PDF para SVG online**

Aspose.PDF for Node.js apresenta a você um aplicativo gratuito online ["PDF para SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para SVG com Aplicativo Gratuito](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** é uma família de especificações de um formato de arquivo baseado em XML para gráficos vetoriais bidimensionais, tanto estáticos quanto dinâmicos (interativos ou animados). A especificação SVG é um padrão aberto que está em desenvolvimento pelo World Wide Web Consortium (W3C) desde 1999.

## Converter PDF para SVG

### Converter PDF para SVG clássico

Caso queira converter um documento PDF, você pode usar [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em \"ResultPdfToSvg.svg\". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em \"ResultPdfToSvg.svg\". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to SVG and save the "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### Converter PDF em SVG compactado

Caso queira converter um documento PDF, você pode usar [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToSvgZip.zip". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to SVG(zip) and save the "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToSvgZip.zip". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*convert a PDF-file to SVG zip and save the "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## Converter PDF para DICOM

Caso queira converter um documento PDF, você pode usar [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfToDICOM{0:D2}.dcm". Onde {0:D2} representa o número da página no formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPdfToDICOM{0:D2}.dcm". Onde {0:D2} representa o número da página no formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DICOM with template "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

## Converter PDF para BMP

Caso queira converter um documento PDF, você pode usar [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) função. 
Por favor, verifique o trecho de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chamada `require` e importar `asposepdfnodejs` módulo como `AsposePdf` variável.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chamada `AsposePdf` como Promise e execute a operação de conversão de arquivo. Receba o objeto caso seja bem-sucedido.
1. Chame a função [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToBmp{0:D2}.bmp". Onde {0:D2} representa o número da página no formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar o `asposepdfnodejs` módulo.
1. Especifique o nome do arquivo PDF que será convertido
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/).
1. Converter arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPdfToBmp{0:D2}.bmp". Onde {0:D2} representa o número da página no formato de dois dígitos. As imagens são salvas com resolução de 150 DPI. Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to BMP with template "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```





