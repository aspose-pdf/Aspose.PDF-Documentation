---
title: 画像抽出器
type: docs
weight: 80
url: /net/plugins/imageextractor/
description: ImageExtractorプラグインでPDFから画像を簡単に抽出
lastmod: "2024-01-24"
draft: false
---

.NETを使用してPDFファイルから画像を抽出する必要がある場合、Aspose.PDF for .NETは強力で簡単なソリューションを提供します。このガイドでは、オブジェクトを作成し、データソースを追加し、[Aspose.PDF Image Extractor](https://products.aspose.org/pdf/net/image-extractor/)を使用してプロセスメソッドを実行する基本的な手順を説明します。

## 前提条件

以下が必要です：

* Visual Studio 2019以降
* Aspose.PDF for .NET 21.1以降
* サンプルPDFファイル

Aspose.PDF for .NETライブラリは公式ウェブサイトからダウンロードするか、Visual StudioのNuGetパッケージマネージャーを使用してインストールできます。
さあ、コードに飛び込んでImageExtractorプラグインの使用方法を学びましょう。

## 手順

提供されたコードは、`ImageExtractor`プラグインを使用してPDFファイルから画像を抽出する方法を示しています。
提供されたコードは、`ImageExtractor`プラグインを使用してPDFファイルから画像を抽出する方法を示しています。

### 1. オブジェクトを作成する（ImageExtractor）

最初のステップは、`ImageExtractor`プラグインのインスタンスを作成することです。これは次のコードを使用して達成されます：

```csharp
using var plugin = new ImageExtractor();
```

ここで、`using`ステートメントは操作が完了したときにリソースが適切に解放されることを保証します。

### 2. データソースを追加

次に、画像抽出プロセスを設定するために`ImageExtractorOptions`クラスのインスタンスが作成されます。入力ファイルパスは`AddInput`メソッドを使用してオプションに追加されます：

```csharp
var imageExtractorOptions = new ImageExtractorOptions();
imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));
```

`"C:\Samples\"`と`"sample.pdf"`をあなたのPDFファイルの適切なパスとファイル名に置き換えてください。

### 3. プロセスメソッドを実行する

最終ステップは、プラグインとオプションを使用して画像抽出プロセスを処理することです：

```csharp

```csharp
var resultContainer = plugin.Process(imageExtractorOptions);
```

結果は`resultContainer`に格納され、抽出された画像が含まれます。

### 4. 抽出された画像を処理する

処理を実行した後、結果コンテナから抽出された画像を取得できます。以下のコードは、最初の抽出された画像を一時的な場所に保存する方法を示しています：

```csharp
var imageExtracted = resultContainer.ResultCollection[0].ToStream();
var someTemporaryPlace = File.OpenWrite("C:\\tmp\\tmp.jpg");
imageExtracted.CopyTo(someTemporaryPlace);
```

目的地のパスとファイル名をあなたの好みに合わせてカスタマイズしてください。

以下の完全な例をコピーできます：

```cs
using Aspose.Pdf.Plugins;

namespace AsposePluginsNet8.Documentation;

internal static class ImageExtractorDemo
{
    // <summary>
    // PDFファイルから画像を抽出するためのImageExtractorプラグインの使用方法を示します。
    // </summary>
    internal static void Run()
    {
        // ImageExtractorプラグインのインスタンスを作成します。
        using var plugin = new ImageExtractor();

        // ImageExtractorOptionsクラスのインスタンスを作成します。
        var imageExtractorOptions = new ImageExtractorOptions();

        // オプションに入力ファイルパスを追加します。
        imageExtractorOptions.AddInput(new FileDataSource(Path.Combine(@"C:\Samples\", "sample.pdf")));

        // プラグインとオプションを使用して画像抽出を処理します。
        var resultContainer = plugin.Process(imageExtractorOptions);

        // 結果コンテナから抽出された画像を取得します。
        var imageExtracted = resultContainer.ResultCollection[0].ToStream();
        var someTemporaryPlace = File.OpenWrite(Path.Combine(@"C:\Samples\","tmp.jpg"));
        imageExtracted.CopyTo(someTemporaryPlace);
    }
}
```

