---
title: Reporting Services の設定
linktitle: Reporting Services の設定
type: docs
weight: 20
url: /ja/reportingservices/setting-up-reporting-services/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services Server での最初の目的地は Reporting Services Configuration Manager です。

{{% /alert %}}

## サービス アカウント:

**Reporting Services で使用しているサービス アカウントを必ず理解してください。問題が発生した場合、使用しているサービス アカウントが原因である可能性があります。デフォルトは Network Service です。新しいビルドをデプロイする際は常にドメイン アカウントを使用します。なぜなら問題が発生しやすいからです。このサーバー インスタンスでは、RSService という名前のドメイン アカウントを使用しています。**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- サービス アカウントの設定**

## Web Service URL:

{{% alert color="primary" %}}

**Web Service URL を構成する必要があります。これは、Reporting Services が使用する Web Services をホストする ReportServer 仮想ディレクトリ (vdir) であり、SharePoint が通信する対象です。vdir のプロパティ (例: SSL、ポート、ホストヘッダー等) をカスタマイズしたくない限り、ここで「Apply」をクリックすればすぐに使用できるはずです。**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- Web Service URL の設定 Web service URL が設定されたら、以下の結果が表示されるはずです**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- Web service URL の設定に成功**
{{% /alert %}}

## データベース:

**Reporting Services カタログ データベースを作成する必要があります。これは任意の SQL 2008 または SQL 2008 R2 データベース エンジンに配置できます。SQL11 も問題なく動作しますが、まだベータ版です。この操作により、デフォルトで 2 つのデータベース、ReportServer と ReportServerTempDB が作成されます。**

{{% alert color="primary" %}}
**この際のもう一つ重要なステップは、データベースの種類として SharePoint Integrated を選択することを確認することです。この選択を行うと、変更できなくなります。**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- レポート サーバー データベースの作成**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- データベースサーバーと認証タイプの設定**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- データベース名とモードの設定**
{{% /alert %}}

**認証情報については、Report Server が SQL Server と通信する方法です。選択したアカウントには、RSExecRole を介して Catalog データベースおよびいくつかのシステムデータベース内で特定の権限が付与されます。MSDB は、SQL Agent を使用するサブスクリプション利用のためのデータベースの一つです。**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- Report Server データベース認証情報の設定**

{{% alert color="primary" %}}

**データベースの資格情報が指定されると、以下に示す結果を取得できるはずです。**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- Report Server データベース作成の進捗**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- Report Server データベース完了の概要**
{{% /alert %}}

## Report Manager の URL:

**SharePoint 統合モードでは Report Manager URL は使用されないため、スキップできます。SharePoint がフロントエンドです。Report Manager は機能しません。**

## 暗号化キー:

{{% alert color="primary" %}}
**暗号化キーをバックアップし、保管場所を把握しておいてください。データベースの移行や復元が必要な状況になった場合、これらが必要になります。**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- Report Server 暗号化キーのバックアップ**
{{% /alert %}}

{{% alert color="primary" %}}
**おめでとうございます！Configuration Manager を使用して Reporting Services の構成に成功しました。Web Service URL タブの URL にアクセスすると、以下のような表示がされるはずです。**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- インストール後の Report Server アクセス**

**エラーの原因: SharePoint は WFE にインストールされており、Reporting Services の設定は完了しています。この例では、Reporting Services と SharePoint が別々のマシン上にあります。同じマシン上にあれば、このエラーは発生しませんでした。実際には RS ボックスに SharePoint をインストールする必要があります。つまり、IIS も有効になるということです。**
{{% /alert %}}


