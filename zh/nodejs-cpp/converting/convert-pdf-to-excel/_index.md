---
title: 在 Node.js 中将 PDF 转换为 Excel
linktitle: 将 PDF 转换为 Excel
type: docs
weight: 20
url: /zh/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-18"
description: Aspose.PDF for Node.js 允许您将 PDF 转换为 XLSX 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用 Node.js 从 PDF 创建电子表格 

**Aspose.PDF for Node.js via C++** 支持将 PDF 文件转换为 Excel 文件的功能。

{{% alert color="success" %}}
**尝试将 PDF 转换为 Excel 在线**

Aspose.PDF for Node.js 为您提供在线免费应用程序 [“PDF to XLSX”](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，在这里您可以尝试了解其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 Excel 的免费应用](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## 将 PDF 转换为 XLSX

如果您想转换 PDF 文档，可以使用 [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作的结果将保存于 \"ResultPDFtoXlsX.xlsx\"。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作的结果将保存于 \"ResultPDFtoXlsX.xlsx\"。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

