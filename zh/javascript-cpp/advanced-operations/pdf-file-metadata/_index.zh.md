---
title: 使用 JavaScript 通过 C++ 处理 PDF 文件元数据
linktitle: PDF 文件元数据
type: docs
weight: 130
url: /javascript-cpp/pdf-file-metadata/
description: 本节解释如何获取 PDF 文件信息，如何从 PDF 文件中获取元数据，设置 PDF 文件信息。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取 PDF 文件信息

1. 创建一个 'FileReader'。
1. 执行 [AsposePdfGetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetinfo/) 函数。
1. 可以获取的 PDF 元数据：
- title - 标题
- creator - 创建者
- author - 作者
- subject - 主题
- keywords - 关键词
- creation - 创建日期
- mod - 修改日期
1. 接下来，如果 'json.errorCode' 为 0，则可以获取 PDF 文件信息列表。如果 'json.errorCode' 参数不等于 0，因此您文件中会有错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。

```js

  var ffilePdfGetInfo = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*从 PDF 文件中获取信息（元数据）。*/
      const json = AsposePdfGetInfo(event.target.result, e.target.files[0].name);
      /* JSON
      title - 标题
      creator - 创建者
      author - 作者
      subject - 主题
      keywords - 关键词
      format - PDF 格式
      version - PDF 版本
      ispdfa - PDF 是 PDF/A
      ispdfua - PDF 是 PDF/UA
      islinearized - PDF 是线性化的
      isencrypted - PDF 是加密的
      permission - PDF 权限
      size - PDF 页面大小
      pagecount - 页数
      creation Date: json.creation
      modify Date:   json.mod
      annotationcount - 注释数量
      bookmarkcount - 书签数量
      attachmentcount - 附件数量
      metadatacount - 元数据数量
      javascriptcount - JavaScript 数量
      imagecount - 图像数量
      */
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


### 使用 Web Workers

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ?
          `信息:\n${JSON.stringify(evt.data.json, null, 4)}` :
          `错误: ${evt.data.json.errorText}`; 

    /*事件处理程序*/
    const ffilePdfGetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*从 PDF 文件获取信息（元数据） - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetInfo', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## 获取所有字体

从 PDF 文件中获取字体可以是一种在其他文档或应用程序中重用字体的有用方法。
 
如果您想从 PDF 文档中获取所有字体，可以使用 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/)。请查看以下代码片段，以便通过 C++ 使用 JavaScript 从现有 PDF 文档中获取所有字体。

1. 创建一个 'FileReader'。
1. 执行 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfgetallfonts/) 函数。
1. 接下来，如果 'json.errorCode' 为 0，那么您可以从 PDF 文件中获取字体列表。如果 'json.errorCode' 参数不等于 0，并且相应地，您的文件中会有错误，则有关此类错误的信息将包含在 'json.errorText' 文件中。

```js

  var ffilePdfGetAllFonts = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*从 PDF 文件中获取字体列表。*/
      const json = AsposePdfGetAllFonts(event.target.result, e.target.files[0].name);
      if (json.errorCode == 0) document.getElementById('output').textContent = "JSON:\n" + JSON.stringify(json, null, 4);
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
          `字体:\n${JSON.stringify(evt.data.json.fonts, null, 4)}` :
          `错误: ${evt.data.json.errorText}`; 

    /*事件处理器*/
    const ffilePdfGetAllFonts = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*获取 PDF 文件的字体列表 - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfGetAllFonts', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```
## 设置 PDF 文件信息

Aspose.PDF for JavaScript via C++ 允许您为 PDF 设置特定于文件的信息，例如作者、创建日期、主题和标题。
 要设置此信息：

1. 创建一个 'FileReader'。
1. 如果不需要设置值，使用 undefined 或 ""（空字符串）。
1. 执行 [AsposePdfSetInfo](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsetinfo/) 函数。
1. 设置生成文件的名称，在此示例中为 "ResultSetInfo.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，并且相应地，文件中会出现错误，则有关此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffilePdfSetInfo = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*设置PDF信息：标题、创建者、作者、主题、关键词、创建日期、修改日期*/
        /*如果不需要设置值，使用 undefined 或 ""（空字符串）*/
        /*在PDF文件中设置信息（元数据）并保存为 "ResultSetInfo.pdf"*/
        const json = AsposePdfSetInfo(event.target.result, e.target.files[0].name, "设置PDF文档信息", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "16/02/2023 11:55 PM", "ResultSetInfo.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

### 使用 Web Worker

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ?
          `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffilePdfSetInfo = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF 信息: 标题, 创建者, 作者, 主题, 关键词, 创建日期, 修改日期*/
        const title = '设置 PDF 文档信息';
        const creator = ''; /*如果不需要设置值，使用: undefined 或 ""/'' (空字符串)*/
        const author = 'Aspose';
        const subject = undefined;
        const keywords = 'Aspose.Pdf, DOM, API';
        const creation = undefined; /*创建日期*/
        const mod = '16/02/2023 11:55 PM'; /*修改日期*/
        /*在 PDF 文件中设置信息（元数据）并保存为 "ResultSetInfo.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSetInfo',
            "params": [event.target.result, e.target.files[0].name, title, creator, author, subject, keywords, creation, mod, "ResultSetInfo.pdf"] },
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


## 删除 PDF 文件信息

Aspose.PDF for JavaScript via C++ 允许您删除 PDF 文件元数据：

1. 创建一个 'FileReader'。
1. 执行 [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/javascript-cpp/metadata/asposepdfremovemetadata/) 函数。
1. 生成文件的名称设置为，在此示例中为 "ResultPdfRemoveMetadata.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，则您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此您的文件中会有错误，那么关于此类错误的信息将包含在 'json.errorText' 文件中。
1. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffilePdfRemoveMetadata = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*删除 PDF 文件的元数据并保存为 "ResultPdfRemoveMetadata.pdf"*/
        const json = AsposePdfRemoveMetadata(event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### 使用 Web Worker

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffilePdfRemoveMetadata = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*移除 PDF 文件的元数据并保存为 "ResultPdfRemoveMetadata.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRemoveMetadata', "params": [event.target.result, e.target.files[0].name, "ResultPdfRemoveMetadata.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [代码片段]

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