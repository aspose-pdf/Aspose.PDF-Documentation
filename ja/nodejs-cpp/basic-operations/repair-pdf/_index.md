---
title: Node.js で PDF を修復する
linktitle: PDF を修復する
type: docs
weight: 10
url: /ja/nodejs-cpp/repair-pdf/
description: このトピックでは、Node.js 環境で PDF を修復する方法について説明します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js は高品質な PDF 修復を可能にします。プログラムやブラウザに関係なく、さまざまな理由で PDF ファイルが開けないことがあります。場合によってはドキュメントを復元できることがありますので、以下のコードを試して確認してください。
PDF ドキュメントを修復したい場合は、次のものを使用できます [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) function。 
Node.js 環境で PDF ファイルを修復するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 修復対象の PDF ファイル名を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、ファイル修復の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. PDFファイルを修復します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfRepair.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. 修復対象の PDF ファイル名を指定してください。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. PDFファイルを修復します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfRepair.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```