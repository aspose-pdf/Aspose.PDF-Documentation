---
title: 在 Node.js 中将 PDF/A 转换为 PDF 格式
linktitle: 将 PDF/A 转换为 PDF 格式
type: docs
weight: 110
url: /zh/nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2026-07-18"
description: 本主题展示了 Aspose.PDF 如何在 Node.js 环境中将 PDF/A 文件转换为 PDF 文档。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将 PDF/A 转换为 PDF 格式

如果您想转换 PDF 文档，可以使用 [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. 转换 PDF 文件。因此，如果 ‘json.errorCode’ 为 0，则操作结果将保存在 "ResultConvertToPDF.pdf"。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，则错误信息将包含在 ‘json.errorText’ 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要转换的 PDF/A 文件的名称
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. 转换 PDF 文件。因此，如果 ‘json.errorCode’ 为 0，则操作结果将保存在 "ResultConvertToPDF.pdf"。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，则错误信息将包含在 ‘json.errorText’ 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```