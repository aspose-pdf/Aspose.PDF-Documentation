---
title: Поворот страниц PDF в Node.js
linktitle: Поворот страниц PDF
type: docs
weight: 50
url: ru/nodejs-cpp/rotate-pages/
description: Эта тема описывает, как программно изменить ориентацию страниц в существующем PDF-файле в среде Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Этот раздел описывает, как поворачивать страницы в существующем PDF-файле с использованием Aspose.PDF для Node.js через C++.

Если вы хотите повернуть страницы PDF, вы можете использовать функцию [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). Эта функция использует специальный параметр 'AsposePdfModule.Rotation' для значения поворота. С его помощью вы можете установить, на сколько градусов необходимо повернуть PDF. Есть варианты: None, 90, 180 или 270 градусов.

Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы повернуть страницы PDF в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.

1. Укажите имя PDF-файла для поворота.
1. Вызовите `AsposePdf` как Promise и выполните операцию по повороту страниц. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
1. Поверните все PDF-файлы. Поворот установлен на 270 градусов (on270). Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultRotation.pdf". Если параметр json.errorCode не равен 0 и, соответственно, возникает ошибка в вашем файле, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Повернуть PDF-страницы и сохранить в "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
2. Укажите имя PDF файла для поворота.
3. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
4. Вызовите функцию [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/).
5. Поверните все PDF файлы. Поворот установлен на 270 градусов (on270). Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultRotation.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Поверните страницы PDF и сохраните "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```