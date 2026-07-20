---
title: Node.js で PDF から画像を抽出する
linktitle: PDF から画像を抽出する
type: docs
weight: 20
url: /ja/nodejs-cpp/extract-images-from-the-pdf-file/
description: C++ ツールキットを介した Aspose.PDF for Node.js via C++ を使用して PDF から画像の一部を抽出する方法。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Node.js 環境で PDF ファイルから画像を抽出する

PDF ドキュメントから画像を抽出したい場合は、次のものを使用できます [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) 関数。 
この関数に 3 つの引数、入力ファイル名と出力ファイル名、そして解像度を渡す必要があります。
Node.js を使用して PDF ファイルから画像を抽出するための、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 画像を抽出する PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、画像抽出の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. PDF ファイルから画像を抽出します。その結果、‘json.errorCode’ が 0 の場合、操作の結果は “ResultPdfExtractImage{0:D2}.jpg” に保存されます。{0:D2} は 2 桁形式のページ番号を表します。画像は 150 DPI の解像度で保存されます。‘json.errorCode’ パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は ‘json.errorText’ に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. 画像を抽出する PDF ファイルの名前を指定してください。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/).
1. PDF ファイルから画像を抽出します。その結果、‘json.errorCode’ が 0 の場合、操作の結果は “ResultPdfExtractImage{0:D2}.jpg” に保存されます。{0:D2} は 2 桁形式のページ番号を表します。画像は 150 DPI の解像度で保存されます。‘json.errorCode’ パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は ‘json.errorText’ に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
    console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```
