---
title: 在 Node.js 中向 PDF 添加图像
linktitle: 添加图像
type: docs
weight: 10
url: /zh/nodejs-cpp/add-image-to-pdf/
description: 本节介绍如何使用 Aspose.PDF for Node.js via C++ 向现有 PDF 文件添加图像。
lastmod: "2026-07-18"
---

## 向现有 PDF 文件添加图像

人们普遍认为向 PDF 文件添加图像需要复杂的专用工具。然而，使用 Aspose.PDF for Node.js，您可以在 Node.js 环境中快速、轻松地将所需的图像添加到 PDF 中。

我们只能在文件末尾添加图像，因此正确的示例是我们拥有一些扫描的文档页面并将它们转换为一个 PDF。

如果你想添加图像，可以使用 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) 函数。 
请查看以下代码片段，以在 Node.js 环境中添加图像。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要添加图像的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行添加图像的操作。成功时接收对象。
1. 调用函数 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. 将图像添加到 PDF 的末尾。因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultAddImage.pdf"。如果 json.errorCode 参数不为 0，随之在你的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要添加图像的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. 将图像添加到 PDF 的末尾。因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultAddImage.pdf"。如果 json.errorCode 参数不为 0，随之在你的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```