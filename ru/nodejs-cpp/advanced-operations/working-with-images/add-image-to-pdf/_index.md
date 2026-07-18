---
title: Добавить изображение в PDF с помощью Node.js
linktitle: Добавить изображение
type: docs
weight: 10
url: /ru/nodejs-cpp/add-image-to-pdf/
description: В этом разделе описывается, как добавить изображение в существующий файл PDF, используя Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
---

## Добавить изображение в существующий файл PDF

Считается, что добавление изображений в PDF‑файлы требует сложного специального инструмента. Однако с Aspose.PDF for Node.js вы можете быстро и легко добавить необходимые изображения в PDF в среде Node.js.

Мы можем добавлять изображения только в конец файла, поэтому правильный пример — у нас есть несколько отсканированных страниц документа, которые мы преобразуем в один PDF.

Если вы хотите добавить изображения, вы можете использовать [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) функция. 
Пожалуйста, посмотрите следующий фрагмент кода, чтобы добавить изображения в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, в который будет добавлено изображение.
1. Вызов `AsposePdf` как Promise и выполнить операцию добавления изображения. Получить объект при успехе.
1. Вызовите функцию [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Добавьте изображение в конец PDF. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в “ResultAddImage.pdf”. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, в который будет добавлено изображение.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Добавьте изображение в конец PDF. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в “ResultAddImage.pdf”. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```