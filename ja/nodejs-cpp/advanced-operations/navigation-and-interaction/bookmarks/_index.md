---
title: Node.js の PDF のブックマーク
linktitle: PDF のブックマーク
type: docs
weight: 10
url: /ja/nodejs-cpp/bookmark/
description: Node.js 環境で PDF ドキュメントのブックマークを追加または削除できます。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントから特定のブックマークを削除する

Aspose.PDF for Node.js via C++ を使用して PDF ファイルからブックマークを削除できます。PDF からブックマークを削除したい場合は、使用できます [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) 関数。 
Node.js 環境で PDF ファイルからブックマークを削除するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出し `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. ブックマークを削除する PDF ファイルの名前を指定します。
1. 呼び出し `AsposePdf` Promiseとして、ブックマーク削除の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. ブックマークを削除します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfDeleteBookmarks.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. ブックマークを削除する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. ブックマークを削除します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfDeleteBookmarks.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```