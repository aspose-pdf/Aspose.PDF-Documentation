---
title: JavaScriptを使用してPDFからテキストを抽出
linktitle: PDFからテキストを抽出
type: docs
weight: 30
url: /javascript-cpp/extract-text-from-pdf/
description: この記事では、Aspose.PDF for JavaScriptを使用してPDFドキュメントからテキストを抽出するさまざまな方法について説明します。
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントからテキストを抽出

PDFドキュメントからテキストを抽出することは非常に一般的で有用な作業です。PDFからのテキスト抽出は、検索と利用可能性の向上から、ビジネス、研究、情報管理などのさまざまな分野でのデータの分析と自動化を可能にすることまで、さまざまな目的に役立ちます。

PDFドキュメントからテキストを抽出したい場合は、[AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) 関数を使用できます。JavaScriptを使用してC++経由でPDFファイルからテキストを抽出するために、以下のコードスニペットを確認してください。

1. 'FileReader'を作成します。

1. [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) 関数が実行されます。
1. 次に、'json.errorCode' が 0 の場合、結果ファイルへのリンクを取得できます。'json.errorCode' パラメータが 0 でない場合、つまりファイルにエラーがある場合、そのようなエラーに関する情報は 'json.errorText' ファイルに含まれます。

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

## Web Workers の使用

```js

    /*Web Workerの作成*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Web Workerからのエラー: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
        (evt.data == 'ready') ? '読み込み完了!' :
        (evt.data.json.errorCode == 0) ?
            evt.data.json.extractText :
            `エラー: ${evt.data.json.errorText}`; 

    /*イベントハンドラー*/
    const ffileExtract = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*PDFファイルからテキストを抽出 - Web Workerに依頼*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```