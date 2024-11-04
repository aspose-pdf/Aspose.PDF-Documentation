---
title: Преобразование PDF в PPTX в Node.js
linktitle: Преобразование PDF в PowerPoint
type: docs
weight: 30
url: /nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-16"
description: Aspose.PDF позволяет конвертировать PDF в формат PPTX, используя Node.js непосредственно в среде Node.js.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в PowerPoint онлайн**

Aspose.PDF для Node.js предлагает вам бесплатное онлайн-приложение ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в PPTX с бесплатным приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Преобразование PDF в PPTX

Если вы хотите преобразовать PDF-документ, вы можете использовать функцию [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).

Пожалуйста, ознакомьтесь со следующим фрагментом кода для преобразования в среде Node.js.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла, который будет конвертирован.
1. Вызовите `AsposePdf` как Promise и выполните операцию по конвертации файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Конвертируйте PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoPptX.pptx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Конвертировать PDF-файл в PptX и сохранить как "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF-файла, который будет преобразован.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Преобразуйте PDF-файл. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPDFtoPptX.pptx". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Преобразуйте PDF-файл в PptX и сохраните "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```