---
title: 在 Node.js 中将 PDF 转换为 PDF/A 格式
linktitle: 将 PDF 转换为 PDF/A 格式
type: docs
weight: 100
url: /zh/nodejs-cpp/convert-pdf-to-pdfa/
lastmod: "2026-07-18"
description: 本主题向您展示 Aspose.PDF 如何在 Node.js 环境中将 PDF 文件转换为符合 PDF/A 标准的 PDF 文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for Node.js** 允许您将 PDF 文件转换为 <abbr title="Portable Document Format for Archiving of electronic documents">PDF/A</abbr> 符合 PDF 标准的文件。 

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF 转 PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，在这里您可以尝试了解其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 PDF/A 的免费应用](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## 将 PDF 转换为 PDF/A 格式

如果您想转换 PDF 文档，可以使用 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. 修复 PDF 文件。 因此，如果 \u0027json.errorCode\u0027 为 0，则操作结果保存在 \u0022ResultConvertToPDFA.pdf\u0022 中。 在转换过程中，会执行验证，验证结果保存在 \u0022ResultConvertToPDFALog.xml.\u0022 中。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 \u0027json.errorText\u0027 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
      /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
      console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttopdfa/).
1. 修复 PDF 文件。 因此，如果 \u0027json.errorCode\u0027 为 0，则操作结果保存在 \u0022ResultConvertToPDFA.pdf\u0022 中。 在转换过程中，会执行验证，验证结果保存在 \u0022ResultConvertToPDFALog.xml.\u0022 中。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 \u0027json.errorText\u0027 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
  /*During conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
  const json = AsposePdfModule.AsposePdfConvertToPDFA(pdf_file, AsposePdfModule.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFALog.xml");
  console.log("AsposePdfConvertToPDFA => %O", json.errorCode == 0 ? [json.fileNameResult, json.fileNameLogResult] : json.errorText);
```





