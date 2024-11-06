---
title: Node.jsでPDFの背景色を設定する
linktitle: 背景色を設定する
type: docs
weight: 80
url: ja/nodejs-cpp/set-background-color/
description: C++を介してNode.jsでPDFファイルの背景色を設定します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFの背景色を設定したい場合は、[AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) 関数を使用できます。

以下のコードスニペットを確認して、Node.js環境でPDFの背景色を設定してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 背景色を設定したいPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、背景色を設定する操作を実行します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) を呼び出します。
1. PDFファイルの背景色を設定します。この関数には3つの引数を渡す必要があります: 入力ファイル名、16進数形式の希望する色、および出力ファイル名です。したがって、'json.errorCode'が0の場合、操作の結果は"ResultRotation.pdf"に保存されます。json.errorCodeパラメータが0でない場合、そしてそれに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* PDFファイルの背景色を設定し、"ResultPdfSetBackgroundColor.pdf"として保存 */
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 背景色を設定したいPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/)を呼び出します。
1. PDFファイルの背景色を設定します。背景色は青の色合いを表す16進数のカラーコードである"#426bf4"に設定されます。したがって、'json.errorCode'が0である場合、操作の結果は"ResultRotation.pdf"に保存されます。json.errorCodeパラメータが0でない場合、つまりファイルにエラーが発生した場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルの背景色を設定し、"ResultPdfSetBackgroundColor.pdf"に保存します*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```