---
title: 更改PDF文件的密码
linktitle: 更改密码
type: docs
weight: 50
url: /zh/javascript-cpp/change-password-pdf/
description: 使用Aspose.PDF for JavaScript通过C++更改PDF文件的密码。
lastmod: "2023-09-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 更改PDF文件的密码

如果您想将PDF文件的密码从“owner”更改为“newowner”，请尝试以下代码片段：

1. 选择一个PDF文件。
1. 创建一个'FileReader'。
1. 执行[AsposePdfChangePassword](https://reference.aspose.com/pdf/javascript-cpp/security/asposepdfchangepassword/)函数。
1. 设置生成文件的名称，在此示例中为“ResultPdfChangePassword.pdf”。
1. 接下来，如果'json.errorCode'为0，则您的DownloadFile将获得您之前指定的名称。如果'json.errorCode'参数不等于0，那么您的文件中会有一个错误，关于此类错误的信息将包含在'json.errorText'文件中。

1. 因此，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接，并允许您将生成的文件下载到用户的操作系统。

```js

    var ffilePdfChangePassword = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*将 PDF 文件的密码从 "owner" 更改为 "newowner" 并保存为 "ResultPdfChangePassword.pdf"*/
        const json = AsposePdfChangePassword(event.target.result, e.target.files[0].name, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建下载结果文件的链接*/
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
        (evt.data.json.errorCode == 0) ? `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `错误: ${evt.data.json.errorText}`;

    /*事件处理程序*/
    const ffilePdfChangePassword = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const ownerPassword = 'owner'; /*拥有者密码*/
        const newUserPassword = "newuser"; /*新用户密码*/
        const newOwnerPassword = "newowner"; /*新拥有者密码*/
        /*将 PDF 文件的密码从 "owner" 更改为 "newowner" 并保存为 "ResultPdfChangePassword.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfChangePassword', "params": [event.target.result, e.target.files[0].name, ownerPassword, newUserPassword, newOwnerPassword, "ResultPdfChangePassword.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [代码片段]

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