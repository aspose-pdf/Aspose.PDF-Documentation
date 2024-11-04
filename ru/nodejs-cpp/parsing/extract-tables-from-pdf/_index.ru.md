---
title: Извлечение таблиц из PDF в Node.js
linktitle: Извлечение таблиц из PDF
type: docs
weight: 10
url: /nodejs-cpp/extract-tables-from-the-pdf-file/
description: Как преобразовать PDF в CSV с использованием Aspose.PDF для Node.js через C++ toolkit.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение таблиц при преобразовании PDF в файлы CSV

### Преобразование PDF в CSV

Если в PDF есть таблицы, они сохраняются в отдельных CSV файлах. В случае, если вы хотите преобразовать PDF документ, вы можете использовать функцию [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/). Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы преобразовать PDF файл в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
2. Укажите имя PDF файла, который будет преобразован.
3. Вызовите `AsposePdf` как Promise и выполните операцию по преобразованию файла. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoXlsX.xlsx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Конвертировать PDF-файл в CSV (извлечь таблицы) с шаблоном "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), TAB в качестве разделителя и сохранить*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.

1. Укажите название PDF-файла, который будет преобразован.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Преобразуйте PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoXlsX.xlsx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразуйте PDF-файл в CSV (извлеките таблицы) с шаблоном "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... формат номера страницы), TAB в качестве разделителя и сохраните*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```