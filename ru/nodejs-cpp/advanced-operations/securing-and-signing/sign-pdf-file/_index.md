---
title: Добавить цифровую подпись в PDF в Node.js
linktitle: Цифровая подпись PDF
type: docs
weight: 70
url: ru/nodejs-cpp/sign-pdf/
description: Подпись PDF документов в среде Node.js.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Цифровая подпись в PDF документе — это способ проверки подлинности и целостности документа. Это процесс электронной подписи PDF документа с использованием закрытого ключа и цифрового сертификата. Эта подпись гарантирует держателю, что документ не был изменен или искажен с момента подписания и что подписавший является тем, кем он себя утверждает. Чтобы подписать PDF с помощью Node.js, используйте инструмент Aspose.PDF.

Если вы хотите подписать PDF файл, вы можете использовать функцию [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).

Возможно использование **параметров**, связанных с подписью:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- reason

- contact
- location
- isVisible
- signatureAppearance
- fileNameResult

Этот фрагмент кода использует модуль AsposePDFforNode.js в среде Node.js для цифровой подписи PDF-файла с использованием подписи PKCS7.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF-файла для подписи, файл ключа PKCS7 и файл изображения подписи. Сертификат и изображение могут быть размещены в любом месте вашей файловой системы, откуда вы их загружаете для подписания PDF.
1. Вызовите `AsposePdf` как Promise и выполните операцию для подписания файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Подпишите PDF-файл с помощью цифровых подписей. Параметры, связанные с подписью (такие как файл ключа, пароль, координаты, причина, контакт, местоположение и т. д.).

1. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultSignPKCS7.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Ключ PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Внешний вид подписи*/
      const sign_img_file = 'Aspose.jpg';
      /*Подпишите PDF-файл цифровыми подписями и сохраните "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.

1. Укажите имя PDF-файла, который нужно подписать, файл ключа PKCS7 и файл изображения подписи.
1. Инициализируйте модуль AsposePdf. Получите объект при успешной инициализации.
1. Вызовите функцию [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Подпишите PDF-файл с помощью цифровых подписей. Параметры, связанные с подписью (например, файл ключа, пароль, координаты, причина, контакт, местоположение и т. д.).
1. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultSignPKCS7.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Ключ PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Внешний вид подписи*/
  const sign_img_file = 'Aspose.jpg';
  /*Подписать PDF-файл с помощью цифровых подписей и сохранить в "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```