---
title: JavaScript経由でC++を使用してPDFを修復する
linktitle: PDFを修復
type: docs
weight: 10
url: /ja/javascript-cpp/repair-pdf/
description: このトピックでは、JavaScriptを介してC++でPDFを修復する方法について説明します
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for JavaScriptは、高品質のPDF修復を可能にします。PDFファイルは、プログラムやブラウザに関係なく、何らかの理由で開かない場合があります。場合によっては、ドキュメントを復元できることがあります。以下のコードを試して、自分で確認してください。

1. 'FileReader'を作成します。
1. [AsposePdfRepair](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfrepair/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では "ResultPdfRepair.pdf" です。
1. 次に、'json.errorCode' が0の場合、結果ファイルへのリンクを取得できます。'json.errorCode' パラメータが0でなく、ファイルにエラーがある場合、そのエラーに関する情報は 'json.errorText' ファイルに含まれています。

1. その結果、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果のファイルをダウンロードできるようにします。

```js

    var ffilePdfRepair = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルを修復し、「ResultPdfRepair.pdf」を保存する*/
        const json = AsposePdfRepair(event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成する*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Web Workersを使用する

```js

    /*Web Workerを作成する*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラー*/
    const ffilePdfRepair = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルを修復し、「ResultPdfRepair.pdf」を保存する - Web Workerに依頼する*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfRepair', "params": [event.target.result, e.target.files[0].name, "ResultPdfRepair.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [コードスニペット]

    /*結果ファイルをダウンロードするためのリンクを作成する*/
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