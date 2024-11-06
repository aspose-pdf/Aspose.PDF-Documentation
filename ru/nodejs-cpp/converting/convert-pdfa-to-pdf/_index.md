---
title: Преобразование PDF/A в формат PDF на Node.js
linktitle: Преобразование PDF/A в формат PDF
type: docs
weight: 110
url: ru/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-16"
description: Эта тема показывает, как Aspose.PDF позволяет преобразовать файл PDF/A в PDF документ в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Преобразование PDF/A в формат PDF

Если вы хотите преобразовать PDF документ, вы можете использовать функцию [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/). 
Пожалуйста, ознакомьтесь со следующим фрагментом кода для преобразования в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет преобразован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по преобразованию файла. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Конвертируйте файл PDF. Таким образом, если 'json.errorCode' равен 0, результат операции будет сохранен в "ResultConvertToPDF.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Конвертируйте PDF/A-файл в PDF и сохраните как "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя файла PDF/A, который будет конвертирован.

1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Преобразуйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultConvertToPDF.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Преобразование файла PDF/A в PDF и сохранение в "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```