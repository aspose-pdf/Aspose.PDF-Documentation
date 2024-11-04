---
title: 在 Node.js 中添加 PDF 数字签名
linktitle: 数字签署 PDF
type: docs
weight: 70
url: /nodejs-cpp/sign-pdf/
description: 在 Node.js 环境中对 PDF 文档进行数字签名。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 文档中的数字签名是一种验证文档真实性和完整性的方法。这是使用私钥和数字证书对 PDF 文档进行电子签名的过程。此签名保证持有人文档在签署后未被更改，并且签署者是其批准的人。要使用 Node.js 签署 PDF，请使用 Aspose.PDF 工具。

如果您想签署 PDF 文件，可以使用 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) 函数。

可以使用与签名相关的 **参数**：

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- reason

- contact
- 位置
- isVisible
- signatureAppearance
- fileNameResult

这个代码片段在 Node.js 环境中使用 AsposePDFforNode.js 模块，以 PKCS7 签名的方式对 PDF 文件进行数字签名。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定要签名的 PDF 文件名、PKCS7 密钥文件和签名外观图像文件。证书和图像可以放在文件系统中的任何位置，从那里上传以进行 PDF 签名。
1. 以 Promise 方式调用 `AsposePdf` 并执行签名文件的操作。如果成功，接收对象。
1. 调用 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) 函数。
1. 使用数字签名签署 PDF 文件。签名相关的参数（如密钥文件、密码、坐标、原因、联系人、位置等）。

1. 因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultSignPKCS7.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PKCS7 密钥*/
      const test_pfx_file = 'test.pfx';
      /*签名外观*/
      const sign_img_file = 'Aspose.jpg';
      /*使用数字签名签署 PDF 文件并保存为 "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。

1. 指定要签名的PDF文件、PKCS7密钥文件和签名外观图像文件。
1. 初始化AsposePdf模块。如果成功，接收对象。
1. 调用[AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/)函数。
1. 使用数字签名签署PDF文件。与签名相关的参数（如密钥文件、密码、坐标、原因、联系人、位置等）。
1. 因此，如果'json.errorCode'为0，操作结果将保存在"ResultSignPKCS7.pdf"中。如果json.errorCode参数不为0，相应地，在文件中出现错误，错误信息将包含在'json.errorText'中。

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