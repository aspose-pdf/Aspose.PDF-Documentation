---
title: PDF/A を PDF 形式に変換する
linktitle: PDF/A を PDF 形式に変換する
type: docs
weight: 110
url: /javascript-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-01"
description: このトピックでは、Aspose.PDF を使用して PDF/A ファイルを PDF ドキュメントに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## PDF/A を PDF 形式に変換する

```js

  /*Web Worker を作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Worker からのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffilePdfAConvertToPDF = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDF/A ファイルを PDF に変換して "ResultConvertToPDF.pdf" として保存 - Web Worker に依頼*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAConvertToPDF', "params": [event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [コードスニペット]

    /*結果ファイルをダウンロードするリンクを作成*/
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


次のJavaScriptコードスニペットは、PDF/AをPDFに変換する簡単な例を示しています：

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaconverttopdf/) 関数が実行されます。
1. 結果ファイルの名前が設定され、この例では「ResultConvertToPDFA.pdf」となっています。
1. 次に、'json.errorCode'が0であれば、あなたのDownloadFileは以前に指定した名前が付けられます。'json.errorCode' パラメータが0でない場合、ファイルにエラーが発生し、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果的に、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることを可能にします。

```js

    var ffilePdfAConvertToPDF = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDF/AファイルをPDFに変換し、「ResultConvertToPDF.pdf」として保存します*/
        const json = AsposePdfAConvertToPDF(event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするためのリンクを作成します*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

```