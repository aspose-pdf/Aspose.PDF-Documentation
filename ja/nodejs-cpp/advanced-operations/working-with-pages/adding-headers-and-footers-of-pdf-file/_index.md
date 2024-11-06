---
title: Node.jsでPDFにヘッダーとフッターを追加
linktitle: PDFにヘッダーとフッターを追加
type: docs
weight: 70
url: ja/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Node.js via C++を使用して、PDFファイルにヘッダーとフッターを追加します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js via C++**を使用すると、既存のPDFファイルにヘッダーとフッターを追加できます。

ヘッダーとフッターを追加したい場合は、[AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/)関数を使用できます。

以下のコードスニペットを確認して、Node.js環境でPDFファイルにヘッダーとフッターを追加してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. ヘッダーとフッターを追加するPDFファイルの名前を指定します。

1. `AsposePdf` を Promise として呼び出し、ヘッダーとフッターを追加する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数 [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/) を呼び出します。
1. PDFファイルのヘッダーとフッターにテキストを追加します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultAddHeaderFooter.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが表示され、そのエラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルのヘッダー/フッターにテキストを追加し、"ResultAddHeaderFooter.pdf" に保存します*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
1. ヘッダーとフッターを追加するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/)を呼び出します。
1. PDFファイルのヘッダーとフッターにテキストを追加します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultAddHeaderFooter.pdf"に保存されます。json.errorCodeパラメータが0でない場合は、エラーがファイルに表示され、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルのヘッダー/フッターにテキストを追加し、"ResultAddHeaderFooter.pdf"を保存します*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++ via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```