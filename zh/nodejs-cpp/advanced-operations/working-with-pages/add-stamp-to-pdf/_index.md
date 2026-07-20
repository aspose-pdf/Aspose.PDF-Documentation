---
title: 在 Node.js 中向 PDF 添加图像印章
linktitle: PDF 文件中的图像印章
type: docs
weight: 60
url: /zh/nodejs-cpp/stamping/
description: 使用 Node.js 工具中的 AsposePdfAddStamp 在您的 PDF 文档中添加图像印章。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在 PDF 文件中添加图像印章

对 PDF 文档进行盖章类似于对纸质文档进行盖章。PDF 文件中的印章为文件提供额外信息，例如保护 PDF 文件免受他人使用以及确认 PDF 文件内容的安全性。
您可以使用 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) 使用 Node.js 向 PDF 文件添加图像印章的函数。

请检查以下代码片段，以在 Node.js 环境中向 PDF 文件添加图像印章。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将添加图像印章的 PDF 文件名称。
1. 调用 `AsposePdf` 作为 Promise 并执行添加图像印章的操作。如果成功，则接收对象。
1. 调用函数 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. 向 PDF 文件添加印章。因此，如果 `json.errorCode` 为 0，操作结果将保存为 “ResultImage.pdf”。如果 `json.errorCode` 参数不为 0，且相应地在您的文件中出现错误，错误信息将包含在 `json.errorText` 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将添加图像印章的 PDF 文件名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. 向 PDF 文件添加印章。因此，如果 `json.errorCode` 为 0，操作结果将保存为 “ResultImage.pdf”。如果 `json.errorCode` 参数不为 0，且相应地在您的文件中出现错误，错误信息将包含在 `json.errorText` 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```