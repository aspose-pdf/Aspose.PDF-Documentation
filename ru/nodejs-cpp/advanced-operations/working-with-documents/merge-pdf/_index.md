---
title: Как объединить PDF в Node.js
linktitle: Объединить PDF файлы
type: docs
weight: 20
url: /ru/nodejs-cpp/merge-pdf/
description: На этой странице объясняется, как объединить PDF‑документы в один PDF‑файл с помощью Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Объединить или соединить два PDF в один PDF в Node.js

Объединение и склейка файлов — очень популярная задача при работе с большим количеством документов. Иногда, при работе с документами и изображениями, когда они сканируются, обрабатываются и упорядочиваются, создаётся несколько файлов.
А что, если вам нужно хранить всё в одном файле? Или вы не хотите печатать несколько документов? Объедините два PDF‑файла с помощью Aspose.PDF for Node.js via C++.

Если вы хотите объединить два PDF, вы можете использовать [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы объединить два PDF‑файла в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файлов, которые будут объединены.
1. Вызов `AsposePdf` как Promise и выполнить операцию объединения. Получить объект, если успешно.
1. Вызовите функцию [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Объедините два PDF‑файла. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultMerge.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файлов, которые будут объединены.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Объедините два PDF‑файла. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultMerge.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```