---
title: Node.js で PDF に画像を追加する
linktitle: 画像を追加
type: docs
weight: 10
url: /ja/nodejs-cpp/add-image-to-pdf/
description: このセクションでは、Aspose.PDF for Node.js via C++ を使用して既存の PDF ファイルに画像を追加する方法について説明します。
lastmod: "2026-07-18"
---

## 既存の PDF ファイルに画像を追加する

PDF ファイルに画像を追加するには複雑な特殊ツールが必要だと一般的に考えられています。しかし、Aspose.PDF for Node.js を使用すれば、Node.js 環境で必要な画像を PDF に素早く簡単に追加できます。

画像はファイルの末尾にのみ追加できるため、正しい例はスキャンしたドキュメントページがあり、それらを 1 つの PDF に変換することです。

画像を追加したい場合は、使用できます [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) 関数。 
Node.js 環境で画像を追加するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 画像が追加される PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、画像を追加する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. PDF の末尾に画像を追加します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultAddImage.pdf” に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は ‘json.errorText’ に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 画像が追加される PDF ファイルの名前を指定してください。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトが返されます。
1. 関数を呼び出す [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. PDF の末尾に画像を追加します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultAddImage.pdf” に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は ‘json.errorText’ に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```