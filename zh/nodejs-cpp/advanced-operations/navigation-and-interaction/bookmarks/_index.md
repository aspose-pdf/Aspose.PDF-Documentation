---
title: 在 Node.js 中的 PDF 书签
linktitle: PDF 中的书签
type: docs
weight: 10
url: zh/nodejs-cpp/bookmark/
description: 您可以在 Node.js 环境中添加或删除 PDF 文档中的书签。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档中删除特定书签

您可以使用 Aspose.PDF for Node.js via C++ 从 PDF 文件中删除书签。如果您想从 PDF 中删除书签，可以使用 [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) 函数。
请查看以下代码片段，以便在 Node.js 环境中从 PDF 文件中删除书签。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定要从中删除书签的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行删除书签的操作。如果成功，则接收对象。

1. 调用函数 [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/)。
1. 删除书签。因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultPdfDeleteBookmarks.pdf"。如果 json.errorCode 参数不为 0，并且您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*从 PDF 文件中删除书签并保存为 "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将移除书签的 PDF 文件的名称。

1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/)。
1. 删除书签。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPdfDeleteBookmarks.pdf" 中。如果 json.errorCode 参数不为 0，并且您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*从 PDF 文件中删除书签并保存为 "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```