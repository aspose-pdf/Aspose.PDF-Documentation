---
title: Convertir PDF a Excel en Node.js
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-16"
keywords: convertir PDF a Excel usando node.js, convertir PDF a XLSX.
description: Aspose.PDF para Node.js te permite convertir PDF a convertir PDF a formato XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Creando hojas de cálculo desde PDF usando Node.js 

**Aspose.PDF para Node.js via C++** soporta la característica de convertir archivos PDF a archivos Excel.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF para Node.js te presenta la aplicación gratuita en línea ["PDF a XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puedes investigar la funcionalidad y calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a Excel con la aplicación gratuita](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Convertir PDF a XLSX

En caso de que desees convertir un documento PDF, puedes usar la función [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
 
Por favor, verifica el siguiente fragmento de código para convertir en el entorno de Node.js.

**CommonJS:**

1. Llama a `require` e importa el módulo `asposepdfnodejs` como la variable `AsposePdf`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llama a `AsposePdf` como Promesa y realiza la operación para convertir el archivo. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoXlsX.xlsx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convierte un archivo PDF a XlsX y guarda en "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importa el módulo `asposepdfnodejs`.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si es exitoso.
1. Llama a la función [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Convierte el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoXlsX.xlsx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en tu archivo, la información del error estará contenida en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convierte un archivo PDF a XlsX y guarda el "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```