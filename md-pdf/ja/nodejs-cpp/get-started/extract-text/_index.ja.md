---
title: Node.jsでPDFからテキストを抽出
linktitle: PDFからテキストを抽出
type: docs
weight: 10
url: /nodejs-cpp/extract-text/
description: このセクションでは、Aspose.PDF for Node.js via C++ ツールキットを使用してPDFドキュメントからテキストを抽出する方法について説明します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントのすべてのページからテキストを抽出

PDFからテキストを抽出するのは簡単ではありません。PDF画像やスキャンされたPDFからテキストを抽出できるPDFリーダーは限られています。しかし、**Aspose.PDF for Node.js via C++** ツールを使用すると、Node.js環境で簡単にすべてのPDFファイルからテキストを抽出できます。

このコードは、指定されたPDFファイルからテキストを抽出し、抽出されたテキストまたは遭遇したエラーをログに記録する方法を示しています。

コードスニペットを確認し、PDFからテキストを抽出する手順に従ってください：

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。

1. PDFファイルからテキストを抽出するための名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、テキストを抽出する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) を呼び出します。
1. 抽出されたテキストはJSONオブジェクトに保存されます。したがって、'json.errorCode'が0の場合、抽出されたテキストがconsole.logを使用して表示されます。json.errorCodeパラメータが0でない場合、ファイルにエラーが表示され、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルからテキストを抽出する*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。

1. テキストを抽出するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) を呼び出します。
1. 抽出されたテキストはJSONオブジェクトに格納されます。したがって、'json.errorCode' が0であれば、抽出されたテキストはconsole.logを使って表示されます。json.errorCodeパラメータが0でない場合、つまりファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルからテキストを抽出*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```