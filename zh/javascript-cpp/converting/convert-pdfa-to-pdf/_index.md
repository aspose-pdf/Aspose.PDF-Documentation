---
title: 将 PDF/A 转换为 PDF 格式
linktitle: 将 PDF/A 转换为 PDF 格式
type: docs
weight: 110
url: /zh/javascript-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-01"
description: 本主题向您展示如何使用 Aspose.PDF 通过 JavaScript 将 PDF/A 文件转换为 PDF 文档。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 将 PDF/A 转换为 PDF 格式

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffilePdfAConvertToPDF = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF/A 文件转换为 PDF 并保存为 "ResultConvertToPDF.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAConvertToPDF', "params": [event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf"] }, [event.target.result]);
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


以下的 JavaScript 代码片段展示了一个将 PDF/A 转换为 PDF 的简单示例：

1. 选择一个 PDF 文件进行转换。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaconverttopdf/) 函数。
1. 设置生成文件的名称，在此示例中为 "ResultConvertToPDFA.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 会被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，则您的文件中会有错误，此类错误的信息将包含在 'json.errorText' 文件中。
1. 最后，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffilePdfAConvertToPDF = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*将 PDF/A 文件转换为 PDF 并保存为 "ResultConvertToPDF.pdf"*/
        const json = AsposePdfAConvertToPDF(event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

```