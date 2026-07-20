---
title: Node.jsでPDFのページを削除
linktitle: PDFページを削除
type: docs
weight: 30
url: /ja/nodejs-cpp/delete-pages/
description: Aspose.PDF for Node.js via C++ を使用して、PDFファイルからページを削除できます。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFページを削除したい場合は、次のものを使用できます [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) 関数。 

この関数の機能のひとつは、numPages パラメーターとして複数の型を受け付けることができる点です。

- string: この場合、特定のページや区間を使用してページの集合を指定できます。例えば、string \u00227, 20, 30-32, 34\u0022 は、ページ 7 と 20、30 から 32、そして 34 を削除したいことを意味します。
- array: この場合、ページのみを指定できます。配列 [3,7] は、ページ 3 と 7 を削除したいことを意味します。
- int: 単一のページ番号です。

Node.js 環境で PDF ページを削除するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` およびインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. ページを削除する PDF ファイルの名前を指定します。
1. 呼び出す `AsposePdf` Promiseとして、ページを削除する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. PDF ファイルから特定のページを削除します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultDeletePages.pdf” に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は ‘json.errorText’ に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポート `asposepdfnodejs` モジュール。
1. ページを削除する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). この関数は PDF ファイルから指定されたページを削除するのに役立ちます。操作は numPages 変数によって決定され、ページ間隔の文字列（例: “7, 20, 22, 30-32, 33, 36-40, 46”）、ページ番号の配列、または単一のページ番号のいずれかにすることができます。
1. PDF ファイルから特定のページを削除します。したがって、‘json.errorCode’ が 0 の場合、操作の結果は “ResultDeletePages.pdf” に保存されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は ‘json.errorText’ に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```