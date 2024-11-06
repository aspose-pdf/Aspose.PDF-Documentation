---
title: Aspose.PDFを使用したPDFの最適化 - JavaScript via C++
linktitle: PDFファイルの最適化
type: docs
weight: 10
url: ja/javascript-cpp/optimize-pdf/
description: JavaScriptツールを使用してPDFファイルを最適化および圧縮し、Web表示を高速化します。
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDFドキュメントの最適化

Aspose.PDF Toolkit for JavaScript via C++は、Web向けにPDFコンテンツを最適化することを可能にします。

Web向けの最適化、または線形化とは、PDFファイルをWebブラウザでのオンラインブラウジングに適したものにするプロセスを指します。ファイルをWeb表示用に最適化するには:

1. 最適化するPDFファイルを選択します。
1. 'FileReader'を作成します。
1. [AsposePdfOptimize](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfoptimize/) 関数が実行されます。
1. 結果ファイルの名前が設定されます。この例では「ResultOptimize.pdf」です。

1. 次に、'json.errorCode' が 0 の場合、DownloadFile には以前に指定した名前が付けられます。'json.errorCode' パラメータが 0 でない場合、したがってファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、ユーザーのオペレーティングシステムに結果ファイルをダウンロードすることを可能にします。

次のコードスニペットは、PDF ドキュメントを最適化する方法を示しています。

```js

  var ffileOptimize = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*PDFファイルを最適化し、"ResultOptimize.pdf"として保存*/
      const json = AsposePdfOptimize(event.target.result, e.target.files[0].name, "ResultOptimize.pdf");
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

    /* Web Workerを作成する */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ?
          `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `エラー: ${evt.data.json.errorText}`;

    /* イベントハンドラ */
    const ffileOptimize = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /* PDFファイルを最適化し"ResultOptimize.pdf"として保存 - Web Workerに依頼 */
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfOptimize', "params": [event.target.result, e.target.files[0].name, "ResultOptimize.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /* 結果ファイルをダウンロードするリンクを作成する */
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "ここをクリックしてファイルをダウンロード: " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```