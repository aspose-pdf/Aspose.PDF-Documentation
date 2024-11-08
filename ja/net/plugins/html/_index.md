---
title: HTML コンバーター
type: docs
weight: 70
url: /ja/net/plugins/html/
description: Aspose.PDF PdfHtml プラグインを使用して PDF ファイルを HTML ファイルに変換する方法
lastmod: "2024-01-24"
draft: false
---

この記事では、PDF ファイルを HTML ファイルに変換するために [PdfHtml プラグイン](https://products.aspose.org/pdf/net/html-converter/) の使用方法を紹介します。

## 前提条件

以下が必要です：

* Visual Studio 2019 以降
* Aspose.PDF for .NET 21.1 以降
* サンプル PDF ファイルとサンプル HTML ファイル

Aspose.PDF for .NET ライブラリは公式ウェブサイトからダウンロードするか、Visual Studio の NuGet パッケージ マネージャーを使用してインストールできます。

## 手順

PdfHtml プラグインを使用して PDF ファイルを HTML ファイルに変換する基本的な手順は以下の通りです：

1. PdfHtml クラスのオブジェクトを作成する
2. 変換の方向に応じて PdfToHtmlOptions クラスまたは HtmlToPdfOptions クラスのオブジェクトを作成する
3. オプションオブジェクトに入力および出力データソースを追加する
4.
4.

変換の各方向に対してC＃コードでこれらのステップを実装する方法を見てみましょう。

### ステップ 1: PdfHtmlクラスのオブジェクトを作成する

PdfHtmlクラスは、PDFファイルをHTMLファイルに変換する機能を提供する主要なクラスです。これを使用するには、デフォルトコンストラクタを使用してインスタンスを作成する必要があります：

```cs
// PdfHtmlプラグインのインスタンスを作成する
var plugin = new PdfHtml();
```

### ステップ 2: 変換の方向に応じて、PdfToHtmlOptionsクラスまたはHtmlToPdfOptionsクラスのオブジェクトを作成する

PdfToHtmlOptionsおよびHtmlToPdfOptionsクラスは、出力形式、ページ範囲、エンコーディング、フォントなど、変換プロセスのさまざまなオプションやパラメータを指定するのに役立つヘルパークラスです。これらのクラスを使用するには、デフォルトコンストラクタを使用して適切なクラスのインスタンスを作成するか、いくつかのパラメータを渡して作成します。たとえば、PDFファイルを埋め込みリソース付きのHTMLファイルに変換するには、次のコードを使用できます：

```cs

```cs
// PdfToHtmlOptions クラスの新しいインスタンスを作成します
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);
```

HTMLファイルをPDFファイルにデフォルト設定で変換するには、次のコードを使用できます：

```cs
// HtmlToPdfOptions クラスの新しいインスタンスを作成します
var options = new HtmlToPdfOptions();
```

また、出力形式、ページ範囲、エンコーディング、フォントなど、オプションクラスのプロパティを使用して他のオプションを設定することもできます。例えば、UTF-8エンコーディングとArialフォントでPDFファイルをHTMLファイルに変換するには、次のコードを使用できます：

```cs
// PdfToHtmlOptions クラスの新しいインスタンスを作成します
var options = new PdfToHtmlOptions(PdfToHtmlOptions.SaveDataType.FileWithEmbeddedResources);

// エンコーディングを UTF-8 に設定します
options.Encoding = Encoding.UTF8;

// フォントを Arial に設定します
options.Font = "Arial";
```

### Step 3: Add the input and output data sources to the options object

入力および出力データソースは、変換して保存するPDFまたはHTMLファイルです。
入力データソースと出力データソースは、変換して保存したいPDFまたはHTMLファイルです。

```cs
// 入力ファイルと出力ファイルのパスを指定する
var inputPath = Path.Combine(@"C:\Samples\", "sample.pdf");
var outputPath = Path.Combine(@"C:\Samples\", "sample.html");

// オプションに入力ファイルと出力ファイルのパスを追加する
options.AddInput(new FileDataSource(inputPath));
options.AddOutput(new FileDataSource(outputPath));
```

### ステップ4: PdfHtmlオブジェクトのProcessメソッドを実行する

最終ステップは、オプションオブジェクトをパラメータとして渡してPdfHtmlオブジェクトのProcessメソッドを実行することです。このメソッドは変換を実行し、変換の結果を含むResultContainerオブジェクトを返します。結果には、状態、メッセージ、出力データソースなどが含まれています。ResultContainerクラスのプロパティやメソッドを使用して結果にアクセスすることができます。たとえば、結果コレクションから最初の結果を取得してコンソールに出力するには、次のコードを使用します：

```cs
// 変換を処理し、結果コンテナを取得する
var resultContainer = plugin.Process(options);

// 結果コレクションから最初の結果を取得する
var result = resultContainer.ResultCollection[0];

// 結果をコンソールに出力する
Console.WriteLine(result);
```
出力ファイルパスなどの情報が含まれます。
