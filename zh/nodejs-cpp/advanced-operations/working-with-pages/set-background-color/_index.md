---
title: 在 Node.js 中设置 PDF 的背景颜色
linktitle: 设置背景颜色
type: docs
weight: 80
url: /zh/nodejs-cpp/set-background-color/
description: 使用 Node.js 通过 C++ 为您的 PDF 文件设置背景颜色。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

如果您想设置 PDF 的背景颜色，可以使用 [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) 函数。 

请查看以下代码片段，以在 Node.js 环境中设置 PDF 的背景颜色。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要设置背景颜色的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行设置背景颜色的操作。如果成功，接收该对象。
1. 调用函数 [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. 为 PDF 文件设置背景颜色。您需要向此函数传递 3 个参数：输入文件名、十六进制形式的目标颜色以及输出文件名。因此，如果 ‘json.errorCode’ 为 0，则操作结果保存为 “ResultPdfSetBackgroundColor.pdf”。如果 json.errorCode 参数不为 0，则您的文件中会出现错误，错误信息将包含在 ‘json.errorText’ 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要设置背景颜色的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. 设置 PDF 文件的背景颜色。背景颜色设置为 "#426bf4"，这是表示蓝色阴影的十六进制颜色代码。因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultPdfSetBackgroundColor.pdf"。如果 json.errorCode 参数不是 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```