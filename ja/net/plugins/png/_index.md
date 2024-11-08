---
title: PNG変換器
type: docs
weight: 110
url: /ja/net/plugins/png/
description: Aspose.PDF PNGプラグインを使用してPDFをPNG画像に変換
lastmod: "2024-01-24"
---

.NETを使用して[PDF文書をPNG画像に変換する](https://products.aspose.org/pdf/net/png-converter/)場合、Aspose.PDF for .NETは堅牢なソリューションを提供します。本記事では、Aspose.PDFライブラリを使用してオブジェクトを作成し、データソースを追加し、プロセスメソッドを実行するための重要なステップを説明します。

## 前提条件

以下が必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 24.1以降
* サンプルPDFファイル

## コードウォークスルー

以下のコードは、Aspose.PDF PNGプラグインを使用したPNG変換デモを示しています：

```csharp
using Aspose.Pdf.Plugins;

//....

// PngOptionsクラスの新しいインスタンスを作成します。
var convertorOptions = new PngOptions();

// PngOptionsに入力パスと出力パスを追加します。
convertorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
convertorOptions.AddOutput(new FileDataSource(Path.Combine(@"C:\Samples\", "images")));

// 出力解像度を300 DPIに設定します。
convertorOptions.OutputResolution = 300;

// Pngクラスの新しいインスタンスを作成します。
Png converter = new ();

// PNG変換を処理し、結果コンテナを取得します。
ResultContainer resultContainer = converter.Process(convertorOptions);

// 結果をコンソールに表示します。
foreach (FileResult operationResult in resultContainer.ResultCollection.Cast<FileResult>())
{
      Console.WriteLine(operationResult.Data.ToString());
}
```
次の主要なステップを分解しましょう。

1. **オブジェクトを作成する（PngOptions および Png）**

   コードは、PNG変換を設定するために `PngOptions` クラスのインスタンスを作成することから始まります。さらに、処理を進めるために `Png` クラスのインスタンスも作成されます。

2. **データソースを追加する**

   入力PDFファイルパスは `PngOptions` に `AddInput` メソッドを使用して追加されます。同様に、PNG画像の出力パスは `AddOutput` メソッドを使用して追加されます。

3. **出力解像度を設定する**

   コードは、`PngOptions` クラスの `OutputResolution` プロパティを使用して出力解像度を300 DPIに設定します。

4. **プロセスメソッドを実行する**

   PNG変換は、設定された `PngOptions` をパスして `Png` クラスの `Process` メソッドを呼び出すことによって開始されます。結果は `resultContainer` に保存されます。

5. **結果を処理する**

   コードは結果をコンソールに表示し、変換されたファイルパスを示します。
