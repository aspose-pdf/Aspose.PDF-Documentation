---
title: MSIインストーラでインストール
linktitle: MSIインストーラでインストール
type: docs
weight: 10
url: /ja/reportingservices/install-with-msi-installer/
description: MSIインストーラを使用してAspose.PDF for Reporting Servicesをインストールする方法を学びます。迅速なセットアップのための簡潔なガイドです。
lastmod: "2026-07-29"
---

MSIインストーラを使用してAspose.PDF for Reporting Servicesをインストールできます。Aspose.Pdf.ReportingServices.msi を実行し、インストーラが提供する手順に従ってください。インストーラはアセンブリやその他のファイルを指定されたディレクトリにコピーし、Reporting Services のデフォルトインスタンスに製品をインストールします。特別な構成パラメータを追加したい場合を除き、手動でファイルをコピーしたり変更したりする必要はありません（'Configure Aspose.PDF for Reporting Services' セクション参照）。

自動インストールはほとんどの場合で最適な選択肢です。ただし、以下のような状況では手動で製品をインストールする必要がある場合があります：
 
- I/O セキュリティの問題により自動インストールが失敗します。
- Reporting Services 2016 の名前付き（デフォルト以外）インスタンス、または複数のインスタンスに製品をインストールする必要があります。
- 最新バージョンにアップグレードし、古いバージョンをアンインストールして新しいものを MSI installer でインストールするのではなく、アセンブリを置き換えるだけです。
 
{{% alert color="primary" %}}

注意: 後者の場合、他のコンポーネント（例えばオフラインドキュメント）が対応するバージョンにアップグレードされないことになる可能性があります。

{{% /alert %}}
