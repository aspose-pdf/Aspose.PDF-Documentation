---
title: 将PDF/A转换为PDF格式在Node.js中
linktitle: 将PDF/A转换为PDF格式
type: docs
weight: 110
url: /nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-16"
description: 本主题向您展示如何在Node.js环境中使用Aspose.PDF将PDF/A文件转换为PDF文档。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将PDF/A转换为PDF格式

如果您想转换PDF文档，可以使用[AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/)函数。
请查看以下代码片段以便在Node.js环境中进行转换。

**CommonJS:**

1. 调用`require`并导入`asposepdfnodejs`模块为`AsposePdf`变量。
1. 指定将被转换的PDF文件的名称。
1. 调用`AsposePdf`作为Promise并执行转换文件的操作。如果成功，接收对象。

1. 调用函数 [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultConvertToPDF.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF/A 文件转换为 PDF 并保存为 "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将被转换的 PDF/A 文件的名称。

1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultConvertToPDF.pdf" 中。如果 json.errorCode 参数不为 0，并且您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*将 PDF/A 文件转换为 PDF 并保存为 "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```