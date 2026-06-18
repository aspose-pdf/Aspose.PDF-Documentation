---
title: インストールの詳細情報
linktitle: インストールの詳細情報
type: docs
weight: 30
url: /ja/sharepoint/more-installation-details/
lastmod: "2026-06-18"
description: PDF SharePoint API のインストールに関する詳細情報では、サイトコレクション上でのデプロイ、アクティベート、およびデアクティベート方法が説明されています。
---

## **デプロイ**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint はデプロイ中に以下の操作を実行します:**
- Aspose.PDF.SharePoint.dll を Global Assembly Cache にインストールし、web.config ファイルに SafeControl エントリを追加します。
- 機能マニフェストとその他の必要なファイルを適切なディレクトリにインストールします。
- 機能を SharePoint データベースに登録し、機能スコープでの有効化ができるようにします。

{{% /alert %}}


## **有効化**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint はサイト（サイトコレクション）レベルの機能としてパッケージ化されており、サイトコレクションで有効化および無効化できます。**

{{% /alert %}}

{{% alert color="primary" %}}

有効化時に、機能はサイトコレクションの親 Web アプリケーションの仮想ディレクトリにいくつかの変更を加えます: 変換設定ページを sitemap ファイルに追加します。必要なリソース ファイルを仮想ディレクトリの App_GlobalResources フォルダーにコピーします。

{{% /alert %}}
