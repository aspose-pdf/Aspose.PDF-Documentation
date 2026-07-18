---
title: Extraer tablas de PDF en Node.js
linktitle: Extraer tablas de PDF
type: docs
weight: 10
url: /es/nodejs-cpp/extract-tables-from-the-pdf-file/
description: Cómo convertir PDF a CSV usando Aspose.PDF for Node.js a través del kit de herramientas C\u002B\u002B.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer tablas mientras se convierten PDF a archivos CSV

### Convertir PDF a CSV

Si hay tablas en el PDF, entonces se guardan en archivos CSV separados. En caso de que desees convertir el documento PDF, puedes usar [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) función. 
Por favor, revise el siguiente fragmento de código para convertir un archivo PDF en un entorno Node.js.

**CommonJS:**

1. Llamar `require` y importar `asposepdfnodejs` módulo como `AsposePdf` variable.
1. Especifica el nombre del archivo PDF que será convertido.
1. Llamar `AsposePdf` como Promise y realiza la operación para convertir el archivo. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoXlsX.xlsx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importar el `asposepdfnodejs` módulo.
1. Especifica el nombre del archivo PDF que será convertido.
1. Inicializa el módulo AsposePdf. Recibe el objeto si tiene éxito.
1. Llame a la función [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convertir archivo PDF. Por lo tanto, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoXlsX.xlsx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```