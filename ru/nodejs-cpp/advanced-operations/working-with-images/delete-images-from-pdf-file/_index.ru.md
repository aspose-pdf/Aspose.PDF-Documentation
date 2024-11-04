---
title: Удаление изображений из PDF файла в Node.js
linktitle: Удаление изображений
type: docs
weight: 20
url: /nodejs-cpp/delete-images-from-pdf-file/
description: Этот раздел объясняет, как удалить изображения из PDF файла, используя Aspose.PDF для Node.js через C++.
lastmod: "2023-11-16"
---

Вы можете удалить изображения из PDF файла, используя Aspose.PDF для Node.js через C++.

Если вы хотите удалить изображения из PDF, вы можете использовать функцию [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/). Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода для удаления изображений в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, из которого будет удалено изображение.
1. Вызовите `AsposePdf` как Promise и выполните операцию по удалению изображений. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).

1. Удалите изображения из PDF. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfDeleteImages.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Удалите изображения из PDF-файла и сохраните "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, в котором будет удалено изображение.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Удалите изображения из PDF. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfDeleteImages.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Удалить изображения из PDF-файла и сохранить как "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```