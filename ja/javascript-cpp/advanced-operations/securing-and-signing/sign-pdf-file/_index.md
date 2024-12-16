---
title: JavaScript経由でC++を使用してPDFにデジタル署名を追加する
linktitle: PDFにデジタル署名
type: docs
weight: 70
url: /ja/javascript-cpp/sign-pdf/
description: JavaScript経由でC++を使用してPDF文書にデジタル署名を付ける。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF文書におけるデジタル署名は、文書の真正性と完全性を確認する方法です。これは、PDF文書を秘密鍵とデジタル証明書を使用して電子的に署名するプロセスです。この署名により、文書が署名以降変更されていないこと、および署名者が承認する者であることが保証されます。JavaScriptでPDFに署名するには、Aspose.PDFツールを使用します。

Aspose.PDF for JavaScript via C++は、[AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/)を使用してPDFファイルにデジタル署名を付ける機能をサポートしています。

## デジタル署名でPDFに署名する

```js

    /*デフォルトのPKCS7キーのファイル名を設定する*/
    var fileSign = "/test.pfx";

    var ffileSign = function (e) {
      const file_reader = new FileReader();
      /*PKCS7キーのファイル名を設定する*/
      fileImage = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*BLOBをメモリFSに保存して処理する*/
        AsposePdfPrepare(event.target.result, fileSign);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*デフォルトの画像（署名の見た目）のファイル名を設定する*/
    var signatureAppearance = "/Aspose.jpg";

    var ffileImage = function (e) {
      const file_reader = new FileReader();
      /*画像のファイル名を設定する*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = (event) => {
        /*BLOBをメモリFSに保存して処理する*/
        AsposePdfPrepare(event.target.result, signatureAppearance);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    var ffileSignPKCS7 = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        let pswSign = document.getElementById("passwordSign").value;
        /*デジタル署名でPDFファイルに署名し、"ResultSignPKCS7.pdf"を保存する*/
        const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするリンクを作成する*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


### Web Workersの使用

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ?
          `結果:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'ファイルが準備されました!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*デフォルトのPKCS7キーのファイル名を設定*/
    var fileSign = "test.pfx";
    /*デフォルトの画像（署名の外観）ファイル名を設定: 'Aspose.jpg'は既に読み込まれています。'settings.json'の設定を参照してください。*/
    var signatureAppearance = "Aspose.jpg";

    /*イベントハンドラ*/
    const ffileSignPKCS7 = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const pageNum = 1;
        const pswSign = document.getElementById("passwordSign").value;
        const setXIndent = 100;
        const setYIndent = 100;
        const setHeight = 200;
        const setWidth = 100;
        const reason = '理由';
        const contact = 'contact@test.com';
        const location = '場所';
        const isVisible = 1;
        /*PDFファイルにデジタル署名を付けて"ResultSignPKCS7.pdf"を保存 - Web Workerに依頼*/
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
      /*PKCS7キーのファイル名を設定*/
      fileSign = e.target.files[0].name;
      file_reader.onload = event => {
        /*処理のためにメモリFSにBLOBを保存*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, fileSign] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*画像のファイル名を設定*/
      signatureAppearance = e.target.files[0].name;
      file_reader.onload = event => {
        /*処理のためにメモリFSにBLOBを保存*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, signatureAppearance] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするためのリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ここをクリックしてファイル " + filename + " をダウンロード";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```