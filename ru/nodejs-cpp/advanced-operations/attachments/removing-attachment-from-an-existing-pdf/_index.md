---
title: Удаление вложений из PDF в Node.js
linktitle: Удаление вложения из существующего PDF
type: docs
weight: 10
url: /ru/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF может удалять вложения из ваших PDF‑документов. Используйте среду Node.js для удаления вложений в PDF‑файлах с помощью Aspose.PDF.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Вы можете удалять вложения из PDF‑файла, используя Aspose.PDF for Node.js via C++. Если вы хотите удалить вложения из PDF, вы можете использовать [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) функция. 
Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы удалить вложения из PDF‑файла в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, из которого будут удалены вложения.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию по удалению вложений. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Удалите вложения. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в «ResultPdfDeleteAttachments.pdf». Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, из которого будут удалены вложения.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. Удалите вложения. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в «ResultPdfDeleteAttachments.pdf». Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```