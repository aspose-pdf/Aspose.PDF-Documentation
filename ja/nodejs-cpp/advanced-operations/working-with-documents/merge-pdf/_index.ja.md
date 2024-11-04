---
title: Node.jsでPDFをマージする方法
linktitle: PDFファイルをマージ
type: docs
weight: 20
url: /nodejs-cpp/merge-pdf/
description: このページでは、Aspose.PDF for Node.js via C++を使用して、PDFドキュメントを単一のPDFファイルにマージする方法を説明します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Node.jsで2つのPDFを単一のPDFにマージまたは結合する

大量のドキュメントを扱う際に、ファイルを結合およびマージすることは非常に一般的な作業です。ドキュメントや画像をスキャン、処理、整理すると、複数のファイルが作成されることがあります。
しかし、すべてを1つのファイルに保存する必要がある場合はどうすればよいでしょうか？または、複数のドキュメントを印刷したくない場合は？Aspose.PDF for Node.js via C++を使用して、2つのPDFファイルを連結します。

2つのPDFをマージしたい場合は、[AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/)関数を使用できます。
以下のコードスニペットを確認して、Node.js環境で2つのPDFファイルをマージしてください。

**CommonJS:**

1. `require` を呼び出し、`asposepdfnodejs` モジュールを `AsposePdf` 変数としてインポートします。
1. 結合されるPDFファイルの名前を指定します。
1. `AsposePdf` をPromiseとして呼び出し、結合の操作を行います。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) を呼び出します。
1. 2つのPDFファイルを結合します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultMerge.pdf" に保存されます。json.errorCode パラメータが 0 でなく、それに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*2つのPDFファイルを結合して "ResultMerge.pdf" に保存します*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. マージされるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/)を呼び出します。
1. 2つのPDFファイルをマージします。したがって、'json.errorCode'が0の場合、操作の結果は"ResultMerge.pdf"に保存されます。json.errorCodeパラメータが0でない場合、またはそれに応じてファイルにエラーが表示される場合、エラー情報は 'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*2つのPDFファイルをマージし、"ResultMerge.pdf"を保存します*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```