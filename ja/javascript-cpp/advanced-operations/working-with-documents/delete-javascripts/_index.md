---
title: PDFファイルからのJavaScriptコードのクリア
linktitle: JavaScriptsを削除
type: docs
weight: 50
url: ja/javascript-cpp/delete-javascripts/
description: Aspose.PDFを使用してWeb上でPDFファイルからJavaScriptマクロをクリアします。
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFファイルからJavaScriptを削除することは、セキュリティとプライバシーの理由で必要になることがあります。PDFファイル内のJavaScriptは、悪意のある目的や望ましくない機能のために使用されることがあります。ブラウザで直接結果を取得できます。

1. 'FileReader'を作成します。
1. [AsposePdfDeleteJavaScripts](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletejavascripts/) 関数が実行されます。
1. 結果として得られるファイルの名前が設定されます。この例では「ResultPdfDeleteJavaScripts.pdf」です。

1. 次に、'json.errorCode' が 0 の場合、DownloadFile には前に指定した名前が付けられます。'json.errorCode' パラメータが 0 と等しくない場合、そしてそれに応じてファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数がリンクを生成し、結果のファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

```js

    var ffilePdfDeleteJavaScripts = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*PDFファイルからJavaScriptを削除し、「ResultPdfDeleteJavaScripts.pdf」を保存します*/
        const json = AsposePdfDeleteJavaScripts(event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成します*/
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

    /*イベントハンドラー*/
    const ffilePdfDeleteJavaScripts = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*PDFファイルからJavaScriptsを削除し、"ResultPdfDeleteJavaScripts.pdf"として保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteJavaScripts', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteJavaScripts.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするためのリンクを作成する*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ファイルをダウンロードするにはここをクリック " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
        }
```