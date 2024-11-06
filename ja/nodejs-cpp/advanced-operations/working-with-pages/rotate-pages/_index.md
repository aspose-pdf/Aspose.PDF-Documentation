---
title: Node.jsでPDFページを回転する
linktitle: PDFページを回転する
type: docs
weight: 50
url: ja/nodejs-cpp/rotate-pages/
description: このトピックでは、Node.js環境で既存のPDFファイルのページの向きをプログラムで回転する方法について説明します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

このセクションでは、Aspose.PDF for Node.js via C++を使用して既存のPDFファイルのページを回転する方法について説明します。

PDFページを回転したい場合は、[AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/)関数を使用できます。この関数は、回転値のための特別なパラメーター 'AsposePdfModule.Rotation' を使用します。これにより、PDFを何度回転させる必要があるかを設定できます。選択肢には、None、90、180、または270度があります。

Node.js環境でPDFページを回転するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. `require` を呼び出し、`asposepdfnodejs` モジュールを `AsposePdf` 変数としてインポートします。

1. 回転するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ページを回転させる操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) を呼び出します。
1. すべてのPDFファイルを回転させます。回転は270度（on270）に設定されています。したがって、'json.errorCode'が0の場合、操作の結果は"ResultRotation.pdf"に保存されます。json.errorCodeパラメータが0でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFページを回転させて"ResultRotation.pdf"を保存します*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. 回転させるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功するとオブジェクトを受け取ります。
1. 関数[AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/)を呼び出します。
1. すべてのPDFファイルを回転させます。回転は270度（on270）に設定されています。したがって、'json.errorCode'が0の場合、操作の結果は「ResultRotation.pdf」に保存されます。json.errorCodeパラメータが0でなく、したがってファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFページを回転して"ResultRotation.pdf"として保存*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```