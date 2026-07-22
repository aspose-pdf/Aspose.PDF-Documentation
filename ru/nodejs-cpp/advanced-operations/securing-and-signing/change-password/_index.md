---
title: Изменить пароль PDF‑файла в Node.js
linktitle: Изменить пароль
type: docs
weight: 50
url: /ru/nodejs-cpp/change-password-pdf/
description: Изменить пароль PDF‑файла с помощью Aspose.PDF for Node.js via C++.
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Измените пароль PDF‑файла

Если вы хотите изменить пароль PDF, вы можете использовать [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) функция. Она изменяет пользовательский пароль и пароль владельца, используя пароль владельца, сохраняя оригинальные настройки безопасности.
Если вы хотите изменить пароль PDF‑файла с \"owner\" на \"newowner\" или \"newuser\", попробуйте следующий фрагмент кода:

**CommonJS:**

1. Вызовите `require` и импортируйте модуль `asposepdfnodejs` как переменную `AsposePdf`.
1. Укажите имя PDF‑файла, в котором будет изменён пароль.
1. Вызовите `AsposePdf` как Promise и выполните операцию по изменению пароля. Получите объект в случае успеха.
1. Вызовите функцию [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Измените пароль. Текущий пароль владельца установлен как \"owner,\" и он изменяется на \"newowner\" с новым пользовательским паролем \"newuser\".
1. Таким образом, если ‘json.errorCode’ равен 0, результат операции сохраняется в файле \"ResultPdfChangePassword.pdf\". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Обратите внимание, что если пароль — пустая строка:

1. Если пользовательский пароль пустой, PDF открывается без запроса пароля (но он всё равно зашифрован).
1. Если пароль владельца пустой, PDF открывается с запросом пароля пользователя.
1. Если оба пусты  - PDF открывается без запроса пароля (но он всё ещё зашифрован).


**ECMAScript/ES6:**

1. Импортируйте модуль `asposepdfnodejs`.
1. Укажите имя PDF‑файла, в котором будет изменён пароль.
1. Инициализируйте модуль AsposePdf. Получите объект, если успешно.
1. Вызовите функцию [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Измените пароль. Текущий пароль владельца установлен как \"owner,\" и он изменяется на \"newowner\" с новым пользовательским паролем \"newuser\".
1. Таким образом, если ‘json.errorCode’ равен 0, результат операции сохраняется в файле \"ResultPdfChangePassword.pdf\". Если параметр json.errorCode не равен 0 и, соответственно, в вашем файле появляется ошибка, информация об ошибке будет содержаться в ‘json.errorText’.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```