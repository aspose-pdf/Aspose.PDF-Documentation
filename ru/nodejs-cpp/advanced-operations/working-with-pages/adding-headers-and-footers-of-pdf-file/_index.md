---
title: Добавить верхний и нижний колонтитулы в PDF в Node.js
linktitle: Добавить верхний и нижний колонтитулы в PDF
type: docs
weight: 70
url: /ru/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Node.js via C++ позволяет добавлять заголовки и нижние колонтитулы в ваш PDF‑файл с помощью AsposePdfAddTextHeaderFooter.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js via C++** позволяет добавить заголовок и нижний колонтитул в ваш существующий PDF‑файл. 

Если вы хотите добавить заголовок и нижний колонтитул, вы можете использовать [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/) функция. 

Пожалуйста, проверьте следующий фрагмент кода, чтобы добавить заголовок и нижний колонтитул в PDF‑файл в среде Node.js.

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, в который будет добавлен заголовок и нижний колонтитул.
1. Вызов `AsposePdf` как Promise и выполнить операцию по добавлению заголовка и нижнего колонтитула. Получить объект при успешном выполнении.
1. Вызовите функцию [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Добавьте текст в заголовок и нижний колонтитул PDF‑файла. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в “ResultAddHeaderFooter.pdf”. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, в который будет добавлен заголовок и нижний колонтитул.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. Добавьте текст в заголовок и нижний колонтитул PDF‑файла. Таким образом, если ‘json.errorCode’ равно 0, результат операции сохраняется в “ResultAddHeaderFooter.pdf”. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```