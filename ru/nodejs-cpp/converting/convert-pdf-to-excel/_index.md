---
title: Преобразование PDF в Excel в Node.js
linktitle: Преобразование PDF в Excel
type: docs
weight: 20
url: /ru/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-16"
description: Aspose.PDF для Node.js позволяет преобразовывать PDF в формат XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Создание таблиц из PDF с использованием Node.js

**Aspose.PDF для Node.js через C++** поддерживает функцию преобразования PDF файлов в файлы Excel.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в Excel онлайн**

Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF в XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете оценить функциональность и качество работы.

[![Aspose.PDF Преобразование PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Преобразование PDF в XLSX

Если вы хотите преобразовать PDF документ, вы можете использовать функцию [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
 
Пожалуйста, проверьте следующий фрагмент кода для конвертации в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет преобразован.
1. Вызовите `AsposePdf` как Promise и выполните операцию для конвертации файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Преобразуйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoXlsX.xlsx". Если параметр json.errorCode не равен 0 и, соответственно, появляется ошибка в вашем файле, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразовать PDF-файл в XlsX и сохранить как "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Конвертируйте PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoXlsX.xlsx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Конвертируйте PDF-файл в XlsX и сохраните как "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```