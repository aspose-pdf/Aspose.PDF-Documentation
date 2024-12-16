---
title: JavaScript 経由で C++ を使用して PDF リソースを最適化する
linktitle: PDF リソースを最適化
type: docs
weight: 15
url: /ja/javascript-cpp/optimize-pdf-resources/
description: JavaScript ツールを使用して高速ウェブビューのために PDF ファイルのリソースを最適化します。
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## PDF リソースを最適化する

ドキュメントのリソースを最適化する:

  1. ドキュメントページで使用されていないリソースが削除されます
  1. 同じリソースが1つのオブジェクトに結合されます
  1. 使用されていないオブジェクトが削除されます

1. 最適化する PDF ファイルを選択します。
1. 'FileReader' を作成します。
1. [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfoptimizeresource/) 関数が実行されます。
1. 結果のファイル名が設定されます。この例では "ResultPdfOptimizeResource.pdf" です。

1. 次に、'json.errorCode' が 0 の場合、DownloadFile は前に指定した名前になります。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが発生し、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。
1. 結果として、[DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) 関数はリンクを生成し、結果のファイルをユーザーのオペレーティングシステムにダウンロードできるようにします。

次のコードスニペットは、PDF ドキュメントを最適化する方法を示しています。

```js

    var ffilePdfOptimizeResource = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルのリソースを最適化し、"ResultPdfOptimizeResource.pdf"として保存する*/
        const json = AsposePdfOptimizeResource(event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*結果ファイルをダウンロードするリンクを作成する*/
        DownloadFile(json.fileNameResult, "application/pdf");
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```


## Web Workers の使用

```js

    /* Web Worker を作成 */
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Worker からのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ? `結果:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `エラー: ${evt.data.json.errorText}`;

    /* イベントハンドラー */
    const ffilePdfOptimizeResource = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /* PDFファイルのリソースを最適化し、"ResultPdfOptimizeResource.pdf" として保存 - Web Worker に依頼 */
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfOptimizeResource', "params": [event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [コードスニペット]

    /* 結果ファイルをダウンロードするためのリンクを作成 */
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