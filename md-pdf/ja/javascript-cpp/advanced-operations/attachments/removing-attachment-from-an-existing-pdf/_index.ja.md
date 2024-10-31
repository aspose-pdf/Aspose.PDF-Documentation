---
title: PDFから添付ファイルを削除するJavaScript
linktitle: 既存のPDFから添付ファイルを削除
type: docs
weight: 10
url: /javascript-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDFはPDFドキュメントから添付ファイルを削除できます。Aspose.PDFを使用してPDFファイルの添付ファイルを削除するJavaScript Webツールキットを使用します。
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for JavaScript via C++を使用して、PDFファイルから添付ファイルを削除できます。結果をブラウザで直接取得できます。

1. 'FileReader'を作成します。
1. [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteattachments/) 関数が実行されます。
1. 結果ファイルの名前が設定され、この例では「ResultPdfDeleteAttachments.pdf」となります。

1. 次に、'json.errorCode' が 0 の場合、DownloadFile には前に指定した名前が付けられます。'json.errorCode' パラメータが 0 と等しくない場合、したがってファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. その結果、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、生成されたファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

```js

    var ffilePdfDeleteAttachments = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*PDFファイルから添付ファイルを削除し、「ResultPdfDeleteAttachments.pdf」を保存する*/
        const json = AsposePdfDeleteAttachments(event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf");
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

    /* Web ワーカーを作成 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web ワーカーからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /* イベントハンドラー */
    const ffilePdfDeleteAttachments = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /* PDF ファイルから添付ファイルを削除して "ResultPdfDeleteAttachments.pdf" を保存 - Web ワーカーに依頼 */
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteAttachments', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteAttachments.pdf"] }, [event.target.result]);
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 結果ファイルをダウンロードするためのリンクを作成 */
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ここをクリックしてファイル " + filename + " をダウンロードしてください";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
        }
```