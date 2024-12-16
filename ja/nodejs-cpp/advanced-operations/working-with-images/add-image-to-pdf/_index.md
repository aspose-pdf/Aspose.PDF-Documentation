---
title: Node.jsでPDFに画像を追加する
linktitle: 画像を追加
type: docs
weight: 10
url: /ja/nodejs-cpp/add-image-to-pdf/
description: このセクションでは、Aspose.PDFを使用して既存のPDFファイルに画像を追加する方法を説明します。
lastmod: "2023-11-16"
---

## 既存のPDFファイルに画像を追加する

一般的には、PDFファイルに画像を追加するには複雑な特別なツールが必要だと考えられています。しかし、Aspose.PDF for Node.jsを使用すれば、Node.js環境で簡単に画像をPDFに追加することができます。

ファイルの末尾にのみ画像を追加できるので、スキャンしたドキュメントページを単一のPDFに変換するのが正しい例です。

画像を追加したい場合は、[AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/)関数を使用できます。Node.js環境で画像を追加するためには、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。

1. 画像が追加されるPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、画像を追加する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/)を呼び出します。
1. PDFの最後に画像を追加します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultAddImage.pdf"に保存されます。json.errorCodeパラメータが0でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルの最後に画像を追加し、"ResultImage.pdf"として保存します*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 画像を追加するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/)を呼び出します。
1. PDFの最後に画像を追加します。したがって、'json.errorCode'が0の場合、操作の結果は「ResultAddImage.pdf」に保存されます。json.errorCodeパラメータが0でなく、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*PDFファイルの最後に画像を追加し、「ResultImage.pdf」を保存する*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```