---
title: 将PDF转换为PDF/A格式在Node.js中
linktitle: 将PDF转换为PDF/A格式
type: docs
weight: 100
url: /zh/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-16"
description: 本主题向您展示如何在Node.js环境中使用Aspose.PDF将PDF文件转换为符合PDF/A标准的PDF文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js** 允许您将PDF文件转换为符合<abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr>标准的PDF文件。

{{% alert color="success" %}}
**尝试在线将PDF转换为PDF/A**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将PDF转换为PDF/A](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## 将PDF转换为PDF/A格式

如果您想转换PDF文档，可以使用 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) 函数。
 
请检查以下代码片段以便在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行文件转换操作。如果成功，接收对象。
1. 调用函数 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/)。
1. 修复 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultConvertToPDFA.pdf" 中。在转换过程中，会执行验证，验证结果将保存为 "ResultConvertToPDFALog.xml"。如果 json.errorCode 参数不为 0，并且因此在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 PDF/A(1A) 并保存为 "ResultConvertToPDFA.pdf"*/
      /*在转换过程中，也会执行验证，"ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的PDF文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/)。
1. 修复 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultConvertToPDFA.pdf" 中。在转换过程中，会进行验证，验证结果保存在 "ResultConvertToPDFALog.xml" 中。如果 json.errorCode 参数不为 0，因此文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 PDF/A(1A) 并保存为 "ResultConvertToPDFA.pdf"*/
  /*在转换过程中，也会进行验证，"ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```