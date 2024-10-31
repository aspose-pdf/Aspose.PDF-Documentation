---
title: Extraer Tablas de PDF en Node.js
linktitle: Extraer Tablas de PDF
type: docs
weight: 10
url: /nodejs-cpp/extract-tables-from-the-pdf-file/
description: Cómo convertir PDF a CSV usando Aspose.PDF para Node.js a través del conjunto de herramientas C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer tablas al convertir archivos PDF a CSV

### Convertir PDF a CSV

Si hay tablas en el PDF, entonces se guardan en archivos CSV separados. En caso de que desee convertir un documento PDF, puede usar la función [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/). 
Por favor, consulte el siguiente fragmento de código para convertir un archivo PDF en el entorno de Node.js.

**CommonJS:**

1. Llame a `require` e importe el módulo `asposepdfnodejs` como variable `AsposePdf`.
1. Especifique el nombre del archivo PDF que se convertirá.
1. Llame a `AsposePdf` como Promise y realice la operación para convertir el archivo. Reciba el objeto si tiene éxito.

1. Llame a la función [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convierta el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoXlsX.xlsx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convertir un archivo PDF a CSV (extraer tablas) con la plantilla "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... formato número de página), TAB como delimitador y guardar*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Importe el módulo `asposepdfnodejs`.

1. Especifique el nombre del archivo PDF que se convertirá.
1. Inicialice el módulo AsposePdf. Reciba el objeto si tiene éxito.
1. Llame a la función [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convierta el archivo PDF. Así, si 'json.errorCode' es 0, el resultado de la operación se guarda en "ResultPDFtoXlsX.xlsx". Si el parámetro json.errorCode no es 0 y, en consecuencia, aparece un error en su archivo, la información del error se encontrará en 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convertir un archivo PDF a CSV (extraer tablas) con la plantilla "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... formato del número de página), TAB como delimitador y guardar*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```