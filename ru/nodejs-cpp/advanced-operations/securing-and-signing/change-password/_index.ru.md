---
title: Изменение пароля PDF файла в Node.js
linktitle: Изменить пароль
type: docs
weight: 50
url: /nodejs-cpp/change-password-pdf/
description: Изменение пароля PDF файла с использованием Aspose.PDF для Node.js через C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Изменение пароля PDF файла

Если вы хотите изменить пароль PDF, вы можете использовать функцию [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/). Она изменяет пользовательский пароль и пароль владельца по паролю владельца, сохраняя исходные настройки безопасности.
Если вы хотите изменить пароль PDF файла с "owner" на "newowner" или "newuser", попробуйте следующий фрагмент кода:

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF файла, для которого будет изменён пароль.
1. Вызовите `AsposePdf` как Promise и выполните операцию по изменению пароля. Получите объект в случае успеха.

1. Вызовите функцию [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Изменить пароль. Существующий пароль владельца установлен как "owner," и он изменяется на "newowner" с новым паролем пользователя "newuser".
1. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfChangePassword.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Измените пароли PDF-файла с "owner" на "newowner" и сохраните как "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


Обратите внимание, что если пароль является пустой строкой:

1. Если пароль пользователя пустой - PDF открывается без запроса пароля (но все еще зашифрован).
2. Если пароль владельца пустой, PDF открывается с запросом пароля пользователя.
3. Если оба пусты - PDF открывается без запроса пароля (но все еще зашифрован).

**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
2. Укажите имя файла PDF, в котором будет изменен пароль.
3. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
4. Вызовите функцию [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
5. Измените пароль. Существующий пароль владельца устанавливается на "owner", и он изменяется на "newowner" с новым паролем пользователя "newuser".

1. Таким образом, если 'json.errorCode' равен 0, результат операции сохраняется в "ResultPdfChangePassword.pdf". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Изменить пароли PDF-файла с "owner" на "newowner" и сохранить как "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```