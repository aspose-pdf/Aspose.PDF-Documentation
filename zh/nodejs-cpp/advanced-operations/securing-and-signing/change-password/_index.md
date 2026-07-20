---
title: 在 Node.js 中更改 PDF 文件的密码
linktitle: 更改密码
type: docs
weight: 50
url: /zh/nodejs-cpp/change-password-pdf/
description: 使用 Aspose.PDF for Node.js via C++ 更改 PDF 文件的密码。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 更改 PDF 文件的密码

如果您想更改 PDF 的密码，您可以使用 [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) 函数。它通过所有者密码更改用户密码和所有者密码，同时保留原始安全设置。
如果您想将 PDF 文件的密码从“owner”更改为“newowner”或“newuser”，请尝试以下代码片段：

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要更改密码的 PDF 文件名称。
1. 调用 `AsposePdf` 作为 Promise 并执行更改密码的操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. 更改密码。现有的所有者密码设置为 “owner,”，并将其更改为 “newowner”，新用户密码为 “newuser”。
1. 因此，如果 ‘json.errorCode’ 为 0，则操作结果保存在 "ResultPdfChangePassword.pdf" 中。如果 json.errorCode 参数不为 0，并因此在您的文件中出现错误，则错误信息将包含在 ‘json.errorText’ 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

请注意，如果密码是空字符串：

1. 如果用户密码为空——PDF 将直接打开而无需输入密码（但仍然是加密的）。
1. 如果所有者密码为空，PDF 将以请求用户密码的方式打开。
1. 如果两者都为空  - PDF 将在不请求密码的情况下打开（但仍然被加密）。


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要更改密码的 PDF 文件名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. 更改密码。现有的所有者密码设置为 “owner,”，并将其更改为 “newowner”，新用户密码为 “newuser”。
1. 因此，如果 ‘json.errorCode’ 为 0，则操作结果保存在 "ResultPdfChangePassword.pdf" 中。如果 json.errorCode 参数不为 0，并因此在您的文件中出现错误，则错误信息将包含在 ‘json.errorText’ 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```