---
title: Извлечь текст из PDF в Node.js
linktitle: Извлечь текст из PDF
type: docs
weight: 30
url: /ru/nodejs-cpp/extract-text-from-pdf/
description: В этой статье описываются различные способы извлечения текста из PDF‑документов с использованием Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечь текст из PDF‑документа

Извлечение текста из PDF‑документа — очень распространённая и полезная задача. 
Извлечение текста из PDF служит множеству целей, от улучшения поиска и доступности до обеспечения анализа и автоматизации данных в разных областях, таких как бизнес, исследования и управление информацией.

Если вы хотите извлечь текст из PDF‑документа, вы можете использовать [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) функция. 
Пожалуйста, проверьте следующий фрагмент кода, чтобы извлечь текст из PDF‑файла, используя Node.js via C++.

Проверьте фрагменты кода и выполните шаги, чтобы извлечь текст из вашего PDF:

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, из которого будет извлечён текст.
1. Вызовите `AsposePdf` как Promise и выполните операцию по извлечению текста. Получите объект в случае успеха.
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

1. Импортируйте модуль `asposepdfnodejs`.
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