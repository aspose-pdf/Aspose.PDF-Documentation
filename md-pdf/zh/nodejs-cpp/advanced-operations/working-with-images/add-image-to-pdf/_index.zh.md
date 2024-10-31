---
title: 将图像添加到 Node.js 中的 PDF 
linktitle: 添加图像
type: docs
weight: 10
url: /nodejs-cpp/add-image-to-pdf/
description: 本节介绍如何使用 Aspose.PDF for Node.js via C++ 将图像添加到现有 PDF 文件。
lastmod: "2023-11-16"
---

## 向现有 PDF 文件添加图像

人们通常认为，将图像添加到 PDF 文件需要复杂的特殊工具。然而，使用 Aspose.PDF for Node.js，您可以在 Node.js 环境中快速轻松地将所需图像添加到 PDF。

我们只能将图像添加到文件的末尾，因此正确的示例是我们有一些扫描的文档页面并将其转换为单个 PDF。

如果您想添加图像，可以使用 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) 函数。
请检查以下代码片段以便在 Node.js 环境中添加图像。

**CommonJS：**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。

1. 指定将添加图像的 PDF 文件的名称。
1. 以 Promise 形式调用 `AsposePdf` 并执行添加图像的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/)。
1. 将图像添加到 PDF 的末尾。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultAddImage.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*将图像添加到 PDF 文件的末尾并保存为 "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要添加图像的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/)。
1. 将图像添加到 PDF 的末尾。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultAddImage.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*将图像添加到 PDF 文件末尾并保存为 "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```