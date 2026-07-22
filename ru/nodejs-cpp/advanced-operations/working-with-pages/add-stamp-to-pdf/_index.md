---
title: Добавить штампы‑изображения в PDF в Node.js
linktitle: Штампы‑изображения в PDF‑файле
type: docs
weight: 60
url: /ru/nodejs-cpp/stamping/
description: Добавьте штамп‑изображение в ваш PDF‑документ, используя AsposePdfAddStamp с инструментом Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавьте штамп‑изображение в PDF‑файл

Нанесение штампа на PDF‑документ аналогично нанесению штампа на бумажный документ. Штамп в PDF‑файле предоставляет дополнительную информацию, такую как защита PDF‑файла от использования другими пользователями и подтверждение безопасности содержимого PDF‑файла.
Вы можете использовать [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) функция для добавления изображения‑штампа в PDF‑файл с использованием Node.js.

Пожалуйста, проверьте следующий фрагмент кода, чтобы добавить изображение‑штамп в PDF‑файл в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, в который будет добавлен изображение‑штамп.
1. Вызовите `AsposePdf` как Promise и выполните операцию добавления штампа изображения. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Добавьте штамп в PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultImage.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, в который будет добавлен изображение‑штамп.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Добавьте штамп в PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultImage.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```