---
title: 在 Node.js 中为 PDF 添加背景
linktitle: 添加背景
type: docs
weight: 10
url: zh/nodejs-cpp/add-background/
description: 在 Node.js 中为您的 PDF 文件添加背景图像
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

以下代码片段展示了如何使用 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) 函数在 Node.js 中为 PDF 页面添加背景图像。

请查看以下代码片段以在 Node.js 环境中添加背景图像。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定要添加背景图像的 PDF 文件的名称。
1. 将 `AsposePdf` 调用为 Promise 并执行添加背景图像的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/)。

1. 将背景图像添加到PDF文件中。因此，如果 'json.errorCode' 为0，则操作结果保存在 "ResultAddBackgroundImage.pdf" 中。如果 json.errorCode 参数不为0，并且因此在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*将背景图像添加到PDF文件中并保存为 "ResultAddBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将添加背景图像的PDF文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。

1. 调用函数 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/)。
1. 向 PDF 文件添加背景图像。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultAddBackgroundImage.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*向 PDF 文件添加背景图像并保存为 "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```