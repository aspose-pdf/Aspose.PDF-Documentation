---
title: 在 Node.js 中从 PDF 提取图像
linktitle: 从 PDF 提取图像
type: docs
weight: 20
url: /zh/nodejs-cpp/extract-images-from-the-pdf-file/
description: 如何使用 Aspose.PDF for Node.js via C++ 工具包从 PDF 中提取图像的一部分。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在 Node.js 环境中从 PDF 文件提取图像

如果您想从 PDF 文档提取图像，可以使用 [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) 函数。 
我们必须向此函数传递三个参数：输入和输出文件名以及分辨率。
请检查下面的代码片段，以使用 Node.js 从 PDF 文件中提取图像。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要从中提取图像的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行提取图像的操作。如果成功，接收该对象。
1. 调用函数 [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. 从 PDF 文件中提取图像。因此，如果 ‘json.errorCode’ 为 0，则操作结果将保存为 "ResultPdfExtractImage{0:D2}.jpg"。其中 {0:D2} 表示两位数格式的页码。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不为 0，文件中相应出现错误，则错误信息将包含在 ‘json.errorText’ 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要从中提取图像的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. 从 PDF 文件中提取图像。因此，如果 ‘json.errorCode’ 为 0，则操作结果将保存为 "ResultPdfExtractImage{0:D2}.jpg"。其中 {0:D2} 表示两位数格式的页码。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不为 0，文件中相应出现错误，则错误信息将包含在 ‘json.errorText’ 中。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
