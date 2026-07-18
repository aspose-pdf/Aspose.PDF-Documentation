---
title: 在 Node.js 中为 PDF 添加数字签名
linktitle: 对 PDF 进行数字签署
type: docs
weight: 70
url: /zh/nodejs-cpp/sign-pdf/
description: 在 Node.js 环境中对 PDF 文档进行数字签署。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


PDF 文档中的数字签名是一种验证文档真实性和完整性的方法。这是使用私钥和数字证书对 PDF 文档进行电子签名的过程。此签名保证持有人文档自签名以来未被更改或篡改，并且签署者即为其批准的人员。要在 Node.js 中签署 PDF，请使用 Aspose.PDF 工具。

如果您想签署 PDF 文件，可以使用 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) 函数。

可以使用与签名相关的 **parameters**：

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- 设置Y缩进
- 设置高度
- 设置宽度
- 原因
- 联系
- 位置
- isVisible
- signatureAppearance
- fileNameResult 

此代码片段在 Node.js 环境中使用 AsposePDFforNode.js 模块通过 PKCS7 签名对 PDF 文件进行数字签名。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要签名的 PDF 文件名称、PKCS7 密钥文件以及签名外观图像文件。证书和图像可以放在文件系统的任何位置，然后上传用于 PDF 签名。
1. 调用 `AsposePdf` 作为 Promise 并执行文件签名操作。如果成功，则接收对象。
1. 调用 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) 函数。 
1. 使用数字签名对 PDF 文件进行签名。与签名相关的参数（例如密钥文件、密码、坐标、原因、联系人、位置等）。 
1. 因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultSignPKCS7.pdf"。如果 json.errorCode 参数不为 0 并相应地在文件中出现错误，错误信息将包含在 'json.errorText' 中。

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

1. 导入 `asposepdfnodejs` 模块。
1. 指定要签名的 PDF 文件名称、PKCS7 密钥文件以及签名外观图像文件。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) 函数。 
1. 使用数字签名对 PDF 文件进行签名。与签名相关的参数（例如密钥文件、密码、坐标、原因、联系人、位置等）。 
1. 因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultSignPKCS7.pdf"。如果 json.errorCode 参数不为 0 并相应地在文件中出现错误，错误信息将包含在 'json.errorText' 中。

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