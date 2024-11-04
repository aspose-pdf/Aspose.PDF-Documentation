---
title: 用 Node.js 加密 PDF
linktitle: 加密 PDF 文件
type: docs
weight: 50
url: /nodejs-cpp/encrypt-pdf/
description: 使用 Aspose.PDF for Node.js via C++ 加密 PDF 文件。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用用户或所有者密码加密 PDF 文件

如果您要通过电子邮件发送包含机密信息的 PDF 附件，您可能希望首先为其添加一些安全性，以防止其落入错误的手中。限制对 PDF 文档的未经授权访问的最佳方法是使用密码保护它。要轻松且安全地加密文档，您可以使用 Aspose.PDF for Node.js via C++。

>在加密 PDF 文件时，请指定不同的用户和所有者密码。

- **用户密码**，如果设置，是您需要提供以打开 PDF 的密码。Acrobat/Reader 会提示用户输入用户密码。如果不正确，文档将无法打开。
- **所有者密码**，如果设置，控制权限，例如打印、编辑、提取、评论等。
 Acrobat/Reader 将根据权限设置禁止这些操作。 如果您想设置/更改权限，Acrobat 将需要此密码。

如果您想加密 PDF 文件，可以使用 [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 函数。 如果您想加密 PDF 文件，请尝试以下代码片段：

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定将被加密的 PDF 文件的名称。
1. 将 `AsposePdf` 调用为 Promise 并执行加密文件的操作。 如果成功，则接收对象。
1. 调用 [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) 函数。
1. 使用密码 "user" 和 "owner" 加密 PDF 文件。
1. 因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultEncrypt.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*使用密码 "user" 和 "owner" 加密一个 PDF 文件，并保存为 "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

有不同的[加密权限](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#acbb404dc8d3b328891faa5fba341ce0c):

- Module.Permissions.PrintDocument
- Module.Permissions.ModifyContent
- Module.Permissions.ExtractContent

- Module.Permissions.ModifyTextAnnotations
- Module.Permissions.FillForm
- Module.Permissions.ExtractContentWithDisabilities
- Module.Permissions.AssembleDocument
- Module.Permissions.PrintingQuality

有各种[加密算法](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ae15d4d8afe86aae14972a6e493d19f66):

- Module.CryptoAlgorithm.RC4x40
- Module.CryptoAlgorithm.RC4x128
- Module.CryptoAlgorithm.AESx128
- Module.CryptoAlgorithm.AESx256

**ECMAScript/ES6:**

1. 导入`asposepdfnodejs`模块。
1. 指定将更改加密的PDF文件的名称。
1. 初始化AsposePdf模块。如果成功，接收对象。
1. 调用[AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/)函数。
1. 使用密码“user”和“owner”解密PDF文件。

1. 因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultEncrypt.pdf" 中。如果 json.errorCode 参数不是 0，那么您的文件中会出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*使用密码 "user" 和 "owner" 加密 PDF 文件，并保存为 "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```