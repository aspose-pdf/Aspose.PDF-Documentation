---
title: JavaScriptでPDFをPPTXに変換
linktitle: PDFをPowerPointに変換
type: docs
weight: 30
url: /ja/javascript-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-01"
description: Aspose.PDFを使用すると、JavaScriptを使ってPDFをPPTX形式に直接変換できます。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

変換操作はドキュメントのページ数に依存し、非常に時間がかかる場合があります。そのため、Web Workersの使用を強くお勧めします。

このコードは、リソースを多く消費するPDFファイルの変換タスクをWeb Workerにオフロードして、メインUIスレッドのブロックを防ぐ方法を示しています。また、変換されたファイルをダウンロードするためのユーザーフレンドリーな方法を提供します。

{{% alert color="success" %}}
**オンラインでPDFをPowerPointに変換してみてください**

Aspose.PDF for JavaScriptは、オンラインで無料アプリケーション["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)を提供しており、その機能や品質を試すことができます。


[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## PDFをPPTXに変換する

```js

  /*Web Workerを作成*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? '読み込み完了！' :
      (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

  /*イベントハンドラ*/
  const ffileToPptX = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*PDFファイルをPptXに変換し、"ResultPDFtoPptX.pptx"として保存 - Web Workerに依頼*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToPptX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx"] }, [event.target.result]);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  /*結果ファイルをダウンロードするリンクを作成*/
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


以下のJavaScriptコードスニペットは、PDFをPPTXファイルに変換する簡単な例を示しています。

1. 変換するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfToPptX](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftopptx/)関数が実行されます。
1. 結果ファイルの名前が設定され、この例では"ResultPDFtoPptX.pptx"です。
1. 次に、'json.errorCode'が0の場合、結果ファイルには前に指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、つまりファイルにエラーがある場合、そのエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)関数がリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

```js

  var ffileToPptX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルをPptXに変換し、"ResultPDFtoPptX.pptx"として保存*/
      const json = AsposePdfToPptX(event.target.result, e.target.files[0].name, "ResultPDFtoPptX.pptx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするためのリンクを作成*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.presentationml.presentation");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```