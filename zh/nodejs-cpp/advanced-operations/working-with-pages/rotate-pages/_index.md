---

title: 在 Node.js 中旋转 PDF 页面  
linktitle: 旋转 PDF 页面  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/rotate-pages/  
description: 本主题介绍如何在 Node.js 环境中以编程方式旋转现有 PDF 文件的页面方向。  
lastmod: "2023-11-16"  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  

---

本节介绍如何使用 Aspose.PDF for Node.js via C++ 旋转现有 PDF 文件中的页面。

如果您想旋转 PDF 页面，可以使用 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) 函数。此函数使用一个特殊参数 'AsposePdfModule.Rotation' 作为旋转值。您可以设置需要旋转 PDF 的度数。有以下选项：无、90、180 或 270 度。

请查看以下代码片段以在 Node.js 环境中旋转 PDF 页面。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。

1. 指定要旋转的PDF文件名称。
1. 调用 `AsposePdf` 作为 Promise 并执行旋转页面的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/)。
1. 旋转所有PDF文件。旋转设置为270度（on270）。因此，如果 'json.errorCode' 为0，操作结果保存在 "ResultRotation.pdf" 中。如果 json.errorCode 参数不为0，则在文件中出现错误，相应的错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*旋转PDF页面并保存为 "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要旋转的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/)。
1. 旋转所有 PDF 文件。旋转设置为 270 度 (on270)。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultRotation.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*旋转 PDF 页面并保存为 "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```