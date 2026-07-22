---
title: Работа с метаданными PDF‑файла в Node.js
linktitle: Метаданные PDF‑файла
type: docs
weight: 130
url: /ru/nodejs-cpp/pdf-file-metadata/
description: В этом разделе объясняется, как получить информацию о PDF‑файле, как получить метаданные из PDF‑файла, установить информацию о PDF‑файле в Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получить информацию о PDF‑файле

Если вы хотите получить информацию о PDF‑файле, вы можете использовать [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы получить информацию о файле PDF в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, из которого будет извлекаться информация.
1. Вызовите `AsposePdf` как Promise и выполните операцию по извлечению информации. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Извлечённые метаданные сохраняются в объекте JSON. Таким образом, если 'json.errorCode' равно 0, извлечённые метаданные выводятся с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get info (metadata) from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Title             : json.title
        Creator           : json.creator
        Author            : json.author
        Subject           : json.subject
        Keywords          : json.keywords
        Creation Date     : json.creation
        Modify Date       : json.mod
        PDF format        : json.format
        PDF version       : json.version
        PDF is PDF/A      : json.ispdfa
        PDF is PDF/UA     : json.ispdfua
        PDF is linearized : json.islinearized
        PDF is encrypted  : json.isencrypted
        PDF permission    : json.permission
        PDF page size     : json.size
        Page count        : json.pagecount
        Annotation count  : json.annotationcount
        Bookmark count    : json.bookmarkcount
        Attachment count  : json.attachmentcount
        Metadata count    : json.metadatacount
        JavaScript count  : json.javascriptcount
        Image count       : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, из которого будет извлекаться информация.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Извлечённые метаданные сохраняются в объекте JSON. Таким образом, если 'json.errorCode' равно 0, извлечённые метаданные выводятся с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Get info (metadata) from a PDF-file*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Title             : json.title
      Creator           : json.creator
      Author            : json.author
      Subject           : json.subject
      Keywords          : json.keywords
      Creation Date     : json.creation
      Modify Date       : json.mod
      PDF format        : json.format
      PDF version       : json.version
      PDF is PDF/A      : json.ispdfa
      PDF is PDF/UA     : json.ispdfua
      PDF is linearized : json.islinearized
      PDF is encrypted  : json.isencrypted
      PDF permission    : json.permission
      PDF page size     : json.size
      Page count        : json.pagecount
      Annotation count  : json.annotationcount
      Bookmark count    : json.bookmarkcount
      Attachment count  : json.attachmentcount
      Metadata count    : json.metadatacount
      JavaScript count  : json.javascriptcount
      Image count       : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```

## Получить все шрифты

Получение шрифтов из PDF‑файла может быть полезным способом повторного использования шрифтов в других документах или приложениях. 

Если вы хотите получить шрифты из PDF‑файла, вы можете использовать [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы получить шрифты из PDF‑файла в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, из которого будут извлечены шрифты.
1. Вызовите `AsposePdf` как Promise и выполните операцию по извлечению шрифтов. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Извлечённые шрифты хранятся в объекте JSON. Таким образом, если 'json.errorCode' равен 0, выводится массив деталей шрифтов, включая имя шрифта, его встраивание и статус доступности, используя console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get list fonts from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, из которого будут извлечены шрифты.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Извлечённые шрифты хранятся в объекте JSON. Таким образом, если 'json.errorCode' равен 0, выводится массив деталей шрифтов, включая имя шрифта, его встраивание и статус доступности, используя console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Get list fonts from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Установите информацию о PDF-файле

Aspose.PDF for Node.js via C++ позволяет задавать специфичную для файла информацию в PDF, такую как автор, дата создания, тема и заголовок. Чтобы задать эту информацию:

Если вы хотите задать информацию, специфичную для файла, вы можете использовать [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы установить информацию о файле в среде Node.js.

Возможно установить: 
- заголовок
- создатель
- автор
- тема
- список ключевых слов
- дата создания
- изменить дату
- имя результирующего файла

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, в котором будет установлена информация.
1. Вызовите `AsposePdf` как Promise и выполните операцию. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Установите информацию о PDF‑файле. Информация, такая как название, создатель, автор, тема, ключевые слова, дата создания и дата изменения, передается в виде параметров. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultSetInfo.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*If not need to set value, use undefined or "" (empty string)*/
      /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, в котором будет установлена информация.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Установите информацию о PDF‑файле. Информация, такая как название, создатель, автор, тема, ключевые слова, дата создания и дата изменения, передается в виде параметров. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultSetInfo.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*If not need to set value, use undefined or "" (empty string)*/
  /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Удалите информацию о PDF-файле

Aspose.PDF for Node.js via C++ позволяет удалять метаданные PDF‑файла:

Если вы хотите удалить метаданные из PDF, вы можете использовать [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы удалить метаданные из PDF в среде Node.js.

**CommonJS:**

1. Требуйте модуль AsposePDFforNode.js.
1. Укажите имя PDF‑файла, из которого будет удалена информация.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Удалите информацию о PDF-файле. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfRemoveMetadata.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, из которого будет удалена информация.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Удалите информацию о PDF-файле. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultPdfRemoveMetadata.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```