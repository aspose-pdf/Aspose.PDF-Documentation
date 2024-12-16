---
title: 从PDF中移除附件在Node.js中
linktitle: 从现有PDF中移除附件
type: docs
weight: 10
url: /zh/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF 可以从您的PDF文档中移除附件。使用Node.js环境通过Aspose.PDF移除PDF文件中的附件。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

您可以使用Aspose.PDF for Node.js via C++从PDF文件中删除附件。如果您想从PDF中删除附件，可以使用[AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/)函数。
请查看以下代码片段以便在Node.js环境中从PDF文件中删除附件。

**CommonJS:**

1. 调用`require`并将`asposepdfnodejs`模块导入为`AsposePdf`变量。
2. 指定要从中移除附件的PDF文件的名称。

1. 调用 `AsposePdf` 作为 Promise 并执行删除附件的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/)。
1. 删除附件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPdfDeleteAttachments.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*从 PDF 文件中删除附件并保存为 "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要删除附件的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/)。
1. 删除附件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPdfDeleteAttachments.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*从 PDF 文件中删除附件并保存为 "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```