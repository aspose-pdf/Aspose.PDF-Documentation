---
title: 如何在 Node.js 中合并 PDF
linktitle: 合并 PDF 文件
type: docs
weight: 20
url: /nodejs-cpp/merge-pdf/
description: 本页解释如何使用 Aspose.PDF for Node.js via C++ 将 PDF 文档合并为一个 PDF 文件。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 在 Node.js 中将两个 PDF 合并为一个 PDF

在处理大量文档时，合并和组合文件是一项非常流行的任务。有时，在处理文档和图像时，当它们被扫描、处理和组织后，会创建几个文件。
但如果你需要将所有内容存储在一个文件中呢？或者你不想打印多个文档？使用 Aspose.PDF for Node.js via C++ 将两个 PDF 文件连接起来。

如果你想合并两个 PDF，可以使用 [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) 函数。
请查看以下代码片段，以便在 Node.js 环境中合并两个 PDF 文件。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块作为 `AsposePdf` 变量。
1. 指定将要合并的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行合并操作。如果成功，接收对象。
1. 调用函数 [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/)。
1. 合并两个 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultMerge.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*合并两个PDF文件并保存为"ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将被合并的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/)。
1. 合并两个 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultMerge.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*合并两个 PDF 文件并保存为 "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```