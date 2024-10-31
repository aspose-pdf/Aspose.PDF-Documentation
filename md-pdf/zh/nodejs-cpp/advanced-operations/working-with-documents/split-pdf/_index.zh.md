---
title: 使用 Node.js 拆分 PDF
linktitle: 拆分 PDF 文件
type: docs
weight: 30
url: /nodejs-cpp/split-pdf/
description: 本主题展示如何使用 Aspose.PDF for Node.js via C++ 将 PDF 页面拆分为单个 PDF 文件。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用 Node.js 将 PDF 拆分为两个文件

如果您想将单个 PDF 拆分为多个部分，可以使用 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) 函数。
请查看以下代码片段，以便在 Node.js 环境中拆分两个 PDF。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块作为 `AsposePdf` 变量。
2. 指定将要拆分的 PDF 文件的名称。
3. 调用 `AsposePdf` 作为 Promise 并执行拆分文件的操作。如果成功，接收对象。
4. 调用函数 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/)。

1. 拆分两个PDF文件。它将变量pageToSplit设置为1，表示PDF文件将在第1页拆分。
1. 因此，如果'json.errorCode'为0，则操作结果将保存在"ResultSplit1.pdf"和"ResultSplit2.pdf"中。如果json.errorCode参数不为0，并且相应地，您的文件中出现错误，则错误信息将包含在'json.errorText'中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*设置要拆分的页面数量*/
      const pageToSplit = 1;
      /*拆分为两个PDF文件并保存为"ResultSplit1.pdf"和"ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入`asposepdfnodejs`模块。

1. 指定将要拆分的PDF文件的名称。
1. 初始化AsposePdf模块。如果成功，接收对象。
1. 调用函数 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/)。
1. 拆分两个PDF文件。它将变量pageToSplit设置为1，表示PDF文件将在第1页被拆分。
1. 因此，如果'json.errorCode'为0，操作结果保存在"ResultSplit1.pdf"和"ResultSplit2.pdf"中。如果json.errorCode参数不为0，相应地，您的文件中出现错误，错误信息将包含在'json.errorText'中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*设置要拆分的页码*/
  const pageToSplit = 1;
  /*拆分为两个PDF文件并保存为"ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```