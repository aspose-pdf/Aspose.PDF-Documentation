---
title: Node.jsでのPDFのブックマーク
linktitle: PDFのブックマーク
type: docs
weight: 10
url: ja/nodejs-cpp/bookmark/
description: Node.js環境でPDFドキュメントにブックマークを追加または削除できます。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントから特定のブックマークを削除する

Aspose.PDF for Node.js via C++を使用して、PDFファイルからブックマークを削除することができます。PDFからブックマークを削除したい場合は、[AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) 関数を使用できます。Node.js環境でPDFファイルからブックマークを削除するには、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. ブックマークを削除するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ブックマークを削除する操作を実行します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) を呼び出します。
1. ブックマークを削除します。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfDeleteBookmarks.pdf" に保存されます。json.errorCode パラメーターが 0 でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*PDFファイルからブックマークを削除し、"ResultPdfDeleteBookmarks.pdf" に保存します*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. ブックマークを削除する PDF ファイルの名前を指定します。

1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/)を呼び出します。
1. ブックマークを削除します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfDeleteBookmarks.pdf"に保存されます。json.errorCodeパラメータが0でない場合、つまりファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js
    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*PDFファイルからブックマークを削除し、"ResultPdfDeleteBookmarks.pdf"に保存*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```