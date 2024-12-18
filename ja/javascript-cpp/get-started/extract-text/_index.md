---
title: JavaScriptを使用してPDFからテキストを抽出する
linktitle: PDFからテキストを抽出する
type: docs
weight: 10
url: /ja/javascript-cpp/extract-text/
description: このセクションでは、JavaScriptツールキットを使用してPDFドキュメントからテキストを抽出する方法について説明します。
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントのすべてのページからテキストを抽出する

PDFからテキストを抽出するのは簡単ではありません。多くのPDFリーダーは、PDF画像やスキャンされたPDFからテキストを抽出することができません。しかし、**Aspose.PDF for JavaScript via C++** ツールを使用すると、すべてのPDFファイルから簡単にテキストを抽出できます。

コードスニペットを確認し、PDFからテキストを抽出する手順に従ってください:

1. テキストを抽出するPDFファイルを選択します。
1. 'FileReader'を作成してテキストを読み取ります。
1. [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/) 関数が実行されます。

1. 次に、'json.errorCode' が 0 の場合、'json.extractText' に抽出されたコンテンツが含まれます。'json.errorCode' パラメーターが 0 でない場合は、ファイルにエラーがあり、エラーに関する情報が 'json.errorText' に含まれます。
1. 結果として、PDF から抽出されたテキストを含む文字列が取得されます。

```js

    var ffileExtract = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*PDFファイルからテキストを抽出*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```

## Web Worker の使用

```js

    /*Web Worker を作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Worker からのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ?
          evt.data.json.extractText :
          `エラー: ${evt.data.json.errorText}`; 

    /*イベントハンドラー*/
    const ffileExtract = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*PDFファイルからテキストを抽出 - Web Worker に依頼*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```