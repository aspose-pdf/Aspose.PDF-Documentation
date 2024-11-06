---
title: フォームエクスポーター
type: docs
weight: 50
url: ja/net/plugins/formexpoter/
description: Aspose.PDFフォームエクスポータープラグインを使用して、CSVファイルにフォームフィールド値をエクスポートする方法
lastmod: "2024-01-24"
draft: false
---

この記事では、PDFファイルからCSVファイルへフォームフィールド値をエクスポートできる[Form Exporterプラグイン](https://products.aspose.org/pdf/net/form-exporter/)の使用方法を説明します。

## 前提条件

以下が必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 21.1以降
* フォームフィールドが含まれるサンプルPDFファイル

Aspose.PDF for .NETライブラリは公式ウェブサイトからダウンロードするか、Visual StudioのNuGetパッケージマネージャーを使用してインストールできます。

## 手順

FormExporterプラグインを使用してCSVファイルにフォームフィールド値をエクスポートする基本的な手順は以下の通りです：

1. `FormExporter` クラスのオブジェクトを作成します
1. `FormExporterValuesToCsvOptions` クラスのオブジェクトを作成し、条件と区切り文字を指定します
1.
1.
1. `FormExporter` オブジェクトの `Process` メソッドを実行する

これらのステップをC#コードで実装する方法を見てみましょう。

### ステップ1: FormExporterクラスのオブジェクトを作成する

FormExporterクラスは、フォームフィールドの値をCSVファイルにエクスポートする機能を提供するメインクラスです。これを使用するには、デフォルトコンストラクタを使用してインスタンスを作成する必要があります：

```cs
// FormExporterプラグインのインスタンスを作成する
var plugin = new FormExporter();
```

### ステップ2: FormExporterValuesToCsvOptionsクラスのオブジェクトを作成し、述語と区切り文字を指定する

FormExporterValuesToCsvOptionsクラスは、エクスポートプロセスのさまざまなオプションやパラメータを指定するためのヘルパークラスです。
FormExporterValuesToCsvOptions クラスは、エクスポートプロセスに関する様々なオプションやパラメータを指定するためのヘルパークラスであり、条件や区切り文字などを設定できます。

```cs
// CSVにフォームフィールド値をエクスポートするためのオプションを作成する
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```

### ステップ 3: オプションオブジェクトに入力と出力のデータソースを追加する

入力および出力のデータソースは、エクスポートしたいPDFファイルと保存したいCSVファイルです。
入力データソースと出力データソースは、エクスポートするPDFファイルと保存するCSVファイルです。

```cs
// オプションに入力と出力のファイルを追加
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### ステップ 4: FormExporterオブジェクトのProcessメソッドを実行する

最終ステップは、FormExporterオブジェクトのProcessメソッドを実行し、オプションオブジェクトをパラメータとして渡すことです。
最終ステップは、FormExporter オブジェクトの Process メソッドを実行し、オプションオブジェクトをパラメータとして渡すことです。

```cs
// プラグインを使用してフォームフィールド値を処理します
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

結果には、入力および出力ファイルのパスなどの情報が含まれます。
