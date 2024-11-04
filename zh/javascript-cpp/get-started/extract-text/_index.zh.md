---
title: 使用 JavaScript 从 PDF 提取文本
linktitle: 从 PDF 提取文本
type: docs
weight: 10
url: /javascript-cpp/extract-text/
description: 本节介绍如何使用 JavaScript 工具包从 PDF 文档中提取文本。
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档的所有页面提取文本

从 PDF 中提取文本并不容易。并不是很多 PDF 阅读器可以从 PDF 图像或扫描的 PDF 中提取文本。但是 **Aspose.PDF for JavaScript via C++** 工具允许您轻松从所有 PDF 文件中提取文本。

查看代码片段并按照步骤从您的 PDF 中提取文本：

1. 选择一个 PDF 文件以提取文本。
2. 创建一个 'FileReader' 来读取文本。
3. 执行 [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/) 函数。

1. 接下来，如果 'json.errorCode' 是 0，则 'json.extractText' 将包含提取的内容。如果 'json.errorCode' 参数不等于 0，那么您的文件将会有错误，此类错误的信息将包含在 'json.errorText' 中。
1. 结果是，您将收到一个包含从 PDF 中提取的文本的字符串。

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
      (evt.data == 'ready') ? '加载完成!' :
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