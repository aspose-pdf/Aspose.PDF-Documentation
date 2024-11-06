---
title: Преобразование PDF в документы Word в Node.js
linktitle: Преобразование PDF в Word
type: docs
weight: 10
url: ru/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2023-11-16"
description: Узнайте, как преобразовать PDF в DOC(DOCX) в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Чтобы редактировать содержимое файла PDF в Microsoft Word или других текстовых процессорах, поддерживающих форматы DOC и DOCX. Файлы PDF редактируемы, но файлы DOC и DOCX более гибкие и настраиваемые.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в DOC онлайн**

Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете изучить функциональность и качество его работы.

[![Преобразовать PDF в DOC](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Преобразование PDF в DOC

Если вы хотите преобразовать PDF документ, вы можете использовать функцию [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
 
Пожалуйста, проверьте следующий фрагмент кода для выполнения в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет преобразован.
1. Вызовите `AsposePdf` как Promise и выполните операцию преобразования файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Преобразуйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoDoc.doc". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразование PDF файла в Doc и сохранение в "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет конвертироваться.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPDFtoDoc.doc". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Конвертируйте PDF-файл в Doc и сохраните как "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF для Node.js представляет вам бесплатное онлайн-приложение ["PDF в Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в Word Free App](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Конвертировать PDF в DOCX

Aspose.PDF для Node.js через C++ toolkit позволяет читать и конвертировать PDF документы в DOCX. DOCX — это известный формат для документов Microsoft Word, структура которого была изменена с простого бинарного на комбинацию XML и бинарных файлов. Файлы Docx могут быть открыты с помощью Word 2007 и более поздних версий, но не с более ранними версиями MS Word, которые поддерживают расширения файлов DOC.

Если вы хотите конвертировать PDF документ, вы можете использовать функцию [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/). Пожалуйста, ознакомьтесь со следующим фрагментом кода для конвертации в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет конвертирован.

1. Вызовите `AsposePdf` как Promise и выполните операцию по конвертации файла. Получите объект, если операция прошла успешно.
1. Вызовите функцию [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoDocX.docx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Преобразовать PDF-файл в DocX и сохранить как "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, который будет конвертирован.

1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. Конвертируйте PDF файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoDocX.docx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Конвертировать PDF-файл в DocX и сохранить в "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```