---
title: Node.jsでPDFから添付ファイルを削除する
linktitle: 既存のPDFから添付ファイルを削除する
type: docs
weight: 10
url: ja/nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDFはPDFドキュメントから添付ファイルを削除できます。Node.js環境を使用してAspose.PDFでPDFファイルの添付ファイルを削除します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for Node.js via C++を使用して、PDFファイルから添付ファイルを削除できます。PDFから添付ファイルを削除したい場合は、[AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/)関数を使用できます。PDFファイルから添付ファイルを削除するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 添付ファイルを削除するPDFファイルの名前を指定します。

1. `AsposePdf`をPromiseとして呼び出し、添付ファイルを削除する操作を実行します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/)を呼び出します。
1. 添付ファイルを削除します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfDeleteAttachments.pdf"に保存されます。json.errorCodeパラメータが0でない場合、つまりファイルにエラーが発生した場合、エラー情報は'json.errorText'に含まれます。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*PDFファイルから添付ファイルを削除し、"ResultPdfDeleteAttachments.pdf"に保存します*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 添付ファイルを削除するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/)を呼び出します。
1. 添付ファイルを削除します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfDeleteAttachments.pdf"に保存されます。json.errorCodeパラメータが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /* PDFファイルから添付ファイルを削除し、"ResultPdfDeleteAttachments.pdf"として保存します */
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```