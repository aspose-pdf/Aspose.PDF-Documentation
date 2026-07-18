---
title: Установите цвет фона для PDF в Node.js
linktitle: Установить цвет фона
type: docs
weight: 80
url: /ru/nodejs-cpp/set-background-color/
description: Установите цвет фона для вашего PDF‑файла с помощью Node.js через C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Если вы хотите установить цвет фона PDF, вы можете использовать [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) функция. 

Пожалуйста, посмотрите следующий фрагмент кода, чтобы установить цвет фона PDF в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF-файла, цвет фона которого вы хотите задать.
1. Вызов `AsposePdf` как Promise и выполнить операцию установки цвета фона. Получить объект в случае успеха.
1. Вызовите функцию [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Установите цвет фона для PDF-файла. Вам необходимо передать 3 аргумента в эту функцию: имя входного файла, желаемый цвет в шестнадцатеричном виде и имя выходного файла. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultRotation.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF-файла, цвет фона которого вы хотите задать.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Установите цвет фона для PDF‑файла. Цвет фона установлен в "#426bf4," что является шестнадцатеричным кодом цвета, представляющим оттенок синего. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultRotation.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```