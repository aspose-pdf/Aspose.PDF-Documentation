---
title: 在 Node.js 中添加 PDF 页眉和页脚
linktitle: 添加 PDF 页眉和页脚
type: docs
weight: 70
url: zh/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Node.js via C++ 允许您使用 AsposePdfAddTextHeaderFooter 向 PDF 文件添加页眉和页脚。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js via C++** 允许您在现有的 PDF 文件中添加页眉和页脚。

如果您想添加页眉和页脚，可以使用 [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/) 函数。

请查看以下代码片段，以便在 Node.js 环境中向 PDF 文件添加页眉和页脚。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定将添加页眉和页脚的 PDF 文件的名称。

1. 调用 `AsposePdf` 作为 Promise 并执行添加页眉和页脚的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/)。
1. 在 PDF 文件的页眉和页脚中添加文本。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultAddHeaderFooter.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*在 PDF 文件的页眉/页脚中添加文本并保存为 "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要添加页眉和页脚的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/)。
1. 在 PDF 文件的页眉和页脚中添加文本。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultAddHeaderFooter.pdf" 中。如果 json.errorCode 参数不为 0，并且因此在文件中出现错误，则错误信息将包含在 'json.errorText'。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*在 PDF 文件的页眉/页脚中添加文本并保存为 "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```