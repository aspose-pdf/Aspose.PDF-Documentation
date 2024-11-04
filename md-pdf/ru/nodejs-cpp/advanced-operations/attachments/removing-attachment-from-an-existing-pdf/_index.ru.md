---
title: Удаление вложений из PDF в Node.js
linktitle: Удаление вложения из существующего PDF
type: docs
weight: 10
url: /nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF может удалять вложения из ваших PDF-документов. Используйте среду Node.js для удаления вложений в PDF-файлах с помощью Aspose.PDF.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Вы можете удалить вложения из PDF-файла, используя Aspose.PDF для Node.js через C++. В случае, если вы хотите удалить вложения из PDF, вы можете использовать функцию [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/). Пожалуйста, ознакомьтесь со следующим фрагментом кода для удаления вложений из PDF-файла в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, из которого будут удалены вложения.

1. Вызовите `AsposePdf` как Promise и выполните операцию по удалению вложений. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Удалите вложения. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfDeleteAttachments.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Удалите вложения из PDF-файла и сохраните "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, из которого будут удалены вложения.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Удалите вложения. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfDeleteAttachments.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Удалить вложения из PDF-файла и сохранить "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```