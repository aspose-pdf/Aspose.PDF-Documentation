---
title: 添加数字签名或通过 C++ 在 JavaScript 中对 PDF 进行数字签名
linktitle: 对 PDF 进行数字签名
type: docs
weight: 70
url: /javascript-cpp/sign-pdf/
description: 使用 JavaScript 通过 C++ 对 PDF 文档进行数字签名。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 文档中的数字签名是一种验证文档真实性和完整性的方法。这是使用私钥和数字证书对 PDF 文档进行电子签名的过程。此签名保证持有人文档自签名以来未被更改或修改，并且签名人是其批准的人。要使用 JavaScript 对 PDF 进行签名，请使用 Aspose.PDF 工具。

Aspose.PDF for JavaScript via C++ 支持使用 [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/) 对 PDF 文件进行数字签名。

## 使用数字签名签署 PDF

```js

    /*设置默认的 PKCS7 密钥文件名*/
    var fileSign = "/test.pfx";

    var ffileSign = function (e) {
      const file_reader = new FileReader();
      /*设置 PKCS7 密钥文件名*/
      fileImage = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*将 BLOB 保存到内存文件系统以进行处理*/
        AsposePdfPrepare(event.target.result, fileSign);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*设置默认图像（签名外观）文件名*/
    var signatureAppearance = "/Aspose.jpg";

    var ffileImage = function (e) {
      const file_reader = new FileReader();
      /*设置图像文件名*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*将 BLOB 保存到内存文件系统以进行处理*/
        AsposePdfPrepare(event.target.result, signatureAppearance);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    var ffileSignPKCS7 = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        let pswSign = document.getElementById("passwordSign").value;
        /*使用数字签名签署 PDF 文件并保存为 "ResultSignPKCS7.pdf"*/
        const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*创建一个链接以下载结果文件*/
        DownloadFile(json.fileNameResult, "application/pdf");
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
          `结果:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '文件已准备好!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `错误: ${evt.data.json.errorText}`;

    /*设置默认的 PKCS7 密钥文件名*/
    var fileSign = "test.pfx";
    /*设置默认的图像（签名外观）文件名: 'Aspose.jpg' 已加载, 请参阅 'settings.json' 中的设置*/
    var signatureAppearance = "Aspose.jpg";

    /*事件处理程序*/
    const ffileSignPKCS7 = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pageNum = 1;
        const pswSign = document.getElementById("passwordSign").value;
        const setXIndent = 100;
        const setYIndent = 100;
        const setHeight = 200;
        const setWidth = 100;
        const reason = '原因';
        const contact = 'contact@test.com';
        const location = '位置';
        const isVisible = 1;
        /*使用数字签名签署 PDF 文件并保存为 "ResultSignPKCS7.pdf" - 请求 Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSignPKCS7',
            "params": [event.target.result, e.target.files[0].name, pageNum, fileSign, pswSign, setXIndent, setYIndent,
                      setHeight, setWidth, reason, contact, location, isVisible, signatureAppearance, "ResultSignPKCS7.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileSign = e => {
      const file_reader = new FileReader();
      /*设置 PKCS7 密钥文件名*/
      fileSign = e.target.files[0].name;
      file_reader.onload = event => {
        /*将 BLOB 保存到内存文件系统中进行处理*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, fileSign] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*设置图像文件名*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = event => {
        /*将 BLOB 保存到内存文件系统中进行处理*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, signatureAppearance] },
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