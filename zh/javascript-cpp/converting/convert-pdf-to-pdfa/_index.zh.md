---
title: 将 PDF 转换为 PDF/A 格式
linktitle: 将 PDF 转换为 PDF/A 格式
type: docs
weight: 100
url: /javascript-cpp/convert-pdf-to-pdfa/
lastmod: "2023-11-01"
description: 本主题向您展示如何使用 Aspose.PDF 将 PDF 文件转换为符合 PDF/A 标准的 PDF 文件。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for JavaScript** 允许您将 PDF 文件转换为符合 <abbr title="Portable Document Format / A">PDF/A</abbr> 的 PDF 文件。

转换操作取决于文档中的页面数量，并且可能非常耗时。因此，我们强烈建议使用 Web Workers。

此代码演示了一种将资源密集型 PDF 文件转换任务卸载到 web worker 的方法，以防止阻塞主 UI 线程。它还提供了一种用户友好的方式来下载转换后的文件。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PDF/A**

Aspose.PDF for JavaScript 为您提供了一个免费的在线应用程序 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 PDF/A 使用免费应用](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## 将 PDF 转换为 PDF/A 格式

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '加载完成!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}\n${DownloadFile(evt.data.json.fileNameLogResult, "application/xml", evt.data.params[1])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理*/
    const ffilePdfConvertToPDFA = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pdfFormat = 'Module.PdfFormat.PDF_A_1A';
        /*将 PDF 文件转换为 PDF/A(1A) 并保存为 "ResultConvertToPDFA.pdf"*/
        /*在转换过程中也会进行验证, "ResultConvertToPDFA.xml"- 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfConvertToPDFA', "params": [event.target.result, e.target.files[0].name, pdfFormat, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml"] }, [event.target.result]);
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


以下的 JavaScript 代码片段展示了将 PDF 转换为 PDF/A 文件的简单示例：

1. 选择一个要转换的 PDF 文件。
2. 创建一个 'FileReader'。
3. 执行 [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/) 函数。
4. 设置生成文件的名称，在此示例中为 "ResultConvertToPDFA.pdf"。在转换过程中，还会进行验证，"ResultConvertToPDFA.xml"。
5. 接下来，如果 'json.errorCode' 是 0，那么 DownloadFile 将使用您之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此您的文件中会有错误，那么有关该错误的信息将包含在 'json.errorText' 文件中。
6. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接并允许您下载生成的文件，以及下载日志 (xml) 文件到用户的操作系统。

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将 PDF 文件转换为 PDF/A(1A) 并保存为 "ResultConvertToPDFA.pdf"*/
      /*在转换过程中，还会进行验证，"ResultConvertToPDFA.xml"*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\n日志文件 (xml 格式): " + json.fileNameLogResult;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\n日志文件 (xml 格式): " + json.fileNameLogResult;
      /*创建一个链接以下载日志 (xml)*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```