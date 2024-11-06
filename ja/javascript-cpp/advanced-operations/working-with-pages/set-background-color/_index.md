---
title: JavaScriptを介してC++でPDFの背景色を設定する
linktitle: 背景色を設定
type: docs
weight: 80
url: ja/javascript-cpp/set-background-color/
description: JavaScriptを介してC++でPDFファイルの背景色を設定します。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

以下のコードスニペットは、JavaScriptを使用して[AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/)関数を使用してPDFページの背景色を設定する方法を示しています。

次の例では、処理するPDFファイルを選択します。

1. 'FileReader'を作成します。
1. [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfsetbackgroundcolor/)関数が実行されます（16進形式“#RRGGBB”、ここでRRは赤、GGは緑、BBは青の16進整数です）。
1. PDFファイルの背景色を設定し、「ResultPdfSetBackgroundColor.pdf」として保存します。

1. 次に、'json.errorCode' が 0 の場合、DownloadFile には先に指定した名前が付けられます。'json.errorCode' パラメータが 0 でない場合は、ファイルにエラーが発生し、そのエラーに関する情報が 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、生成されたファイルをユーザーのオペレーティングシステムにダウンロードすることを可能にします。

```js

  var ffilePdfSetBackgroundColor = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルの背景色を設定し、"ResultPdfSetBackgroundColor.pdf"として保存します*/
        const json = AsposePdfSetBackgroundColor(event.target.result, e.target.files[0].name, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


## Web ワーカーの使用

```js

    /*Web ワーカーの作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web ワーカーからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffilePdfSetBackgroundColor = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const backgroundColor= "#426bf4";
        /*PDF ファイルの背景色を設定し、「ResultPdfSetBackgroundColor.pdf」として保存 - Web ワーカーに依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfSetBackgroundColor', "params": [event.target.result, e.target.files[0].name, backgroundColor, "ResultPdfSetBackgroundColor.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするためのリンクを作成*/
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