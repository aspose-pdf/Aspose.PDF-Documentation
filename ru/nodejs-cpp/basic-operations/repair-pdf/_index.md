---
title: Ремонт PDF в Node.js 
linktitle: Ремонт PDF
type: docs
weight: 10
url: ru/nodejs-cpp/repair-pdf/
description: Эта тема описывает, как ремонтировать PDF в среде Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF для Node.js позволяет выполнять высококачественный ремонт PDF. PDF файл может не открываться по любой причине, независимо от программы или браузера. В некоторых случаях документ может быть восстановлен, попробуйте следующий код и убедитесь сами.
Если вы хотите отремонтировать PDF документ, вы можете использовать функцию [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/). 
Пожалуйста, проверьте следующий фрагмент кода, чтобы отремонтировать PDF файл в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет отремонтирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по ремонту файла. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Восстановите PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfRepair.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Восстановить PDF файл и сохранить как "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет восстановлен.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Восстановите PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfRepair.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Восстановите PDF-файл и сохраните "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```