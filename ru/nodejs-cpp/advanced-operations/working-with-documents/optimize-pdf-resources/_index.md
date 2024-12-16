---
title: Оптимизация ресурсов PDF в Node.js
linktitle: Оптимизация ресурсов PDF
type: docs
weight: 15
url: /ru/nodejs-cpp/optimize-pdf-resources/
description: Оптимизация ресурсов PDF файлов для быстрого веб-просмотра с использованием инструмента Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Оптимизация ресурсов PDF

Оптимизируйте ресурсы в документе:

1. Ресурсы, которые не используются на страницах документа, удаляются
1. Одинаковые ресурсы объединяются в единый объект
1. Неиспользуемые объекты удаляются

Если вы хотите оптимизировать ресурсы PDF, вы можете использовать функцию [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/). Пожалуйста, ознакомьтесь со следующим фрагментом кода для оптимизации ресурсов PDF в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, для которого будут оптимизированы ресурсы.

1. Вызовите `AsposePdf` как Promise и выполните операцию по оптимизации файла. Получите объект, если операция успешна.
1. Вызовите функцию [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Оптимизируйте ресурсы PDF. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfOptimizeResource.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Оптимизировать ресурсы PDF-файла и сохранить как "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, для которого будут оптимизированы ресурсы.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Оптимизируйте ресурсы PDF. Таким образом, если 'json.errorCode' равно 0, результат операции будет сохранен в "ResultPdfOptimizeResource.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Оптимизируйте ресурсы PDF-файла и сохраните в "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```