---
title: 如何在 Node.js 中合并 PDF
linktitle: 合并 PDF 文件
type: docs
weight: 20
url: /zh/nodejs-cpp/merge-pdf/
description: 此页面解释如何使用 Aspose.PDF for Node.js via C++ 将 PDF 文档合并为单个 PDF 文件。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 在 Node.js 中合并或组合两个 PDF 为单个 PDF

在处理大量文档时，合并和组合文件是一项非常常见的任务。有时，在处理文档和图像时，经过扫描、处理和组织，会产生多个文件。
但是如果您需要将所有内容存储在一个文件中怎么办？或者您不想打印多个文档？使用 Aspose.PDF for Node.js via C++ 将两个 PDF 文件合并。

如果您想合并两个 PDF 文件，您可以使用 [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) 函数。 
请查看以下代码片段，以在 Node.js 环境中合并两个 PDF 文件。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要合并的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行合并操作。如果成功，接收该对象。
1. 调用函数 [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. 合并两个 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果会保存为 \"ResultMerge.pdf\"。如果 json.errorCode 参数不为 0，且相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要合并的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. 合并两个 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果会保存为 \"ResultMerge.pdf\"。如果 json.errorCode 参数不为 0，且相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```