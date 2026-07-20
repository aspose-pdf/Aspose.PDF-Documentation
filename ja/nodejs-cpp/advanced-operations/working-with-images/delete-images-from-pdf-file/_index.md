---
title: Node.js で PDF ファイルから画像を削除する
linktitle: 画像を削除
type: docs
weight: 20
url: /ja/nodejs-cpp/delete-images-from-pdf-file/
description: このセクションでは、Aspose.PDF for Node.js via C++ を使用して PDF ファイルから画像を削除する方法を説明します。
lastmod: "2026-07-18"
---


Aspose.PDF for Node.js via C++ を使用して、PDF ファイルから画像を削除できます。

PDF から画像を削除したい場合は、次のものを使用できます [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) 関数。 
Node.js 環境で画像を削除するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 画像を削除する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promiseとして画像削除の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. PDF から画像を削除します。その結果、 'json.errorCode' が 0 の場合は、操作の結果が "ResultPdfDeleteImages.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが表示され、そのエラー情報は 'json.errorText' に含まれます。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 画像を削除する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. PDF から画像を削除します。その結果、 'json.errorCode' が 0 の場合は、操作の結果が "ResultPdfDeleteImages.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが表示され、そのエラー情報は 'json.errorText' に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```