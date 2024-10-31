---
title: 使用JavaScript在PDF中添加书签
linktitle: PDF中的书签
type: docs
weight: 10
url: /javascript-cpp/bookmark/
description: 您可以使用JavaScript在PDF文档中添加或删除书签。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF文档中删除特定书签

您可以使用C++的Aspose.PDF for JavaScript从PDF文件中删除书签。您可以在浏览器中直接获取结果。

1. 创建一个'FileReader'。
1. 执行[AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletebookmarks/)函数。
1. 设置结果文件的名称，在此示例中为"ResultPdfDeleteBookmarks.pdf"。
1. 接下来，如果'json.errorCode'为0，则您的DownloadFile将被赋予您之前指定的名称。如果'json.errorCode'参数不等于0，因此文件中会出现错误，则有关此类错误的信息将包含在'json.errorText'文件中。

1. 因此，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffilePdfDeleteBookmarks = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*从 PDF 文件中删除书签并保存为 "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfDeleteBookmarks(event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf");
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
    const ffilePdfDeleteBookmarks = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*从 PDF 文件中删除书签并保存为 "ResultPdfDeleteBookmarks.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteBookmarks', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf"] }, [event.target.result]);
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