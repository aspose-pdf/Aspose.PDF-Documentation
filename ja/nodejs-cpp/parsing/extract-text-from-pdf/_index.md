---
title: Node.js で PDF からテキストを解析する
linktitle: PDF からテキストを解析する
type: docs
weight: 30
url: /ja/nodejs-cpp/extract-text-from-pdf/
description: この記事では、Aspose.PDF for Node.js via C++ を使用して PDF ドキュメントからテキストを解析するさまざまな方法について説明します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントからテキストを解析する

PDF ドキュメントからテキストを解析することは、非常に一般的で有用な作業です。 
PDF からテキストを抽出することは、検索性と利用可能性の向上から、ビジネス、研究、情報管理などさまざまな分野でのデータの分析や自動化を可能にするまで、様々な目的に役立ちます。

PDF ドキュメントからテキストを抽出したい場合は、次のものを使用できます [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) 関数。 
Node.js via C++ を使用して PDF ファイルからテキストを抽出するために、以下のコードスニペットをご確認ください。

コードスニペットを確認し、手順に従って PDF からテキストを抽出してください:

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. テキストを抽出する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promiseとして、テキスト抽出の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 抽出されたテキストは JSON オブジェクトに格納されます。そのため、'json.errorCode' が 0 の場合は、console.log を使用して抽出テキストが表示されます。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

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

1. インポートする `asposepdfnodejs` モジュール。
1. テキストを抽出する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 抽出されたテキストは JSON オブジェクトに格納されます。そのため、'json.errorCode' が 0 の場合は、console.log を使用して抽出テキストが表示されます。'json.errorCode' パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```