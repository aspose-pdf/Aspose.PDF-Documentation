---
title: Node.jsでPDFのページを削除する
linktitle: PDFページを削除
type: docs
weight: 30
url: /ja/nodejs-cpp/delete-pages/
description: Aspose.PDF for Node.js via C++を使用してPDFファイルからページを削除できます。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFページを削除したい場合は、[AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) 関数を使用できます。

この関数の特徴は、numPagesパラメーターとしていくつかの型を受け入れることができることです:

- string: この場合、特定のページや間隔を使用して一連のページを指定できます。例えば、文字列 "7, 20, 30-32, 34" は、ページ7、20、30から32、そして34を削除したいことを意味します。
- array: この場合、ページのみを指定できます。配列 [3,7] は、ページ3と7を削除したいことを意味します。
- int: 単一のページ番号。

Node.js環境でPDFページを削除するために、次のコードスニペットを確認してください。

**CommonJS:**

```javascript
// 必要なモジュールをインポートする
const asposepdf = require('asposepdf');

// PDFドキュメントをロードする
let pdfDocument = new asposepdf.Document("example.pdf");

// ページを削除する - 例: "7, 20, 30-32, 34" のページを削除
pdfDocument.deletePages("7, 20, 30-32, 34");

// 変更を保存する
pdfDocument.save("modified_example.pdf");

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. ページを削除するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、ページを削除する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/)を呼び出します。
1. PDFファイルから特定のページを削除します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultDeletePages.pdf"に保存されます。json.errorCodeパラメータが0でない場合、そしてそれに応じてファイルにエラーが現れた場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*文字列、間隔でページ番号を含める: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*配列、ページ番号の配列*/
      /*const numPages = [1,3];*/
      /*番号、ページ番号*/
      const numPages = 1;
      /*PDFファイルからページを削除し、"ResultDeletePages.pdf"を保存します*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. ページを削除するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数 [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) を呼び出します。この関数は、PDFファイルから指定されたページを削除するのに役立ちます。操作は、ページ間隔を含む文字列（例: "7, 20, 22, 30-32, 33, 36-40, 46"）、ページ番号の配列、または単一のページ番号である可能性のある numPages 変数によって決定されます。
1. PDFファイルから特定のページを削除します。したがって、'json.errorCode'が0の場合、操作の結果は "ResultDeletePages.pdf" に保存されます。json.errorCode パラメータが0でない場合、およびファイルにエラーが表示された場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*文字列、間隔を含むページ番号: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*配列、ページ番号の配列*/
  /*const numPages = [1,3];*/
  /*数値、ページ番号*/
  const numPages = 1;
  /*PDFファイルからページを削除して "ResultDeletePages.pdf" に保存します*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```