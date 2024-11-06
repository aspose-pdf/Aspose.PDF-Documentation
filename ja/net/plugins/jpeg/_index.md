---
title: JPEG コンバーター
type: docs
weight: 90
url: ja/net/plugins/jpeg/
description: Aspose.PDF JPEG コンバーターを使用して PDF ページを JPEG 画像に変換する方法
lastmod: "2024-01-24"
draft: false
---

この記事では、PDF ページを JPEG 画像に変換し、別々のファイルとして保存する方法を示します。[JPEG コンバーター](https://products.aspose.org/pdf/net/jpeg-converter/) の使用方法について説明します。

## 前提条件

以下が必要です：

* Visual Studio 2019 以降
* Aspose.PDF for .NET 24.1 以降
* いくつかのページを含むサンプル PDF ファイル

Aspose.PDF for .NET ライブラリは、公式ウェブサイトからダウンロードするか、Visual Studio の NuGet パッケージマネージャーを使用してインストールできます。

## 手順

JPEG コンバーターを使用して PDF ページを JPEG 画像に変換する基本的な手順は以下の通りです：

1. Jpeg クラスのオブジェクトを作成する
1. JpegOptions クラスのオブジェクトを作成し、入力ファイルと出力ファイルのパスを追加する
1. Jpeg オブジェクトの Process メソッドを実行し、結果のコンテナを取得する
1.
### ステップ1: Jpegクラスのオブジェクトを作成する

Jpegクラスは、PDFページをJPEG画像に変換する機能を提供する主要なクラスです。これを使用するには、デフォルトコンストラクタを使用してインスタンスを作成する必要があります：

```cs
// Jpegの新しいインスタンスを作成
var converter = new Jpeg();
```

### ステップ2: JpegOptionsクラスのオブジェクトを作成し、入力および出力ファイルのパスを追加する

JpegOptionsクラスは、出力解像度、ページ範囲、画像品質など、変換プロセスのさまざまなオプションやパラメータを指定できるヘルパークラスです。
JpegOptions クラスは、出力解像度、ページ範囲、画像品質など、変換プロセスのさまざまなオプションやパラメータを指定するためのヘルパークラスです。

```cs
// 入力ファイルと出力ファイルのパスを指定
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "images");

// JpegOptions クラスのインスタンスを作成
var converterOptions = new JpegOptions();

// オプションに入力ファイルと出力ファイルのパスを追加
converterOptions.AddInput(new FileDataSource(inputPath));
converterOptions.AddOutput(new FileDataSource(outputPath));
```

出力解像度、ページ範囲、画像品質など、JpegOptions クラスのプロパティを使用して他のオプションも設定できます。たとえば、PDFファイルの最初のページのみを300 dpiの解像度でJPEG画像に変換するには、次のコードを使用します：

```cs
// 出力解像度を300 dpiに設定
converterOptions.OutputResolution = 300;

// ページ範囲を最初のページに設定
converterOptions.PageRange = new PageRange(1);
```
### ステップ3: JpegオブジェクトのProcessメソッドを実行し、結果コンテナを取得する

最終ステップは、converterOptionsオブジェクトをパラメータとしてJpegオブジェクトのProcessメソッドを実行することです。このメソッドは変換を実行し、変換の結果を含むResultContainerオブジェクトを返します。このオブジェクトには、ステータス、メッセージ、出力ファイルパスなどが含まれます。ResultContainerクラスのプロパティやメソッドを使用して結果にアクセスできます。たとえば、結果コンテナを取得して変換のステータスを出力するには、次のコードを使用できます:

```cs
// 変換を処理し、結果コンテナを取得
ResultContainer resultContainer = converter.Process(converterOptions);

// 変換のステータスを出力
Console.WriteLine(resultContainer.Status);
```

変換のステータスは、変換が成功したかどうかによって、SuccessまたはFailureのいずれかになります。

### ステップ4: 変換されたJPEG画像のパスを出力する

結果コンテナには、出力ファイルパスごとに結果のコレクションが含まれています。
結果コンテナには、出力ファイルパスごとに1つの結果のコレクションが含まれています。

```cs
// 変換されたJPEG画像のパスを印刷する
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
  Console.WriteLine(operationResult.Data.ToString());
}
```

出力ファイルパスは{outputPath}{pageNumber}.jpgの形式になります。ここで{outputPath}は出力ディレクトリで、{pageNumber}はPDFファイルのページ番号です。たとえば、出力ディレクトリがC:\Samples\imagesでPDFファイルが3ページある場合、出力ファイルパスは以下の通りになります：

```text
C:\Samples\images\1.jpg
C:\Samples\images\2.jpg
C:\Samples\images\3.jpg
```
