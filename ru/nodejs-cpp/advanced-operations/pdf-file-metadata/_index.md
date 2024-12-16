---
title: Работа с метаданными PDF-файлов в Node.js 
linktitle: Метаданные PDF-файлов
type: docs
weight: 130
url: /ru/nodejs-cpp/pdf-file-metadata/
description: Этот раздел объясняет, как получать информацию о PDF-файле, как получать метаданные из PDF-файла, задавать информацию о PDF-файле в Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение информации о PDF-файле

Если вы хотите получить информацию о PDF-файле, вы можете использовать функцию [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/). Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы получить информацию о PDF-файле в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
2. Укажите имя PDF-файла, из которого будет извлечена информация.
3. Вызовите `AsposePdf` как Promise и выполните операцию для извлечения информации. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Извлеченные метаданные хранятся в объекте JSON. Таким образом, если 'json.errorCode' равен 0, извлеченные метаданные отображаются с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле возникает ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Получить информацию (метаданные) из PDF-файла*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Название          : json.title
        Создатель         : json.creator
        Автор             : json.author
        Тема              : json.subject
        Ключевые слова    : json.keywords
        Дата создания     : json.creation
        Дата изменения    : json.mod
        Формат PDF        : json.format
        Версия PDF        : json.version
        PDF является PDF/A: json.ispdfa
        PDF является PDF/UA: json.ispdfua
        PDF линеаризован  : json.islinearized
        PDF зашифрован    : json.isencrypted
        Разрешение PDF    : json.permission
        Размер страницы PDF: json.size
        Количество страниц: json.pagecount
        Количество аннотаций: json.annotationcount
        Количество закладок: json.bookmarkcount
        Количество вложений: json.attachmentcount
        Количество метаданных: json.metadatacount
        Количество JavaScript: json.javascriptcount
        Количество изображений: json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Название: ' + json.title : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, из которого будет извлечена информация.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. Извлеченные метаданные сохраняются в объекте JSON. Таким образом, если 'json.errorCode' равен 0, извлеченные метаданные отображаются с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Получить информацию (метаданные) из PDF-файла*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Заголовок         : json.title
      Создатель         : json.creator
      Автор             : json.author
      Тема              : json.subject
      Ключевые слова    : json.keywords
      Дата создания     : json.creation
      Дата изменения    : json.mod
      Формат PDF        : json.format
      Версия PDF        : json.version
      PDF является PDF/A: json.ispdfa
      PDF является PDF/UA: json.ispdfua
      PDF линеаризован  : json.islinearized
      PDF зашифрован    : json.isencrypted
      Разрешения PDF    : json.permission
      Размер страницы PDF: json.size
      Количество страниц: json.pagecount
      Количество аннотаций: json.annotationcount
      Количество закладок: json.bookmarkcount
      Количество вложений: json.attachmentcount
      Количество метаданных: json.metadatacount
      Количество JavaScript: json.javascriptcount
      Количество изображений: json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Заголовок: ' + json.title : json.errorText);
```


## Получить Все Шрифты

Получение шрифтов из PDF-файла может быть полезным способом повторного использования шрифтов в других документах или приложениях.

Если вы хотите получить шрифты из PDF-файла, вы можете использовать функцию [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/). 
Пожалуйста, ознакомьтесь с следующим фрагментом кода, чтобы получить шрифты из PDF-файла в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, из которого будут извлечены шрифты.
1. Вызовите `AsposePdf` как Promise и выполните операцию по извлечению шрифтов. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).

1. Извлеченные шрифты хранятся в объекте JSON. Таким образом, если 'json.errorCode' равен 0, отображается массив данных о шрифтах, включая название шрифта, его встроенность и статус доступности, используя console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Получить список шрифтов из PDF-файла*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - массив шрифтов: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => шрифты: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите название PDF-файла, из которого будут извлекаться шрифты.

1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. Извлеченные шрифты сохраняются в объекте JSON. Таким образом, если 'json.errorCode' равно 0, он отображает массив данных о шрифтах, включая имя шрифта, встроен ли он и его статус доступности, используя console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Получить список шрифтов из PDF-файла*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - массив шрифтов: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => шрифты: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Установить информацию о PDF-файле


Aspose.PDF для Node.js через C++ позволяет устанавливать специфичную для файла информацию для PDF, такую как автор, дата создания, тема и заголовок. Чтобы установить эту информацию:

Если вы хотите установить специфичную для файла информацию, вы можете использовать функцию [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/). Пожалуйста, ознакомьтесь со следующим фрагментом кода для установки информации о файле в среде Node.js.

Возможно установить:
- заголовок
- создатель
- автор
- тема
- список ключевых слов
- дата создания
- дата изменения
- имя файла результата

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, в котором будет установлена информация.
1. Вызовите `AsposePdf` как Promise и выполните операцию. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).

1. Задать информацию о PDF-файле. Информация, такая как заголовок, создатель, автор, тема, ключевые слова, дата создания и дата изменения, предоставляется в качестве параметров. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultSetInfo.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Задать информацию о PDF: заголовок, создатель, автор, тема, ключевые слова, дата создания, дата изменения*/
      /*Если значение не нужно задавать, используйте undefined или "" (пустую строку)*/
      /*Установите информацию (метаданные) в PDF-файл и сохраните как "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, в котором будет установлена информация.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. Установите информацию PDF файла. Информация, такая как заголовок, создатель, автор, тема, ключевые слова, дата создания и дата изменения, передается в качестве параметров. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultSetInfo.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* Установить информацию PDF: заголовок, создатель, автор, тема, ключевые слова, создание (дата), изменение (дата модификации) */
  /* Если значение не требуется, используйте undefined или "" (пустая строка) */
  /* Установите информацию (метаданные) в PDF-файл и сохраните как "ResultSetInfo.pdf" */
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Установка информации о PDF документе", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


## Удаление информации из PDF файла

Aspose.PDF для Node.js через C++ позволяет вам удалять метаданные из PDF файла:

В случае, если вы хотите удалить метаданные из PDF, вы можете использовать функцию [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/). 
Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода для удаления метаданных из PDF в среде Node.js.

**CommonJS:**

1. Подключите модуль AsposePDFforNode.js.
1. Укажите имя PDF файла, из которого будет удалена информация.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Удалите информацию из PDF файла. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfRemoveMetadata.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Удалить метаданные из PDF файла и сохранить как "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, из которого будет удалена информация.
1. Инициализируйте модуль AsposePdf. Получите объект при успешном выполнении.
1. Вызовите функцию [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. Удалите информацию из PDF-файла. Таким образом, если 'json.errorCode' равен 0, результат операции будет сохранен в "ResultPdfRemoveMetadata.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Удалите метаданные из PDF-файла и сохраните "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```