---
title: 設定ツールを使ってインストールする
linktitle: 設定ツールを使ってインストールする
type: docs
weight: 30
url: /reportingservices/install-with-configuring-tool/
description: シームレスな統合のための構成ツールを使用して、Aspose.PDF for Reporting Services をインストールするためのステップバイステップ ガイド。
lastmod: "2021-06-05"
---

Aspose.PDF for Reporting Services 構成ツールは、サポートされているレポート サーバー (RS) バージョンのいずれかに対して Aspose.PDF for Reporting Services 拡張機能を構成するのに役立ちます。現在、RS2016、RS2017、RS2019、RS2022、Power BI Report Server をサポートしています。構成ツールには .NET Framework 4.8 が必要です。

拡張機能をインストールしてレポート サーバーに登録する場合は、`Register` アクション タイプを選択します。拡張機能の登録解除とアンインストールには、`Unregister` アクション タイプを選択します。

![Install with configuring tool](install-with-configuring-tool_1.png)

**次の手順では、その使用方法を詳しく説明します。**

1. Reporting Services 拡張機能の Aspose.PDF の DLL ファイルのパスを入力または参照します。
1. 対応するアクション タイプを選択します: [登録] または [登録解除]。
1. 構成するレポート サーバーのバージョンに対応するタブを選択します。RS バージョン用の DLL ファイルを選択していることを確認してください。要求されたバージョンの製品がマシンにインストールされていない場合、構成ツールはヒントを通知します。名前付き RS2016 インスタンス (デフォルトの「MSSQLSERVER」インスタンスではない) の拡張機能を構成している場合は、カスタム インスタンス名を入力して、[更新] ボタンを押してください。
1. 下部のテキストボックスに表示されている構成ファイルのパスと名前が正しいことを確認してください。そうでない場合は、[更新] ボタンを押して RS インスタンスを再度検索するか、手動で検索することができます。
1. 「設定」ボタンを押します。ツールは要求された構成の作成を試行し、構成が成功したかどうかを通知します。
