---
title: 在 Node.js 中拆分 PDF
linktitle: 拆分 PDF 文件
type: docs
weight: 30
url: /zh/nodejs-cpp/split-pdf/
description: 本主题展示了如何使用 Aspose.PDF for Node.js via C++ 将 PDF 页面拆分为单个 PDF 文件 .
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用 Node.js 将 PDF 拆分为两个文件

如果您想将单个 PDF 拆分为多个部分，可以使用 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) 函数。 
请检查以下代码片段，以在 Node.js 环境中拆分两个 PDF。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要拆分的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件拆分操作。如果成功，则接收对象。
1. 调用函数 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. 拆分两个 PDF 文件。它将变量 pageToSplit 设置为 1，表示在第 1 页拆分 PDF 文件。 
1. 因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultSplit1.pdf" 和 "ResultSplit2.pdf"。如果 json.errorCode 参数不是 0，且相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要拆分的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. 拆分两个 PDF 文件。它将变量 pageToSplit 设置为 1，表示在第 1 页拆分 PDF 文件。 
1. 因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultSplit1.pdf" 和 "ResultSplit2.pdf"。如果 json.errorCode 参数不是 0，且相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```