---
title: 使用 JavaScript 删除注释
linktitle: 删除注释
type: docs
weight: 10
url: /javascript-cpp/delete-annotation/
description: 使用 Aspose.PDF for JavaScript 您可以从 PDF 文件中删除注释。
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

您可以使用 Aspose.PDF for JavaScript 通过 C++ 从 PDF 文件中删除注释。您可以直接在浏览器中获得结果。

1. 创建一个 'FileReader'。
1. 执行 [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteannotations/) 函数。
1. 设置结果文件的名称，在此示例中为 "ResultPdfDeleteAnnotations.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 将获得您先前指定的名称。如果 'json.errorCode' 参数不等于 0，因此文件中会出现错误，则此类错误的信息将包含在 'json.errorText' 文件中。

1. 因此，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffilePdfDeleteAnnotations = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*从 PDF 文件中删除注释并保存为 "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfDeleteAnnotations(event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf");
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
    const ffilePdfDeleteAnnotations = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*从 PDF 文件中删除注释并保存为 "ResultPdfDeleteAnnotations.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAnnotations', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf"] }, [event.target.result]);
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