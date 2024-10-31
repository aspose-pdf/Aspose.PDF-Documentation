---
title: 在 PDF 中添加图像印章使用 JavaScript 通过 C++
linktitle: PDF 文件中的图像印章
type: docs
weight: 60
url: /javascript-cpp/stamping/
description: 使用 JavaScript 工具包中的 AsposePdfAddStamp 函数将图像印章添加到您的 PDF 文档中。
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在 PDF 文件中添加图像印章

在 PDF 文档中加盖印章类似于在纸质文档上加盖印章。PDF 文件中的印章为 PDF 文件提供了附加信息，如保护 PDF 文件供他人使用并确认 PDF 文件内容的安全性。
您可以使用 [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) 函数通过 JavaScript 将图像印章添加到 PDF 文件中。

要添加图像印章：

1. 设置默认图像文件名。
1. 创建一个 'FileReader'。
1. 设置图像文件名。
1. 从 BLOB 准备印章文件。

以下代码片段展示了如何在 PDF 文件中添加图像印章。

```js

  /*设置默认印章文件名*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*设置印章文件名*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*从 BLOB 准备（保存）印章文件*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


1. 创建一个 'FileReader'。
1. 执行 [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) 函数。
1. 将图像文件添加到 PDF 文件的末尾并保存为 "ResultImage.pdf"。
1. 接下来，如果 'json.errorCode' 是 0，那么您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，那么文件中将会有错误信息，而这样的错误信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统中。

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将印章文件插入到 PDF 文件中并保存为 "ResultImage.pdf"*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
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
      (evt.data == 'ready') ? '已加载！' :
        (evt.data.json.errorCode == 0) ?
          `结果:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '图像已准备好！':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `错误: ${evt.data.json.errorText}`;

    /*设置默认的图章文件名: 'Aspose.jpg' 已加载，参见 'settings.json' 中的设置*/
    var fileStamp = "Aspose.jpg";

    /*事件处理程序*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*将图章添加到 PDF 文件并保存为 "ResultStamp.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddStamp',
            "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_,
                      setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*设置图章文件名*/
      fileStamp = e.target.files[0].name;
      file_reader.onload = event => {
        /*将 BLOB 保存到内存文件系统中以进行处理*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
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