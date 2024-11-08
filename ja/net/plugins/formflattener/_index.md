---
title: フォームエクスポーター
type: docs
weight: 60
url: /ja/net/plugins/formflattener/
description: Aspose.PDF FormFlattenerプラグインを使用してPDFファイルのフォームフィールドをフラット化する方法
lastmod: "2024-01-24"
---

この記事では、PDFファイルのフォームフィールドをフラット化する[FormFlattenerプラグイン](https://products.aspose.org/pdf/net/form-flattener/)の使用方法を紹介します。

## 前提条件

以下が必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 21.1以降
* いくつかのフォームフィールドが含まれているサンプルPDFファイル

公式ウェブサイトからAspose.PDF for .NETライブラリをダウンロードするか、Visual StudioのNuGetパッケージマネージャーを使用してインストールできます。

## 手順

FormFlattenerプラグインを使用してPDFファイルのフォームフィールドをフラット化する基本的な手順は以下のとおりです：

1. FormFlattenerクラスのオブジェクトを作成する
1. FormFlattenAllFieldsOptionsクラスまたはFormFlattenSelectedFieldsOptionsクラスのオブジェクトを作成する。すべてのフィールドをフラット化するか、一部のフィールドをフラット化するかによって異なります
1. FormFlattener オブジェクトの Process メソッドを実行する

これらのステップを C# コードで実装する方法を見てみましょう。

### ステップ 1: FormFlattener クラスのオブジェクトを作成する

FormFlattener クラスは、PDF ファイルのフォームフィールドをフラット化する機能を提供するメインクラスです。これを使用するには、デフォルトコンストラクタを使用してインスタンスを作成する必要があります：

```cs
// FormFlattener プラグインのインスタンスを作成する
var plugin = new FormFlattener();
```

### ステップ 2: FormFlattenAllFieldsOptions または FormFlattenSelectedFieldsOptions クラスのオブジェクトを作成する。これは、すべてのフィールドをフラット化するか、または一部のフィールドをフラット化するかによって異なります

FormFlattenAllFieldsOptions および FormFlattenSelectedFieldsOptions クラスは、フラット化プロセスのさまざまなオプションとパラメータを指定するためのヘルパークラスです。
FormFlattenAllFieldsOptionsクラスとFormFlattenSelectedFieldsOptionsクラスは、フラット化プロセスのためのさまざまなオプションとパラメータを指定するためのヘルパークラスです。

```cs
// 全てのフィールドをフラット化するためのオプションを作成
var options = new FormFlattenAllFieldsOptions();
```

左下のx座標が300より大きいフォームフィールドのみをフラット化するには、以下のコードを使用できます：

```cs
// 選択したフィールドをフラット化するためのオプションを作成
var options = new FormFlattenSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Step 3: Add the input and output data sources to the options object

入力および出力データソースは、フラット化して保存したいPDFファイルです。
入力と出力のデータソースは、フラット化して保存したいPDFファイルです。

```cs
// オプションに入力と出力のデータソースを追加
options.Inputs.Add(new FileDataSource("sample.pdf"));
options.Outputs.Add(new FileDataSource("sample-flat.pdf"));
```

### ステップ4: FormFlattenerオブジェクトのProcessメソッドを実行する

最終ステップは、FormFlattenerオブジェクトのProcessメソッドを実行し、オプションオブジェクトをパラメータとして渡すことです。このメソッドはフラット化プロセスを実行し、ResultContainerオブジェクトを返します。ResultContainerオブジェクトには、プロセスの結果、ステータス、メッセージ、出力データソースなどが含まれています。ResultContainerクラスのプロパティやメソッドを使用して結果にアクセスできます。例えば、結果コレクションから最初の結果を取得し、コンソールに印刷するには、以下のコードを使用できます：

```cs
// オプションを処理して結果コンテナを取得
var resultContainer = plugin.Process(options);

// 結果コンテナから最初の結果を取得
var result = resultContainer.ResultCollection[0];

// 結果を印刷
Console.WriteLine(result);
```
出力ファイルパスのような情報が含まれます。
