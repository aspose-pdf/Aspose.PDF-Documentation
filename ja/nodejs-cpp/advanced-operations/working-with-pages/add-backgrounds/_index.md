---
title: Node.jsでPDFに背景を追加
linktitle: 背景を追加
type: docs
weight: 10
url: /ja/nodejs-cpp/add-background/
description: Node.jsでPDFファイルに背景画像を追加
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

以下のコードスニペットは、PDFページに背景画像を追加する方法を示しています [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) Node.jsの関数です。

Node.js 環境で背景画像を追加するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 背景画像を追加する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promiseとして、背景画像を追加する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. PDF ファイルに背景画像を追加します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultAddBackgroundImage.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 背景画像を追加する PDF ファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. PDF ファイルに背景画像を追加します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultAddBackgroundImage.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```