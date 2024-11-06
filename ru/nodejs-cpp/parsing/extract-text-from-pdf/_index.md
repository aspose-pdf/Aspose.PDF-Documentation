---
title: Извлечение текста из PDF в Node.js
linktitle: Извлечение текста из PDF
type: docs
weight: 30
url: ru/nodejs-cpp/extract-text-from-pdf/
description: В этой статье описываются различные способы извлечения текста из PDF-документов с использованием Aspose.PDF для Node.js через C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста из PDF-документа

Извлечение текста из PDF-документа — это очень распространенная и полезная задача. 
Извлечение текста из PDF служит множеству целей, от улучшения поиска и доступности до обеспечения анализа и автоматизации данных в различных областях, таких как бизнес, исследования и управление информацией.

Если вы хотите извлечь текст из PDF-документа, вы можете использовать функцию [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/). 
Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода, чтобы извлечь текст из PDF-файла с использованием Node.js через C++.

Проверьте фрагменты кода и следуйте шагам, чтобы извлечь текст из вашего PDF:


**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, из которого будет извлечен текст.
1. Вызовите `AsposePdf` как Promise и выполните операцию по извлечению текста. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Извлеченный текст сохраняется в JSON-объекте. Таким образом, если 'json.errorCode' равен 0, извлеченный текст отображается с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

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
1. Укажите имя PDF-файла, из которого будет извлечен текст.
1. Инициализируйте модуль AsposePdf. Получите объект, если инициализация прошла успешно.
1. Вызовите функцию [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Извлеченный текст сохраняется в объекте JSON. Таким образом, если 'json.errorCode' равен 0, извлеченный текст отображается с помощью console.log. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле возникает ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Извлечение текста из PDF-файла*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```