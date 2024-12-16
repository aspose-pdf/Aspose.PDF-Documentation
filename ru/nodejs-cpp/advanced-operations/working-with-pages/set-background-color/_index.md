---
title: Установить цвет фона для PDF в Node.js
linktitle: Установить цвет фона
type: docs
weight: 80
url: /ru/nodejs-cpp/set-background-color/
description: Установите цвет фона для вашего PDF файла с помощью Node.js через C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Если вы хотите установить цвет фона для PDF, вы можете использовать функцию [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).

Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы установить цвет фона PDF в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, для которого вы хотите установить цвет фона.
1. Вызовите `AsposePdf` как Promise и выполните операцию по установке цвета фона. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
1. Установите цвет фона для PDF-файла. Вам нужно передать 3 аргумента этой функции: имя входного файла, желаемый цвет в шестнадцатеричном формате и имя выходного файла. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultRotation.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Установите цвет фона для PDF-файла и сохраните "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, для которого вы хотите установить цвет фона.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/).
1. Установите цвет фона для PDF-файла. Цвет фона устанавливается на "#426bf4", что является шестнадцатеричным кодом цвета, представляющим оттенок синего. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultRotation.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Установите цвет фона для PDF-файла и сохраните "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```