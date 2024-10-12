---
title: 他のAspose.PDF for C++の例を実行する方法
linktitle: 他の例を実行する方法
type: docs
weight: 50
url: /cpp/how-to-run-other-examples/
description: このページは、例をダウンロードして実行する前に役立つガイドラインを示しています。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ソフトウェア要件

例をダウンロードして実行する前に、次の要件を満たしていることを確認してください。

1. Microsoft Visual Studio 2017以降。
1. Visual StudioにNuGetパッケージマネージャーがインストールされていること。Visual Studioに最新のNuGet APIバージョンがインストールされていることを確認してください。NuGetパッケージマネージャーのインストール方法については、<http://docs.nuget.org/ndocs/guides/install-nuget>を確認してください。
1. `ツール->オプション->NuGetパッケージマネージャー->パッケージソース`に移動し、オプション**nuget.org**がチェックされていることを確認してください。
1. Example project uses NuGet Automatic Package Restore feature therefore you should have an active internet connection. If you do not have an active internet connection on the machine where examples are to be executed please check [Installation](/pdf/cpp/installation/) and manually add reference to Aspose.PDF.dll in the example project.

## Download from GitHub

All examples of Aspose.PDF for C++ are hosted on [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-C).

- お気に入りのGitHubクライアントを使用してリポジトリをクローンするか、[ここ](https://codeload.github.com/aspose-pdf/Aspose.PDF-for-C/zip/master)からZIPファイルをダウンロードできます。
- ZIPファイルの内容をコンピュータ上の任意のフォルダーに抽出します。すべての例は**Examples**フォルダーにあります。
- 2つのVisual Studioソリューションファイルがあり、1つはコンソール用、もう1つはWebアプリケーション用です。
- プロジェクトはVisual Studio 2013で作成されていますが、ソリューションファイルはVisual Studio 2010 SP1以降と互換性があります。

- Visual Studioでソリューションファイルを開き、プロジェクトをビルドします。- 初回実行時に依存関係がNuGetを通じて自動的にダウンロードされます。
- **Examples**のルートフォルダにある**Data**フォルダには、CSharpの例で使用される入力ファイルが含まれています。例のプロジェクトと一緒に**Data**フォルダをダウンロードすることが必須です。
- *RunExamples.cs*ファイルを開き、すべての例はここから呼び出されます。
- プロジェクト内で実行したい例のコメントを外します。

例の設定や実行に問題がある場合は、フォーラムを通じてお気軽にご連絡ください。

## Contribute

例を追加したり改善したりしたい場合は、プロジェクトへの貢献をお勧めします。このリポジトリのすべての例とショーケースプロジェクトはオープンソースであり、自分のアプリケーションで自由に使用できます。

貢献するには、リポジトリをフォークし、ソースコードを編集してプルリクエストを作成します。変更をレビューし、有用であればリポジトリに含めます。