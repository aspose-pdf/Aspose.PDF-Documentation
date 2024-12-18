---
title: 使用 JavaScript 和 C++ 优化 PDF 资源 
linktitle: 优化 PDF 资源
type: docs
weight: 15
url: /zh/javascript-cpp/optimize-pdf-resources/
description: 使用 JavaScript 工具优化 PDF 文件的资源以实现快速网页视图。
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 优化 PDF 资源

优化文档中的资源：

  1. 删除文档页面上未使用的资源
  1. 将相同的资源合并为一个对象
  1. 删除未使用的对象

1. 选择一个 PDF 文件进行优化。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfoptimizeresource/) 函数。
1. 设定生成文件的名称，本例中为 "ResultPdfOptimizeResource.pdf"。

1. 接下来，如果 'json.errorCode' 是 0，那么您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，并且相应地，您的文件中会出现错误，那么有关此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

以下代码片段显示了如何优化 PDF 文档。

```js

    var ffilePdfOptimizeResource = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*优化 PDF 文件的资源并保存为 "ResultPdfOptimizeResource.pdf"*/
        const json = AsposePdfOptimizeResource(event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf");
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
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffilePdfOptimizeResource = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*优化 PDF 文件的资源并保存为 "ResultPdfOptimizeResource.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfOptimizeResource', "params": [event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf"] }, [event.target.result]);
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
        link.innerHTML = "点击此处下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```