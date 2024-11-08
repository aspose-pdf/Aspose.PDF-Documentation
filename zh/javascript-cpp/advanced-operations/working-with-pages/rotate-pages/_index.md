---
title: 使用 JavaScript 通过 C++ 旋转 PDF 页面
linktitle: 旋转 PDF 页面
type: docs
weight: 50
url: /zh/javascript-cpp/rotate-pages/
description: 本主题描述如何通过 JavaScript 通过 C++ 以编程方式旋转现有 PDF 文件中的页面方向
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

本节描述如何在现有 PDF 文件中使用 JavaScript 通过 C++ 将页面方向从横向更改为纵向，反之亦然。

1. 创建一个 'FileReader'。
1. 执行 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfrotateallpages/) 函数。
1. 设置结果文件的名称，在此示例中为 "ResultRotation.pdf"。

1. 接下来，如果 'json.errorCode' 为 0，那么你的 DownloadFile 将被赋予你之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此你的文件中会出现错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许你将生成的文件下载到用户的操作系统。

```js

  var ffileRotateAllPages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*旋转所有页面的 PDF 文件并保存为 "ResultRotation.pdf"*/
      const json = AsposePdfRotateAllPages(event.target.result, e.target.files[0].name, Module.Rotation.on270, "ResultRotation.pdf");
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
    const ffileRotateAllPages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const rotation = 'Module.Rotation.on270';
        /*旋转 PDF 页并保存为 "ResultRotation.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfRotateAllPages',
            "params": [event.target.result, e.target.files[0].name, rotation, "ResultRotation.pdf"] },
          [event.target.result]
        );
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