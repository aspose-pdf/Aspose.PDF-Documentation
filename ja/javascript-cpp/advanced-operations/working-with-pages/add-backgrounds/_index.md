---
title: JavaScriptを介してC++でPDFに背景を追加する
linktitle: 背景を追加
type: docs
weight: 10
url: ja/javascript-cpp/add-backgrounds/
description: JavaScriptを介してC++でPDFファイルに背景画像を追加します。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

次のコードスニペットは、JavaScriptを使用して[AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/)関数を使用し、PDFページに背景画像を追加する方法を示しています。

次のコードスニペットでは、内部ファイルシステムでの作業を続けるために画像をアップロードします：

1. 'FileReader'を作成します。
1. 画像のファイル名を設定します。
1. BLOBから画像ファイルを準備します。

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*画像のファイル名を設定する*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*BLOBから画像ファイルを準備（保存）する*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


次の例では、処理するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) 関数が実行されます。
1. 画像ファイルをPDFに追加し、「ResultBackgroundImage.pdf」として保存します。
1. 次に、'json.errorCode'が0の場合、DownloadFileには以前に指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、ファイルにエラーが発生し、そのようなエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、結果のファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

```js

  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*背景画像ファイルをPDFに追加し、「ResultBackgroundImage.pdf」として保存します*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするリンクを作成します*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Webワーカーの使用

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? 
          `結果:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            '画像準備完了!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*デフォルトの画像ファイル名を設定: 'Aspose.jpg' は既に読み込まれています。'settings.json'の設定を参照*/
    var fileBackgroundImage = "Aspose.jpg";

    /*イベントハンドラ*/
    const ffileAddBackgroundImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルに背景画像を追加し、"ResultBackgroundImage.pdf"として保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddBackgroundImage',
            "params": [event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*画像ファイル名を設定*/
      fileBackgroundImage = e.target.files[0].name;
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
        link.innerHTML = "ファイル " + filename + " をダウンロードするにはここをクリック";
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```