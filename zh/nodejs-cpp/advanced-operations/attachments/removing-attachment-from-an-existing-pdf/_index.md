---
title: 在 Node.js 中从 PDF 中移除附件
linktitle: 从现有 PDF 中移除附件
type: docs
weight: 10
url: /zh/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF 可以从您的 PDF 文档中移除附件。使用 Node.js 环境通过 Aspose.PDF 移除 PDF 文件中的附件。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

您可以使用 Aspose.PDF for Node.js via C++ 删除 PDF 文件中的附件。 如果您想删除 PDF 中的附件，可以使用 [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) 函数。 
请查看以下代码片段，以在 Node.js 环境中删除 PDF 文件的附件。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要删除附件的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行删除附件的操作。成功时接收该对象。
1. 调用函数 [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. 删除附件。因此，如果 ‘json.errorCode’ 为 0，则操作结果保存在 “ResultPdfDeleteAttachments.pdf” 中。如果 json.errorCode 参数不为 0，因而在文件中出现错误，则错误信息将包含在 ‘json.errorText’ 中。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要删除附件的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. 删除附件。因此，如果 ‘json.errorCode’ 为 0，则操作结果保存在 “ResultPdfDeleteAttachments.pdf” 中。如果 json.errorCode 参数不为 0，因而在文件中出现错误，则错误信息将包含在 ‘json.errorText’ 中。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```