---
title: 将PDF转换为Excel在Node.js中
linktitle: 将PDF转换为Excel
type: docs
weight: 20
url: /zh/nodejs-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-16"
keywords: 使用node.js将PDF转换为Excel, 将PDF转换为XLSX。
description: Aspose.PDF for Node.js允许您将PDF转换为XLSX格式。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用Node.js从PDF创建电子表格

**Aspose.PDF for Node.js via C++** 支持将PDF文件转换为Excel文件的功能。

{{% alert color="success" %}}
**尝试在线将PDF转换为Excel**

Aspose.PDF for Node.js为您提供了免费的在线应用程序["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF转换PDF为Excel使用免费应用程序](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## 将PDF转换为XLSX

如果您想转换PDF文档，可以使用[AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/)函数。
 
请检查以下代码片段以便在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。
2. 指定将要转换的 PDF 文件的名称。
3. 将 `AsposePdf` 作为 Promise 调用并执行文件转换操作。如果成功，接收对象。
4. 调用函数 [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/)。
5. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoXlsX.xlsx" 中。如果 json.errorCode 参数不为 0，相应地，文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 XlsX 并保存为 "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
      console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将被转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfToXlsX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxlsx/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoXlsX.xlsx" 中。如果 json.errorCode 参数不为 0，相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 XlsX 并保存为 "ResultPDFtoXlsX.xlsx"*/
  const json = AsposePdfModule.AsposePdfToXlsX(pdf_file, "ResultPDFtoXlsX.xlsx");
  console.log("AsposePdfToXlsX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```