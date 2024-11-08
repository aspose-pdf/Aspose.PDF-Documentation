---
title: Node.jsで注釈を削除する
linktitle: 注釈を削除する
type: docs
weight: 10
url: /ja/nodejs-cpp/delete-annotation/
description: Aspose.PDF for Node.jsを使用してPDFファイルから注釈を削除することができます。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js via C++を使用して、PDFファイルから注釈を削除することができます。PDFから注釈を削除したい場合は、[AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/) 関数を使用できます。以下のコードスニペットを確認して、Node.js環境でPDFファイルから注釈を削除してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 注釈を削除するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、注釈を削除する操作を実行します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/) を呼び出します。
1. 注釈を削除します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfDeleteAnnotations.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*PDFファイルから注釈を削除し、"ResultPdfDeleteAnnotations.pdf"として保存します*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 注釈を削除するPDFファイルの名前を指定します。

1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/)を呼び出します。
1. 注釈を削除します。したがって、'json.errorCode'が0の場合、操作の結果は「ResultPdfDeleteAnnotations.pdf」に保存されます。json.errorCodeパラメータが0でない場合、そしてそれに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*PDFファイルから注釈を削除し、"ResultPdfDeleteAnnotations.pdf"に保存します*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```