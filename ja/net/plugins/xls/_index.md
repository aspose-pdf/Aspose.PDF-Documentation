---
title: XLS コンバーター
type: docs
weight: 20
url: ja/net/plugins/xls/
description: Aspose.Pdf プラグインを使用して PDF を Excel スプレッドシートに変換する方法
lastmod: "2024-01-24"
---

{{% alert color="primary" %}}

この記事では、[PdfXls プラグイン](https://products.aspose.org/pdf/net/xls-converter/)を使用して PDF ファイルを高精度で Excel 形式に変換する方法を紹介します。

{{% /alert %}}

## 前提条件

以下が必要です：

* Visual Studio 2019 以降
* Aspose.PDF for .NET 24.1 以降
* Excel 形式に変換したいサンプル PDF ファイル

Aspose.PDF for .NET ライブラリは公式ウェブサイトからダウンロードするか、Visual Studio の NuGet パッケージマネージャーを使用してインストールできます。

## 手順

PdfXls プラグインを使用して PDF ファイルを Excel 形式に変換する基本的な手順は以下の通りです：

1. PdfXls クラスのオブジェクトを作成する
1. 入力および出力データソースを PdfToXlsOptions オブジェクトに追加する
1. PdfXls オブジェクトの Process メソッドを実行する

これらの手順を C# コードで実装する方法を見てみましょう。
これらの手順をC#コードで実装する方法を見てみましょう。

### ステップ1: PdfXlsクラスのオブジェクトを作成する

PdfXlsクラスは、PDFをExcelに変換する機能を提供するメインクラスです。これを使用するには、デフォルトコンストラクタを使用してインスタンスを作成する必要があります：

```csharp
// PdfXlsプラグインのインスタンスを作成する
var plugin = new PdfXls();
```

### ステップ2: 入力および出力データソースをPdfToXlsOptionsオブジェクトに追加する

PdfToXlsOptionsクラスは、変換プロセスのさまざまなオプションやパラメータを指定するためのヘルパークラスです。これを使用するには、インスタンスを作成し、`AddInput`および`AddOutput`メソッドを使用して入力および出力データソースを追加する必要があります。データソースは、ファイルパスまたはストリームのいずれかにすることができます。例えば、`C:\Samples`フォルダにある`sample.pdf`というPDFファイルを同じフォルダの`sample.xlsx`というExcelファイルに変換する場合、次のコードを使用できます：

```csharp
// 入力および出力ファイルパスを指定する
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.xlsx");

// PdfToXlsOptionsクラスのインスタンスを作成する
var options = new PdfToXlsOptions();

// オプションに入力および出力ファイルパスを追加する
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```
他のオプションも設定できます。たとえば、出力形式、ページ範囲、ワークシート名などを、PdfToXlsOptionsクラスのプロパティを使用して設定できます。例えば、PDFファイルをXLSX形式に変換し、最初の位置に空の列を挿入し、ワークシートを"MySheet"という名前にする場合、次のコードを使用できます。

```csharp
// 出力形式をXLSXに設定
options.Format = PdfToXlsOptions.ExcelFormat.XLSX;

// 最初の位置に空の列を挿入
options.InsertBlankColumnAtFirst = true;
```

### ステップ3: PdfXlsオブジェクトのProcessメソッドを実行する

最後のステップは、PdfXlsオブジェクトのProcessメソッドを実行し、パラメータとしてPdfToXlsOptionsオブジェクトを渡すことです。
最終的なステップは、PdfToXlsOptionsオブジェクトをパラメータとして渡して、PdfXlsオブジェクトのProcessメソッドを実行することです。

```csharp
// PDFをExcel変換するプラグインとオプションを使用して処理
var resultContainer = plugin.Process(options);

// 結果コレクションから最初の結果を取得
var result = resultContainer.ResultCollection[0];

// 結果を出力
Console.WriteLine(result);
```

結果には出力ファイルパスなどの情報が含まれます。
