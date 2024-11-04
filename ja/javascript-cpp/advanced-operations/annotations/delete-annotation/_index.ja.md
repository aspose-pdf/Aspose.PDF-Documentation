---
title: JavaScriptを使用して注釈を削除する
linktitle: 注釈を削除
type: docs
weight: 10
url: /javascript-cpp/delete-annotation/
description: Aspose.PDF for JavaScriptを使用してPDFファイルから注釈を削除できます。
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for JavaScriptを使用して、C++経由でPDFファイルから注釈を削除できます。結果を直接ブラウザで取得できます。

1. 'FileReader'を作成します。
1. [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteannotations/) 関数が実行されます。
1. 結果ファイルの名前が設定され、この例では "ResultPdfDeleteAnnotations.pdf" になります。
1. 次に、'json.errorCode'が0の場合、指定した名前でDownloadFileが提供されます。'json.errorCode' パラメータが0でない場合、ファイルにエラーがあり、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。

1. その結果、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果のファイルをダウンロードできるようにします。

```js

    var ffilePdfDeleteAnnotations = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*PDFファイルから注釈を削除し、"ResultPdfDeleteAnnotations.pdf"として保存する*/
        const json = AsposePdfDeleteAnnotations(event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成する*/
        DownloadFile(json.fileNameResult, "application/pdf");
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Web Workersの使用

```js

    /*Web Workerを作成する*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffilePdfDeleteAnnotations = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*PDFファイルから注釈を削除し、"ResultPdfDeleteAnnotations.pdf"として保存する - Web Workerに依頼する*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAnnotations', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAnnotations.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするためのリンクを作成する*/
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