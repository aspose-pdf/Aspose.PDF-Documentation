---
title: 在 Node.js 中删除注释
linktitle: 删除注释
type: docs
weight: 10
url: /zh/nodejs-cpp/delete-annotation/
description: 使用 Aspose.PDF for Node.js，您可以从 PDF 文件中删除注释。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

您可以使用 Aspose.PDF for Node.js via C++ 删除 PDF 文件中的注释。如果您想删除 PDF 中的注释，可以使用 [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/) 函数。 
请检查下面的代码片段，以在 Node.js 环境中删除 PDF 文件的批注。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要删除批注的 PDF 文件名称。
1. 调用 `AsposePdf` 作为 Promise 并执行删除注释的操作。如果成功，接收该对象。
1. 调用函数 [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. 删除注释。因此，如果 'json.errorCode' 为 0，操作的结果将保存在 "ResultPdfDeleteAnnotations.pdf" 中。如果 json.errorCode 参数不为 0，并相应地在你的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要删除批注的 PDF 文件名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. 删除注释。因此，如果 'json.errorCode' 为 0，操作的结果将保存在 "ResultPdfDeleteAnnotations.pdf" 中。如果 json.errorCode 参数不为 0，并相应地在你的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```
