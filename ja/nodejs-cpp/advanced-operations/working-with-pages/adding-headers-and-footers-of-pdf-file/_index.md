---
title: Node.js で PDF にヘッダーとフッターを追加する
linktitle: PDF にヘッダーとフッターを追加する
type: docs
weight: 70
url: /ja/nodejs-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Node.js via C++ は、AsposePdfAddTextHeaderFooter を使用して PDF ファイルにヘッダーとフッターを追加できるようにします。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js via C++** は、既存の PDF ファイルにヘッダーとフッターを追加できるようにします。 

ヘッダーとフッターを追加したい場合は、次を使用できます [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/) 関数。 

Node.js 環境で PDF ファイルにヘッダーとフッターを追加するために、以下のコードスニペットを確認してください。

**CommonJS:**

1. 呼び出す `require` とインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. ヘッダーとフッターを追加する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promise としてヘッダーとフッターを追加する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. PDFファイルのヘッダーとフッターにテキストを追加します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultAddHeaderFooter.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが表示され、そのエラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
      const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
      console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール.
1. ヘッダーとフッターを追加する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddtextheaderfooter/).
1. PDFファイルのヘッダーとフッターにテキストを追加します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultAddHeaderFooter.pdf" に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが表示され、そのエラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add text in Header/Footer of a PDF-file and save the "ResultAddHeaderFooter.pdf"*/
  const json = AsposePdfModule.AsposePdfAddTextHeaderFooter(pdf_file, "Aspose.PDF for Node.js via C++", "ASPOSE", "ResultAddHeaderFooter.pdf");
  console.log("AsposePdfAddTextHeaderFooter => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```