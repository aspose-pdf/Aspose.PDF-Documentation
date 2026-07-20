---
title: Node.jsでPDFから添付ファイルを削除する
linktitle: 既存のPDFから添付ファイルを削除する
type: docs
weight: 10
url: /ja/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF は PDF ドキュメントから添付ファイルを削除できます。Node.js 環境を使用して Aspose.PDF による PDF ファイルの添付ファイルを削除します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Node.js via C++ を使用して PDF ファイルから添付ファイルを削除できます。PDF から添付ファイルを削除したい場合は、次のものを使用できます [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) 関数。 
Node.js 環境で PDF ファイルから添付ファイルを削除するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出し `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 添付ファイルを削除する PDF ファイルの名前を指定します。
1. 呼び出し `AsposePdf` Promiseとして、添付ファイルを削除する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. 添付ファイルを削除します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfDeleteAttachments.pdf" に保存されます。json.errorCode パラメーターが 0 でなく、それに応じてファイルにエラーが表示された場合、エラー情報は 'json.errorText' に含まれます。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 添付ファイルを削除する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/).
1. 添付ファイルを削除します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfDeleteAttachments.pdf" に保存されます。json.errorCode パラメーターが 0 でなく、それに応じてファイルにエラーが表示された場合、エラー情報は 'json.errorText' に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```