---
title: 他の例を実行する方法
linktitle: 他の例を実行する方法
type: docs
weight: 50
url: /ja/net/how-to-run-other-examples/    
description: このページは、例をダウンロードして実行する前に以下の要件を満たすためのガイドラインを示します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## ソフトウェア要件

例をダウンロードして実行する前に、以下の要件を満たしていることを確認してください。

1. Visual Studio 2010 以降
1. Visual Studio に NuGet パッケージマネージャーがインストールされていること。Visual Studio に最新の NuGet API バージョンがインストールされていることを確認してください。NuGet パッケージマネージャーをインストールする方法の詳細については、<https://docs.microsoft.com/en-us/nuget/install-nuget-client-tools> をご覧ください。
1. `Tools->Options->NuGet Package Manager->Package Sources` に移動し、**nuget.org** のオプションがチェックされていることを確認してください。
1.
## GitHubからダウンロード

Aspose.PDF for .NETのすべての例は[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-.NET)にホストされています。

- 好きなGitHubクライアントを使用してリポジトリをクローンするか、[こちら](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/archive/master.zip)からZIPファイルをダウンロードします。
- ZIPファイルの内容をコンピュータの任意のフォルダに抽出します。すべての例は**Examples**フォルダにあります。
- Visual Studioのソリューションファイルが2つあります。1つはコンソール用、もう1つはWebアプリケーション用です。
- プロジェクトはVisual Studio 2013で作成されていますが、ソリューションファイルはVisual Studio 2010 SP1以降と互換性があります。
- Visual Studioでソリューションファイルを開き、プロジェクトをビルドします。
- 最初の実行時に依存関係がNuGetを通じて自動的にダウンロードされます。
- **Examples**のルートフォルダにある**Data**フォルダには、CSharpの例で使用される入力ファイルが含まれています。例のプロジェクトと一緒に**Data**フォルダをダウンロードすることが必須です。
- *RunExamples.cs*ファイルを開きます。ここからすべての例が呼び出されます。
- *RunExamples.cs* ファイルを開きます。ここからすべての例が呼び出されます。
- プロジェクト内で実行したい例のコメントを解除します。

何か問題があれば、私たちのフォーラムを通じて気軽にお問い合わせください。

## 貢献

例を追加または改善したい場合、プロジェクトに貢献することをお勧めします。このリポジトリのすべての例やショーケースプロジェクトはオープンソースであり、自分のアプリケーションで自由に使用できます。

貢献するには、リポジトリをフォークし、ソースコードを編集してプルリクエストを作成します。変更をレビューし、役立つと判断された場合、リポジトリに含めます。
