---
title: Node.jsでPDFに背景を追加する
linktitle: 背景を追加
type: docs
weight: 10
url: /ja/nodejs-cpp/add-background/
description: Node.jsでPDFファイルに背景画像を追加する
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

次のコードスニペットは、Node.jsで[AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/)関数を使用してPDFページに背景画像を追加する方法を示しています。

Node.js環境で背景画像を追加するには、次のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
2. 背景画像を追加するPDFファイルの名前を指定します。
3. `AsposePdf`をPromiseとして呼び出し、背景画像を追加する操作を実行します。成功した場合はオブジェクトを受け取ります。
4. 関数[AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/)を呼び出します。

1. PDFファイルに背景画像を追加します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultAddBackgroundImage.pdf"に保存されます。json.errorCodeパラメータが0でない場合、そしてファイルにエラーが発生した場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルに背景画像を追加し、"ResultBackgroundImage.pdf"として保存します*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 背景画像を追加するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合にオブジェクトを受け取ります。

1. 関数 [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) を呼び出します。
1. PDFファイルに背景画像を追加します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultAddBackgroundImage.pdf" に保存されます。json.errorCode パラメータが0でない場合、したがって、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*PDFファイルに背景画像を追加して "ResultBackgroundImage.pdf" を保存します*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```