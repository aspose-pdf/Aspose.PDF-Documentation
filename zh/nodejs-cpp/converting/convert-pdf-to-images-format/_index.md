---
title: 将 PDF 转换为 Node.js 中的图像格式
linktitle: 将 PDF 转换为图像
type: docs
weight: 70
url: /zh/nodejs-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-16"
description: 本主题向您展示如何在 Node.js 环境中使用 Aspose.PDF 将 PDF 转换为各种图像格式，例如 TIFF、BMP、JPEG、PNG、SVG，只需几行代码。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Node.js 将 PDF 转换为图像

在本文中，我们将向您展示将 PDF 转换为图像格式的选项。

以前扫描的文档通常以 PDF 文件格式保存。但是，您是否需要在图形编辑器中编辑它或进一步以图像格式发送？我们为您提供了一个通用工具，可以使用将 PDF 转换为图像。
最常见的任务是当您需要将整个 PDF 文档或文档的某些特定页面保存为一组图像时。
 **Aspose for Node.js via C++** 允许您将 PDF 转换为 JPG 和 PNG 格式，以简化从特定 PDF 文件获取图像的步骤。

**Aspose.PDF for Node.js via C++** 支持各种 PDF 到图像格式的转换。请查看 [Aspose.PDF 支持的文件格式](https://docs.aspose.com/pdf/nodejs-cpp/supported-file-formats/) 部分。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 JPEG**

Aspose.PDF for Node.js 为您提供免费的在线应用程序 ["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF conversion PDF to JPEG with Free App](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## 将 PDF 转换为 JPEG

如果您想转换 PDF 文档，可以使用 [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/) 函数。

请查看以下代码片段以在 Node.js 环境中进行转换。
**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定将要转换的PDF文件名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行文件转换操作。如果成功，将接收到对象。
1. 调用函数 [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/)。
1. 转换PDF文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPdfToJpg{0:D2}.jpg" 中。其中 {0:D2} 表示两位格式的页码。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不为 0，则文件中会出现错误，相应的错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将PDF文件转换为JPG，使用模板 "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率150 DPI并保存*/
      const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
      console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要转换的PDF文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestojpg/)。
1. 转换PDF文件。因此，如果 'json.errorCode' 是0，操作结果保存在 "ResultPdfToJpg{0:D2}.jpg" 中。其中 {0:D2} 表示两位数格式的页码。图像以150 DPI的分辨率保存。如果 json.errorCode 参数不是0，因此，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将PDF文件转换为JPG，使用模板 "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率150 DPI并保存*/
  const json = AsposePdfModule.AsposePdfPagesToJpg(pdf_file, "ResultPdfToJpg{0:D2}.jpg", 150);
  console.log("AsposePdfPagesToJpg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 TIFF**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，您可以在此尝试研究其功能和质量。

[![Aspose.PDF 转换 PDF 到 TIFF 免费应用程序](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## 将 PDF 转换为 TIFF

如果您想转换 PDF 文档，可以使用 [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/) 函数。
请检查以下代码片段，以便在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行文件转换操作。如果成功，接收对象。

1. 调用函数 [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 是 0，操作结果将保存在 "ResultPdfToTiff{0:D2}.tiff" 中。其中 {0:D2} 代表两位数格式的页码。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不是 0，并且相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 TIFF，使用模板 "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率 150 DPI 并保存*/
      const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
      console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestotiff/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPdfToTiff{0:D2}.tiff" 中。其中 {0:D2} 代表两位数字格式的页码。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不为 0，相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 TIFF，模板为 "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率为 150 DPI 并保存*/
  const json = AsposePdfModule.AsposePdfPagesToTiff(pdf_file, "ResultPdfToTiff{0:D2}.tiff", 150);
  console.log("AsposePdfPagesToTiff => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PNG**

作为我们免费应用程序工作方式的示例，请查看以下功能。

Aspose.PDF for Node.js 向您展示在线免费应用程序 ["PDF 转 PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，您可以尝试调查其功能和质量。

[![如何使用免费应用程序将 PDF 转换为 PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 将 PDF 转换为 PNG

如果您想转换 PDF 文档，可以使用 [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/) 函数。
请查看以下代码片段，以便在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块作为 `AsposePdf` 变量导入。
1. 指定将要转换的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行文件转换操作。如果成功，接收对象。

1. 调用函数 [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 是 0，操作结果将保存在 "ResultPdfToPng{0:D2}.png" 中。其中 {0:D2} 代表两位数字格式的页码。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不是 0，因此在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 PNG，使用模板 "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率 150 DPI 并保存*/
      const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
      console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功则接收对象。
1. 调用函数 [AsposePdfPagesToPng](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestopng/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPdfToPng{0:D2}.png" 中。其中 {0:D2} 表示两位数格式的页码。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不为 0，并且因此在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 PNG，模板为 "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率 150 DPI 并保存*/
  const json = AsposePdfModule.AsposePdfPagesToPng(pdf_file, "ResultPdfToPng{0:D2}.png", 150);
  console.log("AsposePdfPagesToPng => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 SVG**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 SVG](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**可缩放矢量图形 (SVG)** 是基于 XML 的二维矢量图形文件格式规范的家族，包括静态和动态（交互式或动画）。SVG 规范是一个开放标准，自 1999 年以来由万维网联盟 (W3C) 开发。

## 将 PDF 转换为 SVG

### 将 PDF 转换为经典 SVG

如果您想转换 PDF 文档，可以使用 [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/) 函数。
请查看以下代码片段以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，接收对象。
1. 调用函数 [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 是 0，操作结果将保存在 "ResultPdfToSvg.svg" 中。如果 json.errorCode 参数不是 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 SVG 并保存为 "ResultPdfToSvg.svg"*/
      const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
      console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要转换的PDF文件的名称。
1. 初始化AsposePdf模块。如果成功，接收该对象。
1. 调用函数 [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvg/)。
1. 转换PDF文件。因此，如果 'json.errorCode' 为0，操作结果将保存在 "ResultPdfToSvg.svg" 中。如果 json.errorCode 参数不为0，相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将PDF文件转换为SVG并保存为 "ResultPdfToSvg.svg"*/
  const json = AsposePdfModule.AsposePdfPagesToSvg(pdf_file, "ResultPdfToSvg.svg");
  console.log("AsposePdfPagesToSvg => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```

### 将PDF转换为压缩的SVG

如果您想转换PDF文档，可以使用 [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/) 函数。
 
请检查以下代码片段以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功则接收对象。
1. 调用函数 [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPdfToSvgZip.zip" 中。如果 json.errorCode 参数不为 0，则文件中会出现错误，相应的错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 SVG(zip) 并保存为 "ResultPdfToSvgZip.zip"*/
      const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
      console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestosvgzip/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPdfToSvgZip.zip" 中。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 SVG 压缩包并保存为 "ResultPdfToSvgZip.zip"*/
  const json = AsposePdfModule.AsposePdfPagesToSvgZip(pdf_file, "ResultPdfToSvgZip.zip");
  console.log("AsposePdfPagesToSvgZip => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText)
```

## 将 PDF 转换为 DICOM

如果您想转换 PDF 文档，可以使用 [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/) 函数。
 
请检查以下代码片段以便在 Node.js 环境中转换。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
2. 指定将要转换的 PDF 文件的名称。
3. 调用 `AsposePdf` 作为 Promise 并执行转换文件的操作。如果成功，接收对象。
4. 调用函数 [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/)。
5. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPdfToDICOM{0:D2}.dcm" 中。其中 {0:D2} 代表两位数字格式的页码。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 DICOM，模板为 "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率为 150 DPI 并保存*/
      const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
      console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要转换的 PDF 文件名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestodicom/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作的结果将保存在 "ResultPdfToDICOM{0:D2}.dcm" 中。其中 {0:D2} 表示两位数字格式的页码。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 DICOM，模板为 "ResultPdfToDICOM{0:D2}.dcm"（{0}, {0:D2}, {0:D3}, ... 格式页码），分辨率为 150 DPI 并保存*/
  const json = AsposePdfModule.AsposePdfPagesToDICOM(pdf_file, "ResultPdfToDICOM{0:D2}.dcm", 150);
  console.log("AsposePdfPagesToDICOM => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```


## 将 PDF 转换为 BMP

如果你想转换 PDF 文档，你可以使用 [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/) 函数。
请检查以下代码片段以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行文件转换操作。如果成功，则接收对象。
1. 调用函数 [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/)。

1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将被保存为 "ResultPdfToBmp{0:D2}.bmp"。其中 {0:D2} 表示两位数格式的页码。图像将以 150 DPI 的分辨率保存。如果 json.errorCode 参数不为 0，并且因此在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 BMP，使用模板 "ResultPdfToBmp{0:D2}.bmp"（{0}, {0:D2}, {0:D3}, ... 格式页码），分辨率为 150 DPI，并保存*/
      const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
      console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称。

1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfpagestobmp/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPdfToBmp{0:D2}.bmp" 中。其中 {0:D2} 表示页码，以两位数字格式表示。图像以 150 DPI 的分辨率保存。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 BMP，使用模板 "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率为 150 DPI 并保存*/
  const json = AsposePdfModule.AsposePdfPagesToBmp(pdf_file, "ResultPdfToBmp{0:D2}.bmp", 150);
  console.log("AsposePdfPagesToBmp => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```