---
title: Optimizer 
type: docs
weight: 80
url: /ja/net/plugins/optimizer/
description: Aspose.PDF Optimizerを使用してPDFファイルの最適化と操作を行う方法
lastmod: "2024-01-24"
---

この章では、[Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/) を使用して、C# アプリケーションでPDFファイルを最適化、リサイズ、回転する方法について探求します。
それでは、これらのタスクをステップバイステップで行う方法を学びましょう。

## 前提条件

以下が必要になります：

* Visual Studio 2019以降
* Aspose.PDF for .NET 24.1以降
* いくつかのフォームフィールドを含むサンプルPDFファイル

## PDFファイルの最適化

PDFファイルを最適化することは、そのサイズを減らし、パフォーマンスを向上させることを含みます。以下のスニペットは、このタスクを達成する方法を示しています。PDFファイルを最適化する方法は以下の通りです：

* 入力PDFファイル用の新しいファイルデータソースを作成します。
* 最適化された出力PDFファイル用の新しいファイルデータソースを作成します。
* `OptimizeOptions` のインスタンスを作成します。
* 入力および出力データソースを最適化オプションに追加します。
* 最適化オプションに入力および出力データソースを追加します。
* `Optimizer` のインスタンスを作成し、最適化オプションを使用して最適化を処理します。

```cs
// 入力PDFファイルのための新しいファイルデータソースを作成します。
var inputDataSource = new FileDataSource(inputPath);

// 最適化された出力PDFファイルのための新しいファイルデータソースを作成します。
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// OptimizeOptions の新しいインスタンスを作成します。
var options = new OptimizeOptions();

// 最適化オプションに入力および出力データソースを追加します。
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);


// Optimizer の新しいインスタンスを作成します。
var optimizer = new Optimizer();

// 最適化オプションを使用して最適化を処理します。
optimizer.Process(options);
```

## PDFファイルのリサイズ

PDFファイルのリサイズには、そのページサイズを変更することが含まれます。次のコードは、このタスクを達成する方法を示しています。PDFファイルをリサイズするためにこれらのステップに従ってください：

* 入力PDFファイルのための新しいファイルデータソースを作成します。
* 入力PDFファイル用の新しいファイルデータソースを作成します。
* リサイズされた出力PDFファイル用の新しいファイルデータソースを作成します。
* `ResizeOptions` のインスタンスを作成し、希望のページサイズを設定します。
* リサイズオプションに入力および出力データソースを追加します。
* `Optimizer` のインスタンスを作成し、リサイズオプションを使用してリサイズ処理を行います。

```cs
// 入力PDFファイル用の新しいファイルデータソースを作成します。
var inputDataSource = new FileDataSource("sample.pdf");

// リサイズされた出力PDFファイル用の新しいファイルデータソースを作成します。
var outputDataSource = new FileDataSource("sample_resized.pdf");

// ResizeOptionsの新しいインスタンスを作成し、希望のページサイズを設定します。
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// リサイズオプションに入力および出力データソースを追加します。
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Optimizerの新しいインスタンスを作成します。
var optimizer = new Optimizer();

// リサイズオプションを使用してリサイズ処理を行います。
optimizer.Process(opt);
```

## PDFページの回転
## PDFページの回転

PDFページの回転を行うことで、PDF文書内のページの向きを変更できます。以下の方法でPDFページを回転できます：

* 入力PDFファイル用の新しいファイルデータソースを作成します。
* 出力PDFファイル用の新しいファイルデータソースを作成します。
* `RotateOptions`のインスタンスを作成し、回転値を設定します。
* 入力と出力のデータソースを回転オプションに追加します。
* `Optimizer`のインスタンスを作成し、回転オプションを使用して回転処理を行います。

```cs
// 入力PDFファイル用の新しいファイルデータソースを作成します。
var inputDataSource = new FileDataSource(inputPath);

// 最適化された出力PDFファイル用の新しいファイルデータソースを作成します。
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// OptimizeOptionsの新しいインスタンスを作成します。
var opt = new RotateOptions();

// 最適化オプションに入力と出力のデータソースを追加します。
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// 回転値を設定します
opt.Rotation = Rotation.on180;

// Optimizerの新しいインスタンスを作成します。
var optimizer = new Optimizer();

// 最適化オプションを使用して最適化処理を行います。
optimizer.Process(opt)
```
## 結論

Aspose.PDF Optimizerプラグインを使用して、C#でPDFファイルを最適化、リサイズ、回転する方法を学びました。これらの技術をアプリケーションに取り入れて、要件に応じてPDFドキュメントを効率的に操作できます。
