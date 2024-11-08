---
title: Удалить страницу в PDF в Node.js
linktitle: Удаление страниц PDF
type: docs
weight: 30
url: /ru/nodejs-cpp/delete-pages/
description: Вы можете удалить страницы из своего PDF файла, используя Aspose.PDF для Node.js через C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Если вы хотите удалить страницы PDF, вы можете использовать функцию [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).

Особенность этой функции в том, что она может принимать несколько типов в качестве параметра numPages:

- строка: в этом случае мы можем указать набор страниц, используя конкретные страницы или интервалы. Например, строка "7, 20, 30-32, 34" означает, что мы хотим удалить страницы 7, 20, с 30 по 32 и 34.
- массив: в этом случае мы можем указать только страницы. Массив [3,7] означает, что мы хотим удалить страницы 3 и 7.
- int: номер одной страницы.

Пожалуйста, проверьте следующий фрагмент кода, чтобы удалить страницы PDF в среде Node.js.

**CommonJS:**

```javascript
// Импортируем модуль asposepdf
const asposepdf = require('asposepdf');

// Загружаем PDF-документ
let document = asposepdf.PdfDocument.fromFile('example.pdf');

// Удаляем страницы, указав номера страниц
document.removePages('7, 20, 30-32, 34');

// Сохраняем обновленный PDF-документ
document.save('updated_example.pdf');
``

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, из которого будут удалены страницы.
1. Вызовите `AsposePdf` как Promise и выполните операцию по удалению страниц. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/).
1. Удаляет определенные страницы из PDF файла. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultDeletePages.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*строка, включает номера страниц с интервалом: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*массив, массив номеров страниц*/
      /*const numPages = [1,3];*/
      /*число, номер страницы*/
      const numPages = 1;
      /*Удалите страницы из PDF-файла и сохраните в "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, из которого будут удалены страницы.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). Эта функция помогает удалить указанные страницы из PDF-файла. Операция определяется переменной numPages, которая может быть строкой с интервалами страниц (например, "7, 20, 22, 30-32, 33, 36-40, 46"), массивом номеров страниц или одним номером страницы.
1. Удаляет конкретные страницы из PDF-файла. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultDeletePages.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*строка, включает номера страниц с интервалом: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*массив, массив номеров страниц*/
  /*const numPages = [1,3];*/
  /*номер, номер страницы*/
  const numPages = 1;
  /*Удалить страницы из PDF-файла и сохранить в "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```