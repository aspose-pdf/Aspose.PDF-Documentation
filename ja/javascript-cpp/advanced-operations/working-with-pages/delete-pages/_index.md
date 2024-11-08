---
title: JavaScriptを介してC++でPDFページを削除する 
linktitle: PDFページを削除
type: docs
weight: 30
url: /ja/javascript-cpp/delete-pages/
description: Aspose.PDF for JavaScriptを介してC++でPDFファイルからページを削除できます。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for JavaScriptを介してC++でPDFファイルからページを削除できます。結果を直接ブラウザで取得できます。

1. 'FileReader'を作成します。
1. 削除するページ番号を指定します。
1. [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/) 関数が実行されます。
1. 結果として得られるファイルの名前が設定されます。この例では "ResultDeletePages.pdf" です。
1. 次に、'json.errorCode'が0の場合、指定した名前がDownloadFileに付けられます。'json.errorCode'パラメータが0でない場合、およびファイルにエラーがある場合、そのようなエラーに関する情報が'json.errorText'ファイルに含まれます。

1. その結果、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、結果ファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*文字列、インターバルを含むページ番号: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*配列、ページ番号の配列*/
      /*const numPages = [1,3];*/
      /*数値、ページ番号*/
      /*const numPages = 1;*/
      /*1-3ページを削除し、"ResultOptimize.pdf"として保存*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするリンクを作成*/
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
          `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*文字列、インターバルを含むページ番号: "7, 20, 22, 30-32, 33, 36-40, 46"*/
        const numPages = "1-3";
        /*配列、ページ番号の配列*/
        /*const numPages = [1,3];*/
        /*番号、ページ番号*/
        /*const numPages = 1;*/
        /*PDFファイルからページを削除し、"ResultDeletePages.pdf - Ask Web Worker"として保存*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

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