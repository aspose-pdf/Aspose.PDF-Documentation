---
title: Node.jsでPDFファイルのメタデータを操作する
linktitle: PDFファイルのメタデータ
type: docs
weight: 130
url: ja/nodejs-cpp/pdf-file-metadata/
description: このセクションでは、PDFファイル情報を取得する方法、PDFファイルからメタデータを取得する方法、Node.jsでPDFファイル情報を設定する方法について説明します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイル情報の取得

PDFファイル情報を取得したい場合は、[AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) 関数を使用できます。Node.js環境でPDFファイル情報を取得するためのコードスニペットを以下に示します。

**CommonJS:**

1. `require`を呼び出して`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
2. 情報を抽出するPDFファイルの名前を指定します。
3. `AsposePdf`をPromiseとして呼び出し、情報抽出の操作を行います。成功した場合はオブジェクトを受け取ります。

1. 関数 [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) を呼び出します。
1. 抽出されたメタデータは JSON オブジェクトに保存されます。そのため、'json.errorCode' が 0 の場合、抽出されたメタデータは console.log を使用して表示されます。もし json.errorCode パラメータが 0 でなく、ファイルにエラーが発生した場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルから情報（メタデータ）を取得*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        タイトル         : json.title
        作成者           : json.creator
        著者             : json.author
        件名             : json.subject
        キーワード       : json.keywords
        作成日           : json.creation
        修正日           : json.mod
        PDF形式         : json.format
        PDFバージョン    : json.version
        PDFはPDF/A       : json.ispdfa
        PDFはPDF/UA      : json.ispdfua
        PDFは線形化されている : json.islinearized
        PDFは暗号化されている : json.isencrypted
        PDFの権限        : json.permission
        PDFページサイズ  : json.size
        ページ数         : json.pagecount
        注釈数           : json.annotationcount
        ブックマーク数   : json.bookmarkcount
        添付ファイル数   : json.attachmentcount
        メタデータ数     : json.metadatacount
        JavaScript数     : json.javascriptcount
        画像数           : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'タイトル: ' + json.title : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 情報を抽出する PDF ファイルの名前を指定します。
1. AsposePdf モジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数 [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) を呼び出します。
1. 抽出されたメタデータは JSON オブジェクトに格納されます。したがって、'json.errorCode' が 0 の場合、抽出されたメタデータは console.log を使用して表示されます。'json.errorCode' パラメータが 0 でない場合は、ファイルにエラーが表示され、エラー情報は 'json.errorText' に含まれます。

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*PDFファイルから情報（メタデータ）を取得します*/
    const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
    /* JSON
      タイトル           : json.title
      作成者             : json.creator
      著者               : json.author
      件名               : json.subject
      キーワード         : json.keywords
      作成日             : json.creation
      変更日             : json.mod
      PDF 形式           : json.format
      PDF バージョン     : json.version
      PDF は PDF/A      : json.ispdfa
      PDF は PDF/UA     : json.ispdfua
      PDF は線形化      : json.islinearized
      PDF は暗号化      : json.isencrypted
      PDF 許可          : json.permission
      PDF ページサイズ  : json.size
      ページ数           : json.pagecount
      注釈数             : json.annotationcount
      ブックマーク数     : json.bookmarkcount
      添付ファイル数     : json.attachmentcount
      メタデータ数       : json.metadatacount
      JavaScript 数      : json.javascriptcount
      画像数             : json.imagecount
    */
    console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'タイトル: ' + json.title : json.errorText);
```


## すべてのフォントを取得

PDFファイルからフォントを取得することは、他のドキュメントやアプリケーションでフォントを再利用する便利な方法です。

PDFファイルからフォントを取得したい場合は、[AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) 関数を使用できます。Node.js環境でPDFファイルからフォントを取得するために以下のコードスニペットを確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
2. フォントを抽出するPDFファイルの名前を指定します。
3. `AsposePdf`をPromiseとして呼び出し、フォントを抽出する操作を実行します。成功した場合はオブジェクトを受け取ります。
4. 関数 [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) を呼び出します。

1. 抽出されたフォントはJSONオブジェクトに保存されます。したがって、'json.errorCode' が0の場合、フォント名、埋め込みの有無、そのアクセシビリティステータスを含むフォントの詳細の配列をconsole.logを使用して表示します。json.errorCodeパラメータが0でない場合、またはファイルにエラーが表示された場合、エラー情報は 'json.errorText' に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルからフォントのリストを取得*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - フォントの配列: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. フォントを抽出するPDFファイルの名前を指定します。

1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数[AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/)を呼び出します。
1. 抽出されたフォントはJSONオブジェクトに保存されます。したがって、'json.errorCode'が0であれば、フォント名、埋め込みの有無、およびアクセシビリティの状態を含むフォントの詳細の配列をconsole.logを使用して表示します。json.errorCodeパラメータが0でない場合、およびそれに応じてエラーがファイルに表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルからフォントのリストを取得*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - フォントの配列: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## PDFファイル情報を設定する


Aspose.PDF for Node.js via C++を使用すると、PDFに対してファイル固有の情報（著者、作成日、件名、タイトルなど）を設定できます。この情報を設定するには次のようにします：

ファイル固有の情報を設定する場合は、[AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/)関数を使用できます。Node.js環境でファイル情報を設定するための以下のコードスニペットを確認してください。

設定可能な項目:
- タイトル
- 作成者
- 著者
- 件名
- キーワードのリスト
- 作成日
- 修正日
- 結果ファイル名

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。
1. 情報を設定するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/)を呼び出します。

1. PDFファイル情報を設定します。タイトル、作成者、著者、主題、キーワード、作成日、変更日などの情報はパラメータとして提供されます。したがって、'json.errorCode'が0の場合、操作の結果は"ResultSetInfo.pdf"に保存されます。json.errorCodeパラメータが0でない場合、およびファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js
const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*PDF情報を設定: タイトル、作成者、著者、主題、キーワード、作成日、変更日*/
    /*値を設定する必要がない場合は、undefinedまたは""（空の文字列）を使用*/
    /*PDFファイルに情報(メタデータ)を設定し、"ResultSetInfo.pdf"を保存*/
    const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "PDFドキュメント情報の設定", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
    console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```


**ECMAScript/ES6:**

1. `asposepdfnodejs` モジュールをインポートします。
1. 情報が設定されるPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合、オブジェクトを受け取ります。
1. 関数 [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) を呼び出します。
1. PDFファイル情報を設定します。タイトル、作成者、著者、件名、キーワード、作成日、および変更日などの情報がパラメータとして提供されます。したがって、'json.errorCode' が0の場合、操作の結果は "ResultSetInfo.pdf" に保存されます。'json.errorCode' パラメータが0でなく、ファイルにエラーが表示される場合、エラー情報は 'json.errorText' に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDF情報を設定: タイトル、作成者、著者、件名、キーワード、作成日、変更日*/
  /*値を設定する必要がない場合、undefined または ""（空の文字列）を使用*/
  /*PDFファイルに情報（メタデータ）を設定し、"ResultSetInfo.pdf" を保存*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


## PDFファイル情報の削除

Aspose.PDF for Node.js via C++を使用すると、PDFファイルのメタデータを削除することができます。

PDFからメタデータを削除したい場合は、[AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) 関数を使用できます。
Node.js環境でPDFからメタデータを削除するための以下のコードスニペットを確認してください。

**CommonJS:**

1. AsposePDFforNode.jsモジュールを要求します。
1. 情報を削除するPDFファイルの名前を指定します。
1. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/)を呼び出します。
1. PDFファイル情報を削除します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfRemoveMetadata.pdf"に保存されます。json.errorCodeパラメータが0でない場合、つまりファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルからメタデータを削除し、"ResultPdfRemoveMetadata.pdf"として保存する*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
2. 情報を削除するPDFファイルの名前を指定します。
3. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
4. 関数[AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/)を呼び出します。
5. PDFファイル情報を削除します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultPdfRemoveMetadata.pdf"に保存されます。json.errorCodeパラメータが0でない場合、およびそれに応じてファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*PDFファイルからメタデータを削除し、"ResultPdfRemoveMetadata.pdf"に保存します*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```