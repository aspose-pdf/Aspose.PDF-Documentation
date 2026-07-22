---
title: Восстановить PDF в Node.js
linktitle: Восстановить PDF
type: docs
weight: 10
url: /ru/nodejs-cpp/repair-pdf/
description: Эта статья описывает, как восстановить PDF в среде Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js позволяет выполнять высококачественное восстановление PDF. PDF‑файл может не открываться по любой причине, независимо от программы или браузера. В некоторых случаях документ можно восстановить, попробуйте следующий код и убедитесь сами.
Если вы хотите восстановить PDF‑документ, вы можете использовать [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы восстановить PDF‑файл в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет восстановлен.
1. Вызовите `AsposePdf` как Promise и выполните операцию по восстановлению файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Восстановите PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfRepair.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет восстановлен.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Восстановите PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfRepair.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```