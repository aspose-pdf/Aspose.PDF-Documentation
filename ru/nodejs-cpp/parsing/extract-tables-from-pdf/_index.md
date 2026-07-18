---
title: Извлечь таблицы из PDF в Node.js
linktitle: Извлечь таблицы из PDF
type: docs
weight: 10
url: /ru/nodejs-cpp/extract-tables-from-the-pdf-file/
description: Как конвертировать PDF в CSV с использованием Aspose.PDF for Node.js via C++ toolkit.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлекать таблицы при конвертации PDF в CSV файлы

### Конвертировать PDF в CSV

Если в PDF есть таблицы, они сохраняются в отдельные CSV файлы. В случае, если вы хотите конвертировать документ PDF, вы можете использовать [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы конвертировать PDF-файл в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по конвертации файла. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Преобразовать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPDFtoXlsX.xlsx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Преобразовать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPDFtoXlsX.xlsx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```