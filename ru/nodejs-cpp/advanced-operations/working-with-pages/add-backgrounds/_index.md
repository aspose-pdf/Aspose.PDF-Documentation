---
title: Добавить фон в PDF в Node.js
linktitle: Добавить фон
type: docs
weight: 10
url: /ru/nodejs-cpp/add-background/
description: Добавьте фоновое изображение в ваш PDF файл в Node.js 
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Следующие фрагменты кода показывают, как добавить фоновое изображение на страницы PDF с использованием функции [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) в Node.js.

Пожалуйста, ознакомьтесь с следующим фрагментом кода для добавления фонового изображения в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, в который будет добавлено фоновое изображение.
1. Вызовите `AsposePdf` как Promise и выполните операцию по добавлению фонового изображения. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).

1. Добавить фоновое изображение в PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultAddBackgroundImage.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Добавить фоновое изображение в PDF-файл и сохранить как "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, в который будет добавлено фоновое изображение.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. Добавьте фоновое изображение в файл PDF. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultAddBackgroundImage.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Добавьте фоновое изображение в PDF-файл и сохраните "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```