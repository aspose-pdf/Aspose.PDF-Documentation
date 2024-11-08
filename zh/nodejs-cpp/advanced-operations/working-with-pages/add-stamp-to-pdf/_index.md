---
title: 将图像印章添加到 PDF 中的 Node.js
linktitle: PDF 文件中的图像印章
type: docs
weight: 60
url: /zh/nodejs-cpp/stamping/
description: 使用 AsposePdfAddStamp 和 Node.js 工具在您的 PDF 文档中添加图像印章。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在 PDF 文件中添加图像印章

在 PDF 文档上盖章类似于在纸质文档上盖章。PDF 文件中的印章为 PDF 文件提供了附加信息，例如保护 PDF 文件供他人使用并确认 PDF 文件内容的安全性。
您可以使用 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) 函数在使用 Node.js 的环境下向 PDF 文件添加图像印章。

请查看以下代码片段，以便在 Node.js 环境中向 PDF 文件添加图像印章。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。

1. 指定将添加图像印章的PDF文件的名称。
1. 调用 `AsposePdf` 作为 Promise，并执行添加图像印章的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/)。
1. 在PDF文件中添加印章。因此，如果 'json.errorCode' 为0，操作结果将保存在 "ResultImage.pdf" 中。如果 json.errorCode 参数不是0，相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*将印章添加到PDF文件并保存为 "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要添加图像印章的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/)。
1. 将印章添加到 PDF 文件中。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultImage.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*将印章添加到 PDF 文件并保存为 "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```