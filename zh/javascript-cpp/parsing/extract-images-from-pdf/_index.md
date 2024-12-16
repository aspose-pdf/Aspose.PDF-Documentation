---
title: 从PDF中提取图像 JavaScript
linktitle: 从PDF中提取图像
type: docs
weight: 20
url: /zh/javascript-cpp/extract-images-from-the-pdf-file/
description: 如何使用 Aspose.PDF for JavaScript 工具包从PDF中提取部分图像。
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF 的Web工具包可以让您轻松从PDF文件中提取图像。

如果您想从PDF文档中提取图像，可以使用[AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/)函数。
请查看以下代码片段，以便通过JavaScript和C++从PDF文件中提取图像。

1. 创建一个 'FileReader'。
2. 执行 [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/) 函数。
3. 设置结果文件的名称，在此示例中为 "ResultPdfExtractImage{0:D2}.jpg"。

1. 接下来，如果 'json.errorCode' 是 0，那么您可以获取到结果文件的链接。如果 'json.errorCode' 参数不等于 0，并且相应地，您的文件中会有一个错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数会生成一个链接，并允许您将生成的文件下载到用户的操作系统中。

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*从PDF文件中提取图像，模板为"ResultPdfExtractImage{0:D2}.jpg"（{0}, {0:D2}, {0:D3}, ... 格式页码），分辨率150 DPI并保存*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "文件（图像）数量: " + json.filesCount.toString();
        /*为结果文件创建链接*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## 使用 Web Workers

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载！' :
        (evt.data.json.errorCode == 0) ? 
          `文件(图片)数量: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*从 PDF 文件中提取图片，使用模板 "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... 格式页码)，分辨率 150 DPI 并保存*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
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