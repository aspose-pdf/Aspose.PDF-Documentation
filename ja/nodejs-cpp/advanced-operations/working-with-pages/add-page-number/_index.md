---
title: Node.jsでPDFにページ番号付けを追加する
linktitle: ページ番号を追加
type: docs
weight: 100
url: /ja/nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C\u002B\u002B は、AsposePdfAddPageNum を使用して PDF ファイルにページ番号スタンプを追加できるようにします。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

ページ番号は、読者が文書のさまざまな部分を見つけやすくします。以下のコードスニペットは、これを使用して PDF ページにページ番号を追加する方法を示します。 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) Node.js の関数です。

Node.js 環境で PDF にページ番号を追加するため、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. ページ番号を追加する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promise として、ページ番号を追加する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. PDFファイルにページ番号を追加します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultAddPageNum.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add page number to a PDF-file save the "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. ページ番号を追加する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出します [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. PDFファイルにページ番号を追加します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultAddPageNum.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、そのエラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add page number to a PDF-file and save the "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```