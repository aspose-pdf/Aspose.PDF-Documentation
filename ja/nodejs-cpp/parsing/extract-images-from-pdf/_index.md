---
title: PDFから画像を抽出する方法 Node.js
linktitle: PDFから画像を抽出
type: docs
weight: 20
url: /ja/nodejs-cpp/extract-images-from-the-pdf-file/
description: Aspose.PDF for Node.js via C++ツールキットを使用して、PDFから画像の一部を抽出する方法。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Node.js環境でPDFファイルから画像を抽出する

PDFドキュメントから画像を抽出したい場合は、[AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/)関数を使用できます。
この関数には、入力ファイル名、出力ファイル名、解像度の3つの引数を渡す必要があります。
以下のコードスニペットを確認して、Node.jsを使用してPDFファイルから画像を抽出する方法を確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 画像を抽出するPDFファイルの名前を指定します。

1. `AsposePdf`をPromiseとして呼び出し、画像抽出の操作を行います。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/)を呼び出します。
1. PDFファイルから画像を抽出します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfExtractImage{0:D2}.jpg"に保存されます。ここで、{0:D2}は2桁の形式でページ番号を表します。画像は150 DPIの解像度で保存されます。もしjson.errorCodeパラメータが0でなく、それに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*テンプレート"ResultPdfExtractImage{0:D2}.jpg"でPDFファイルから画像を抽出し、解像度150 DPIで保存*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 画像を抽出する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数 [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) を呼び出します。
1. PDF ファイルから画像を抽出します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfExtractImage{0:D2}.jpg" に保存されます。ここで、{0:D2} は 2 桁の形式のページ番号を表します。画像は 150 DPI の解像度で保存されます。json.errorCode パラメータが 0 でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*PDF ファイルから "ResultPdfExtractImage{0:D2}.jpg" というテンプレートで画像を抽出し、150 DPI の解像度で保存します*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```