---
title: 構成ツールでインストール
linktitle: 構成ツールでインストール
type: docs
weight: 30
url: /ja/reportingservices/install-with-configuring-tool/
description: 構成ツールを使用して Aspose.PDF for Reporting Services をシームレスに統合するためのステップバイステップ ガイド。
lastmod: "2026-07-29"
---

Aspose.PDF for Reporting Services Configuring Tool は、サポートされている Report Server (RS) バージョンのいずれかに対して Aspose.PDF for Reporting Services 拡張機能を構成するのに役立ちます。現在、RS2016、RS2017、RS2019、RS2022、および Power BI Report Server をサポートしています。構成ツールは .NET Framework 4.8 が必要です。

拡張機能をインストールして Report Server に登録したい場合は、‘Register’ アクションタイプを選択してください。拡張機能の登録解除およびアンインストールを行う場合は、‘Unregister’ アクションタイプを選択してください。

![todo:image_alt_text](install-with-configuring-tool_1.png)

**以下の手順では、詳細な使用方法を説明します。**

1. Aspose.PDF for Reporting Services 拡張機能の DLL ファイルのパスを入力するか参照してください;
1. 対応するアクションタイプを選択します: Register または Unregister;
1. 構成したい Report Server のバージョンに対応するタブを選択してください。対象の RS バージョン用に意図された DLL ファイルを選択したことを確認してください。要求されたバージョンの製品がマシンにインストールされていない場合、構成ツールがヒントで通知します。名前付き RS2016 インスタンス（デフォルトの \u0027MSSQLSERVER\u0027 ではない）用に拡張機能を構成している場合は、カスタムインスタンス名を入力し、\u0027Refresh\u0027 ボタンを押してください。
1. 下部のテキストボックスに表示されている構成ファイルのパスと名前が正しいことを確認してください。正しくない場合は、\u0027Refresh\u0027 ボタンを押して RS インスタンスを再度検索するか、手動で確認することができます。
1. \u0027Config\u0027 ボタンを押してください。ツールは要求された構成を実行し、構成が成功したかどうかを通知します。
 
