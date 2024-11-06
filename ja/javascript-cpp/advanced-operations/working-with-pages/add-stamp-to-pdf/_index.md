---
title: JavaScriptとC++を使用してPDFに画像スタンプを追加する 
linktitle: PDFファイルへの画像スタンプ
type: docs
weight: 60
url: ja/javascript-cpp/stamping/
description: JavaScriptツールキットを使用してAsposePdfAddStamp関数でPDFドキュメントに画像スタンプを追加します。
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルに画像スタンプを追加する

PDFドキュメントにスタンプを押すことは、紙のドキュメントにスタンプを押すことに似ています。PDFファイルにスタンプを押すことで、他の人が利用するためにPDFファイルを保護することや、PDFファイルの内容の安全性を確認するなど、PDFファイルに追加情報を提供します。
JavaScriptを使用してPDFファイルに画像スタンプを追加するには、[AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/)関数を使用できます。

画像スタンプを追加するには、以下の手順に従います：

1. デフォルトの画像ファイル名を設定します。
1. 'FileReader'を作成します。
1. 画像ファイル名を設定します。
1. BLOBからスタンプファイルを準備します。

以下のコードスニペットは、PDFファイルに画像スタンプを追加する方法を示しています。

```js

  /*デフォルトのスタンプファイル名を設定する*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*スタンプファイル名を設定する*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*BLOBからスタンプファイルを準備（保存）する*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


1. 'FileReader'を作成します。
1. [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/)関数が実行されます。
1. 画像ファイルをPDFファイルの最後に追加し、「ResultImage.pdf」として保存します。
1. 次に、'json.errorCode'が0の場合、DownloadFileには以前に指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、つまりファイルにエラーがある場合は、そのエラーに関する情報が'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)関数はリンクを生成し、結果のファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*スタンプファイルをPDFファイルに挿入し、「ResultImage.pdf」として保存します*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするリンクを作成します*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Web Workersの使用

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了！' :
        (evt.data.json.errorCode == 0) ?
          `結果:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '画像が準備されました！':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*デフォルトのスタンプファイル名を設定: 'Aspose.jpg'は既にロードされています。'settings.json'の設定を参照*/
    var fileStamp = "Aspose.jpg";

    /*イベントハンドラ*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*PDFファイルにスタンプを追加し、「ResultStamp.pdf」として保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddStamp',
            "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_,
                      setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*スタンプファイル名を設定*/
      fileStamp = e.target.files[0].name;
      file_reader.onload = event => {
        /*処理のためにメモリFSにBLOBを保存*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*結果ファイルをダウンロードするためのリンクを作成*/
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