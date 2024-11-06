---
title: PDFからテキストを抽出する方法（Node.js）
linktitle: PDFからテキストを抽出する
type: docs
weight: 30
url: ja/nodejs-cpp/extract-text-from-pdf/
description: 本記事では、Aspose.PDF for Node.js via C++を使用してPDFドキュメントからテキストを抽出する様々な方法について説明します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントからテキストを抽出する

PDFドキュメントからテキストを抽出することは、非常に一般的で有用なタスクです。PDFからテキストを抽出することは、検索と可用性の向上から、ビジネス、研究、情報管理などの様々な分野でのデータの分析と自動化を可能にするために役立ちます。

PDFドキュメントからテキストを抽出したい場合は、[AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) 関数を使用できます。
Node.jsを通じてC++を使用してPDFファイルからテキストを抽出するための以下のコードスニペットを確認してください。

コードスニペットを確認し、PDFからテキストを抽出する手順に従ってください：

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. テキストを抽出するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、テキストを抽出する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/)を呼び出します。
1. 抽出されたテキストはJSONオブジェクトに格納されます。したがって、'json.errorCode'が0の場合、抽出されたテキストはconsole.logを使用して表示されます。json.errorCodeパラメータが0でない場合、つまりファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /* PDFファイルからテキストを抽出 */
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. テキストを抽出するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/)を呼び出します。
1. 抽出されたテキストはJSONオブジェクトに格納されます。したがって、'json.errorCode'が0の場合、抽出されたテキストはconsole.logを使用して表示されます。json.errorCodeパラメータが0でない場合、ファイルにエラーが表示され、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルからテキストを抽出する*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```