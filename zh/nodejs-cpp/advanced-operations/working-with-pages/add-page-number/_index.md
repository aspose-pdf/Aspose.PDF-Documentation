---
title: 在 Node.js 中为 PDF 添加页码
linktitle: 添加页码
type: docs
weight: 100
url: /zh/nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++ 允许您使用 AsposePdfAddPageNum 向 PDF 文件添加页码印章。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

页码使读者更容易定位文档的不同部分。以下代码片段展示了如何使用 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) 函数在 Node.js 中为 PDF 添加页码。

请查看以下代码片段，以在 Node.js 环境中向 PDF 添加页码。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要添加页码的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行添加页码的操作。成功时接收对象。
1. 调用函数 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. 向 PDF 文件添加页码。因此，如果 ‘json.errorCode’ 为 0，操作结果将保存为 “ResultAddPageNum.pdf”。如果 json.errorCode 参数不为 0，则您的文件中会出现错误，错误信息将包含在 ‘json.errorText’ 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add page number to a PDF-file save the "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要添加页码的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. 向 PDF 文件添加页码。因此，如果 ‘json.errorCode’ 为 0，操作结果将保存为 “ResultAddPageNum.pdf”。如果 json.errorCode 参数不为 0，则您的文件中会出现错误，错误信息将包含在 ‘json.errorText’ 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add page number to a PDF-file and save the "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```