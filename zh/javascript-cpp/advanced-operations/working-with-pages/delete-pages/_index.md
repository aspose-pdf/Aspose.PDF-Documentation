---
title: 使用 JavaScript 通过 C++ 删除 PDF 页面 
linktitle: 删除 PDF 页面
type: docs
weight: 30
url: /zh/javascript-cpp/delete-pages/
description: 您可以使用 Aspose.PDF for JavaScript 通过 C++ 从 PDF 文件中删除页面。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

您可以使用 Aspose.PDF for JavaScript 通过 C++ 从 PDF 文件中删除页面。您可以直接在浏览器中获取结果。

1. 创建一个 'FileReader'。
1. 指定要删除的页码。
1. 执行 [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/) 函数。
1. 设置生成文件的名称，在此示例中为 "ResultDeletePages.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此文件中会出现错误，则有关此类错误的信息将包含在 'json.errorText' 文件中。

1. 因此，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*字符串，包含页面编号和间隔："7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*数组，页面编号数组*/
      /*const numPages = [1,3];*/
      /*数字，页面编号*/
      /*const numPages = 1;*/
      /*删除 PDF 文件的 1-3 页并保存为 "ResultOptimize.pdf"*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
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

    /*事件处理程序*/
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*字符串，包括页码区间: "7, 20, 22, 30-32, 33, 36-40, 46"*/
        const numPages = "1-3";
        /*数组，页码数组*/
        /*const numPages = [1,3];*/
        /*数字，页码*/
        /*const numPages = 1;*/
        /*从 PDF 文件中删除页面并保存为 "ResultDeletePages.pdf - Ask Web Worker"*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

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