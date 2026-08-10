---
title: インストールの詳細
linktitle: インストールの詳細
type: docs
weight: 30
url: /ja/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: PDF SharePoint API のインストールの詳細では、サイト コレクション上で PDF SharePoint API を展開、アクティブ化、非アクティブ化する方法について説明しています。
---

## 導入

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint は、展開中に次のアクションを実行します。**
- Aspose.PDF.SharePoint.dll をグローバル アセンブリ キャッシュにインストールし、SafeControl エントリを web.config ファイルに追加します。
- 機能マニフェストとその他の必要なファイルを適切なディレクトリにインストールします。
- SharePoint データベースに機能を登録し、機能スコープでアクティブ化できるようにします。

{{% /alert %}}

## アクティベーション

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint はサイト (サイト コレクション) レベルの機能としてパッケージ化されており、サイト コレクションでアクティブ化または非アクティブ化できます。**

{{% /alert %}}

{{% alert color="primary" %}}

この機能は、アクティブ化中に、サイト コレクションの親 Web アプリケーションの仮想ディレクトリにいくつかの変更を加えます。変換設定ページをサイトマップ ファイルに追加します。必要なリソース ファイルを仮想ディレクトリの App_GlobalResources フォルダーにコピーします。

{{% /alert %}}

