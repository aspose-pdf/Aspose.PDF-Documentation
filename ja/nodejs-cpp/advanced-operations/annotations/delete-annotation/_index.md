---
title: Node.js のアノテーションを削除
linktitle: アノテーションを削除
type: docs
weight: 10
url: /ja/nodejs-cpp/delete-annotation/
description: Aspose.PDF for Node.js を使用すると、PDF ファイルからアノテーションを削除できます。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js via C++ を使用して PDF ファイルから注釈を削除できます。PDF から注釈を削除したい場合は、次のものを使用できます [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/) 関数。 
Node.js 環境で PDF ファイルから注釈を削除するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 注釈を削除する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promise として、アノテーションを削除する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. 注釈を削除します。したがって、'json.errorCode' が 0 の場合、操作の結果は \"ResultPdfDeleteAnnotations.pdf\" に保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが表示された場合、エラー情報は 'json.errorText' に含まれます。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. 注釈を削除する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/).
1. 注釈を削除します。したがって、'json.errorCode' が 0 の場合、操作の結果は \"ResultPdfDeleteAnnotations.pdf\" に保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが表示された場合、エラー情報は 'json.errorText' に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```
