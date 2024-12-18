---
title: 使用 JavaScript 将 PDF 转换为 Word 文档
linktitle: 将 PDF 转换为 Word
type: docs
weight: 10
url: /zh/javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: 学习如何编写 JavaScript 代码以直接在 Web 中将 PDF 转换为 DOC(DOCX)。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

转换操作取决于文档中的页数，并且可能非常耗时。因此，我们强烈建议使用 Web Workers。

此代码演示了一种将资源密集型 PDF 文件转换任务卸载到 web worker 的方法，以防止阻塞主 UI 线程。它还提供了一种用户友好的方式来下载转换后的文件。

要在 Microsoft Word 或其他支持 DOC 和 DOCX 格式的文字处理器中编辑 PDF 文件的内容。PDF 文件是可编辑的，但 DOC 和 DOCX 文件更灵活且可定制。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for JavaScript 向您展示了一个在线免费应用程序 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，您可以尝试调查其功能和工作质量。

[![将 PDF 转换为 DOC](/pdf/zh/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 将 PDF 转换为 DOC

```js

  /*创建 Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '已加载!' :
      (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

  /*事件处理器*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*将 PDF 文件转换为 Doc 并保存为 "ResultPDFtoDoc.doc" - 请求 Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
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


以下JavaScript代码片段展示了将PDF页面转换为DOC文件的简单示例：

1. 选择要转换的PDF文件。
1. 创建一个'FileReader'。
1. 执行[AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/)函数。
1. 设置生成文件的名称，在此示例中为"ResultPDFtoDoc.doc"。
1. 接下来，如果'json.errorCode'为0，则生成的文件将被赋予您之前指定的名称。如果'json.errorCode'参数不等于0，因此文件中会出现错误，则有关此类错误的信息将包含在'json.errorText'文件中。
1. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将PDF文件转换为Doc并保存为"ResultPDFtoDoc.doc"*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*创建下载结果文件的链接*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


{{% alert color="warning" %}}
**尝试在线将PDF转换为DOCX**

Aspose.PDF for JavaScript 为您提供在线免费应用程序 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/zh/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 将PDF转换为DOCX

Aspose.PDF for JavaScript API 允许您读取和转换PDF文档为DOCX。DOCX是Microsoft Word文档的知名格式，其结构从简单的二进制文件更改为XML和二进制文件的组合。Docx文件可以用Word 2007及以后的版本打开，但不能用支持DOC文件扩展名的早期版本的MS Word打开。

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '加载完成!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF 文件转换为 DocX 并保存为 "ResultPDFtoDocX.docx" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
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


以下的 JavaScript 代码片段展示了将 PDF 页面转换为 DOCX 文件的简单示例：

1. 选择一个 PDF 文件进行转换。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/) 函数。
1. 设置结果文件的名称，在此示例中为 "ResultPDFtoDocX.docx"。
1. 接下来，如果 'json.errorCode' 为 0，则结果文件将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，并且因此文件中会有错误，则有关此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将结果文件下载到用户的操作系统。

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将 PDF 文件转换为 DocX 并保存为 "ResultPDFtoDocX.docx"*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*创建一个链接以下载结果文件*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```