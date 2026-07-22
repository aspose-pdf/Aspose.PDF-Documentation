---
title: Оптимизировать PDF с помощью Aspose.PDF for Node.js via C++
linktitle: Оптимизировать PDF файл
type: docs
weight: 10
url: /ru/nodejs-cpp/optimize-pdf/
description: Оптимизировать и сжать PDF файлы для быстрого веб‑просмотра с использованием среды Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Оптимизировать PDF Document

Набор средств Aspose.PDF for Node.js via C++ позволяет оптимизировать PDF‑контент для среды Node.js. 

Оптимизация, или линейризация, относится к процессу подготовки PDF‑файла к онлайн‑просмотру с использованием веб‑браузера.

Если вы хотите оптимизировать PDF, вы можете использовать [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) функция. 
Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы оптимизировать PDF-файлы в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, который будет оптимизирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по оптимизации файла. Получите объект при успехе.
1. Вызовите функцию [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Оптимизируйте PDF-файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultOptimize.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, который будет оптимизирован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Оптимизируйте PDF-файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultOptimize.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```