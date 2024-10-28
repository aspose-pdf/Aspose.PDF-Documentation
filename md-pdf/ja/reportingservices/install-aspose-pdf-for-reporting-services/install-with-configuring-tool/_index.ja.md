---
title: 設定ツールによるインストール
type: docs
weight: 30
url: /reportingservices/install-with-configuring-tool/
lastmod: "2021-06-05"
---

Aspose.Pdf for Reporting Services 設定ツールは、サポートされている任意のレポートサーバー (RS) バージョンに対して、Aspose.Pdf for Reporting Services 拡張機能を設定するのに役立ちます。現在、RS2016、RS2017、RS2019、RS2022、および Power BI レポートサーバーをサポートしています。設定ツールは .NET Framework 4.8 を必要とします。

拡張機能をインストールしてレポートサーバーに登録する場合は、「Register」アクションタイプを選択します。拡張機能の登録解除とアンインストールを行う場合は、「Unregister」アクションタイプを選択します。

![todo:image_alt_text](install-with-configuring-tool_1.png)

**詳細な使用手順は次のとおりです:**

1. Aspose.Pdf for Reporting Services 拡張機能の DLL ファイルのパスを入力または参照します;
1. 対応するアクションタイプを選択します: Register または Unregister;
1. タブを選択して設定したいReport Serverのバージョンに対応してください。必ず、RSバージョンに対応するDLLファイルを選択してください。製品の要求されたバージョンがマシンにインストールされていない場合、設定ツールはヒントと共に通知します。名前付きRS2016インスタンス（デフォルトの'MSSQLSERVER'ではない）用の拡張機能を設定する場合は、カスタムインスタンス名を入力し、'Refresh'ボタンを押してください。
1. 底部のテキストボックスに表示される設定ファイルのパスと名前が正しいことを確認してください。正しくない場合は、'Refresh'ボタンを押して再度RSインスタンスを探すか、手動で調べることができます。
1. 'Config'ボタンを押してください。ツールは要求された設定を試行し、設定が成功したかどうかを通知します。