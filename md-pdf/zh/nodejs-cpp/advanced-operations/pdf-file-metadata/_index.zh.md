---
title: 使用 Node.js 处理 PDF 文件元数据
linktitle: PDF 文件元数据
type: docs
weight: 130
url: /nodejs-cpp/pdf-file-metadata/
description: 本节解释如何获取 PDF 文件信息、如何从 PDF 文件中获取元数据、在 Node.js 中设置 PDF 文件信息。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取 PDF 文件信息

如果您想获取 PDF 文件信息，可以使用 [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) 函数。
请查看以下代码片段，以获取 Node.js 环境中的 PDF 文件信息。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定将从中提取信息的 PDF 文件的名称。
1. 将 `AsposePdf` 调用为 Promise 并执行提取信息的操作。如果成功，接收对象。

1. 调用函数 [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/)。
1. 提取的元数据存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，则使用 console.log 显示提取的元数据。如果 json.errorCode 参数不为 0，并且相应地，文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*从 PDF 文件获取信息（元数据）*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        标题             : json.title
        创建者           : json.creator
        作者             : json.author
        主题             : json.subject
        关键词           : json.keywords
        创建日期         : json.creation
        修改日期         : json.mod
        PDF 格式         : json.format
        PDF 版本         : json.version
        PDF 是否为 PDF/A : json.ispdfa
        PDF 是否为 PDF/UA: json.ispdfua
        PDF 是否线性化   : json.islinearized
        PDF 是否加密     : json.isencrypted
        PDF 权限         : json.permission
        PDF 页面大小     : json.size
        页数             : json.pagecount
        注释数           : json.annotationcount
        书签数           : json.bookmarkcount
        附件数           : json.attachmentcount
        元数据数量       : json.metadatacount
        JavaScript 数量  : json.javascriptcount
        图像数量         : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要从中提取信息的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/)。
1. 提取的元数据存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，则使用 console.log 显示提取的元数据。如果 json.errorCode 参数不为 0，并且相应地在文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*从 PDF 文件中获取信息（元数据）*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      标题             : json.title
      创建者           : json.creator
      作者             : json.author
      主题             : json.subject
      关键词           : json.keywords
      创建日期         : json.creation
      修改日期         : json.mod
      PDF 格式         : json.format
      PDF 版本         : json.version
      PDF 是 PDF/A    : json.ispdfa
      PDF 是 PDF/UA   : json.ispdfua
      PDF 是线性化的  : json.islinearized
      PDF 是加密的    : json.isencrypted
      PDF 权限        : json.permission
      PDF 页面大小    : json.size
      页数            : json.pagecount
      注释数          : json.annotationcount
      书签数          : json.bookmarkcount
      附件数          : json.attachmentcount
      元数据数        : json.metadatacount
      JavaScript 数量 : json.javascriptcount
      图像数          : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```


## 获取所有字体

从 PDF 文件中获取字体可以是一种在其他文档或应用程序中重用字体的有用方法。

如果你想从 PDF 文件中获取字体，可以使用 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) 函数。请查看以下代码片段，以便在 Node.js 环境中从 PDF 文件中获取字体。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块作为 `AsposePdf` 变量。
1. 指定要从中提取字体的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行提取字体的操作。如果成功，则接收对象。
1. 调用函数 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/)。

1. 提取的字体存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，它将显示一个字体详细信息的数组，包括字体名称、是否嵌入以及其可访问状态，使用 console.log。如果 json.errorCode 参数不为 0，并且相应地在文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*从 PDF 文件中获取字体列表*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - 字体数组：{ fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将从中提取字体的 PDF 文件的名称。

1. 初始化 AsposePdf 模块。成功时接收对象。
1. 调用函数 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/)。
1. 提取的字体存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，它会显示一个字体详细信息的数组，包括字体名称、是否嵌入以及其可访问性状态，使用 console.log。如果 json.errorCode 参数不为 0，并且在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*从 PDF 文件中获取字体列表*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - 字体数组: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## 设置 PDF 文件信息


Aspose.PDF for Node.js via C++允许您为PDF设置特定于文件的信息，例如作者、创建日期、主题和标题。要设置此信息：

如果您想设置特定于文件的信息，可以使用[AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/)函数。
请检查以下代码片段，以便在Node.js环境中设置文件信息。

可以设置：
- 标题
- 创建者
- 作者
- 主题
- 列出关键词
- 创建日期
- 修改日期
- 结果文件名

**CommonJS:**

1. 调用`require`并将`asposepdfnodejs`模块导入为`AsposePdf`变量。
1. 指定将设置信息的PDF文件的名称。
1. 将`AsposePdf`作为Promise调用并执行操作。如果成功，则接收对象。
1. 调用函数[AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/)。

1. 设置 PDF 文件信息。信息如标题、创建者、作者、主题、关键词、创建日期和修改日期作为参数提供。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultSetInfo.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*设置 PDF 信息：标题、创建者、作者、主题、关键词、创建日期、修改日期*/
      /*如果不需要设置值，使用 undefined 或 ""（空字符串）*/
      /*在 PDF 文件中设置信息（元数据）并保存为 "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要设置信息的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/)。
1. 设置 PDF 文件信息。标题、创建者、作者、主题、关键词、创建日期和修改日期等信息作为参数提供。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultSetInfo.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地在文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*设置 PDF 信息：标题，创建者，作者，主题，关键词，创建（日期），修改（日期修改）*/
  /*如果不需要设置值，使用 undefined 或 ""（空字符串）*/
  /*在 PDF 文件中设置信息（元数据）并保存为 "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


## 删除 PDF 文件信息

Aspose.PDF for Node.js via C++ 允许您删除 PDF 文件的元数据：

如果您想从 PDF 中删除元数据，可以使用 [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) 函数。
请查看以下代码片段，以便在 Node.js 环境中从 PDF 中删除元数据。

**CommonJS:**

1. 引入 AsposePDFforNode.js 模块。
1. 指定要删除信息的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如成功，接收对象。
1. 调用函数 [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/)。
1. 删除 PDF 文件信息。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPdfRemoveMetadata.pdf" 中。如果 json.errorCode 参数不为 0，则相应地，您的文件中会出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*从 PDF 文件中删除元数据并保存为 "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
2. 指定要从中删除信息的 PDF 文件的名称。
3. 初始化 AsposePdf 模块。如果成功，接收对象。
4. 调用函数 [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/)。
5. 删除 PDF 文件信息。因此，如果 'json.errorCode' 为 0，则操作结果将保存在 "ResultPdfRemoveMetadata.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*从 PDF 文件中删除元数据并保存为 "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```