---
title: 使用JavaScript解密PDF
linktitle: 解密PDF文件
type: docs
weight: 40
url: /javascript-cpp/decrypt-pdf/
description: 使用Aspose.PDF for JavaScript via C++解密PDF文件。
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用所有者密码解密PDF文件

最近，越来越多的用户交换加密文档，以避免成为网络欺诈的受害者并保护他们的文件。在这种情况下，有必要访问加密的PDF文件，因为这种访问只能由授权用户获得。同时，人们也在寻找各种解决方案来解密PDF文件。

最好使用Aspose.PDF for JavaScript via C++直接在您的网络浏览器中解决此问题。以下代码片段向您展示如何解密PDF文件。

1. 选择要解密的PDF文件。
1. 创建一个“FileReader”。
1. 执行[AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/)函数。

1. 生成文件的名称已设置，在此示例中为 "ResultDecrypt.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，那么您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此您文件中会有错误信息，那么此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果是，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffileDecrypt = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*使用密码 "owner" 解密 PDF 文件并保存为 "ResultDecrypt.pdf"*/
        const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
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
    const ffileDecrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password = 'owner';
        /*使用密码 "owner" 解密 PDF 文件并保存为 "ResultDecrypt.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDecrypt',
            "params": [event.target.result, e.target.files[0].name, password, "ResultDecrypt.pdf"] }, 
          [event.target.result]
        );
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