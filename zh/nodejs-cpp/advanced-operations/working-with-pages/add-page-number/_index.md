---
title: 在 Node.js 中为 PDF 添加页码
linktitle: 添加页码
type: docs
weight: 100
url: zh/nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++ 允许您使用 AsposePdfAddPageNum 向 PDF 文件添加页码印记。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

页码使读者更容易定位文档的不同部分。以下代码片段展示了如何在 Node.js 中使用 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) 函数为 PDF 页添加页码。

请查看以下代码片段以便在 Node.js 环境中向 PDF 添加页码。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块作为 `AsposePdf` 变量导入。
1. 指定要添加页码的 PDF 文件名称。
1. 将 `AsposePdf` 作为 Promise 调用，并执行添加页码操作。如果成功，接收对象。

1. 调用函数 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/)。
1. 向 PDF 文件添加页码。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultAddPageNum.pdf" 中。如果 json.errorCode 参数不为 0，并且在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*向 PDF 文件添加页码并保存为 "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要添加页码的 PDF 文件名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。

1. 调用函数 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/)。
1. 向 PDF 文件添加页码。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultAddPageNum.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*向 PDF 文件中添加页码并保存为 "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```