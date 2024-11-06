---
title: Закладки в PDF в Node.js
linktitle: Закладки в PDF
type: docs
weight: 10
url: ru/nodejs-cpp/bookmark/
description: Вы можете добавить или удалить закладки в PDF документе в среде Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Удаление конкретной закладки из PDF документа

Вы можете удалить закладки из файла PDF, используя Aspose.PDF для Node.js через C++. Если вы хотите удалить закладки из PDF, вы можете использовать функцию [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
Пожалуйста, ознакомьтесь со следующим фрагментом кода для удаления закладок из PDF файла в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, из которого будут удалены закладки.
1. Вызовите `AsposePdf` как Promise и выполните операцию по удалению закладки. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Удалите закладки. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfDeleteBookmarks.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Удалите закладки из PDF-файла и сохраните "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, из которого будут удалены закладки.

1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Удалите закладки. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfDeleteBookmarks.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Удалите закладки из PDF-файла и сохраните в "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```