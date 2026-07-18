---
title: Конвертировать PDF в Excel в Node.js
linktitle: Конвертировать PDF в Excel
type: docs
weight: 20
url: /ru/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-18"
description: Aspose.PDF for Node.js позволяет конвертировать PDF в формат XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Создание таблиц из PDF с помощью Node.js 

**Aspose.PDF for Node.js via C++** поддерживает функцию конвертации PDF‑файлов в Excel‑файл.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF преобразование PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Конвертировать PDF в XLSX

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по конвертации файла. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Преобразовать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPDFtoXlsX.xlsx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. Преобразовать PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPDFtoXlsX.xlsx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

