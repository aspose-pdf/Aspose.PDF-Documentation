---
title: Преобразование PDF в форматы PDF/A в Node.js
linktitle: Преобразование PDF в форматы PDF/A
type: docs
weight: 100
url: /nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-16"
description: Эта тема показывает, как Aspose.PDF позволяет преобразовать файл PDF в файл PDF, соответствующий PDF/A, в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF для Node.js** позволяет преобразовать файл PDF в файл PDF, соответствующий <abbr title="Формат портативных документов для архивирования электронных документов">PDF/A</abbr>. 

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в PDF/A онлайн**

Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF в PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в PDF/A с бесплатным приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Преобразование PDF в формат PDF/A

Если вы хотите преобразовать документ PDF, вы можете использовать функцию [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
 
Пожалуйста, проверьте следующий фрагмент кода для конвертации в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, который будет преобразован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по конвертации файла. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Исправьте PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultConvertToPDFA.pdf". В процессе конвертации выполняется проверка, и результаты проверки сохраняются как "ResultConvertToPDFALog.xml". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразование PDF-файла в PDF/A(1A) и сохранение в "ResultConvertToPDFA.pdf"*/
      /*В процессе конвертации также выполняется проверка, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет преобразован.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. Исправьте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultConvertToPDFA.pdf". В процессе конверсии выполняется валидация, и результаты валидации сохраняются как "ResultConvertToPDFALog.xml." Если параметр json.errorCode не равен 0 и, соответственно, появляется ошибка в вашем файле, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразуйте PDF файл в PDF/A(1A) и сохраните в "ResultConvertToPDFA.pdf"*/
  /*Во время процесса конверсии также выполняется валидация, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```