---
title: Merger
type: docs
weight: 100
url: /net/plugins/merger/
description: Aspose.PDF Merger プラグインを使用して複数の PDF ファイルを 1 つにマージする方法
lastmod: "2024-01-24"
---

この記事では、複数の PDF ファイルを 1 つにマージして新しいファイルとして保存する [Merger プラグイン](https://products.aspose.org/pdf/net/merger/) の使用方法を紹介します。

## 前提条件

以下が必要です：

* Visual Studio 2019 以降
* Aspose.PDF for .NET 21.1 以降
* マージしたい 3 つのサンプル PDF ファイル

Aspose.PDF for .NET ライブラリは公式ウェブサイトからダウンロードするか、Visual Studio の NuGet パッケージマネージャーを使用してインストールできます。

## 手順

Merger プラグインを使用して複数の PDF ファイルを 1 つにマージする基本的な手順は以下の通りです：

1. Merger クラスのオブジェクトを作成する
2. MergeOptions クラスのオブジェクトを作成し、入力および出力ファイルのパスを追加する
3. Merger オブジェクトの Process メソッドを実行する

これらの手順を C# コードで実装する方法を見ていきましょう。

### ステップ 1: Merger クラスのオブジェクトを作成する
### ステップ1: Mergerクラスのオブジェクトを作成する

Mergerクラスは、複数のPDFファイルを一つに統合する機能を提供するメインクラスです。これを使用するには、デフォルトコンストラクタを使用してインスタンスを作成する必要があります：

```cs
// Mergerの新しいインスタンスを作成
var pdfMerger = new Merger();
```

### ステップ2: MergeOptionsクラスのオブジェクトを作成し、入力ファイルと出力ファイルのパスを追加する

MergeOptionsクラスは、ページ範囲、順序、セキュリティなど、マージプロセスのさまざまなオプションやパラメータを指定するためのヘルパークラスです。
MergeOptions クラスは、マージプロセスのために様々なオプションとパラメータを指定するためのヘルパークラスです。ページ範囲、順序、セキュリティなどを指定できます。

```cs
// 入力と出力ファイルパスを指定
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// MergeOptions クラスのインスタンスを作成
var mergeOptions = new MergeOptions();

// オプションに入力と出力ファイルパスを追加
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

### Step 3: Run the Process method of the Merger object

最終ステップは、Merger オブジェクトの Process メソッドを実行することです。その際、mergeOptions オブジェクトをパラメータとして渡します。
最終ステップは、MergerオブジェクトのProcessメソッドを実行し、mergeOptionsオブジェクトをパラメータとして渡すことです。

```cs
// マージを処理し、マージされたファイルを保存します
pdfMerger.Process(mergeOptions);

// 確認メッセージを出力する
Console.WriteLine("PDFファイルのマージが成功しました。");
```
