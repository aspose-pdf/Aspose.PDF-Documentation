---
title: 在 Node.js 中从 PDF 文件删除图像
linktitle: 删除图像
type: docs
weight: 20
url: /zh/nodejs-cpp/delete-images-from-pdf-file/
description: 本节说明如何使用 Aspose.PDF for Node.js via C++ 从 PDF 文件中删除图像。
lastmod: "2026-07-18"
---


您可以使用 Aspose.PDF for Node.js via C++ 删除 PDF 文件中的图像。

如果您想从 PDF 中删除图像，您可以使用 [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) 函数。 
请检查以下代码片段，以在 Node.js 环境中删除图像。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要删除图像的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行删除图像的操作。成功时接收对象。
1. 调用函数 [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. 从 PDF 中删除图像。因此，如果 'json.errorCode' 为 0，则操作结果将保存为 "ResultPdfDeleteImages.pdf"。如果 json.errorCode 参数不为 0，且相应地在文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要删除图像的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. 从 PDF 中删除图像。因此，如果 'json.errorCode' 为 0，则操作结果将保存为 "ResultPdfDeleteImages.pdf"。如果 json.errorCode 参数不为 0，且相应地在文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```