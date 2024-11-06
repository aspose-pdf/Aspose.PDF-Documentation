---
title: 使用 JavaScript 通过 C++ 向 PDF 添加图像
linktitle: 添加图像
type: docs
weight: 10
url: zh/javascript-cpp/add-image-to-pdf/
description: 本节介绍如何使用 Aspose.PDF for JavaScript 通过 C++ 向现有 PDF 文件添加图像。
lastmod: "2023-12-15"
---

## 在现有 PDF 文件中添加图像

您需要在 PDF 中附加图像吗？想要提高 PDF 的可读性吗？在 PDF 中添加图像，您的演示或简历将显得更加得体。

人们普遍认为，向 PDF 文件添加图像需要复杂的专业工具。然而，使用 Aspose.PDF for JavaScript，您可以直接在浏览器中使用 JavaScript 快速轻松地向 PDF 添加所需的图像。

要向现有 PDF 文件添加图像：

1. 设置默认图像文件名。
1. 创建一个 'FileReader'。
1. 设置图像文件名。
1. 从 BLOB 准备图像文件。
1. 执行 [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/) 函数。

1. 将图像文件添加到 PDF 文件末尾并保存为 "ResultImage.pdf"。
2. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 将获得您之前指定的名称。如果 'json.errorCode' 参数不等于 0，相应地，您的文件中将出现错误，那么此类错误的信息将包含在 'json.errorText' 文件中。
3. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

以下代码片段显示了如何在 PDF 文档中添加图像。

```js

  /*设置默认图像文件名*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*设置图像文件名*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*从 BLOB 准备（保存）图像文件*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

在下一个例子中，我们选择要处理的图像：

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将图像文件添加到PDF文件末尾并保存为"ResultImage.pdf"*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*创建链接以下载结果文件*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## 使用Web Workers

```js

    /*创建Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自Web Worker的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ?
          `结果:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '图像已准备好!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `错误: ${evt.data.json.errorText}`;

    /*设置默认图像文件名: 'Aspose.jpg' 已加载, 参见 'settings.json' 中的设置*/
    var fileImage = "Aspose.jpg";

    /*事件处理程序*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将图像添加到PDF文件末尾并保存为"ResultImage.pdf" - 请求Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*设置图像文件名*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*将BLOB保存到内存文件系统以进行处理*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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
        link.innerHTML = "点击这里下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```