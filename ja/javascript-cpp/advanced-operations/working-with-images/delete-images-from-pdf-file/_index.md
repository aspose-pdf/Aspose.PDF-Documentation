---
title: JavaScriptを使用してPDFファイルから画像を削除する
linktitle: 画像を削除
type: docs
weight: 20
url: ja/javascript-cpp/delete-images-from-pdf-file/
description: このセクションでは、Aspose.PDF for JavaScriptを使用してPDFファイルから画像を削除する方法を説明します。
lastmod: "2022-02-17"
---

Aspose.PDF for JavaScriptを使用して、C++経由でPDFファイルから画像を削除することができます。ブラウザで直接結果を得ることができます。

1. 'FileReader'を作成します。
1. [AsposePdfDeleteImages](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeleteimages/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では "ResultPdfDeleteImages.pdf" です。
1. 次に、'json.errorCode' が0の場合、DownloadFileに先に指定した名前が付けられます。'json.errorCode' パラメータが0でない場合、つまりファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。

1. その結果、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、結果のファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

```js

    var ffilePdfDeleteImages = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*PDFファイルから画像を削除し、「ResultPdfDeleteImages.pdf」として保存する*/
        const json = AsposePdfDeleteImages(event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf");
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

    /*Web ワーカーを作成する*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web ワーカーからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラー*/
    const ffilePdfDeleteImages = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*PDFファイルから画像を削除し、「ResultPdfDeleteImages.pdf」として保存する - Web ワーカーに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteImages', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteImages.pdf"] }, [event.target.result]);
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