---
title: 将PDF转换为PPTX在Node.js中
linktitle: 将PDF转换为PowerPoint
type: docs
weight: 30
url: zh/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-16"
description: Aspose.PDF允许您在Node.js环境中直接将PDF转换为PPTX格式。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**尝试在线将PDF转换为PowerPoint**

Aspose.PDF for Node.js为您提供在线免费应用程序["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF转换PDF到PPTX免费应用](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## 将PDF转换为PPTX

如果您想转换PDF文档，可以使用[AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/)函数。

请查看以下代码片段以在Node.js环境中进行转换。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行文件转换操作。如果成功，接收对象。
1. 调用函数 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoPptX.pptx" 中。如果 json.errorCode 参数不为 0，且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 PptX 并保存为 "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将被转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoPptX.pptx" 中。如果 json.errorCode 参数不为 0，因此，在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 PptX 并保存为 "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```