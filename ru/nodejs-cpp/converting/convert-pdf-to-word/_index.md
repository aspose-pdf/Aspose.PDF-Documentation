---
title: Конвертировать PDF в документы Word в Node.js
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: /ru/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2026-07-18"
description: Узнайте, как конвертировать PDF в DOC(DOCX) в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Чтобы редактировать содержимое PDF‑файла в Microsoft Word или других текстовых процессорах, поддерживающих форматы DOC и DOCX. PDF‑файлы редактируемы, но файлы DOC и DOCX более гибкие и настраиваемые.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение ["PDF в DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попробовать исследовать функциональность и качество его работы.

[![Конвертировать PDF в DOC](/pdf/ru/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Конвертируйте PDF в DOC

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoDoc.doc". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoDoc.doc". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF for Node.js представляет вам онлайн бесплатное приложение [\"PDF в Word\"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF конвертация PDF в Word бесплатное приложение](/pdf/ru/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Конвертируйте PDF в DOCX

Aspose.PDF for Node.js via C++ toolkit позволяет читать и конвертировать PDF‑документы в DOCX. DOCX — известный формат документов Microsoft Word, структура которых была изменена от простого бинарного формата к комбинации XML‑ и бинарных файлов. Файлы DOCX можно открыть в Word 2007 и более поздних версиях, но не в более ранних версиях MS Word, которые поддерживают расширения файлов DOC.

Если вы хотите конвертировать PDF-документ, вы можете использовать [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы выполнить конвертацию в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию конвертации файла. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPDFtoDocX.docx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, который будет преобразован
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Конвертируйте PDF‑файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPDFtoDocX.docx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


