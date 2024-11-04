---
title: PDFファイルのパスワードを変更する
linktitle: パスワードを変更する
type: docs
weight: 50
url: /javascript-cpp/change-password-pdf/
description: Aspose.PDF for JavaScript via C++でPDFファイルのパスワードを変更する。
lastmod: "2023-09-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFファイルのパスワードを変更する

PDFファイルのパスワードを「owner」から「newowner」に変更したい場合は、次のコードスニペットを試してください:

1. PDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfChangePassword](https://reference.aspose.com/pdf/javascript-cpp/security/asposepdfchangepassword/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では「ResultPdfChangePassword.pdf」です。
1. 次に、'json.errorCode'が0の場合、指定した名前でDownloadFileが与えられます。'json.errorCode'パラメータが0でない場合、つまりファイルにエラーがある場合、そのようなエラーについての情報は 'json.errorText' ファイルに含まれます。

1. その結果、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることを可能にします。

```js

    var ffilePdfChangePassword = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルのパスワードを"owner"から"newowner"に変更し、"ResultPdfChangePassword.pdf"として保存する*/
        const json = AsposePdfChangePassword(event.target.result, e.target.files[0].name, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするリンクを作成する*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Web Workersの利用

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffilePdfChangePassword = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const ownerPassword = 'owner'; /*オーナーパスワード*/
        const newUserPassword = "newuser"; /*新しいユーザーパスワード*/
        const newOwnerPassword = "newowner"; /*新しいオーナーパスワード*/
        /*PDFファイルのパスワードを"owner"から"newowner"に変更し、"ResultPdfChangePassword.pdf"として保存する - Web Workerを使用*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfChangePassword', "params": [event.target.result, e.target.files[0].name, ownerPassword, newUserPassword, newOwnerPassword, "ResultPdfChangePassword.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [コードスニペット]

    /*結果ファイルをダウンロードするリンクを作成する*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ファイル " + filename + " をダウンロードするにはここをクリック";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```