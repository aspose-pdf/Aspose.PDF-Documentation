---
title: Converter PDF para documentos Word no Node.js
linktitle: Converter PDF para Word
type: docs
weight: 10
url: /nodejs-cpp/convert-pdf-to-doc/
lastmod: "2023-11-16"
description: Aprenda como converter PDF para DOC(DOCX) no ambiente Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Para editar o conteúdo de um arquivo PDF no Microsoft Word ou outros processadores de texto que suportam os formatos DOC e DOCX. Arquivos PDF são editáveis, mas arquivos DOC e DOCX são mais flexíveis e personalizáveis.

{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF para Node.js apresenta a você um aplicativo online gratuito ["PDF para DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Converter PDF para DOC](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Converter PDF para DOC

Caso você queira converter um documento PDF, você pode usar a função [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será convertido.
1. Chame `AsposePdf` como Promise e execute a operação para converter o arquivo. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação será salvo em "ResultPDFtoDoc.doc". Se o parâmetro json.errorCode não for 0 e, consequentemente, aparecer um erro no seu arquivo, as informações sobre o erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Converter um arquivo PDF para Doc e salvar como "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF que será convertido.
1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPDFtoDoc.doc". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, a informação do erro será contida em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Converter um arquivo PDF para Doc e salvar como "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF para Node.js apresenta a você o aplicativo online gratuito ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade do trabalho.

[![Aspose.PDF Conversão PDF para Word App Gratuita](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Converter PDF para DOCX

Aspose.PDF para Node.js via C++ toolkit permite que você leia e converta documentos PDF para DOCX. DOCX é um formato bem conhecido para documentos do Microsoft Word, cuja estrutura foi alterada de binário simples para uma combinação de arquivos XML e binários. Arquivos Docx podem ser abertos com o Word 2007 e versões posteriores, mas não com as versões anteriores do MS Word que suportam extensões de arquivo DOC.

Caso você queira converter um documento PDF, você pode usar a função [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/). 
Por favor, verifique o snippet de código a seguir para converter no ambiente Node.js.

**CommonJS:**

1. Chame `require` e importe o módulo `asposepdfnodejs` como variável `AsposePdf`.
1. Especifique o nome do arquivo PDF que será convertido.

1. Chame `AsposePdf` como uma Promise e execute a operação para converter o arquivo. Receba o objeto se bem-sucedido.
1. Chame a função [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPDFtoDocX.docx". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer no seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Converte um arquivo PDF para DocX e salva o "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe o módulo `asposepdfnodejs`.
1. Especifique o nome do arquivo PDF que será convertido.

1. Inicialize o módulo AsposePdf. Receba o objeto se for bem-sucedido.
1. Chame a função [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Converta o arquivo PDF. Assim, se 'json.errorCode' for 0, o resultado da operação é salvo em "ResultPDFtoDocX.docx". Se o parâmetro json.errorCode não for 0 e, consequentemente, um erro aparecer em seu arquivo, as informações do erro estarão contidas em 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Converta um arquivo PDF para DocX e salve como "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```