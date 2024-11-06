---
title: Convertir PDF a formatos PDF/A en Node.js 
linktitle: Convertir PDF a formatos PDF/A
type: docs
weight: 100
url: es/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-16"
description: Este tema te muestra cómo Aspose.PDF permite convertir un archivo PDF a un archivo PDF compatible con PDF/A en el entorno Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para Node.js** te permite convertir un archivo PDF a un archivo PDF compatible con <abbr title="Formato de Documento Portátil para Archivar documentos electrónicos">PDF/A</abbr>. 

{{% alert color="success" %}}
**Intenta convertir PDF a PDF/A en línea**

Aspose.PDF para Node.js te presenta la aplicación gratuita en línea ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puedes intentar investigar la funcionalidad y calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a PDF/A con aplicación gratuita](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Convertir PDF a formato PDF/A

En caso de que desees convertir un documento PDF, puedes usar la función [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
 
Por favor, revise el siguiente fragmento de código para convertir en el entorno de Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF que será convertido.
1. Llame a `AsposePdf` como Promesa y realice la operación para convertir el archivo. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Repare el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultConvertToPDFA.pdf". Durante el proceso de conversión, se realiza una validación, y los resultados de la validación se guardan como "ResultConvertToPDFALog.xml." Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un archivo PDF a PDF/A(1A) y guardar en "ResultConvertToPDFA.pdf"*/
      /*Durante el proceso de conversión, también se realiza la validación, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que se convertirá.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llama a la función [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Repara el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultConvertToPDFA.pdf". Durante el proceso de conversión, se realiza la validación, y los resultados de la validación se guardan como "ResultConvertToPDFALog.xml". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convierte un archivo PDF a PDF/A(1A) y guarda el "ResultConvertToPDFA.pdf"*/
  /*Durante el proceso de conversión, también se realiza la validación, "ResultConvertToPDFALog.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```