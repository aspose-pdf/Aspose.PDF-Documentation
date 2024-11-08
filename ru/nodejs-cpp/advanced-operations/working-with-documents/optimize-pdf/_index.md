---
title: Оптимизация PDF с использованием Aspose.PDF для Node.js через C++
linktitle: Оптимизация PDF файла
type: docs
weight: 10
url: /ru/nodejs-cpp/optimize-pdf/
description: Оптимизация и сжатие PDF файлов для быстрого просмотра в вебе с использованием среды Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Оптимизация PDF документа

Инструментарий Aspose.PDF для Node.js через C++ позволяет оптимизировать содержимое PDF для среды Node.js.

Оптимизация, или линеаризация, относится к процессу подготовки PDF файла для онлайн просмотра с использованием веб-браузера.

Если вы хотите оптимизировать PDF, вы можете использовать функцию [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы оптимизировать PDF файлы в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
2. Укажите имя PDF файла, который будет оптимизирован.

1. Вызовите `AsposePdf` как Promise и выполните операцию по оптимизации файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Оптимизируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultOptimize.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Оптимизируйте PDF-файл и сохраните в "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет оптимизирован.

1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Оптимизируйте PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultOptimize.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Оптимизация PDF-файла и сохранение "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```