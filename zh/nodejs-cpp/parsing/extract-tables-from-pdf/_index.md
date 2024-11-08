---
title: 从 PDF 中提取表格在 Node.js 中
linktitle: 从 PDF 中提取表格
type: docs
weight: 10
url: /zh/nodejs-cpp/extract-tables-from-the-pdf-file/
description: 如何使用 Aspose.PDF for Node.js via C++ 工具包将 PDF 转换为 CSV。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在将 PDF 转换为 CSV 文件时提取表格

### 将 PDF 转换为 CSV

如果 PDF 中有表格，它们会被保存为单独的 CSV 文件。如果您想转换 PDF 文档，可以使用 [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) 函数。
请查看以下代码片段，以便在 Node.js 环境中转换 PDF 文件。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，接收对象。

1. 调用函数 [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoXlsX.xlsx" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* 将 PDF 文件转换为 CSV（提取表格），使用模板 "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... 格式页码)，使用 TAB 作为分隔符并保存 */
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。

1. 指定要转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoXlsX.xlsx" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 CSV（提取表格），使用模板 "ResultPdfTablesToCSV{0:D2}.csv" （{0}, {0:D2}, {0:D3}, ... 格式页码），TAB 作为分隔符并保存*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```