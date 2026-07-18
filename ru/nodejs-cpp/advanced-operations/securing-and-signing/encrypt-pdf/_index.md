---
title:  Зашифровать PDF в Node.js
linktitle: Зашифровать PDF-файл
type: docs
weight: 50
url: /ru/nodejs-cpp/encrypt-pdf/
description: Зашифровать PDF-файл с помощью Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Зашифровать PDF-файл, используя пользовательский или владельческий пароль

Если вы отправляете по электронной почте кому‑то PDF‑вложение, содержащее конфиденциальную информацию, вы можете захотеть сначала добавить к нему защиту, чтобы не допустить попадания в неправильные руки. Лучший способ ограничить неавторизованный доступ к PDF‑документу — защитить его паролем. Чтобы легко и безопасно шифровать документы, вы можете использовать Aspose.PDF for Node.js via C++.

>Пожалуйста, укажите разные пользовательский и владельческий пароли при шифровании PDF‑файла.

- Пароль **User password**, если установлен, — это то, что необходимо предоставить для открытия PDF. Acrobat/Reader запросит у пользователя ввод пароля пользователя. Если он неверен, документ не откроется.
- Пароль **Owner password**, если установлен, управляет разрешениями, такими как печать, редактирование, извлечение, комментирование и т.д. Acrobat/Reader запретит эти действия в соответствии с настройками разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

Если вы хотите зашифровать PDF‑файл, вы можете использовать [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) функция. 
Если вы хотите зашифровать PDF‑файл, попробуйте следующий фрагмент кода:

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, который будет зашифрован.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию шифрования файла. Получить объект, если успешно.
1. Вызовите the [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) функция. 
1. Зашифруйте PDF‑файл с паролями "user" и "owner".
1. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultEncrypt.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Есть разные [разрешения шифрования](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent
- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

Есть различные [алгоритмы шифрования](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, который будет изменять зашифрованный.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите the [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) функция. 
1. Расшифровать PDF‑файл с паролями "user" и "owner".
1. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultEncrypt.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```