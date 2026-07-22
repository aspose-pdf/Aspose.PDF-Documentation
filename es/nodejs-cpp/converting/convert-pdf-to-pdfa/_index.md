---
title: Convertir PDF a formatos PDF/A en Node.js
linktitle: Convertir PDF a formatos PDF/A
type: docs
weight: 100
url: /es/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2026-07-18"
description: Este tema le muestra cómo Aspose.PDF permite convertir un archivo PDF a un archivo PDF compatible con PDF/A en el entorno Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js** permite convertir un archivo PDF a un <abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr> archivo PDF compatible. 

{{% alert color="success" %}}
**Intente convertir PDF a PDF/A en línea**

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea [“PDF a PDF/A-1A”](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de PDF a PDF/A de Aspose.PDF con aplicación gratuita](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Convertir PDF al formato PDF/A

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Reparar el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultConvertToPDFA.pdf". Durante el proceso de conversión, se realiza la validación y los resultados de la validación se guardan como "ResultConvertToPDFALog.xml". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
      /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Reparar el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultConvertToPDFA.pdf". Durante el proceso de conversión, se realiza la validación y los resultados de la validación se guardan como "ResultConvertToPDFALog.xml". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
  /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```





