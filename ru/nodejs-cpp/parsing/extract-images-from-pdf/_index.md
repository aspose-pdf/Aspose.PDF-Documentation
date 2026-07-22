---
title: Извлечь изображения из PDF в Node.js
linktitle: Извлечь изображения из PDF
type: docs
weight: 20
url: /ru/nodejs-cpp/extract-images-from-the-pdf-file/
description: Как извлечь часть изображения из PDF с помощью Aspose.PDF for Node.js via C++ toolkit.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлекать изображения из PDF-файлов в среде Node.js

Если вам нужно извлечь изображения из PDF-документа, вы можете использовать [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) функция. 
Мы должны передать три аргумента этой функции: имя входного и выходного файла и разрешение.
Пожалуйста, проверьте следующий фрагмент кода для извлечения изображений из PDF-файла с использованием Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, из которого будет извлечено изображение.
1. Вызовите `AsposePdf` как Promise и выполните операцию по извлечению изображения. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Извлеките изображения из PDF-файла. Таким образом, если ‘json.errorCode’ равен 0, результат операции сохраняется в “ResultPdfExtractImage{0:D2}.jpg”. Где {0:D2} представляет номер страницы в двухциферном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, из которого будет извлечено изображение.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. Извлеките изображения из PDF-файла. Таким образом, если ‘json.errorCode’ равен 0, результат операции сохраняется в “ResultPdfExtractImage{0:D2}.jpg”. Где {0:D2} представляет номер страницы в двухциферном формате. Изображения сохраняются с разрешением 150 DPI. Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
