---
title: Удалить Page в PDF в Node.js
linktitle: Удалить PDF Pages
type: docs
weight: 30
url: /ru/nodejs-cpp/delete-pages/
description: Вы можете удалять страницы из вашего PDF‑файла, используя Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Если вы хотите удалить PDF pages, вы можете использовать [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) функция. 

Особенность этой функции заключается в том, что она может принимать несколько типов в качестве параметра numPages:

- string: в этом случае мы можем указать набор страниц, используя отдельные страницы или интервалы. Например, строка \u00227, 20, 30-32, 34\u0022 означает, что мы хотим удалить страницы 7, 20, с 30 по 32 и 34.
- array: в этом случае мы можем упоминать только страницы. Array [3,7] означает, что мы хотим удалить страницы 3 и 7.
- int: один номер страницы.

Пожалуйста, проверьте следующий фрагмент кода, чтобы удалить страницы PDF в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, из которого будут удаляться страницы.
1. Вызов `AsposePdf` как Promise и выполнить операцию по удалению страниц. Получить объект, если успешно.
1. Вызовите функцию [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. Удаляет конкретные страницы из PDF‑файла. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultDeletePages.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, из которого будут удаляться страницы.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Эта функция помогает удалить указанные страницы из PDF-файла. Операция определяется переменной numPages, которая может быть строкой с интервалами страниц (например, \u00227, 20, 22, 30-32, 33, 36-40, 46\u0022), массивом номеров страниц или одиночным номером страницы.
1. Удаляет конкретные страницы из PDF‑файла. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultDeletePages.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```