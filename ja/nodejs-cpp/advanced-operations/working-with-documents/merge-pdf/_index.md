---
title: Node.jsでPDFをマージする方法
linktitle: PDFファイルをマージする
type: docs
weight: 20
url: /ja/nodejs-cpp/merge-pdf/
description: このページでは、Aspose.PDF for Node.js via C++ を使用して PDF ドキュメントを単一の PDF ファイルにマージする方法を説明します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Node.jsで2つのPDFを単一のPDFにマージまたは結合する

大量のドキュメントを扱う作業では、ファイルの結合やマージは非常に一般的なタスクです。ドキュメントや画像をスキャン、処理、整理する際に、複数のファイルが作成されることがあります。
しかし、すべてを1つのファイルに保存する必要がある場合はどうでしょうか？あるいは、複数のドキュメントを印刷したくないですか？Aspose.PDF for Node.js via C++ を使用して 2 つの PDF ファイルを連結します。

2つのPDFをマージしたい場合は、次を使用できます [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) 関数。 
Node.js 環境で 2 つの PDF ファイルをマージするために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. マージする PDF ファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして、マージ操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. 2 つの PDF ファイルをマージします。したがって、`json.errorCode` が 0 の場合、操作の結果は “ResultMerge.pdf” に保存されます。`json.errorCode` パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は `json.errorText` に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. マージする PDF ファイルの名前を指定してください。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. 2 つの PDF ファイルをマージします。したがって、`json.errorCode` が 0 の場合、操作の結果は “ResultMerge.pdf” に保存されます。`json.errorCode` パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は `json.errorText` に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```