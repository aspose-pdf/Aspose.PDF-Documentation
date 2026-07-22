---
title: Конвертировать PDF в форматы PDF/A в Node.js
linktitle: Конвертировать PDF в форматы PDF/A
type: docs
weight: 100
url: /ru/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2026-07-18"
description: Эта тема показывает, как Aspose.PDF позволяет преобразовать файл PDF в PDF, соответствующий стандарту PDF/A, в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js** позволяет вам конвертировать PDF‑файл в <abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr> соответствующий требованиям PDF-файл. 

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PDF/A онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение [\u0022PDF в PDF/A-1A\u0022](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PDF/A с помощью бесплатного приложения](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## Конвертируйте PDF в формат PDF/A

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Восстановите PDF‑файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultConvertToPDFA.pdf". Во время процесса конвертации выполняется проверка, и результаты проверки сохраняются как "ResultConvertToPDFALog.xml". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
      /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Восстановите PDF‑файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultConvertToPDFA.pdf". Во время процесса конвертации выполняется проверка, и результаты проверки сохраняются как "ResultConvertToPDFALog.xml". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
  /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```





