---
title: 将PDF转换为图像格式在JavaScript中
linktitle: 将PDF转换为图像
type: docs
weight: 70
url: /zh/javascript-cpp/convert-pdf-to-images-format/
lastmod: "2023-11-01"
description: 本主题向您展示如何使用Aspose.PDF将PDF转换为多种图像格式，例如TIFF、BMP、JPEG、PNG、SVG，仅需几行代码。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## JavaScript将PDF转换为图像

在本文中，我们将向您展示将PDF转换为图像格式的选项。

以前扫描的文档通常以PDF文件格式保存。然而，您是否需要在图形编辑器中编辑它或以图像格式进一步发送？我们为您提供了一个通用工具，可以使用将PDF转换为图像。
最常见的任务是当您需要将整个PDF文档或文档的某些特定页面保存为一组图像时。**通过C++的Aspose for JavaScript**允许您将PDF转换为JPG和PNG格式，以简化从特定PDF文件获取图像所需的步骤。

**通过C++的Aspose.PDF for JavaScript**支持各种PDF到图像格式的转换。
 请检查[Aspose.PDF 支持的文件格式](https://docs.aspose.com/pdf/javascript-cpp/supported-file-formats/)部分。

转换操作取决于文档中的页数，可能非常耗时。因此，我们强烈建议使用Web Workers。

此代码演示了一种将资源密集型PDF文件转换任务卸载到Web Worker的方法，以防止阻塞主UI线程。它还提供了一种用户友好的方式来下载转换后的文件。

{{% alert color="success" %}}
**尝试在线将PDF转换为JPEG**

Aspose.PDF for JavaScript为您提供了在线免费应用程序["PDF to JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF转换PDF为JPEG与免费应用程序](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## 将PDF转换为JPEG

```js

  /*创建Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自Web Worker的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '加载完成!' :
        (evt.data.json.errorCode == 0) ? 
          `文件(页)数量: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffileToJpg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*将PDF文件转换为模板为"ResultPdfToJpg{0:D2}.jpg"的jpg文件({0}, {0:D2}, {0:D3}, ...格式页码)，分辨率150 DPI并保存 - 请求Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToJpg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [代码片段]

    /*创建链接以下载结果文件*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "点击这里下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

以下的JavaScript代码片段展示了一个将PDF页面转换为Jpeg文件的简单示例：

1. 选择一个PDF文件进行转换。
2. 创建一个'FileReader'。
3. 执行[AsposePdfPagesToJpg](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestojpg/)函数。
4. 设置生成文件的名称，在此示例中为"ResultPdfToJpg{0:D2}.jpg"。
5. 接下来，如果'json.errorCode'为0，则结果文件将被赋予您之前指定的名称。如果'json.errorCode'参数不等于0，因此文件中会有错误信息，这样的错误信息将包含在'json.errorText'文件中。
6. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

  var ffileToJpg = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将PDF文件转换为jpg文件，模板为“ResultPdfToJpg{0:D2}.jpg”（{0}、{0:D2}、{0:D3}等格式页码），分辨率为150 DPI并保存*/
      const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "文件（页面）数量: " + json.filesCount.toString();
        /*生成链接到结果文件*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 TIFF**

Aspose.PDF for JavaScript 为您提供免费在线应用程序 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，您可以尝试调查其功能和质量。

[![Aspose.PDF 转换 PDF 为 TIFF 免费应用](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## 将 PDF 转换为 TIFF

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载！' :
        (evt.data.json.errorCode == 0) ? 
          `文件（页面）数量: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/tiff", element) ) ?? ""}` : 
          `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffileToTiff = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF 文件转换为 TIFF，使用模板 "ResultPdfToTiff{0:D2}.tiff" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率150 DPI并保存 - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToTiff', "params": [event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*创建下载结果文件的链接*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "点击这里下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下 JavaScript 代码片段展示了将 PDF 页面转换为 Tiff 文件的简单示例：

1. 选择一个要转换的 PDF 文件。
2. 创建一个 'FileReader'。
3. 执行 [AsposePdfPagesToTiff](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestotiff/) 函数。
4. 设置生成文件的名称，在此示例中为 "ResultPdfToTiff{0:D2}.tiff"。
5. 接下来，如果 'json.errorCode' 为 0，那么您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，那么您的文件中会有错误，关于此类错误的信息将包含在 'json.errorText' 文件中。
6. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffileToTiff = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*使用模板 "ResultPdfToTiff{0:D2}.tiff"（{0}, {0:D2}, {0:D3}, ... 格式页码），分辨率 150 DPI 转换 PDF 文件为 TIFF 并保存*/
        const json = AsposePdfPagesToTiff(event.target.result, e.target.files[0].name, "ResultPdfToTiff{0:D2}.tiff", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "文件（页面）数量: " + json.filesCount.toString();
          /*为结果文件创建链接*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/tiff");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PNG**

作为我们免费应用程序如何工作的示例，请查看下一个功能。

Aspose.PDF for JavaScript 为您提供在线免费应用程序 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，您可以尝试研究其功能和工作质量。

[![如何使用免费应用将 PDF 转换为 PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 将 PDF 转换为 PNG

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '加载完成!' :
        (evt.data.json.errorCode == 0) ? 
          `文件（页面）计数: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/png", element) ) ?? ""}` : 
          `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileToPng = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*将 PDF 文件转换为 png 文件，模板为 "ResultPdfToPng{0:D2}.png"（{0}, {0:D2}, {0:D3}, ... 格式页码），分辨率为 150 DPI 并保存 - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToPng', "params": [event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [代码片段]

    /*创建一个链接以下载结果文件*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "点击这里下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下JavaScript代码片段展示了将PDF页面转换为PNG文件的简单示例：

1. 选择一个PDF文件进行转换。
1. 创建一个'FileReader'。
1. 执行[AsposePdfPagesToPng](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestopng/)函数。
1. 结果文件的名称被设置为，在此示例中是"ResultPdfToPng{0:D2}.png"。
1. 接下来，如果'json.errorCode'为0，则您的DownloadFile会被赋予您之前指定的名称。如果'json.errorCode'参数不等于0，则您的文件中会出现错误，此类错误信息将包含在'json.errorText'文件中。
1. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)函数生成一个链接，并允许您将结果文件下载到用户的操作系统。

```js

  var ffileToPng = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将PDF文件转换为png文件，模板为"ResultPdfToPng{0:D2}.png"（{0}, {0:D2}, {0:D3}, ... 格式页码），分辨率150 DPI并保存*/
      const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "文件（页）数量: " + json.filesCount.toString();
        /*创建结果文件的链接*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/png");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```


{{% alert color="success" %}}
**尝试在线将PDF转换为SVG**

Aspose.PDF for JavaScript 为您提供在线免费应用程序["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 SVG 免费应用](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**可缩放矢量图形 (SVG)** 是一种基于 XML 的文件格式的二维矢量图形的规范家族，既包括静态也包括动态（交互或动画）图形。SVG 规范是一种开放标准，自 1999 年以来一直由万维网联盟 (W3C) 开发。

## 将 PDF 转换为 SVG

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? 
          `文件(页面)数量: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/svg", element) ) ?? ""}` : 
          `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileToSvg = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将PDF文件转换为SVG - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvg', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*创建一个链接以下载结果文件*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "点击这里下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下 JavaScript 代码片段展示了将 PDF 页面转换为 SVG 文件的简单示例：

1. 选择一个 PDF 文件进行转换。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfPagesToSvg](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvg/) 函数。
1. 设置生成文件的名称，在本例中为 "ResultPdfToSvg.svg"。
1. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，并且相应地，您的文件中会有错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。
1. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js
var ffileToSvg = function (e) {
  const file_reader = new FileReader();
  file_reader.onload = (event) => {
    /*将 PDF 文件转换为 SVG*/
    const json = AsposePdfPagesToSvg(event.target.result, e.target.files[0].name, "ResultPdfToSvg.svg");
    if (json.errorCode == 0) {
      document.getElementById('output').textContent = "文件（页面）数量: " + json.filesCount.toString();
      /*创建结果文件的链接*/
      for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/svg");
    }
    else document.getElementById('output').textContent = json.errorText;
  }
  file_reader.readAsArrayBuffer(e.target.files[0]);
}
```


### 将PDF转换为压缩SVG

```js

  /*创建Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Worker错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/zip", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffileToSvgZip = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将PDF文件转换为SVG(zip)并保存为"ResultPdfToSvgZip.zip" - 请求Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToSvgZip', "params": [event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*创建链接以下载结果文件*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "点击这里下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下的JavaScript代码片段展示了将PDF页面转换为SVG(zip)文件的简单示例：

1. 选择一个PDF文件进行转换。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfPagesToSvgZip](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestosvgzip/) 函数。
1. 结果文件的名称被设置，在此示例中为 "ResultPdfToSvgZip.zip"。
1. 接下来，如果 'json.errorCode' 为0，那么你的 DownloadFile 将被赋予你之前指定的名称。如果 'json.errorCode' 参数不等于0，那么文件中将有一个错误，关于此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许你将结果文件下载到用户的操作系统。

```js

    var ffileToSvgZip = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*将PDF文件转换为SVG(zip)并保存为 "ResultPdfToSvgZip.zip"*/
        const json = AsposePdfPagesToSvgZip(event.target.result, e.target.files[0].name, "ResultPdfToSvgZip.zip");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## 将 PDF 转换为 DICOM

```js

  /*创建 Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '已加载!' :
      (evt.data.json.errorCode == 0) ?
        `文件（页）数量: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
          (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "application/dicom", element) ) ?? ""}` :
        `错误: ${evt.data.json.errorText}`;

  /*事件处理程序*/
  const ffileToDICOM = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*将 PDF 文件转换为 DICOM，使用模板 "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率 150 DPI 并保存 - 请求 Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToDICOM', "params": [event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*创建一个链接以下载结果文件*/
  const DownloadFile = (filename, mime, content) => {
      mime = mime || "application/octet-stream";
      var link = document.createElement("a"); 
      link.href = URL.createObjectURL(new Blob([content], {type: mime}));
      link.download = filename;
      link.innerHTML = "点击这里下载文件 " + filename;
      document.body.appendChild(link); 
      document.body.appendChild(document.createElement("br"));
      return filename;
    }
```


以下的 JavaScript 代码片段展示了一个将 PDF 页面转换为 DICOM 文件的简单示例：

1. 选择一个 PDF 文件进行转换。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfPagesToDICOM](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestodicom/) 函数。
1. 设置生成文件的名称，在这个例子中为 "ResultPdfToDICOM{0:D2}.dcm"。
1. 接下来，如果 'json.errorCode' 为 0，那么生成的文件将被赋予你之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此在你的文件中会有一个错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果是，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许你将生成的文件下载到用户的操作系统。

```js

  var ffileToDICOM = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将 PDF 文件转换为 DICOM，模板为 "ResultPdfToDICOM{0:D2}.dcm" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率为 150 DPI 并保存*/
      const json = AsposePdfPagesToDICOM(event.target.result, e.target.files[0].name, "ResultPdfToDICOM{0:D2}.dcm", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "文件（页面）数量: " + json.filesCount.toString();
        /*创建结果文件的链接*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "application/dicom");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## 将 PDF 转换为 BMP

```js

    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? 
          `文件(页)数量: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/bmp", element) ) ?? ""}` : 
          `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileToBmp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF 文件转换为 BMP，使用模板 "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率为 150 DPI 并保存 - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPagesToBmp', "params": [event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*创建一个链接以下载结果文件*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "点击这里下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下的 JavaScript 代码片段展示了将 PDF 页面转换为 BMP 文件的简单示例：

1. 选择一个 PDF 文件进行转换。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfPagesToBmp](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfpagestobmp/) 函数。
1. 设置生成文件的名称，在此示例中为 "ResultPdfToBmp{0:D2}.bmp"。
1. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此您的文件中会出现错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统中。

```js

    var ffileToBmp = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*将 PDF 文件转换为 BMP，模板为 "ResultPdfToBmp{0:D2}.bmp" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率为 150 DPI 并保存*/
        const json = AsposePdfPagesToBmp(event.target.result, e.target.files[0].name, "ResultPdfToBmp{0:D2}.bmp", 150);
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "文件（页）数： " + json.filesCount.toString();
          /*生成结果文件的链接*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/bmp");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```