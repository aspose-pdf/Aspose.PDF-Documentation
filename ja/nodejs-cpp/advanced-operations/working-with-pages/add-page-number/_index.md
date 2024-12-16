---
title: PDFにページ番号を追加する方法 (Node.js)
linktitle: ページ番号を追加
type: docs
weight: 100
url: /ja/nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++を使用してPDFファイルにページ番号スタンプを追加する方法をAsposePdfAddPageNumを通じて説明します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

ページ番号は、読者が文書の異なる部分を見つけやすくします。以下のコードスニペットは、Node.jsで[AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/)関数を使用してPDFページにページ番号を追加する方法を示しています。

Node.js環境でPDFにページ番号を追加するための以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出して`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. ページ番号を追加するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ページ番号を追加する操作を実行します。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) を呼び出します。
1. PDFファイルにページ番号を追加します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultAddPageNum.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、つまり、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルにページ番号を追加し、"ResultAddPageNum.pdf" を保存します*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. ページ番号を追加するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。

1. 関数 [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) を呼び出します。
1. PDFファイルにページ番号を追加します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultAddPageNum.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、つまりファイルにエラーが表示される場合は、エラー情報が 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /* PDFファイルにページ番号を追加し、「ResultAddPageNum.pdf」として保存します */
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```