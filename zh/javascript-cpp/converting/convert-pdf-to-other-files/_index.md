---
title: 将PDF转换为EPUB、TeX、Text、XPS格式在JavaScript中
linktitle: 将PDF转换为其他格式
type: docs
weight: 90
url: zh/javascript-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-01"
keywords: convert, PDF, EPUB, TeX, Text, XPS, JavaScript
description: 本主题向您展示如何使用JavaScript将PDF文件转换为其他文件格式，如EPUB、LaTeX、Text、XPS等。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

转换操作取决于文档中的页数，可能非常耗时。因此，我们强烈建议使用Web Workers。

此代码演示了一种将资源密集型PDF文件转换任务卸载到Web Worker的方法，以防止阻塞主UI线程。它还提供了一种用户友好的方式来下载转换后的文件。

{{% alert color="success" %}}
**尝试在线将PDF转换为EPUB**

Aspose.PDF for JavaScript为您提供在线免费应用程序["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 EPUB 免费应用](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## 转换 PDF 到 EPUB

**<abbr title="电子出版物">EPUB</abbr>** 是国际数字出版论坛 (IDPF) 的一个免费和开放的电子书标准。文件具有 .epub 扩展名。  
EPUB 旨在用于可重排内容，这意味着 EPUB 阅读器可以为特定的显示设备优化文本。EPUB 还支持固定布局内容。该格式被设想为出版商和转换公司可以在内部使用的单一格式，同时也用于分发和销售。它取代了开放电子书标准。

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载！' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/epub+zip", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffileToEPUB = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF 文件转换为 ePub 并保存为 "ResultPDFtoEPUB.epub" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToEPUB', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*创建一个链接以下载结果文件*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "单击此处下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```


以下是一个将PDF页面转换为EPUB文件的简单JavaScript代码示例：

1. 选择一个PDF文件进行转换。
2. 创建一个'FileReader'。
3. 执行[AsposePdfToEPUB](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoepub/)函数。
4. 设置生成文件的名称，在此示例中为"ResultPDFtoEPUB.epub"。
5. 接下来，如果'json.errorCode'为0，则生成的文件将被赋予您之前指定的名称。如果'json.errorCode'参数不等于0，并且因此您的文件中会有错误，则此类错误的信息将包含在'json.errorText'文件中。
6. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffileToEPUB = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*将PDF文件转换为EPUB并保存为"ResultPDFtoEPUB.epub"*/
        const json = AsposePdfToEPUB(event.target.result, e.target.files[0].name, "ResultPDFtoEPUB.epub");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/epub+zip");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for JavaScript 为您提供在线免费应用程序 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 LaTeX/TeX 免费应用程序](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## 将 PDF 转换为 TeX

**Aspose.PDF for JavaScript** 支持将 PDF 转换为 TeX。
LaTeX 文件格式是一种具有特殊标记的文本文件格式，用于基于 TeX 的文档准备系统中，以实现高质量的排版。

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '加载完成!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/x-tex", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileToTeX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF 文件转换为 TeX 并保存为 "ResultPDFtoTeX.tex" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTeX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex"] }, [event.target.result]);
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


以下的 JavaScript 代码片段展示了将 PDF 页转换为 TEX 文件的简单示例：

1. 选择要转换的 PDF 文件。
2. 创建一个 'FileReader'。
3. 执行 [AsposePdfToTeX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotex/) 函数。
4. 设置生成文件的名称，在此示例中为 "ResultPDFtoTeX.tex"。
5. 接下来，如果 'json.errorCode' 为 0，那么您的结果文件将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，并且相应地，您的文件中会出现错误，那么有关此类错误的信息将包含在 'json.errorText' 文件中。
6. 最终， [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffileToTeX = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*将 PDF 文件转换为 TeX 并保存为 "ResultPDFtoTeX.tex"*/
        const json = AsposePdfToTeX(event.target.result, e.target.files[0].name, "ResultPDFtoTeX.tex");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/x-tex");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为文本**

Aspose.PDF for JavaScript 为您提供在线免费应用程序 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以在此尝试调查其功能和质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为文本](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 TXT

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "text/plain", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileToTxt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF 文件转换为 Txt 并保存为 "ResultPDFtoTxt.txt" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToTxt', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt"] }, [event.target.result]);
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


以下的 JavaScript 代码片段展示了将 PDF 页面转换为 TXT 文件的简单示例：

1. 选择一个要转换的 PDF 文件。
2. 创建一个 'FileReader'。
3. 执行 [AsposePdfToTxt](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftotxt/) 函数。
4. 设置结果文件的名称，在此示例中为 "ResultPDFtoTxt.txt"。
5. 接下来，如果 'json.errorCode' 是 0，则结果文件将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，那么您的文件中将会有一个错误，此类错误的信息将包含在 'json.errorText' 文件中。
6. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将结果文件下载到用户的操作系统。

```js

    var ffileToTxt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*将 PDF 文件转换为 Txt 并保存为 "ResultPDFtoTxt.txt"*/
        const json = AsposePdfToTxt(event.target.result, e.target.files[0].name, "ResultPDFtoTxt.txt");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "text/plain");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for JavaScript 为您提供免费在线应用程序 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 XPS 免费应用](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## 将 PDF 转换为 XPS

XPS 文件类型主要与微软公司的 XML Paper Specification 关联。XML Paper Specification (XPS)，以前代号为 Metro，包含下一代打印路径 (NGPP) 营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的倡议。

**Aspose.PDF for JavaScript** 提供了将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式的可能性。让我们尝试使用所提供的代码片段将 PDF 文件转换为 XPS 格式。

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '加载完成!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.ms-xpsdocument", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileToXps = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF 文件转换为 Xps 并保存为 "ResultPDFtoXps.xps" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXps', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps"] }, [event.target.result]);
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


以下JavaScript代码片段显示了将PDF页面转换为XPS文件的简单示例：

1. 选择一个PDF文件进行转换。
2. 创建一个 'FileReader'。
3. 执行 [AsposePdfToXps](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftoxps/) 函数。
4. 设置生成文件的名称，在此示例中为 "ResultPDFtoXps.xps"。
5. 接下来，如果 'json.errorCode' 是0，那么结果文件将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于0，那么您的文件中将出现错误，此类错误的信息将包含在 'json.errorText' 文件中。
6. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffileToXps = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*将PDF文件转换为Xps并保存为 "ResultPDFtoXps.xps"*/
        const json = AsposePdfToXps(event.target.result, e.target.files[0].name, "ResultPDFtoXps.xps");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/vnd.ms-xpsdocument");
      }
      file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## 转换 PDF 为灰度 PDF

使用通过 C++ Web 工具包的 Aspose.PDF for JavaScript 将 PDF 转换为黑白。 为什么我要将 PDF 转换为灰度？如果 PDF 文件包含许多彩色图像，并且文件大小比颜色更重要，则转换可以节省空间。如果您以黑白打印 PDF 文件，转换它可以让您直观地检查最终结果的外观。

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileConvertToGrayscale = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF 文件转换为灰度并保存为 "ResultConvertToGrayscale.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToGrayscale', "params": [event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [代码片段]

    /*创建一个链接来下载结果文件*/
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


以下的 JavaScript 代码片段展示了将 PDF 页面转换为灰度 PDF 的简单示例：

1. 选择一个 PDF 文件进行转换。
2. 创建一个 'FileReader'。
3. 执行 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttograyscale/) 函数。
4. 设置生成文件的名称，在此示例中为 "ResultConvertToGrayscale.pdf"。
5. 接下来，如果 'json.errorCode' 为 0，那么你的 DownloadFile 将使用你之前指定的名称。如果 'json.errorCode' 参数不等于 0，则你的文件中会有一个错误，此类错误的信息将包含在 'json.errorText' 文件中。
6. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，允许你将生成的文件下载到用户的操作系统。

```js

  var ffileConvertToGrayscale = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将 PDF 文件转换为灰度并保存为 "ResultConvertToGrayscale.pdf"*/
      const json = AsposePdfConvertToGrayscale(event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*生成一个链接以下载结果文件*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```