---
title: インストールの詳細
linktitle: インストールの詳細
type: docs
weight: 30
url: /ja/sharepoint/more-installation-details/
lastmod: "2026-08-10"
description: PDF SharePoint API のインストールに関する詳細情報では、サイト コレクション上での展開、アクティベート、非アクティベートの方法が説明されています。
---

## デプロイ

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint はデプロイ時に次の操作を実行します：**
- Global Assembly Cache に Aspose.PDF.SharePoint.dll をインストールし、web.config ファイルに SafeControl エントリを追加します。
- 機能マニフェストおよびその他の必要なファイルを適切なディレクトリにインストールします。
- 機能を SharePoint データベースに登録し、機能スコープでの有効化が可能になるようにします。

{{% /alert %}}

## 有効化

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint はサイト（サイト コレクション）レベルの機能としてパッケージ化されており、サイト コレクションで有効化および無効化できます。**

{{% /alert %}}

{{% alert color="primary" %}}

有効化中に、この機能はサイト コレクションの親 Web アプリケーションの仮想ディレクトリに対していくつかの変更を行います: 変換設定ページをサイトマップ ファイルに追加します。必要なリソース ファイルを仮想ディレクトリの App_GlobalResources フォルダーにコピーします。

{{% /alert %}}
