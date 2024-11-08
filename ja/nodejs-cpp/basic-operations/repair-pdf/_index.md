---
title: Node.jsでPDFを修復する 
linktitle: PDFを修復する
type: docs
weight: 10
url: /ja/nodejs-cpp/repair-pdf/
description: このトピックでは、Node.js環境でPDFを修復する方法について説明します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.jsは、高品質なPDF修復を可能にします。PDFファイルがプログラムやブラウザに関係なく開かない場合があります。場合によってはドキュメントを復元できることがあり、以下のコードを試して自分で確認してください。
PDFドキュメントを修復したい場合は、[AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/)関数を使用できます。
Node.js環境でPDFファイルを修復するための以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 修復するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイル修復の操作を行います。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) を呼び出します。
1. PDFファイルを修復します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfRepair.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、つまり、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*PDFファイルを修復し、"ResultPdfRepair.pdf" を保存する*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 修復するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) を呼び出します。
1. PDFファイルを修復します。したがって、'json.errorCode' が0の場合、操作の結果は "ResultPdfRepair.pdf" に保存されます。json.errorCodeパラメータが0でない場合、つまり、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルを修復し、"ResultPdfRepair.pdf"に保存します*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```