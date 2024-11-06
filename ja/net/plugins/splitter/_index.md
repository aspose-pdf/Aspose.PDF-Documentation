---
title: Splitter
type: docs
weight: 120
url: ja/net/plugins/splitter/
description: PDFドキュメントを個別のページに分割します
lastmod: "2024-01-24"
draft: false
---

大きなPDFドキュメントをより小さく、扱いやすいファイルに分割したいですか？[Aspose.PDF Splitter for .NET](https://products.aspose.org/pdf/net/splitter/)を使用すれば、この作業を簡単に実行できます。この記事では、Aspose.PDFプラグインを使用してPDFドキュメントを複数のファイルに分割するプロセスを探ります。コードに飛び込み、手順を見ていきましょう。

## 前提条件

以下が必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 24.1以降
* サンプルPDFファイル

さらに、`SplitOptions`クラスとそのプロパティについて熟知してください。このクラスに関する詳細情報は、[API Reference](https://reference.aspose.com/pdf/net/aspose.pdf/SplitOptions/)で見つけることができます。各出力`FileDataSource`は、分割されたPDFファイルの単一ページを表していることに注意してください。

これで、提供されたコードを探索し、PDFドキュメントを分割する方法を理解しましょう。
提供されたコードを調べて、PDF文書を分割する方法を理解しましょう。

## コードの説明

以下のコードは、Aspose.PDF.Pluginsを使用したPDF分割デモを示しています：

```csharp
using Aspose.Pdf.Plugins;
// ...........

// 分割するPDF文書の入力パスを設定します。
using var inputStream = File.OpenRead(Path.Combine(@"C:\Samples\", "sample.pdf"));

// Splitterの新しいインスタンスを作成します。
var splitter = new Splitter();

// 文書を分割するためのオプションを作成します。
var options = new SplitOptions();

// オプションに入力および出力データソースを追加します。
options.AddInput(new StreamDataSource(inputStream));

var document = new Aspose.Pdf.Document(inputStream);

for (int i = 1; i <= document.Pages.Count; i++)
{
   var pageNum = string.Format("{0,3}", i.ToString("D3"));
   options.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", $"splitter_{pageNum}.pdf")));
}

// オプションを処理して文書を分割します。
var result = splitter.Process(options);
Console.WriteLine(result);
```

重要なステップを詳しく説明しましょう：
以下は、主要な手順を分解したものです：

1. **入力PDFの設定**

   コードは、分割する入力PDFドキュメントのパスを指定することから始まります。これは、`File.OpenRead` メソッドを使用して行われます。

2. **オブジェクトの作成（SplitterとSplitOptions）**

   コードは、分割プロセスを処理するための `Splitter` クラスのインスタンスを作成します。さらに、分割操作を設定するための `SplitOptions` クラスのインスタンスも作成されます。

3. **データソースの追加（入力と出力）**

   入力PDFドキュメントは、`SplitOptions` に入力データソースとして `AddInput` メソッドを使用して追加されます。ドキュメントの各ページに対して、出力ファイルパスが出力データソースとして `AddOutput` メソッドを使用して追加されます。

4. **プロセスメソッドの実行**

   分割プロセスは、設定された `SplitOptions` を `Splitter` クラスに渡して `Process` メソッドを呼び出すことによって開始されます。操作の結果は `result` 変数に格納されます。

5. **結果の処理**

   コードは、分割プロセスに関する情報を提供しながら、結果をコンソールに出力します。

コードはコンソールに結果を出力し、分割プロセスに関する情報を提供します。
```
