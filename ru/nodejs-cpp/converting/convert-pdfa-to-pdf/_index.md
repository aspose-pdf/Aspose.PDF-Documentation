---
title: Конвертировать PDF/A в формат PDF в Node.js
linktitle: Конвертировать PDF/A в формат PDF
type: docs
weight: 110
url: /ru/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2026-07-18"
description: В этом разделе показано, как Aspose.PDF позволяет конвертировать файл PDF/A в документ PDF в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Конвертируйте PDF/A в формат PDF

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultConvertToPDF.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя файла PDF/A, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultConvertToPDF.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```
