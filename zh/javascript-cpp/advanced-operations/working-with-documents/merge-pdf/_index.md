---
title: 如何通过 C++ 使用 JavaScript 合并 PDF
linktitle: 合并 PDF 文件
type: docs
weight: 20
url: zh/javascript-cpp/merge-pdf/
description: 本页解释如何使用 Aspose.PDF for JavaScript via C++ 将 PDF 文档合并成单个 PDF 文件
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 在 JavaScript 中将两个 PDF 合并或组合成一个 PDF

在处理大量文档时，合并和组合文件是一个非常流行的任务。有时，在处理文档和图像时，当它们被扫描、处理和组织时，会创建多个文件。
但是如果您需要将所有内容存储在一个文件中怎么办？或者您不想打印多个文档？使用 Aspose.PDF for JavaScript via C++ 将两个 PDF 文件连接。

这个 JavaScript 工具允许使用 Aspose.PDF for JavaScript via C++ 将两个 PDF 文件合并成一个 PDF 文档。示例用 JavaScript 编写。

1. 选择要合并的 PDF 文件。
1. 创建一个 'FileReader'。

1. [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/) 函数被执行。
1. 结果文件的名称被设置，在这个例子中是 "ResultMerge.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，则你的 DownloadFile 被赋予你之前指定的名称。如果 'json.errorCode' 参数不等于 0，并且因此你的文件中会有一个错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许你将结果文件下载到用户的操作系统中。

以下代码片段展示了如何连接 PDF 文件：

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*仅两个文件*/
      if (index >= e.target.files.length || index >= 2) {
        /*合并两个 PDF 文件并保存为 "ResultMerge.pdf"*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*从 BLOB 准备（保存）文件*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```


### 使用 Web Workers

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? 
          `结果:\n${(evt.data.operation == 'AsposePdfPrepare') ? 
                      fileProcess('AsposePdfMerge2Files', evt.data.json.optdata[0].file, {"fileName2": evt.data.json.fileNameResult}) ?? '请稍候...' : 
                      DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0]) /*AsposePdfMerge2Files*/
                    }` :
          `错误: ${evt.data.json.errorText}`;

    /*事件处理程序。仅合并两个文件。如果只选择了一个文件，则使用它。对于第二个文件，您需要执行 AsposePdfPrepare */
    const ffileMerge = evt => fileProcess('AsposePdfPrepare',  evt.target.files[(evt.target.files.length == 1) ? 0 : 1],
                                          [{"operation": 'AsposePdfMerge2Files', "file": evt.target.files[0]}])
    /* 请求 Web Worker */
    const fileProcess = (operation, ffile, optdata) => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        if (operation == 'AsposePdfPrepare')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, "params": [event.target.result, ffile.name, optdata] },
                  [event.target.result]
                );
        else if (operation == 'AsposePdfMerge2Files')
          return AsposePDFWebWorker.postMessage(
                  { "operation": operation, 
                    "params": [event.target.result, undefined, ffile.name, (optdata === undefined) ? ffile.name : optdata.fileName2,
                                `Result${operation}.pdf`] },
                  [event.target.result]
                );
      }
      file_reader.readAsArrayBuffer(ffile);
    }

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