---
title: Закладки в PDF в Node.js
linktitle: Закладки в PDF
type: docs
weight: 10
url: /ru/nodejs-cpp/bookmark/
description: Вы можете добавить или удалить закладки в PDF‑документе в среде Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Удалить конкретную закладку из PDF‑документа

Вы можете удалить закладки из PDF‑файла, используя Aspose.PDF for Node.js via C++. Если вы хотите удалить закладки из PDF, вы можете использовать [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы удалить закладки из PDF‑файла в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, из которого будут удалены закладки.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по удалению закладки. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Удалить закладки. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в «ResultPdfDeleteBookmarks.pdf». Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, из которого будут удалены закладки.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Удалить закладки. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в «ResultPdfDeleteBookmarks.pdf». Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```