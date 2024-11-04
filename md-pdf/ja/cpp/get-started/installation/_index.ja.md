---
title: Aspose.PDF を C++ にインストールする
linktitle: インストール
type: docs
weight: 20
url: /cpp/installation/
description: このセクションでは、Aspose.PDF for C++ の製品説明と、独自にインストールする方法、および NuGet を使用する方法を示します。
lastmod: "2021-11-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aspose.PDF C++ コンポーネント

{{% alert color="primary" %}}

Aspose.PDF for C++ は、開発者が Adobe Acrobat を使用せずに PDF ドキュメントを作成、読み取り、操作できるネイティブ C++ ライブラリです。Aspose.PDF for C++ を使用すると、開発者はフォームを作成したり、テキストを追加/編集したり、PDF ページを操作したり、注釈を追加したり、カスタムフォントを扱ったりすることができます。ここでは、Aspose.PDF for C++ のドキュメントセクションで、API のすべての機能と、それらの機能を C++ アプリケーションで実装するための基本的な例を探索できます。

{{% /alert %}}

# インストール

## Aspose.PDF for C++ の評価

評価用に Aspose.PDF for C++ を簡単にダウンロードできます。 The evaluation download is the same as the purchased download. The evaluation version simply becomes licensed when you add a few lines of code to apply the license.

Aspose.PDFの評価版（ライセンスが指定されていない場合）は、製品の完全な機能を提供しますが、2つの制限があります：評価用の透かしを挿入し、任意のコレクションの要素は4つしか表示/編集できません。

{{% alert color="primary" %}}

Aspose.PDF for C++の評価版の制限なしでテストしたい場合は、30日間の一時ライセンスをリクエストすることもできます。[一時ライセンスを取得する方法](https://purchase.aspose.com/temporary-license)を参照してください。

{{% /alert %}}

## NuGetを通じたAspose.PDF for C++のインストール

NuGetは、C++プラットフォーム向けの無料でオープンソースの開発者向けパッケージ管理システムであり、開発中にサードパーティライブラリをC++アプリケーションに組み込むプロセスを簡素化することを目的としています。 これは、C++フレームワークを使用するVisual Studioプロジェクトでライブラリやツールを簡単に追加、削除、更新できるVisual Studio拡張機能です。ライブラリやツールは、NuGetパッケージを作成して[NuGetリポジトリ](https://www.nuget.org/packages/Aspose.PDF.Cpp/)に保存することで、他の開発者と簡単に共有できます。パッケージをインストールすると、NuGetはファイルをソリューションにコピーし、参照の追加やapp.configまたはweb.configファイルの変更など、必要な変更を自動的に行います。ライブラリを削除することにした場合、NuGetはファイルを削除し、プロジェクトに行った変更を元に戻して、混乱が残らないようにします。

### Aspose.PDF for C++の参照

#### パッケージマネージャーコンソールを使用してパッケージをインストール

- Visual StudioでC++アプリケーションを開きます。
- ツールメニューで、**NuGetパッケージマネージャー**を選択し、次に**パッケージマネージャーコンソール**を選択します。

- 最新のフルリリースをインストールするには、コマンド `Install-Package Aspose.PDF` を入力します。または、ホットフィックスを含む最新リリースをインストールするには、コマンド `Install-Package Aspose.PDF -prerelease` を入力します。- `Enter`キーを押します

#### パッケージをパッケージマネージャーコンソールを使用して更新する

既にNuGetを通じてコンポーネントを参照している場合、以下の手順に従って最新バージョンへの参照を更新してください:

- Visual StudioでC++アプリケーションを開きます。
- ツールメニューから、**NuGetパッケージマネージャー**を選択し、次に**パッケージマネージャーコンソール**を選択します。
- コマンド `Update-Package Aspose.PDF` を入力して最新の完全リリースを参照するか、コマンド `Update-Package Aspose.PDF -prerelease` を入力してホットフィックスを含む最新のリリースをインストールします。

#### パッケージマネージャーGUIを使用してパッケージをインストールする

パッケージマネージャーGUIを使用してコンポーネントを参照するには、以下の手順に従ってください:

- Visual StudioでC++アプリケーションを開きます。
- プロジェクトメニューから**NuGetパッケージの管理**を選択します。
- **参照**タブを選択します。
- 検索ボックスにAspose.PDFを入力してC++用のAspose.PDFを探します。
- C++用のAspose.PDFの最新バージョンの横にあるインストール/更新をクリックします。

![Installation](../images/install.gif)