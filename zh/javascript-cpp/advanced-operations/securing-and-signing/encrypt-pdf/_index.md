---
title: 使用 JavaScript 加密 PDF
linktitle: 加密 PDF 文件
type: docs
weight: 50
url: /zh/javascript-cpp/encrypt-pdf/
description: 使用 Aspose.PDF for JavaScript via C++ 加密 PDF 文件。
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用用户密码或所有者密码加密 PDF 文件

如果您要发送包含机密信息的 PDF 附件的电子邮件，您可能希望先为其添加一些安全措施，以防止其落入不当之手。限制对 PDF 文档的未经授权访问的最佳方法是用密码保护它。为了轻松且安全地加密文档，您可以使用 Aspose.PDF for JavaScript via C++。

>加密 PDF 文件时，请指定不同的用户密码和所有者密码。

- 如果设置了**用户密码**，则需要提供该密码才能打开 PDF。Acrobat/Reader 会提示用户输入用户密码。如果密码不正确，文档将无法打开。
- 如果设置了**所有者密码**，则控制权限，例如打印、编辑、提取、评论等。
 Acrobat/Reader 将根据权限设置禁止这些操作。如果您想设置/更改权限，Acrobat 将需要此密码。

以下代码片段向您展示如何加密 PDF 文件。

1. 选择一个 PDF 文件进行加密。
1. 创建一个 'FileReader'。
1. 执行 [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/) 函数。
1. 设置结果文件的名称，在此示例中为 "ResultEncrypt.pdf"。
1. 接下来，如果 'json.errorCode' 为 0，那么您的 DownloadFile 将被赋予您之前指定的名称。如果 'json.errorCode' 参数不等于 0，因此您的文件中会出现错误，那么有关此类错误的信息将包含在 'json.errorText' 文件中。
1. 结果，[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 函数生成一个链接并允许您将结果文件下载到用户的操作系统。

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*使用密码 "user" 和 "owner" 加密 PDF 文件，并保存为 "ResultEncrypt.pdf"*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
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

    /* 创建 Web Worker */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`来自 Web Worker 的错误: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '已加载!' :
        (evt.data.json.errorCode == 0) ?
          `结果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `错误: ${evt.data.json.errorText}`;

    /* 事件处理程序 */
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'user';
        const password_owner = 'owner';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /* 使用密码 "user" 和 "owner" 加密 PDF 文件，并保存为 "ResultEncrypt.pdf" - 请求 Web Worker */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 创建一个链接以下载结果文件 */
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