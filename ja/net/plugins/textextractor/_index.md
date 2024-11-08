---
title: テキストエクストラクター
type: docs
weight: 140
url: /ja/net/plugins/textextractor/
description: PDFドキュメントからテキストコンテンツを抽出します。
lastmod: "2024-01-24"
---

プログラムで[テキストを抽出](https://products.aspose.org/pdf/net/text-extractor/)する必要があるPDFドキュメントはありますか？Aspose.PDF for .NETを使用すると、TextExtractorクラスを使用してこのタスクを簡単に実行できます。この記事では、.NETでテキスト抽出アプリケーションを作成する基本的な手順を説明します。TextExtractorオブジェクトの作成、データソースの追加、テキスト抽出プロセスの実行をカバーします。

## 前提条件

以下が必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 24.1以降
* サンプルPDFファイル

さらに、`TextExtractorOptions`クラスとその機能について熟知してください。詳細は[Aspose.PDF API Reference](https://reference.aspose.com/pdf/net/aspose.pdf/TextExtractorOptions/)で見つけることができます。

さあ、コードに飛び込んで、PDFドキュメントからテキストを抽出する方法を探りましょう。
さて、PDFドキュメントからテキストを抽出する方法についてコードを詳しく見ていきましょう。

## コードウォークスルー

以下のコードは、テキスト抽出機能を示しています。主要なステップを順に見ていきましょう：

### 1. TextExtractorオブジェクトを作成

コードは、`TextExtractor`クラスの新しいインスタンスを作成することから始まります。このクラスはPDFドキュメントからテキストを抽出するメソッドを提供します。

```csharp
using TextExtractor extractor = new();
```

### 2. データソースを追加

次に、入力PDFファイル用の`FileDataSource`を作成します。これはテキストが抽出されるファイルです。

```csharp
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

### 3. TextExtractorOptionsを作成

テキスト抽出プロセスを設定するための`TextExtractorOptions`オブジェクトを作成します。入力ファイルソースがオプションに追加されます。

```csharp
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);
```

### 4. テキスト抽出プロセスを実行

設定されたオプションを渡して、`TextExtractor`オブジェクト上で`Process`メソッドが呼び出されます。
`Process` メソッドが `TextExtractor` オブジェクトに呼び出され、設定されたオプションを渡します。

```csharp
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;
Console.WriteLine(results[0]);
```

以下に完全なコードを示します：

``````cs
using Aspose.Pdf.Plugins;
// ...

// TextExtractorの新しいインスタンスを作成します。
using TextExtractor extractor = new();

// 入力PDFファイルのためのFileDataSourceを作成します。
FileDataSource fileSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));

// TextExtractorOptionsを作成します。
TextExtractorOptions textExtractorOptions = new();
textExtractorOptions.AddInput(fileSource);

// テキスト抽出を処理します。
var resultContainer = extractor.Process(textExtractorOptions);
var results = resultContainer.ResultCollection;

// 抽出されたテキストを出力します。
Console.WriteLine(results[0]);

```
