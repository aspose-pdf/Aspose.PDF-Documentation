---
title: JavaScript経由でC++を使用してPDFに画像を追加 
linktitle: 画像を追加
type: docs
weight: 10
url: ja/javascript-cpp/add-image-to-pdf/
description: このセクションでは、Aspose.PDF for JavaScriptを使用して既存のPDFファイルに画像を追加する方法について説明します。
lastmod: "2023-12-15"
---

## 既存のPDFファイルに画像を追加

PDFに画像を添付する必要がありますか？PDFの読みやすさを向上させたいですか？PDFに画像を追加すると、プレゼンテーションや履歴書がより見栄え良くなります。

一般的に、PDFファイルに画像を追加するには複雑な特別なツールが必要とされています。しかし、Aspose.PDF for JavaScriptを使用すれば、ブラウザ内で直接JavaScriptを使って簡単に必要な画像をPDFに追加できます。

既存のPDFファイルに画像を追加するには、以下の手順を実行します。

1. デフォルトの画像ファイル名を設定します。
1. 'FileReader' を作成します。
1. 画像ファイル名を設定します。
1. BLOBから画像ファイルを準備します。
1. [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/) 関数が実行されます。

1. 画像ファイルをPDFファイルの末尾に追加し、「ResultImage.pdf」として保存します。
1. 次に、'json.errorCode'が0の場合、DownloadFileには前に指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、ファイルにエラーがあり、そのようなエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードできるようにします。

以下のコードスニペットは、PDF文書に画像を追加する方法を示しています。

```js
  /*デフォルトの画像ファイル名を設定*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*画像ファイル名を設定*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*BLOBから画像ファイルを準備(保存)*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

次の例では、処理する画像を選択します：

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*画像ファイルをPDFファイルの最後に追加し、"ResultImage.pdf"を保存する*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするリンクを作成する*/
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
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ?
          `結果:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '画像が準備された！':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*デフォルトの画像ファイル名を設定する: 'Aspose.jpg'はすでにロードされている。'settings.json'の設定を参照*/
    var fileImage = "Aspose.jpg";

    /*イベントハンドラ*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*画像をPDFファイルの最後に追加し、"ResultImage.pdf"を保存する - Web Workerに依頼する*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*画像ファイル名を設定する*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*BLOBをメモリFSに保存して処理する*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするリンクを作成する*/
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