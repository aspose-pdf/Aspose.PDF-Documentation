---
title: Как объединить PDF в Node.js
linktitle: Объединение PDF файлов
type: docs
weight: 20
url: ru/nodejs-cpp/merge-pdf/
description: Эта страница объясняет, как объединить PDF документы в один PDF файл с помощью Aspose.PDF для Node.js через C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Объединение или комбинирование двух PDF в один PDF в Node.js

Комбинирование и объединение файлов - это очень популярная задача при работе с большим количеством документов. Иногда, при работе с документами и изображениями, когда они сканируются, обрабатываются и организуются, создается несколько файлов.
Но что если вам нужно хранить все в одном файле? Или вы не хотите печатать несколько документов? Объедините два PDF файла с помощью Aspose.PDF для Node.js через C++.

Если вы хотите объединить два PDF, вы можете использовать функцию [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/). 
Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы объединить два PDF файла в среде Node.js.


**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файлов, которые будут объединены.
1. Вызовите `AsposePdf` как Promise и выполните операцию по объединению. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Объедините два PDF-файла. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultMerge.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Объедините два PDF-файла и сохраните "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите названия PDF-файлов, которые будут объединены.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Объедините два PDF-файла. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultMerge.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Объедините два PDF-файла и сохраните "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```