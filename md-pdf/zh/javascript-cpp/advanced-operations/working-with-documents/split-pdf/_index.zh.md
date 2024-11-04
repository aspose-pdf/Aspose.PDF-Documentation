---
title: 使用 JavaScript 拆分 PDF
linktitle: 拆分 PDF 文件
type: docs
weight: 30
url: /javascript-cpp/split-pdf/
description: 本主题展示如何使用 Aspose.PDF for JavaScript via C++ 将 PDF 页面拆分为单独的 PDF 文件。
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用 JavaScript 将 PDF 拆分为两个文件

本主题展示如何使用 JavaScript 将 PDF 页面拆分为单独的 PDF 文件。目前，我们支持拆分为两部分。这意味着 `pageToSplit` 是分割的标记。第一个文件将包含从 1 到 `pageToSplit`（包括）的所有页面，第二个文件将包含其余的页面。

拆分操作取决于文档中的页面数量，可能非常耗时。因此，我们强烈建议使用 Web Workers。

提供的代码片段是一个使用 JavaScript 中的 Web Worker 将 PDF 文件拆分为两个独立 PDF 文件的示例，并为用户提供下载结果文件的选项。
 Here's a steps of the code:

1. 创建一个 Web Worker。Web worker 使用 "AsposePDFforJS.js" 脚本文件初始化。这个 web worker 将在后台处理 PDF 文件拆分任务。在我们的示例中，worker 中发生的任何错误都会被捕获并记录到控制台中。
1. 消息处理。设置 web worker 使用 onmessage 事件处理程序监听消息。当它从网页接收到消息时，它会处理请求并将响应发送回主线程。
1. 文件拆分事件处理程序。当用户选择 PDF 文件进行拆分时，会触发一个事件处理程序 fileSplit。它使用 FileReader 读取所选的 PDF 文件，并通过 postMessage 调用将文件内容和相关参数（例如要拆分的页数和输出文件名）发送到 web worker。
1. 下载文件功能。 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数负责生成一个链接，允许用户下载文件。它接受文件名、MIME 类型和文件内容。该函数创建一个下载链接，将文件内容与之关联，设置文件名，并将其添加到文档中。这使用户可以下载生成的 PDF 文件。

1. Web Worker 中的消息处理。接下来，如果 'json.errorCode' 为 0，则 json.fileNameResult 将包含您之前指定的名称。如果 'json.errorCode' 参数不等于 0，并且相应地，您的文件中会出现错误，那么有关此类错误的信息将包含在 'json.errorText' 属性中。

1. 结果显示。主页包含一个ID为'output'的元素。当web worker发送带有结果的消息时，它会更新'output'元素。如果操作成功，它会显示两个拆分PDF文件的下载链接。如果出现错误，它会显示错误信息。

此代码展示了一种将资源密集型PDF文件拆分任务卸载到web worker的方法，以防止阻塞主UI线程。它还提供了一种用户友好的方式来下载拆分后的PDF文件。

```js

    /*创建Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自Web Worker的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ?
          `结果:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*设置拆分的页数*/
        const pageToSplit = 1;
        /*拆分为两个PDF文件并保存为"ResultSplit1.pdf", "ResultSplit2.pdf" - 请求Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
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

以下的 JavaScript 代码片段展示了将 PDF 页面拆分为单独 PDF 文件的简单示例：

1. 选择一个要拆分的 PDF 文件。
1. 在处理程序中创建一个 'FileReader' 对象。
1. 设置要拆分的页码。
1. 在最后一个处理程序中调用 [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsplit2files/)。
1. 分析结果。生成文件的名称在此示例中设置为 "ResultSplit2.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，则 json.fileNameResult 将包含您之前指定的名称。如果 'json.errorCode' 参数不等于 0，则您的文件中会出现错误，此类错误的信息将包含在 'json.errorText' 属性中。
1. 您可以使用辅助函数 [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)。

```js

  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*设置要拆分的页码*/
      const pageToSplit = 1;
      /*拆分为两个 PDF 文件并保存为 "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " 拆分: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*创建链接下载第一个结果文件*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*创建链接下载第二个结果文件*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```