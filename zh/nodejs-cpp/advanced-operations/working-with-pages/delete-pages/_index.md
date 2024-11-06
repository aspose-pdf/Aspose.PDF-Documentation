---
title: 在 Node.js 中删除 PDF 页面
linktitle: 删除 PDF 页面
type: docs
weight: 30
url: zh/nodejs-cpp/delete-pages/
description: 您可以使用 Aspose.PDF for Node.js via C++ 从 PDF 文件中删除页面。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

如果您想删除 PDF 页面，可以使用 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) 函数。

该函数的一个特点是它可以接受几种类型作为 numPages 参数：

- 字符串：在这种情况下，我们可以使用特定页面或区间来指定一组页面。例如，字符串 "7, 20, 30-32, 34" 意味着我们想删除第 7, 20, 从 30 到 32 和第 34 页。
- 数组：在这种情况下，我们只能指定页面。数组 [3,7] 意味着我们想删除第 3 和第 7 页。
- 整数：单个页面编号。

请查看以下代码片段，以在 Node.js 环境中删除 PDF 页面。

**CommonJS:**


1. 调用 `require` 并导入 `asposepdfnodejs` 模块作为 `AsposePdf` 变量。
1. 指定要删除页面的 PDF 文件名称。
1. 调用 `AsposePdf` 作为 Promise，并执行删除页面的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/)。
1. 从 PDF 文件中删除特定页面。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultDeletePages.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*字符串，包括带间隔的页码: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*数组，页码数组*/
      /*const numPages = [1,3];*/
      /*数字，页码*/
      const numPages = 1;
      /*从 PDF 文件中删除页面并保存为 "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
2. 指定要删除页面的PDF文件的名称。
3. 初始化 AsposePdf 模块。如果成功，接收对象。
4. 调用函数 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/)。此函数帮助从PDF文件中删除指定的页面。操作由 numPages 变量确定，该变量可以是带有页面区间的字符串（例如，“7, 20, 22, 30-32, 33, 36-40, 46”）、页面号码数组或单个页面号。
5. 从PDF文件中删除特定页面。因此，如果 'json.errorCode' 为0，操作的结果将保存在“ResultDeletePages.pdf”中。如果 json.errorCode 参数不为0，并且文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*字符串，包括具有区间的页面号码："7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*数组，页面号码数组*/
  /*const numPages = [1,3];*/
  /*数字，页面号码*/
  const numPages = 1;
  /*从PDF文件中删除页面并保存为“ResultDeletePages.pdf”*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```