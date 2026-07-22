---
title: Оптимизировать ресурсы PDF в Node.js
linktitle: Оптимизировать ресурсы PDF
type: docs
weight: 15
url: /ru/nodejs-cpp/optimize-pdf-resources/
description: Оптимизировать ресурсы PDF‑файлов для быстрого веб‑просмотра с помощью инструмента Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Оптимизировать ресурсы PDF

Оптимизировать ресурсы в документе:

1. Ресурсы, не используемые на страницах документа, удаляются
1. Эквивалентные ресурсы объединяются в один объект
1. Неиспользуемые объекты удаляются
 
Если вы хотите оптимизировать ресурсы PDF, вы можете использовать [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы оптимизировать ресурсы PDF в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, ресурсы которого будут оптимизированы.
1. Вызовите `AsposePdf` как Promise и выполните операцию по оптимизации файла. Получите объект при успехе.
1. Вызовите функцию [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Оптимизируйте ресурсы PDF. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfOptimizeResource.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, ресурсы которого будут оптимизированы.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Оптимизируйте ресурсы PDF. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfOptimizeResource.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```