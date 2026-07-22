---
title: Добавить нумерацию страниц в PDF с помощью Node.js
linktitle: Добавить номер страницы
type: docs
weight: 100
url: /ru/nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++ позволяет добавить штамп с номером страницы в ваш PDF‑файл, используя AsposePdfAddPageNum.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Номер страницы облегчает читателю поиск различных частей документа Следующий фрагмент кода показывает, как добавить номера страниц в PDF‑страницы, используя [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) функцию в Node.js.

Пожалуйста, проверьте следующий фрагмент кода, чтобы добавить номера страниц в PDF в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, в который будут добавлены номера страниц.
1. Вызовите `AsposePdf` как Promise и выполните операцию добавления номеров страниц. Получите объект при успехе.
1. Вызовите функцию [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Добавьте номер страницы в PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultAddPageNum.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add page number to a PDF-file save the "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, в который будут добавлены номера страниц.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Добавьте номер страницы в PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultAddPageNum.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add page number to a PDF-file and save the "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```