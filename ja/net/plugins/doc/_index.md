---
title: DOC Converter
type: docs
weight: 10
url: ja/net/plugins/doc/
description: PDFをWordに簡単に変換するPdfDocプラグイン
lastmod: "2024-01-24"
---

この記事では、[Aspose.Pdf DOC Converter for .NET](https://products.aspose.org/pdf/net/doc-converter/) を使用してPDFドキュメントをMicrosoft Word形式（.doc / .docx）に変換する方法を案内します。

## 前提条件

以下が必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 24.1以降
* いくつかのフォームフィールドが含まれているサンプルPDFファイル

Aspose.PDF for .NETライブラリは公式ウェブサイトからダウンロードするか、Visual StudioのNuGetパッケージマネージャを使用してインストールできます。

## 手順

### 1. 変換の設定（FileDataSourceクラスのスクリーンショット）

変換プロセスには三つの主要ステップが関与します：入力ファイルと出力ファイルを定義する、`PdfDoc`オブジェクトを作成する、変換オプションを指定する。

#### 1.1. データソースの定義

* **入力ファイル：** `FileDataSource`クラスを使用して、変換したいPDFファイルの場所を指定します。
* **入力ファイル:** `FileDataSource` クラスを使用して、変換するPDFファイルの場所を指定します。

```csharp
  FileDataSource inputDataSource = new(Path.Combine(@"C:\Samples\", "sample.pdf"));
```

  * `"C:\Samples\sample.pdf"`を実際のPDFファイルのパスに置き換えてください。

* **出力ファイル:** 同様に、別の`FileDataSource`オブジェクトを使用して、結果として得られるWordドキュメントの場所とファイル名を定義します。

```csharp
  FileDataSource outputDataSource = new(Path.Combine(@"C:\Samples\", "sample.docx"));
```

* `"C:\Samples\sample.docx"`を希望の出力パスとファイル名に置き換えてください。

### 2. PdfDocプラグインオブジェクトの作成 (PdfDocクラスのスクリーンショット)

次に、`PdfDoc`クラスのインスタンスを作成して変換を行います。

```csharp
  var plugin = new PdfDoc();
```

このオブジェクトは変換プロセスのエンジンとして機能します。

### 3. 変換オプションの設定

`PdfToDocOptions`クラスを使用して、変換プロセスを微調整できます。
`PdfToDocOptions` クラスでは、変換プロセスを細かく調整できます。

* **保存形式:** Word文書の出力形式を指定します。この場合、`SaveFormat.DocX` を使用して、Microsoft Word 2007以降の互換文書 (.docx) を生成します。

* **変換モード:** 変換時にプラグインがPDF構造をどのように解釈するかを定義します。`ConversionMode.EnhancedFlow` を使用して、レイアウトとフォーマットを最適化したWord文書を得るためです。

こちらはオプションを設定するためのコードスニペットです：

```csharp
  PdfToDocOptions options = new()
  {
      SaveFormat = SaveFormat.DocX,
      ConversionMode = ConversionMode.EnhancedFlow
  };
```

**入力と出力の追加:**

最後に、以前に定義したデータソースを `AddInput` および `AddOutput` メソッドを使用して変換オプションに関連付けます：

```csharp
  options.AddInput(inputDataSource);
  options.AddOutput(outputDataSource);
```

これにより、入力PDFと希望する出力Word文書が変換プロセスに接続されます。

### 4.
### 4.

すべてが設定されたので、設定されたオプションを渡して `PdfDoc` プラグインの `Process` メソッドを呼び出すことで変換を開始しましょう：

```csharp
  var resultContainer = plugin.Process(options);
```

このメソッドは変換を実行し、プロセスに関する詳細を含む `ResultContainer` オブジェクトを返します。

**結果の取得：**

基本的な変換には必須ではありませんが、`ResultContainer` オブジェクトの `ResultCollection` プロパティを通じて結果にアクセスできます。これはデバッグや特定の変換の詳細を追跡するのに役立つかもしれません。

```csharp
  var result = resultContainer.ResultCollection[0];

  // 結果を印刷する（デモンストレーション目的でオプション）
  Console.WriteLine(result);
```

この最終ステップで、PDF文書は指定されたWord形式に変換され、定義された出力場所に保存されます。

