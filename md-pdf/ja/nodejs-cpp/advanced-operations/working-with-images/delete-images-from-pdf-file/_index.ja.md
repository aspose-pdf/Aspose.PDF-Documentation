---
title: Node.jsでPDFファイルから画像を削除する
linktitle: 画像を削除
type: docs
weight: 20
url: /nodejs-cpp/delete-images-from-pdf-file/
description: このセクションでは、Aspose.PDF for Node.js via C++を使用してPDFファイルから画像を削除する方法を説明します。
lastmod: "2023-11-16"
---

Aspose.PDF for Node.js via C++を使用して、PDFファイルから画像を削除することができます。

PDFから画像を削除したい場合は、[AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/)関数を使用することができます。Node.js環境で画像を削除するための次のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 画像が削除されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、画像を削除する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/)を呼び出します。

1. PDFから画像を削除します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfDeleteImages.pdf"に保存されます。json.errorCodeパラメータが0でない場合、そして結果としてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /* PDFファイルから画像を削除し、"ResultPdfDeleteImages.pdf"に保存します */
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 画像を削除するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) を呼び出します。
1. PDFから画像を削除します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPdfDeleteImages.pdf" に保存されます。json.errorCode パラメータが0でなく、その結果、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*PDFファイルから画像を削除し、"ResultPdfDeleteImages.pdf" に保存する*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```