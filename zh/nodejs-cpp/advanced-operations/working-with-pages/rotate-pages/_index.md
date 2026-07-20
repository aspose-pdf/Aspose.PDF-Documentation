---
title: 在 Node.js 中旋转 PDF 页面
linktitle: 旋转 PDF 页面
type: docs
weight: 50
url: /zh/nodejs-cpp/rotate-pages/
description: 本主题描述了如何在 Node.js 环境中以编程方式旋转现有 PDF 文件的页面方向。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

本节描述了如何使用 Aspose.PDF for Node.js via C++ 旋转现有 PDF 文件中的页面。

如果您想旋转 PDF 页面，可以使用 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) 函数。此函数使用特殊参数 'AsposePdfModule.Rotation' 来指定旋转值。通过它可以设置需要将 PDF 旋转多少度。有以下选项：None、90、180 或 270 度。

请检查以下代码片段，以在 Node.js 环境中旋转 PDF 页面。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要旋转的 PDF 文件名称。
1. 调用 `AsposePdf` 作为 Promise 并执行旋转页面的操作。成功时接收该对象。
1. 调用函数 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. 旋转所有 PDF 文件。旋转角度设置为 270 度 (on270)。因此，如果 'json.errorCode' 为 0，则操作结果会保存为 "ResultRotation.pdf"。如果 json.errorCode 参数不为 0，进而在文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要旋转的 PDF 文件名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. 旋转所有 PDF 文件。旋转角度设置为 270 度 (on270)。因此，如果 'json.errorCode' 为 0，则操作结果会保存为 "ResultRotation.pdf"。如果 json.errorCode 参数不为 0，进而在文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```