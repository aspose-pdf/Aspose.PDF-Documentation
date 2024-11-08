---
title: 使用JavaScript从PDF中提取文本
linktitle: 从PDF中提取文本
type: docs
weight: 30
url: /zh/javascript-cpp/extract-text-from-pdf/
description: 本文描述了使用Aspose.PDF for JavaScript从PDF文档中提取文本的各种方法。
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF文档中提取文本

从PDF文档中提取文本是一项非常常见且有用的任务。从PDF中提取文本可用于多种目的，从提高搜索和可用性到支持商业、研究和信息管理等各个领域的数据分析和自动化。

如果您想从PDF文档中提取文本，可以使用[AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/)函数。请查看以下代码片段，以便通过JavaScript使用C++从PDF文件中提取文本。

1. 创建一个 'FileReader'。

1. [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) 函数被执行。
1. 接下来，如果 'json.errorCode' 为 0，那么您可以获得结果文件的链接。如果 'json.errorCode' 参数不等于 0，相应地，您的文件中将会出现错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。

```js

    var ffileExtract = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*从 PDF 文件中提取文本*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
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
            evt.data.json.extractText :
            `错误: ${evt.data.json.errorText}`; 

    /*事件处理器*/
    const ffileExtract = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*从 PDF 文件中提取文本 - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```