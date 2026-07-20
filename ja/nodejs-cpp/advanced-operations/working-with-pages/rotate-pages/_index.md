---
title: Node.jsでPDFページを回転
linktitle: PDFページを回転する
type: docs
weight: 50
url: /ja/nodejs-cpp/rotate-pages/
description: このトピックでは、Node.js環境でプログラム的に既存のPDFファイルのページ向きを回転させる方法について説明します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

このセクションでは、Aspose.PDF for Node.js via C++ を使用して既存のPDFファイルのページを回転させる方法について説明します。

PDFページを回転したい場合は、次のものを使用できます。 [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) 関数。この関数は回転値のための特別なパラメータ 'AsposePdfModule.Rotation' を使用します。これにより PDF を回転させる角度を設定できます。バリエーションは: None、90、180、または 270 度です。

Node.js 環境で PDF ページを回転させるために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出し `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 回転させる PDF ファイルの名前を指定します。
1. 呼び出し `AsposePdf` Promiseとして、ページを回転させる操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. すべての PDF ファイルを回転させます。回転は 270 度 (on270) に設定されています。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultRotation.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 回転させる PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. すべての PDF ファイルを回転させます。回転は 270 度 (on270) に設定されています。そのため、'json.errorCode' が 0 の場合、操作の結果は "ResultRotation.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```