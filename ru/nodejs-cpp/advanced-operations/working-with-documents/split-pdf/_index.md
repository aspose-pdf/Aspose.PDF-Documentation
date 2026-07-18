---
title: Разделить PDF в Node.js
linktitle: Разделить PDF-файлы
type: docs
weight: 30
url: /ru/nodejs-cpp/split-pdf/
description: В этой теме показано, как разбить страницы PDF на отдельные PDF-файлы с помощью Aspose.PDF for Node.js via C++ .
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Разделить PDF на два файла с использованием Node.js

Если вы хотите разделить один PDF на части, вы можете использовать [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы разделить два PDF в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файлов, которые будут разделены.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию разделения файла. Получить объект, если успешно.
1. Вызовите функцию [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Разделите два PDF‑файла. Задается переменная pageToSplit со значением 1, указывая, что PDF‑файл будет разделён на странице 1. 
1. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в «ResultSplit1.pdf» и «ResultSplit2.pdf». Если параметр json.errorCode не равен 0 и соответственно в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файлов, которые будут разделены.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Разделите два PDF‑файла. Задается переменная pageToSplit со значением 1, указывая, что PDF‑файл будет разделён на странице 1. 
1. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в «ResultSplit1.pdf» и «ResultSplit2.pdf». Если параметр json.errorCode не равен 0 и соответственно в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```