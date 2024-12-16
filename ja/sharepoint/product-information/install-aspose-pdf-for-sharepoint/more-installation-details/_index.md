---
title: さらなるインストールの詳細
type: docs
weight: 30
url: /ja/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: PDF SharePoint APIのインストールに関する詳細情報では、サイトコレクションでの展開、アクティベーション、非アクティベーションの方法について説明します。
---

## **展開**

{{% alert color="primary" %}}

**Aspose.PDF for SharePointは、展開中に以下のアクションを実行します:**
- Aspose.PDF.SharePoint.dllをグローバルアセンブリキャッシュにインストールし、web.configファイルにSafeControlエントリを追加します。
- 機能マニフェストやその他の必要ファイルを適切なディレクトリにインストールします。
- SharePointデータベースに機能を登録し、機能スコープでのアクティベーションが可能になるようにします。

{{% /alert %}}


## **アクティベーション**

{{% alert color="primary" %}}

**Aspose.PDF for SharePointは、サイト（サイトコレクション）レベルの機能としてパッケージ化されており、サイトコレクションでアクティベーションおよび非アクティベーションが可能です。**

{{% /alert %}}

{{% alert color="primary" %}}

アクティベーション中、この機能はサイトコレクションの親Webアプリケーションの仮想ディレクトリにいくつかの変更を加えます: サイトマップファイルに変換設定ページを追加します。
 必要なリソースファイルを仮想ディレクトリ内の App_GlobalResources フォルダーにコピーします。
 {{% /alert %}}
