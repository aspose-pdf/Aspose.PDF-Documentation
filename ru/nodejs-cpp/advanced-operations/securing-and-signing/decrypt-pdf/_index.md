---
title: Расшифровать PDF в Node.js
linktitle: Расшифровать PDF-файл
type: docs
weight: 40
url: /ru/nodejs-cpp/decrypt-pdf/
description: Расшифровать PDF-файл с помощью Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Расшифровать PDF-файл, используя пароль владельца

В последнее время всё больше пользователей обмениваются зашифрованными документами, чтобы не стать жертвами интернет-мошенничества и защитить свои документы.
В связи с этим возникает необходимость доступа к зашифрованному PDF-файлу, поскольку такой доступ может получить только уполномоченный пользователь. Также люди ищут различные решения для расшифровки PDF-файлов. 

Если вы хотите расшифровать PDF‑файл, вы можете использовать [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) функция. 
Если вы хотите расшифровать PDF‑файл, попробуйте следующий фрагмент кода:

**CommonJS:**

1. Вызов `require` и импортировать `asposepdfnodejs` модуль как `AsposePdf` переменная.
1. Укажите имя PDF‑файла, который будет изменён после расшифровки.
1. Вызов `AsposePdf` в виде Promise и выполнить операцию расшифровки файла. Получить объект при успешном выполнении.
1. Вызовите the [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) функция.
1. Расшифровать PDF-файл с паролем "owner".
1. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultDecrypt.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле возникает ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортировать `asposepdfnodejs` модуль.
1. Укажите имя PDF‑файла, который будет изменён после расшифровки.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите the [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) функция.
1. Расшифровать PDF-файл с паролем "owner".
1. Таким образом, если 'json.errorCode' равно 0, результат операции сохраняется в "ResultDecrypt.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле возникает ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```