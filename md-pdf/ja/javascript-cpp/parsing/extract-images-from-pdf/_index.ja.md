---
title: PDFから画像を抽出するJavaScript
linktitle: PDFから画像を抽出する
type: docs
weight: 20
url: /javascript-cpp/extract-images-from-the-pdf-file/
description: Aspose.PDF for JavaScriptツールキットを使用してPDFから画像の一部を抽出する方法。
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDFのWebツールキットを使用すると、PDFファイルから簡単に画像を抽出できます。

PDFドキュメントから画像を抽出したい場合は、[AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/)関数を使用できます。
JavaScriptを介してC++を使用してPDFファイルから画像を抽出するために、以下のコードスニペットを確認してください。

1. 'FileReader'を作成します。
1. [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/)関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では「ResultPdfExtractImage{0:D2}.jpg」です。

1. 次に、'json.errorCode'が0の場合、結果ファイルへのリンクを取得できます。'json.errorCode'パラメータが0と等しくない場合、およびそれに応じてファイルにエラーが発生する場合、そのようなエラーに関する情報は'json.errorText'ファイルに含まれます。
1. その結果、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)関数はリンクを生成し、ユーザーのオペレーティングシステムに結果のファイルをダウンロードすることができます。

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*テンプレート"ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... ページ番号の形式)、解像度150 DPIでPDFファイルから画像を抽出して保存*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "ファイル(画像)数: " + json.filesCount.toString();
        /*結果ファイルへのリンクを作成*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```


## Web Workersの使用

```js

  /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? 
          `ファイル(画像)の数: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*テンプレート"ResultPdfExtractImage{0:D2}.jpg"（{0}, {0:D2}, {0:D3}などのフォーマットページ番号）、解像度150 DPIでPDFファイルから画像を抽出して保存*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするリンクを作成*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "こちらをクリックしてファイル " + filename + " をダウンロード";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```