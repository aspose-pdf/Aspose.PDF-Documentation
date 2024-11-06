---
title: 将PDF转换为Excel使用JavaScript
linktitle: 将PDF转换为Excel
type: docs
weight: 20
url: zh/javascript-cpp/convert-pdf-to-xlsx/
lastmod: "2023-11-01"
keywords: 使用javascript将PDF转换为Excel, 将PDF转换为XLSX, 将PDF转换为CSV。
description: Aspose.PDF for JavaScript允许您将PDF转换为XLSX和CSV格式。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用JavaScript从PDF创建电子表格

**Aspose.PDF for JavaScript** 支持将PDF文件转换为Excel和CSV格式的功能。

{{% alert color="success" %}}
**尝试在线将PDF转换为Excel**

Aspose.PDF for JavaScript为您提供了一个免费的在线应用程序["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将PDF转换为Excel](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

转换操作取决于文档中的页数，可能非常耗时。
 因此，我们强烈建议使用 Web Workers。

此代码演示了一种将资源密集型的 PDF 文件转换任务卸载到 web worker 的方法，以防止阻塞主 UI 线程。它还提供了一种用户友好的方式来下载转换后的文件。

## 将 PDF 转换为 XLSX

```js

  /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理器*/
    const ffileToXlsX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*将 PDF 文件转换为 XlsX 并保存为 "ResultPDFtoXlsX.xlsx" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToXlsX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx"] }, [event.target.result]);
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
        link.innerHTML = "点击此处下载文件 " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```

以下的 JavaScript 代码片段展示了将 PDF 页面转换为 XlsX 文件的简单示例：

1. 选择一个 PDF 文件进行转换。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/) 函数。
1. 设置生成文件的名称，在本例中为 "ResultPDFtoXlsX.xlsx"。
1. 接下来，如果 'json.errorCode' 为 0，则您的结果文件将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此您的文件中会出现错误，那么有关此类错误的信息将包含在 'json.errorText' 文件中。
1. 最终， [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成链接，并允许您将结果文件下载到用户的操作系统。

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*将 PDF 文件转换为 XlsX 并保存为 "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*创建一个链接以下载结果文件*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


## 将 PDF 转换为 CSV

```js

    /*创建 Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '加载完成!' :
        (evt.data.json.errorCode == 0) ? 
          `文件(表)数量: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "text/csv", element) ) ?? ""}` : 
          `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffileToCSV = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*使用模板 "ResultPdfTablesToCSV{0:D2}.csv" 将 PDF 文件转换为 CSV（提取表），TAB 作为分隔符并保存 - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfTablesToCSV', "params": [event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t"] }, [event.target.result]);
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


以下的JavaScript代码片段展示了将PDF转换为CSV的简单示例：

1. 选择一个PDF文件进行转换。
1. 创建一个'FileReader'。
1. 执行[AsposePdfTablesToCSV](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftablestocsv/)函数。
1. 生成文件的名称被设置为，在此示例中为"ResultPdfTablesToCSV{0:D2}.csv"。
1. 接下来，如果'json.errorCode'为0，那么您的结果文件将被赋予您之前指定的名称。如果'json.errorCode'参数不等于0，并且相应地，您的文件中会有错误，那么有关此类错误的信息将包含在'json.errorText'文件中。
1. 最终，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)函数生成一个链接并允许您将结果文件下载到用户的操作系统中。

```js

  var ffileToCSV = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*使用模板"ResultPdfTablesToCSV{0:D2}.csv" 将PDF文件转换为CSV(提取表格) ({0}, {0:D2}, {0:D3}, ... 格式页码), TAB作为分隔符*/
        const json = AsposePdfTablesToCSV(event.target.result, e.target.files[0].name, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
        if (json.errorCode == 0) {
          document.getElementById('output').textContent = "文件(表格)数量: " + json.filesCount.toString();
          /*生成到结果文件的链接*/
          for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "text/csv");
        }
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```