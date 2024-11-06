---
title: Добавить Заголовок и Колонтитул в PDF на Node.js
linktitle: Добавить Заголовок и Колонтитул в PDF
type: docs
weight: 70
url: ru/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Node.js через C++ позволяет добавлять заголовки и колонтитулы в ваш PDF файл, используя AsposePdfAddTextHeaderFooter.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js через C++** позволяет добавлять заголовок и колонтитул в ваш существующий PDF файл. 

Если вы хотите добавить заголовок и колонтитул, вы можете использовать функцию [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).

Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода, чтобы добавить заголовок и колонтитул в PDF файл в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, в который будут добавлены заголовок и колонтитул.

1. Вызовите `AsposePdf` как Promise и выполните операцию по добавлению верхнего и нижнего колонтитула. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Добавьте текст в верхний и нижний колонтитул PDF файла. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultAddHeaderFooter.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Добавьте текст в верхний/нижний колонтитул PDF-файла и сохраните "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
2. Укажите имя PDF файла, в который будут добавлены заголовок и нижний колонтитул.
3. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
4. Вызовите функцию [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
5. Добавьте текст в заголовок и нижний колонтитул PDF файла. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultAddHeaderFooter.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Добавьте текст в заголовок/нижний колонтитул PDF-файла и сохраните как "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```