---
title:  Шифрование PDF в Node.js
linktitle: Шифрование файла PDF
type: docs
weight: 50
url: /nodejs-cpp/encrypt-pdf/
description: Шифрование файла PDF с использованием Aspose.PDF для Node.js через C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Шифрование файла PDF с использованием пароля пользователя или владельца

Если вы отправляете кому-то по электронной почте вложение PDF, которое содержит конфиденциальную информацию, вы можете сначала добавить некоторую защиту, чтобы оно не попало в неверные руки. Лучший способ ограничить несанкционированный доступ к PDF-документу - это защитить его паролем. Для простого и безопасного шифрования документов вы можете использовать Aspose.PDF для Node.js через C++.

>Пожалуйста, укажите разные пароли пользователя и владельца при шифровании PDF файла.

- **Пароль пользователя**, если установлен, необходимо указать для открытия PDF. Acrobat/Reader предложит пользователю ввести пароль пользователя. Если он неверный, документ не откроется.
- **Пароль владельца**, если установлен, контролирует разрешения, такие как печать, редактирование, извлечение, комментирование и т.д.
 Acrobat/Reader будет запрещать эти действия на основе настроек разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

Если вы хотите зашифровать PDF файл, вы можете использовать функцию [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/). 
Если вы хотите зашифровать PDF файл, попробуйте следующий фрагмент кода:

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
2. Укажите имя PDF файла, который будет зашифрован.
3. Вызовите `AsposePdf` как Promise и выполните операцию шифрования файла. Получите объект в случае успеха.
4. Вызовите функцию [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
5. Зашифруйте PDF файл с паролями "user" и "owner".
1. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultEncrypt.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Зашифруйте PDF-файл с паролями "user" и "owner" и сохраните в "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Существуют различные [права шифрования](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent

- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

Существуют различные [алгоритмы шифрования](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, для которого будет изменено шифрование.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успешного выполнения.
1. Вызовите функцию [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/).
1. Расшифруйте PDF файл с паролями "user" и "owner".

1. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultEncrypt.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Зашифровать PDF-файл с паролями "user" и "owner", и сохранить как "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```