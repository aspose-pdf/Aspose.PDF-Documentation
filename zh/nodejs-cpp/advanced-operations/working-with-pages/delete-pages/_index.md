---
title: 在 Node.js 中删除 PDF 页面
linktitle: 删除 PDF 页面
type: docs
weight: 30
url: /zh/nodejs-cpp/delete-pages/
description: 您可以使用 Aspose.PDF for Node.js via C++ 从 PDF 文件中删除页面。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

如果您想删除 PDF 页面，可以使用 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) 函数。 

此函数的一个特性是它可以接受多种类型作为 numPages 参数：

- string: 在这种情况下，我们可以使用特定页面或区间来指定一组页面。例如，字符串 "7, 20, 30-32, 34" 表示我们要删除第7页、第20页、从第30页到第32页以及第34页。
- array: 在这种情况下，我们只能指定页面。数组 [3,7] 表示我们要删除第3页和第7页。
- int: 单个页码。

请查看以下代码片段，以在 Node.js 环境中删除 PDF 页面。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要删除页面的 PDF 文件名。
1. 调用 `AsposePdf` 作为 Promise 并执行删除页面的操作。成功时接收该对象。
1. 调用函数 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. 从 PDF 文件中删除特定页面。因此，如果 'json.errorCode' 为 0，则操作结果会保存在 "ResultDeletePages.pdf" 中。如果 json.errorCode 参数不为 0，且相应地在文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要删除页面的 PDF 文件名。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 该函数帮助从 PDF 文件中删除指定页面。操作由 numPages 变量确定，该变量可以是带有页面区间的字符串（例如 \u00227, 20, 22, 30-32, 33, 36-40, 46\u0022），页面号数组，或单个页面号。
1. 从 PDF 文件中删除特定页面。因此，如果 'json.errorCode' 为 0，则操作结果会保存在 "ResultDeletePages.pdf" 中。如果 json.errorCode 参数不为 0，且相应地在文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```