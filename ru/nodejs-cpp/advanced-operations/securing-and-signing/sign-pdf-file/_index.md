---
title: Добавить цифровую подпись в PDF в Node.js
linktitle: Подписать PDF цифровой подписью
type: docs
weight: 70
url: /ru/nodejs-cpp/sign-pdf/
description: Подписать PDF-документы цифровой подписью в среде Node.js.
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


Цифровая подпись в PDF‑документе — это способ проверки подлинности и целостности документа. Это процесс электронной подписи PDF‑документа с использованием закрытого ключа и цифрового сертификата. Эта подпись гарантирует владельцу, что документ не был изменён после подписания и что подписант действительно тот, кто его утвердил. Для подписи PDF с помощью Node.js используйте инструмент Aspose.PDF.

Если вы хотите подписать PDF‑файл, вы можете использовать функцию [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).

Можно использовать **параметры**, связанные с подписью:

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

Этот фрагмент кода использует модуль AsposePDFforNode.js в среде Node.js для цифровой подписи PDF‑файла с использованием подписи PKCS7.

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, который нужно подписать, файл ключа PKCS7 и файл изображения внешнего вида подписи. Сертификат и изображение могут находиться в любом месте файловой системы, откуда вы их загружаете для подписания PDF.
1. Вызовите `AsposePdf` как Promise и выполните операцию подписи файла. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfSignPKS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/). 
1. Подпишите PDF‑файл цифровыми подписями. Параметры, связанные с подписью (например, файл ключа, пароль, координаты, причина, контакт, местоположение и т.д.). 
1. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultSignPKCS7.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Key PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Signature appearance*/
      const sign_img_file = 'Aspose.jpg';
      /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла для подписи, файл ключа PKCS7 и файл изображения внешнего вида подписи.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/).
1. Подпишите PDF‑файл цифровыми подписями. Параметры, связанные с подписью (например, файл ключа, пароль, координаты, причина, контакт, местоположение и т.д.). 
1. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultSignPKCS7.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Key PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Signature appearance*/
  const sign_img_file = 'Aspose.jpg';
  /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```