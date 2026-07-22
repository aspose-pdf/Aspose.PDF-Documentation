---
title: Повернуть страницы PDF в Node.js
linktitle: Повернуть страницы PDF
type: docs
weight: 50
url: /ru/nodejs-cpp/rotate-pages/
description: В этой теме описывается, как программно изменить ориентацию страниц в существующем PDF‑файле в среде Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

В этом разделе описывается, как повернуть страницы в существующем PDF‑файле, используя Aspose.PDF for Node.js via C++.

Если вы хотите повернуть страницы PDF, вы можете использовать [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) function. Эта функция использует специальный параметр \u0027AsposePdfModule.Rotation\u0027 для задания значения вращения. С помощью него можно установить, на сколько градусов нужно повернуть PDF. Доступные варианты: None, 90, 180 или 270 градусов.

Пожалуйста, проверьте следующий фрагмент кода, чтобы повернуть страницы PDF в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, который нужно повернуть.
1. Вызовите `AsposePdf` как Promise и выполните операцию вращения страниц. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Поверните все PDF-файлы. Поворот установлен на 270 градусов (on270). Таким образом, если \u0027json.errorCode\u0027 равно 0, результат операции сохраняется в \u0022ResultRotation.pdf\u0022. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в \u0027json.errorText\u0027.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, который нужно повернуть.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Поверните все PDF-файлы. Поворот установлен на 270 градусов (on270). Таким образом, если \u0027json.errorCode\u0027 равно 0, результат операции сохраняется в \u0022ResultRotation.pdf\u0022. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в \u0027json.errorText\u0027.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```