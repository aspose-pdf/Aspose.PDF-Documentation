---
title: Node.jsでPDFを分割する
linktitle: PDFファイルを分割する
type: docs
weight: 30
url: /ja/nodejs-cpp/split-pdf/
description: このトピックでは、Aspose.PDF for Node.js via C++ を使用して、PDFページを個別のPDFファイルに分割する方法を示します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Node.jsを使用してPDFを2つのファイルに分割する

単一のPDFを部分に分割したい場合は、[AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/)関数を使用できます。 Node.js環境で2つのPDFを分割するための以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 分割するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ファイルを分割する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/)を呼び出します。

1. 2つのPDFファイルを分割します。PDFファイルがページ1で分割されることを示すために、変数pageToSplitを1に設定します。
1. したがって、'json.errorCode'が0の場合、操作の結果は"ResultSplit1.pdf"と"ResultSplit2.pdf"に保存されます。json.errorCodeパラメータが0でない場合、したがってファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*分割するページ番号を設定*/
      const pageToSplit = 1;
      /*2つのPDFファイルに分割し、"ResultSplit1.pdf"、"ResultSplit2.pdf"を保存する*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。

1. 分割されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/)を呼び出します。
1. 2つのPDFファイルを分割します。pageToSplit変数を1に設定し、PDFファイルがページ1で分割されることを示します。
1. したがって、'json.errorCode'が0の場合、操作の結果は"ResultSplit1.pdf"と"ResultSplit2.pdf"に保存されます。json.errorCodeパラメータが0でない場合、したがってエラーがファイルに表示される場合、エラー情報は'json.errorText'に含まれます。

```js
  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*分割するページ番号を設定*/
  const pageToSplit = 1;
  /*2つのPDFファイルに分割し、"ResultSplit1.pdf"と"ResultSplit2.pdf"を保存*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```