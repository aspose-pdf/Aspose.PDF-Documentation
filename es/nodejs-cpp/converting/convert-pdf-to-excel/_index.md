---
title: Convertir PDF a Excel en Node.js
linktitle: Convertir PDF a Excel
type: docs
weight: 20
url: /es/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-18"
description: Aspose.PDF for Node.js le permite convertir PDF al formato XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Creando hojas de cálculo a partir de PDF usando Node.js 

**Aspose.PDF for Node.js via C++** admite la función de convertir archivos PDF a archivos de Excel.

{{% alert color="success" %}}
**Intenta convertir PDF a Excel en línea**

Aspose.PDF para Node.js le presenta una aplicación gratuita en línea ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), donde puede probar la funcionalidad y la calidad con la que funciona.

[![Conversión de Aspose.PDF de PDF a Excel con aplicación gratuita](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Convertir PDF a XLSX

En caso de que desees convertir un documento PDF, puedes usar [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/) función. 
Por favor, revisa el siguiente fragmento de código para convertir en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoXlsX.xlsx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoXlsX.xlsx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

