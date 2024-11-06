---

title: PDFに画像スタンプを追加する方法（Node.js）
linktitle: PDFファイルへの画像スタンプ
type: docs
weight: 60
url: ja/nodejs-cpp/stamping/
description: AsposePdfAddStampを使用して、Node.jsツールでPDFドキュメントに画像スタンプを追加します。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルに画像スタンプを追加する

PDFドキュメントにスタンプを押すことは、紙のドキュメントにスタンプを押すことに似ています。PDFファイルのスタンプは、他の人が使用するためのPDFファイルの保護やPDFファイルの内容の安全性の確認など、PDFファイルに追加情報を提供します。
Node.jsを使用してPDFファイルに画像スタンプを追加するには、[AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/)関数を使用できます。

以下のコードスニペットを確認して、Node.js環境でPDFファイルに画像スタンプを追加する方法を確認してください。

**CommonJS:**

1. `require`を呼び出し、`asposepdfnodejs`モジュールを`AsposePdf`変数としてインポートします。

1. 画像スタンプを追加するPDFファイルの名前を指定します。
1. `AsposePdf`をPromiseとして呼び出し、画像スタンプを追加する操作を実行します。成功した場合はオブジェクトを受け取ります。
1. 関数[AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/)を呼び出します。
1. PDFファイルにスタンプを追加します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultImage.pdf"に保存されます。json.errorCodeパラメータが0でない場合、ファイルにエラーが表示され、エラー情報は'json.errorText'に含まれます。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*PDFファイルにスタンプを追加し、"ResultImage.pdf"を保存する*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. `asposepdfnodejs`モジュールをインポートします。
2. 画像スタンプを追加するPDFファイルの名前を指定します。
3. AsposePdfモジュールを初期化します。成功した場合はオブジェクトを受け取ります。
4. 関数[AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/)を呼び出します。
5. PDFファイルにスタンプを追加します。したがって、'json.errorCode'が0の場合、操作の結果は"ResultImage.pdf"に保存されます。json.errorCodeパラメータが0でない場合、つまり、ファイルにエラーが表示される場合、エラー情報は'json.errorText'に含まれます。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /* PDFファイルにスタンプを追加し、"ResultImage.pdf"を保存します */
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```