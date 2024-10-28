---
title: ToC Generator
type: docs
weight: 150
url: /net/plugins/tocgenerator/
description: Aspose.PDF ToCジェネレーターを使用して目次を作成します
lastmod: "2024-01-24"
draft: false
---

PDFドキュメントを[目次 (TOC) を追加する](https://products.aspose.org/pdf/net/toc-generator/)ことで強化したいですか？Aspose.PDF for .NETは、`TocGenerator` クラスを提供しており、これを使用して簡単にTOCを生成できます。このガイドでは、Aspose.PDFを使用してPDFドキュメントにTOCを作成する基本的な手順を説明します。これには、`TocGenerator` オブジェクトの作成、入力/出力パスの追加、およびTOC生成プロセスの実行が含まれます。

## 前提条件

以下が必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 24.1以降
* サンプルPDFファイル

さらに、`TocOptions` クラスとその機能について熟知してください。詳細は[Aspose.PDF APIリファレンス](https://reference.aspose.com/pdf/net/aspose.pdf/TocOptions/)で確認できます。

それでは、コードに飛び込んで、PDFドキュメントの目次を生成する方法を探りましょう。
さあ、コードを見ていきましょう。PDFドキュメントの目次を生成する方法を探ります。

## コードウォークスルー

`TocGeneratorDemo` クラスと `Run` メソッドを使用して目次の作成方法を示します。主なステップを詳しく見ていきましょう：

```csharp
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation
{
    internal static class TocGeneratorDemo
    {
        private const string PathForSamples = @"C:\Samples\";

        // 目次生成デモを実行します。
        internal static void Run()
        {
            // TocGenerator クラスの新しいインスタンスを作成します。
            TocGenerator generator = new();

            // TocOptions クラスの新しいインスタンスを作成します。
            TocOptions options = new();
            // TocOptions に入力パスと出力パスを追加します。
            options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
            options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));

            // 目次生成を処理し、結果コンテナを取得します。
            var resultContainer = generator.Process(options);

            // 結果コンテナから結果を取得します。
            var result = resultContainer.ResultCollection[0];

            // 結果をコンソールに表示します。
            Console.WriteLine(result);
        }
    }
}
```
### 1. TocGenerator オブジェクトを作成する

このコードは、`TocGenerator` クラスの新しいインスタンスを作成することから始まります。このクラスは、PDF文書のTOCを生成するためのメソッドを提供します。

```csharp
TocGenerator generator = new();
```

### 2. TocOptions を作成する

次に、TOC生成プロセスを設定するために `TocOptions` クラスの新しいインスタンスが作成されます。入力および出力ファイルパスがオプションに追加されます。

```csharp
TocOptions options = new();
options.AddInput(new FileDataSource(Path.Combine(PathForSamples, "sample.pdf")));
options.AddOutput(new FileDataSource(Path.Combine(PathForSamples, "sample_toc.pdf")));
```

### 3. TOC生成プロセスを実行する

設定されたオプションを渡して `TocGenerator` オブジェクトに `Process` メソッドが呼び出されます。結果コンテナは生成されたTOCを保持し、それがコンソールに出力されます。

```csharp
var resultContainer = generator.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);
```
