---
title: 使用 Aspose.PDF for JavaScript via C++ 优化 PDF
linktitle: 优化 PDF 文件
type: docs
weight: 10
url: /zh/javascript-cpp/optimize-pdf/
description: 使用 JavaScript 工具优化和压缩 PDF 文件以实现快速网页浏览。
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 优化 PDF 文档

Aspose.PDF for JavaScript via C++ 工具包允许您为网络优化 PDF 内容。

网络优化或线性化是指使 PDF 文件适合使用网络浏览器在线浏览的过程。要优化文件以便网络显示：

1. 选择一个要优化的 PDF 文件。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfOptimize](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfoptimize/) 函数。
1. 设置生成文件的名称，在此示例中为 "ResultOptimize.pdf"。

1. 接下来，如果 'json.errorCode' 是 0，那么您的 DownloadFile 会被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此您的文件中会有错误，那么有关此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

下面的代码片段展示了如何优化 PDF 文档。

```js

  var ffileOptimize = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*优化一个 PDF 文件并保存为 "ResultOptimize.pdf"*/
      const json = AsposePdfOptimize(event.target.result, e.target.files[0].name, "ResultOptimize.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*创建一个链接以下载结果文件*/
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
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ?
          `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffileOptimize = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*优化 PDF 文件并保存为 "ResultOptimize.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfOptimize', "params": [event.target.result, e.target.files[0].name, "ResultOptimize.pdf"] },
          [event.target.result]
        );
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