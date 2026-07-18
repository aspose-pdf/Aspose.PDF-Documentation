---
title: Извлечение текста из PDF в Node.js
linktitle: Извлечение текста из PDF
type: docs
weight: 10
url: /ru/nodejs-cpp/extract-text/
description: В этом разделе описывается, как извлечь текст из PDF‑документа с помощью инструментария Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF‑документа

Извлечение текста из PDF — не простая задача. Только несколько PDF‑читалок могут извлекать текст из PDF‑изображений или сканированных PDF. Но инструмент **Aspose.PDF for Node.js via C++** позволяет легко извлекать текст из всех PDF‑файлов в среде Node.js. 

Этот код демонстрирует, как использовать модуль AsposePDFforNode.js для извлечения текста из указанного PDF‑файла и записи либо извлечённого текста, либо возникших ошибок.

Проверьте фрагменты кода и выполните шаги, чтобы извлечь текст из вашего PDF:

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, из которого будет извлечён текст.
1. Вызов `AsposePdf` как Promise и выполнить операцию по извлечению текста. Получить объект в случае успеха.
1. Вызовите функцию [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Извлечённый текст сохраняется в JSON‑объекте. Таким образом, если 'json.errorCode' равен 0, извлечённый текст выводится с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, из которого будет извлечён текст.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Извлечённый текст сохраняется в JSON‑объекте. Таким образом, если 'json.errorCode' равен 0, извлечённый текст выводится с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
