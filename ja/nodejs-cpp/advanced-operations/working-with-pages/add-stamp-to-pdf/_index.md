---
title: Node.jsでPDFに画像スタンプを追加する
linktitle: PDFファイルの画像スタンプ
type: docs
weight: 60
url: /ja/nodejs-cpp/stamping/
description: Node.jsツールのAsposePdfAddStampを使用して、PDFドキュメントに画像スタンプを追加します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルに画像スタンプを追加する

PDF文書にスタンプを付けることは、紙の文書にスタンプを付けることと似ています。PDFファイル内のスタンプは、他者がPDFファイルを使用できないように保護したり、PDFファイルの内容のセキュリティを確認したりするなど、PDFファイルに追加情報を提供します。
以下を使用できます [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) Node.js を使用して PDF ファイルに画像スタンプを追加する関数です。

Node.js 環境で PDF ファイルに画像スタンプを追加するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 画像スタンプを追加する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promise として、画像スタンプを追加する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. PDF ファイルにスタンプを追加します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は "ResultImage.pdf" に保存されます。json.errorCode パラメータが 0 でなく、結果としてファイルにエラーが出た場合、エラー情報は ‘json.errorText’ に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 画像スタンプを追加する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. PDF ファイルにスタンプを追加します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は "ResultImage.pdf" に保存されます。json.errorCode パラメータが 0 でなく、結果としてファイルにエラーが出た場合、エラー情報は ‘json.errorText’ に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```