---
title: Извлечение текста из PDF в Node.js
linktitle: Извлечение текста из PDF
type: docs
weight: 10
url: ru/nodejs-cpp/extract-text/
description: Этот раздел описывает, как извлечь текст из PDF-документа с использованием Aspose.PDF для Node.js через C++ toolkit.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF-документа

Извлечение текста из PDF — задача не из легких. Лишь немногие PDF-читалки могут извлечь текст из изображений PDF или отсканированных PDF. Но инструмент **Aspose.PDF для Node.js через C++** позволяет с легкостью извлечь текст из всех файлов PDF в среде Node.js.

Этот код демонстрирует, как использовать модуль AsposePDFforNode.js для извлечения текста из указанного PDF-файла и записи либо извлеченного текста, либо возникших ошибок.

Изучите фрагменты кода и следуйте шагам для извлечения текста из вашего PDF:

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.

1. Укажите имя PDF-файла, из которого будет извлечен текст.
1. Вызовите `AsposePdf` как Promise и выполните операцию извлечения текста. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Извлеченный текст сохраняется в объекте JSON. Таким образом, если 'json.errorCode' равно 0, извлеченный текст отображается с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Извлечение текста из PDF-файла*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.

1. Укажите имя PDF-файла, из которого будет извлекаться текст.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Извлеченный текст хранится в объекте JSON. Таким образом, если 'json.errorCode' равен 0, извлеченный текст отображается с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Извлечение текста из PDF-файла*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```