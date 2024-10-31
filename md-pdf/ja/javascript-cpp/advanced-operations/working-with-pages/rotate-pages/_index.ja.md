---
title: JavaScriptを使用してC++経由でPDFページを回転 
linktitle: PDFページを回転
type: docs
weight: 50
url: /javascript-cpp/rotate-pages/
description: このトピックでは、JavaScriptを使用してC++経由で既存のPDFファイルのページの向きをプログラムで回転する方法について説明します。
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

このセクションでは、JavaScriptを使用してC++経由で既存のPDFファイルでページの向きを横向きから縦向き、またはその逆に変更する方法について説明します。

1. 'FileReader'を作成します。
1. [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfrotateallpages/) 関数が実行されます。
1. 結果ファイルの名前を設定します。この例では "ResultRotation.pdf" です。

1. 次に、'json.errorCode'が0であれば、DownloadFileには前に指定した名前が付けられます。'json.errorCode'パラメータが0でない場合、ファイルにエラーが発生し、そのようなエラーに関する情報は'json.errorText'ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/)関数はリンクを生成し、生成されたファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

```js

  var ffileRotateAllPages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*すべてのページを回転させてPDFファイルを保存し、「ResultRotation.pdf」に名前を付ける*/
      const json = AsposePdfRotateAllPages(event.target.result, e.target.files[0].name, Module.Rotation.on270, "ResultRotation.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルのダウンロードリンクを作成する*/
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
        (evt.data.json.errorCode == 0) ?
          `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileRotateAllPages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const rotation = 'Module.Rotation.on270';
        /*PDFページを回転させ、"ResultRotation.pdf"として保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfRotateAllPages',
            "params": [event.target.result, e.target.files[0].name, rotation, "ResultRotation.pdf"] },
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
        link.innerHTML = "ファイルをダウンロードするにはここをクリック " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```