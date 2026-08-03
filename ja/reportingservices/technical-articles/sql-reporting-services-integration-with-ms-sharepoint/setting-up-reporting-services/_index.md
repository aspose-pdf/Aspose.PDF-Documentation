---
title: レポートサービスの設定
linktitle: レポートサービスの設定
type: docs
weight: 20
url: /reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services サーバーで最初に停止するのは、Reporting Services 構成マネージャーです。

{{% /alert %}}

## サービスアカウント:

** Reporting Services に使用しているサービス アカウントを必ず理解してください。問題が発生した場合は、使用しているサービス アカウントに関連している可能性があります。デフォルトはネットワークサービスです。新しいビルドをデプロイするときは、問題が発生する可能性が高いため、常にドメイン アカウントを使用します。このサーバーのインスタンスでは、RSService.** というドメイン アカウントを使用しました。

![設定](setting-up-reporting-services_1.png)

**画像1:- サービスアカウントの設定**

## WebサービスURL:

{{% alert color="primary" %}}

**Web サービス URL を構成する必要があります。これは、Web サービス Reporting Services が使用する ReportServer 仮想ディレクトリ (vdir) であり、SharePoint が通信する相手となります。 vdir のプロパティ (つまり、SSL、ポート、ホスト ヘッダーなど) をカスタマイズしない限り、ここで [適用] をクリックするだけで準備完了です。**
![WebサービスURL](setting-up-reporting-services_2.png)

**画像 2:- Web サービス URL の設定 Web サービス URL が設定されると、次の結果が表示されるはずです**

![WebサービスURLの結果](setting-up-reporting-services_3.png)

**画像3:- WebサービスURLのセットアップ成功**
{{% /alert %}}

## データベース:

**Reporting Services カタログ データベースを作成する必要があります。これは、SQL 2008 または SQL 2008 R2 データベース エンジンに配置できます。 SQL11 も問題なく動作しますが、まだベータ版です。このアクションにより、デフォルトで ReportServer と ReportServerTempDB という 2 つのデータベースが作成されます。**

{{% alert color="primary" %}}
**これに関するもう 1 つの重要な手順は、データベースの種類として SharePoint Integrated を選択していることを確認することです。この選択を行うと、変更することはできません。**

![レポート サーバー データベースの作成](setting-up-reporting-services_4.png)

**画像 4:- レポート サーバー データベースの作成**

![データベースサーバーと認証タイプの設定](setting-up-reporting-services_5.png)

**画像5:- データベースサーバーと認証タイプの設定**

![データベース名とモードの設定](setting-up-reporting-services_6.png)

**画像6:- データベース名とモードの設定**
{{% /alert %}}

**資格情報については、これがレポート サーバーが SQL Server と通信する方法です。どのアカウントを選択しても、RSExecRole を介してカタログ データベースおよびいくつかのシステム データベース内で特定の権限が与えられます。 MSDB は、SQL エージェントを使用するため、サブスクリプションで使用するデータベースの 1 つです。**

![レポート サーバー データベースの資格情報のセットアップ](setting-up-reporting-services_7.png)

**画像 7:- レポート サーバー データベースの資格情報のセットアップ**

{{% alert color="primary" %}}

**データベース認証情報を指定すると、以下に指定されている結果を取得できるようになります。**

![レポート サーバー データベースの作成の進行状況](setting-up-reporting-services_8.png)

**画像8:- レポート サーバー データベースの作成の進行状況**

![レポート サーバー データベースの完了の概要](setting-up-reporting-services_9.png)

**画像9:- レポート サーバー データベースの完成の概要**
{{% /alert %}}

## レポートマネージャーの URL:

**レポート マネージャー URL は、SharePoint 統合モードでは使用されないため、スキップできます。 SharePoint は私たちのフロントエンドです。レポート マネージャーが機能しません。**

## 暗号化キー:

{{% alert color="primary" %}}
**暗号化キーをバックアップし、保管場所を確認してください。データベースを移行または復元する必要がある状況に陥った場合は、これらが必要になります。**

![レポート サーバーの暗号化キーのバックアップ](setting-up-reporting-services_10.png)

**画像10:- レポート サーバー暗号化キーのバックアップ**
{{% /alert %}}

{{% alert color="primary" %}}
**おめでとうございます! Configuration Manager を使用して Reporting Services を正常に構成しました。 [Web サービス URL] タブで URL を参照すると、次のような内容が表示されるはずです。**

![インストール後のレポート サーバーへのアクセス](setting-up-reporting-services_11.png)

**画像11:- インストール後のレポート サーバーへのアクセス**

**エラーの理由: SharePoint が WFE にインストールされており、Reporting Services のセットアップが完了しました。この例では、Reporting Services と SharePoint は別のマシン上にあります。それらが同じマシン上にあった場合、このエラーは発生しなかったでしょう。技術的には、RS Box に SharePoint をインストールする必要があります。つまり、IIS も有効になります。**
{{% /alert %}}

