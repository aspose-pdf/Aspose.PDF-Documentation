---
title: 通过 C++ 使用 JavaScript 向 PDF 添加页眉和页脚
linktitle: 向 PDF 添加页眉和页脚
type: docs
weight: 70
url: /javascript-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for JavaScript via C++ 允许您使用 AsposePdfAddTextHeaderFooter 向 PDF 文件添加页眉和页脚。
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for JavaScript via C++** 允许您在现有 PDF 文件中添加页眉和页脚。

1. 创建一个 'FileReader'。
1. 执行 [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddtextheaderfooter/) 函数。
1. 设置生成文件的名称，在此示例中为 "ResultAddHeader.pdf"。

1. 接下来，如果 'json.errorCode' 是 0，那么你的 DownloadFile 将被赋予你之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此你的文件中会有错误，则关于此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许你将生成的文件下载到用户的操作系统。

以下代码片段展示了如何使用 JavaScript 在 PDF 文件的页眉中添加文本。

```js

  var ffileAddTextHeaderFooter = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*在 PDF 文件中添加页眉并保存为 "ResultAddHeader.pdf"*/
      const json = AsposePdfAddTextHeaderFooter(event.target.result, e.target.files[0].name, "Aspose.PDF for JavaScript via C++", "", "ResultAddHeader.pdf");
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
    const ffileAddTextHeaderFooter = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const header = 'Aspose.PDF for JavaScript via C++';
        const footer = 'ASPOSE';
        /*在 PDF 文件的页眉/页脚中添加文本并保存为 "ResultAddHeaderFooter.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddTextHeaderFooter',
            "params": [event.target.result, e.target.files[0].name, header, footer, "ResultAddHeaderFooter.pdf"] },
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
        link.innerHTML = "点击此处下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```