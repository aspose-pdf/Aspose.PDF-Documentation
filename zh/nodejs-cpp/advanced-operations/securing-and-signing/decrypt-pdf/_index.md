---
title: 在 Node.js 中解密 PDF
linktitle: 解密 PDF 文件
type: docs
weight: 40
url: /zh/nodejs-cpp/decrypt-pdf/
description: 使用 Aspose.PDF for Node.js via C++ 解密 PDF 文件。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用所有者密码解密 PDF 文件

最近，越来越多的用户交换加密文档，以免成为互联网诈骗的受害者并保护他们的文件。
在这方面，访问加密的 PDF 文件变得必要，因为只有授权用户才能获得此类访问权限。同时，人们正在寻找各种解密 PDF 文件的方案。 

如果您想要解密 PDF 文件，您可以使用 [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 函数。 
如果您想要解密 PDF 文件，请尝试以下代码片段：

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定 PDF 文件的名称，该文件将被解密。
1. 调用 `AsposePdf` 作为 Promise 并执行文件解密操作。如果成功，接收对象。
1. 调用 [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 函数。
1. 使用密码 "owner" 解密 PDF 文件。
1. 因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultDecrypt.pdf"。如果 json.errorCode 参数不为 0，并相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

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

1. 导入 `asposepdfnodejs` 模块。
1. 指定 PDF 文件的名称，该文件将被解密。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用 [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) 函数。
1. 使用密码 "owner" 解密 PDF 文件。
1. 因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultDecrypt.pdf"。如果 json.errorCode 参数不为 0，并相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```