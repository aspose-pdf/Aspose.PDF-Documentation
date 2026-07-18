---
title: 在 Node.js 中 处理 PDF 文件 元数据
linktitle: PDF 文件元数据
type: docs
weight: 130
url: /zh/nodejs-cpp/pdf-file-metadata/
description: 本节介绍如何获取 PDF 文件信息、如何从 PDF 文件获取元数据、以及如何在 Node.js 中设置 PDF 文件信息。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取 PDF 文件信息

如果您想获取 PDF 文件信息，您可以使用 [AsposePdf获取信息](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) 函数。 
请检查以下代码片段，以在 Node.js 环境中获取 PDF 文件信息。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要提取信息的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行提取信息的操作。如果成功，接收该对象。
1. 调用函数 [AsposePdf获取信息](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. 提取的元数据存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，则使用 console.log 显示提取的元数据。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get info (metadata) from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Title             : json.title
        Creator           : json.creator
        Author            : json.author
        Subject           : json.subject
        Keywords          : json.keywords
        Creation Date     : json.creation
        Modify Date       : json.mod
        PDF format        : json.format
        PDF version       : json.version
        PDF is PDF/A      : json.ispdfa
        PDF is PDF/UA     : json.ispdfua
        PDF is linearized : json.islinearized
        PDF is encrypted  : json.isencrypted
        PDF permission    : json.permission
        PDF page size     : json.size
        Page count        : json.pagecount
        Annotation count  : json.annotationcount
        Bookmark count    : json.bookmarkcount
        Attachment count  : json.attachmentcount
        Metadata count    : json.metadatacount
        JavaScript count  : json.javascriptcount
        Image count       : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要提取信息的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdf获取信息](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. 提取的元数据存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，则使用 console.log 显示提取的元数据。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Get info (metadata) from a PDF-file*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Title             : json.title
      Creator           : json.creator
      Author            : json.author
      Subject           : json.subject
      Keywords          : json.keywords
      Creation Date     : json.creation
      Modify Date       : json.mod
      PDF format        : json.format
      PDF version       : json.version
      PDF is PDF/A      : json.ispdfa
      PDF is PDF/UA     : json.ispdfua
      PDF is linearized : json.islinearized
      PDF is encrypted  : json.isencrypted
      PDF permission    : json.permission
      PDF page size     : json.size
      Page count        : json.pagecount
      Annotation count  : json.annotationcount
      Bookmark count    : json.bookmarkcount
      Attachment count  : json.attachmentcount
      Metadata count    : json.metadatacount
      JavaScript count  : json.javascriptcount
      Image count       : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```

## 获取所有字体

从 PDF 文件中获取字体是一种在其他文档或应用程序中重复使用字体的有用方式。 

如果您想从 PDF 文件中获取字体，可以使用 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) 函数。 
请检查以下代码片段，以在 Node.js 环境中从 PDF 文件获取字体。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要从中提取字体的 PDF 文件名称。
1. 调用 `AsposePdf` 作为 Promise 并执行提取字体的操作。成功时接收对象。
1. 调用函数 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. 提取的字体存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，则使用 console.log 显示一个包含字体详细信息的数组，包括字体名称、是否嵌入以及其可访问性状态。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get list fonts from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要从中提取字体的 PDF 文件名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. 提取的字体存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，则使用 console.log 显示一个包含字体详细信息的数组，包括字体名称、是否嵌入以及其可访问性状态。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Get list fonts from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## 设置 PDF 文件信息

Aspose.PDF for Node.js via C++ 允许您为 PDF 设置特定于文件的信息，例如作者、创建日期、主题和标题。要设置这些信息：

如果您想设置特定于文件的信息，您可以使用 [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) 函数。 
请检查以下代码片段，以在 Node.js 环境中设置文件信息。

可以设置： 
- 标题
- 创建者
- 作者
- 主题
- 列出关键字
- 创建日期
- 修改日期
- 结果文件名

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将设置信息的 PDF 文件名。
1. 调用 `AsposePdf` 作为 Promise 并执行该操作。成功时接收对象。
1. 调用函数 [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. 设置 PDF 文件信息。标题、创建者、作者、主题、关键词、创建日期和修改日期等信息作为参数提供。因此，如果 'json.errorCode' 为 0，则操作结果将保存在 \"ResultSetInfo.pdf\" 中。如果 json.errorCode 参数不为 0，且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*If not need to set value, use undefined or "" (empty string)*/
      /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将设置信息的 PDF 文件名。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. 设置 PDF 文件信息。标题、创建者、作者、主题、关键词、创建日期和修改日期等信息作为参数提供。因此，如果 'json.errorCode' 为 0，则操作结果将保存在 \"ResultSetInfo.pdf\" 中。如果 json.errorCode 参数不为 0，且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*If not need to set value, use undefined or "" (empty string)*/
  /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## 删除 PDF 文件信息

Aspose.PDF for Node.js via C++ 允许您删除 PDF 文件元数据：

如果您想要删除 PDF 中的元数据，您可以使用 [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) 函数。 
请检查以下代码片段，以在 Node.js 环境中删除 PDF 的元数据。

**CommonJS:**

1. 需要 AsposePDFforNode.js 模块。
1. 指定要从中删除信息的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. 删除 PDF 文件信息。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPdfRemoveMetadata.pdf"。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要从中删除信息的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. 删除 PDF 文件信息。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPdfRemoveMetadata.pdf"。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```