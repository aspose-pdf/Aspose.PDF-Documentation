---
title: Node.js で PDF からテキストを抽出する
linktitle: PDF からテキストを抽出する
type: docs
weight: 10
url: /ja/nodejs-cpp/extract-text/
description: このセクションでは、Aspose.PDF for Node.js via C++ ツールキットを使用して PDF ドキュメントからテキストを抽出する方法について説明します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントのすべてのページからテキストを抽出する

PDF からテキストを抽出するのは容易ではありません。PDF 画像やスキャンされた PDF からテキストを抽出できる PDF リーダーはごく少数です。しかし **Aspose.PDF for Node.js via C++** ツールを使用すれば、Node.js 環境ですべての PDF ファイルから簡単にテキストを抽出できます。 

このコードは、指定された PDF ファイルからテキストを抽出し、抽出されたテキストまたは発生したエラーのいずれかをログに記録するために AsposePDFforNode.js モジュールを使用する方法を示しています。

コードスニペットを確認し、PDFからテキストを抽出する手順に従ってください:

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. テキストを抽出するPDFファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、テキスト抽出操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 抽出されたテキストは JSON オブジェクトに格納されます。そのため、'json.errorCode' が 0 の場合、抽出されたテキストは console.log を使用して表示されます。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. テキストを抽出するPDFファイルの名前を指定してください。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 抽出されたテキストは JSON オブジェクトに格納されます。そのため、'json.errorCode' が 0 の場合、抽出されたテキストは console.log を使用して表示されます。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
