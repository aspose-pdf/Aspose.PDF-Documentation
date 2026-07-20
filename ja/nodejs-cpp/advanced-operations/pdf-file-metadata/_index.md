---
title: Node.jsでPDFファイルメタデータを操作する
linktitle: PDFファイルメタデータ
type: docs
weight: 130
url: /ja/nodejs-cpp/pdf-file-metadata/
description: このセクションでは、PDFファイル情報の取得方法、PDFファイルからメタデータを取得する方法、Node.jsでPDFファイル情報を設定する方法について説明します。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ファイル情報を取得

PDFファイル情報を取得したい場合は、次のものを使用できます [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) 関数。 
Node.js 環境で PDF ファイル情報を取得するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 情報が抽出されるPDFファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promise として、情報抽出の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. 抽出されたメタデータは JSON オブジェクトに保存されます。したがって、'json.errorCode' が 0 の場合、抽出されたメタデータは console.log を使用して表示されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get info (metadata) from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Title             : json.title
        Creator           : json.creator
        Author            : json.author
        Subject           : json.subject
        Keywords          : json.keywords
        Creation Date     : json.creation
        Modify Date       : json.mod
        PDF format        : json.format
        PDF version       : json.version
        PDF is PDF/A      : json.ispdfa
        PDF is PDF/UA     : json.ispdfua
        PDF is linearized : json.islinearized
        PDF is encrypted  : json.isencrypted
        PDF permission    : json.permission
        PDF page size     : json.size
        Page count        : json.pagecount
        Annotation count  : json.annotationcount
        Bookmark count    : json.bookmarkcount
        Attachment count  : json.attachmentcount
        Metadata count    : json.metadatacount
        JavaScript count  : json.javascriptcount
        Image count       : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. 情報が抽出されるPDFファイルの名前を指定してください。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/).
1. 抽出されたメタデータは JSON オブジェクトに保存されます。したがって、'json.errorCode' が 0 の場合、抽出されたメタデータは console.log を使用して表示されます。json.errorCode パラメータが 0 でない場合、そしてそれに応じてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Get info (metadata) from a PDF-file*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      Title             : json.title
      Creator           : json.creator
      Author            : json.author
      Subject           : json.subject
      Keywords          : json.keywords
      Creation Date     : json.creation
      Modify Date       : json.mod
      PDF format        : json.format
      PDF version       : json.version
      PDF is PDF/A      : json.ispdfa
      PDF is PDF/UA     : json.ispdfua
      PDF is linearized : json.islinearized
      PDF is encrypted  : json.isencrypted
      PDF permission    : json.permission
      PDF page size     : json.size
      Page count        : json.pagecount
      Annotation count  : json.annotationcount
      Bookmark count    : json.bookmarkcount
      Attachment count  : json.attachmentcount
      Metadata count    : json.metadatacount
      JavaScript count  : json.javascriptcount
      Image count       : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```

## すべてのフォントを取得

PDF ファイルからフォントを取得することは、他の文書やアプリケーションでフォントを再利用する便利な方法です。 

PDF ファイルからフォントを取得したい場合は、次の方法を使用できます [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) 関数。 
Node.js 環境で PDF ファイルからフォントを取得するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. フォントを抽出するPDFファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとしてフォント抽出の操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. 抽出されたフォントは JSON オブジェクトに格納されます。そのため、\u0027json.errorCode\u0027 が 0 の場合、フォント名、埋め込まれているかどうか、アクセシビリティステータスなどのフォント詳細の配列が console.log を使用して表示されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は \u0027json.errorText\u0027 に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get list fonts from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. フォントを抽出するPDFファイルの名前を指定してください。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/).
1. 抽出されたフォントは JSON オブジェクトに格納されます。そのため、\u0027json.errorCode\u0027 が 0 の場合、フォント名、埋め込まれているかどうか、アクセシビリティステータスなどのフォント詳細の配列が console.log を使用して表示されます。json.errorCode パラメータが 0 でない場合、ファイルにエラーが発生し、エラー情報は \u0027json.errorText\u0027 に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Get list fonts from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## PDF ファイル情報を設定

Aspose.PDF for Node.js via C++ は、PDF のファイル固有情報（author、creation date、subject、title など）を設定することができます。この情報を設定するには:

ファイル固有の情報を設定したい場合は、次のように使用できます [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) 関数。 
Node.js 環境でファイル情報を設定するために、次のコードスニペットを確認してください。

設定可能です: 
- タイトル
- 作成者
- 著者
- 件名
- キーワードのリスト
- 作成日
- 日付を変更
- 結果ファイル名

**CommonJS:**

1. 呼び出す `require` そしてインポート `asposepdfnodejs` モジュールとして `AsposePdf` 変数。
1. 情報が設定されるPDFファイルの名前を指定してください。
1. 呼び出す `AsposePdf` Promiseとして操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. PDFファイル情報を設定します。タイトル、作成者、著者、件名、キーワード、作成日、更新日などの情報はパラメータとして提供されます。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultSetInfo.pdf" に保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*If not need to set value, use undefined or "" (empty string)*/
      /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. 情報が設定されるPDFファイルの名前を指定してください。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/).
1. PDFファイル情報を設定します。タイトル、作成者、著者、件名、キーワード、作成日、更新日などの情報はパラメータとして提供されます。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultSetInfo.pdf" に保存されます。json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*If not need to set value, use undefined or "" (empty string)*/
  /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## PDFファイル情報を削除

Aspose.PDF for Node.js via C++ は PDF ファイルのメタデータを削除することを可能にします:

PDFからメタデータを削除したい場合は、次の方法を使用できます [AsposePdfメタデータ削除](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) 関数。 
Node.js 環境で PDF からメタデータを削除するために、以下のコードスニペットをご確認ください。

**CommonJS:**

1. AsposePDFforNode.jsモジュールが必要です。
1. 情報が削除されるPDFファイルの名前を指定してください。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfメタデータ削除](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. PDFファイル情報を削除します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfRemoveMetadata.pdf" に保存されます。json.errorCode パラメータが 0 でなく、結果としてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. インポートする `asposepdfnodejs` モジュール。
1. 情報が削除されるPDFファイルの名前を指定してください。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数を呼び出す [AsposePdfメタデータ削除](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/).
1. PDFファイル情報を削除します。したがって、'json.errorCode' が 0 の場合、操作の結果は "ResultPdfRemoveMetadata.pdf" に保存されます。json.errorCode パラメータが 0 でなく、結果としてファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```