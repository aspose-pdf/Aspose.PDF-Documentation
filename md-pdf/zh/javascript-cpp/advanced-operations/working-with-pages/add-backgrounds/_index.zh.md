---
title: 使用 C++ 通过 JavaScript 为 PDF 添加背景
linktitle: 添加背景
type: docs
weight: 10
url: /javascript-cpp/add-backgrounds/
description: 使用 C++ 通过 JavaScript 为您的 PDF 文件添加背景图像。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

以下代码片段展示了如何使用 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) 函数通过 JavaScript 向 PDF 页面添加背景图像。

在下一个代码片段中，我们将图像上传到内部文件系统以供进一步处理：

1. 创建一个 'FileReader'。
1. 设置图像文件名。
1. 从 BLOB 准备图像文件。

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*设置图像文件名*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*从 BLOB 准备（保存）图像文件*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


在下一个示例中，我们选择要处理的 PDF 文件。  
1. 创建一个 'FileReader'。  
1. 执行 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) 函数。  
1. 将图像文件添加到 PDF 中并保存为 "ResultBackgroundImage.pdf"。  
1. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，相应地，您的文件中将会出现错误，那么有关此类错误的信息将包含在 'json.errorText' 文件中。  
1. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统中。

```js

  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将背景图像文件添加到 PDF 中并保存为 "ResultBackgroundImage.pdf"*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
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
          `结果:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '图像已准备好!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `错误: ${evt.data.json.errorText}`;

    /*设置默认图像文件名: 'Aspose.jpg' 已加载, 请参见 'settings.json' 中的设置*/
    var fileBackgroundImage = "Aspose.jpg";

    /*事件处理程序*/
    const ffileAddBackgroundImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*向 PDF 文件添加背景图像并保存为 "ResultBackgroundImage.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddBackgroundImage',
            "params": [event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*设置图像文件名*/
      fileBackgroundImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*将 BLOB 保存到内存文件系统中以进行处理*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*创建下载结果文件的链接*/
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