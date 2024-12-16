---
title: 从PDF中移除附件与JavaScript
linktitle: 从现有PDF中移除附件
type: docs
weight: 10
url: /zh/javascript-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF可以从您的PDF文档中移除附件。使用JavaScript Web工具包通过Aspose.PDF来移除PDF文件中的附件。
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

您可以使用Aspose.PDF通过C++在JavaScript中删除PDF文件中的附件。您可以直接在浏览器中获得结果。

1. 创建一个'FileReader'。
1. 执行[AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteattachments/)函数。
1. 设置结果文件的名称，在本例中为"ResultPdfDeleteAttachments.pdf"。

1. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此您的文件中会出现错误，则有关此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffilePdfDeleteAttachments = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*从 PDF 文件中删除附件并保存为 "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfDeleteAttachments(event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf");
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
        (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffilePdfDeleteAttachments = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*从 PDF 文件中删除附件并保存为 "ResultPdfDeleteAttachments.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAttachments', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf"] }, [event.target.result]);
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