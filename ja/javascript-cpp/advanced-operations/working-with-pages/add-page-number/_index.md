---
title: JavaScript経由でC++を使用してPDFにページ番号を追加 
linktitle: ページ番号を追加
type: docs
weight: 100
url: /ja/javascript-cpp/add-page-number/
description: Aspose.PDF for JavaScript via C++を使用すると、AsposePdfAddPageNumを使用してPDFファイルにページ番号スタンプを追加できます。
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

すべてのドキュメントにはページ番号が必要です。ページ番号は、読者が文書の異なる部分を見つけやすくします。

**Aspose.PDF for JavaScript via C++**を使用すると、[AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/)を使用してページ番号を追加できます。

1. 'FileReader'を作成します。
1. [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/)関数が実行されます。
1. 結果のファイル名が設定されます。この例では「ResultAddPageNum.pdf」です。

1. 次に、'json.errorCode' が 0 の場合、DownloadFile には以前に指定した名前が付けられます。'json.errorCode' パラメーターが 0 でない場合、したがってファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、結果として得られるファイルをユーザーのオペレーティングシステムにダウンロードすることを可能にします。

```js
  var ffileAddPageNum = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*ページ番号を PDF ファイルに追加し、"ResultAddPageNum.pdf" として保存する*/
      const json = AsposePdfAddPageNum(event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*結果ファイルをダウンロードするリンクを作成する*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```


## Web ワーカーの使用

```js

    /*Web Workerを作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ?
          `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /*イベントハンドラ*/
    const ffileAddPageNum = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルにページ番号を追加し、「ResultAddPageNum.pdf」として保存 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddPageNum', "params": [event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf"] },
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
        link.innerHTML = "ファイルをダウンロードするにはここをクリック " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```