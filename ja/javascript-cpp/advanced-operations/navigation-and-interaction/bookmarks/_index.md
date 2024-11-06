---
title: JavaScriptでPDFにブックマークを追加
linktitle: PDFのブックマーク
type: docs
weight: 10
url: ja/javascript-cpp/bookmark/
description: JavaScriptを使用してPDFドキュメントにブックマークを追加または削除できます。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 特定のブックマークをPDFドキュメントから削除する

Aspose.PDF for JavaScript via C++を使用してPDFファイルからブックマークを削除できます。ブラウザで直接結果を取得できます。

1. 'FileReader'を作成します。
1. [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletebookmarks/) 関数が実行されます。
1. 結果ファイルの名前を設定します。この例では "ResultPdfDeleteBookmarks.pdf" です。
1. 次に、'json.errorCode' が0の場合、DownloadFileに先ほど指定した名前が付けられます。'json.errorCode' パラメータが0でない場合、ファイルにエラーが発生し、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。

1. その結果、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティング システムに結果のファイルをダウンロードできるようにします。

```js

    var ffilePdfDeleteBookmarks = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*PDFファイルからブックマークを削除し、「ResultPdfDeleteBookmarks.pdf」として保存します*/
        const json = AsposePdfDeleteBookmarks(event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成する*/
        DownloadFile(json.fileNameResult, "application/pdf");
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Web ワーカーの使用

```js

    /*Web Workerを作成する*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラー*/
    const ffilePdfDeleteBookmarks = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*PDFファイルからブックマークを削除し、「ResultPdfDeleteBookmarks.pdf」として保存します - Web Workerに依頼する*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteBookmarks', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするためのリンクを作成する*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ここをクリックしてファイル " + filename + " をダウンロードします";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
        }
```