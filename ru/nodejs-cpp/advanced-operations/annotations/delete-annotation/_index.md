---
title: Удаление аннотации в Node.js
linktitle: Удалить аннотацию
type: docs
weight: 10
url: ru/nodejs-cpp/delete-annotation/
description: С помощью Aspose.PDF для Node.js вы можете удалить аннотацию из вашего PDF файла.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Вы можете удалить аннотации из PDF файла, используя Aspose.PDF для Node.js через C++. Если вы хотите удалить аннотации из PDF, вы можете использовать функцию [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/). Пожалуйста, ознакомьтесь со следующим фрагментом кода для удаления аннотаций из PDF файла в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, из которого будет удалена аннотация.
1. Вызовите `AsposePdf` как Promise и выполните операцию по удалению аннотаций. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Удалите аннотации. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfDeleteAnnotations.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Удалите аннотации из PDF-файла и сохраните "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, из которого будет удалена аннотация.

1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. Удалите аннотации. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfDeleteAnnotations.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Удалите аннотации из PDF-файла и сохраните в "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```