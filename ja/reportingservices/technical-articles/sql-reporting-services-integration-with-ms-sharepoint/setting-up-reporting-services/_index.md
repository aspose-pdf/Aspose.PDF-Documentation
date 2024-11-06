---
title: レポート サービスのセットアップ
type: docs
weight: 20
url: ja/reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

レポート サービス サーバーで最初に確認するのは、レポート サービス構成マネージャーです。

{{% /alert %}}

## サービス アカウント:

**レポート サービスに使用しているサービス アカウントを理解していることを確認してください。問題が発生した場合、それは使用しているサービス アカウントに関連している可能性があります。デフォルトはネットワーク サービスです。新しいビルドを展開する際には、常にドメイン アカウントを使用します。これは、問題が発生しやすい場所だからです。このサーバーのインスタンスでは、RSService というドメイン アカウントを使用しました。**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**画像1:- サービス アカウントのセットアップ**

## Web サービス URL:

{{% alert color="primary" %}}

**Web サービス URL を構成する必要があります。 これはレポートサーバーの仮想ディレクトリ（vdir）で、Webサービスが使用するレポートサービスをホストし、SharePointが通信します。vdirのプロパティ（SSL、ポート、ホストヘッダなど）をカスタマイズしたいのでなければ、ここで「適用」をクリックするだけで問題ありません。**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**画像2:- WebサービスURLの設定 WebサービスURLが設定されたら、次の結果が表示されるはずです**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**画像3:- WebサービスURLの正常な設定**
{{% /alert %}}

## データベース:

**レポートサービスカタログデータベースを作成する必要があります。これは、任意のSQL 2008またはSQL 2008 R2データベースエンジンに配置できます。SQL11も問題なく動作しますが、まだベータ版です。このアクションにより、デフォルトで2つのデータベース、ReportServerとReportServerTempDBが作成されます。**

{{% alert color="primary" %}}
**ここでのもう一つの重要なステップは、データベースの種類としてSharePoint統合を選択することを確認することです。  この選択が行われると、変更することはできません。**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**画像4:- レポートサーバーデータベースの作成**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**画像5:- データベースサーバーと認証タイプの設定**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**画像6:- データベース名とモードの設定**
{{% /alert %}}

**資格情報については、これはレポートサーバーがSQLサーバーと通信する方法です。選択したアカウントには、RSExecRoleを通じて、カタログデータベースおよびいくつかのシステムデータベース内で特定の権利が与えられます。サブスクリプション使用のためにSQLエージェントを利用するため、MSDBはこれらのデータベースの一つです。**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**画像7:- レポートサーバーデータベースの資格情報の設定**

{{% alert color="primary" %}}

**データベースの資格情報が指定されると、以下のように結果を得ることができるはずです。**


![todo:image_alt_text](setting-up-reporting-services_8.png)
**Image8:- レポートサーバーデータベース作成進行状況**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- レポートサーバーデータベース完了サマリー**
{{% /alert %}}

## レポートマネージャーURL:

**SharePoint統合モードでは使用されないため、レポートマネージャーURLをスキップできます。SharePointがフロントエンドです。レポートマネージャーは機能しません。**

## 暗号化キー:

{{% alert color="primary" %}}
**暗号化キーをバックアップし、どこに保管しているかを確認してください。データベースを移行したり復元したりする必要がある場合には、これらが必要になります。**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- レポートサーバー暗号化キーのバックアップ**
{{% /alert %}}

{{% alert color="primary" %}}
**おめでとうございます！構成マネージャーを使用してレポートサービスを正常に構成しました。WebサービスURLタブのURLにアクセスすると、以下のようなものが表示されるはずです。**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- インストール後のレポートサーバーアクセス**

**エラーの理由: SharePointが私たちのWFEにインストールされており、Reporting Servicesのセットアップが完了しました。この例では、Reporting ServicesとSharePointは異なるマシンにあります。同じマシンにあれば、このエラーは発生しません。技術的にはRSボックスにSharePointをインストールする必要があります。それはIISも有効になることを意味します。**
{{% /alert %}}
