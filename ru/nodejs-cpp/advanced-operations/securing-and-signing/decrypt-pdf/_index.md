---
title: Расшифровать PDF в Node.js
linktitle: Расшифровать PDF Файл
type: docs
weight: 40
url: ru/nodejs-cpp/decrypt-pdf/
description: Расшифровать PDF Файл с помощью Aspose.PDF для Node.js через C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Расшифровка PDF файла с использованием пароля владельца

В последнее время всё больше пользователей обмениваются зашифрованными документами, чтобы не стать жертвами интернет-мошенничества и защитить свои документы.
В связи с этим возникает необходимость доступа к зашифрованному PDF файлу, так как такой доступ может быть получен только авторизованным пользователем. Также люди ищут различные решения для расшифровки PDF файлов.

Если вы хотите расшифровать PDF файл, вы можете использовать функцию [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
Если вы хотите расшифровать PDF файл, попробуйте следующий фрагмент кода:

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, который будет изменен на расшифрованный.

1. Вызовите `AsposePdf` как Promise и выполните операцию по расшифровке файла. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Расшифруйте PDF файл с паролем "owner".
1. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultDecrypt.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Расшифровать PDF-файл с паролем "owner" и сохранить в "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF файла, для которого будет изменено шифрование.
1. Инициализируйте модуль AsposePdf. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/).
1. Расшифруйте PDF файл с паролем "owner".
1. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultDecrypt.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Расшифруйте PDF файл с паролем "owner" и сохраните как "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```