---
title: Разделение PDF в Node.js
linktitle: Разделение PDF файлов
type: docs
weight: 30
url: /nodejs-cpp/split-pdf/
description: Эта тема показывает, как разделить страницы PDF на отдельные файлы PDF с помощью Aspose.PDF для Node.js через C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Разделение PDF на два файла с использованием Node.js

Если вы хотите разделить один PDF на части, вы можете использовать функцию [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/). Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы разделить два PDF в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
2. Укажите имя PDF файлов, которые будут разделены.
3. Вызовите `AsposePdf` как Promise и выполните операцию по разделению файла. Получите объект, если операция успешна.
4. Вызовите функцию [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).

1. Разделите два PDF файла. Устанавливает переменную pageToSplit в 1, указывая, что PDF файл будет разделён на странице 1.
1. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultSplit1.pdf" и "ResultSplit2.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Установить номер страницы для разделения*/
      const pageToSplit = 1;
      /*Разделить на два PDF-файла и сохранить "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.

1. Укажите имя PDF файлов, которые будут разделены.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Разделите два PDF файла. Устанавливает переменную pageToSplit в 1, указывая, что PDF файл будет разделен на странице 1.
1. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultSplit1.pdf" и "ResultSplit2.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Установите номер страницы для разделения*/
  const pageToSplit = 1;
  /*Разделите на два PDF-файла и сохраните в "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```