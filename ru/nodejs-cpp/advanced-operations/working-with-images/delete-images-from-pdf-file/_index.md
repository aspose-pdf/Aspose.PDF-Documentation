---
title: Удалить изображения из PDF-файла в Node.js
linktitle: Удалить изображения
type: docs
weight: 20
url: /ru/nodejs-cpp/delete-images-from-pdf-file/
description: В этом разделе объясняется, как удалить изображения из PDF-файла с помощью Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
---


Вы можете удалить изображения из PDF-файла, используя Aspose.PDF for Node.js via C++.

Если вы хотите удалить изображения из PDF, вы можете использовать [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы удалить изображения в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, из которого будет удалено изображение.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по удалению изображений. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Удалите изображения из PDF. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в “ResultPdfDeleteImages.pdf”. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, из которого будет удалено изображение.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Удалите изображения из PDF. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в “ResultPdfDeleteImages.pdf”. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```