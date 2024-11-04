---
title: Добавление нумерации страниц в PDF в Node.js
linktitle: Добавить номер страницы
type: docs
weight: 100
url: /nodejs-cpp/add-page-number/
description: Aspose.PDF для Node.js через C++ позволяет добавлять штамп с номером страницы в ваш PDF файл, используя AsposePdfAddPageNum.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Номер страницы облегчает читателю поиск различных частей документа. Следующие фрагменты кода показывают, как добавить номера страниц в PDF с помощью функции [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) в Node.js.

Пожалуйста, ознакомьтесь с следующим фрагментом кода для добавления номеров страниц в PDF в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, в который будут добавлены номера страниц.
1. Вызовите `AsposePdf` как Promise и выполните операцию по добавлению номеров страниц. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Добавьте номер страницы в PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultAddPageNum.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Добавить номер страницы в PDF файл и сохранить в "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, в который будут добавлены номера страниц.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Добавьте номер страницы в PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultAddPageNum.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Добавить номер страницы в PDF-файл и сохранить "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```