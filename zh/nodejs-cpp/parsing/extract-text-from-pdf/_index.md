---
title: 从 PDF 中提取文本在 Node.js 中
linktitle: 从 PDF 中提取文本
type: docs
weight: 30
url: /zh/nodejs-cpp/extract-text-from-pdf/
description: 本文介绍了使用 Aspose.PDF for Node.js via C++ 从 PDF 文档中提取文本的各种方法。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档中提取文本

从 PDF 文档中提取文本是一项非常常见且有用的任务。从 PDF 中提取文本有多种用途，从改善搜索和可用性到实现商业、研究和信息管理等各个领域的数据分析和自动化。

如果您想从 PDF 文档中提取文本，可以使用 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) 函数。
请查看以下代码片段，以便通过 C++ 在 Node.js 中从 PDF 文件中提取文本。

查看代码片段并按照步骤从您的 PDF 中提取文本：

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块作为 `AsposePdf` 变量。
1. 指定将要提取文本的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行提取文本的操作。如果成功，则接收对象。
1. 调用函数 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/)。
1. 提取的文本存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，则使用 console.log 显示提取的文本。如果 json.errorCode 参数不是 0，并且相应地，在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*从 PDF 文件中提取文本*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要从中提取文本的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收该对象。
1. 调用函数 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/)。
1. 提取的文本存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，则使用 console.log 显示提取的文本。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*从 PDF 文件中提取文本*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```