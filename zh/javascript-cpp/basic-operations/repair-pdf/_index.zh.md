---
title: 通过 C++ 使用 JavaScript 修复 PDF
linktitle: 修复 PDF
type: docs
weight: 10
url: /javascript-cpp/repair-pdf/
description: 本主题描述了如何通过 JavaScript 和 C++ 修复 PDF
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for JavaScript 允许高质量的 PDF 修复。PDF 文件可能由于任何原因无法打开，无论是程序还是浏览器。在某些情况下，文档可以恢复，尝试以下代码并亲自查看。

1. 创建一个 'FileReader'。
1. 执行 [AsposePdfRepair](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfrepair/) 函数。
1. 设置生成文件的名称，在本例中为 "ResultPdfRepair.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，那么您可以获取结果文件的链接。如果 'json.errorCode' 参数不等于 0，并且相应地，您的文件中会有错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。

1. 因此，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffilePdfRepair = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*修复 PDF 文件并保存为 "ResultPdfRepair.pdf"*/
        const json = AsposePdfRepair(event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## 使用 Web Workers

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '加载完成!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffilePdfRepair = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*修复 PDF 文件并保存为 "ResultPdfRepair.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRepair', "params": [event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf"] }, [event.target.result]);
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