---
title: Reporting Services ServerでのSharePointのセットアップ
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

次に、SharePoint WFEで行ったのと同様の手順を実行する必要があります。最初にやるべきことは、必須コンポーネントのインストールを行い、それが完了したらSharePointのセットアップを開始します。

{{% /alert %}}

セットアップのために、私はServer Farmと完全インストールを選択しました。これは、SharePointの単独インストールを望んでいないため、私のSharePoint Boxに合わせるためです。

## SharePointの構成

{{% alert color="primary" %}}

**SharePoint構成ウィザードでは、既存のファームに接続したいと思います。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- SharePoint構成ウィザード**
{{% /alert %}}

{{% alert color="primary" %}}

**次に、私たちのファームが使用しているSharePoint_Configデータベースを指し示します。 If you don't know where this is, you can find out through Central Admin through System Settings -> Manager Servers in this farm.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- データベース構成設定を指定する**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- SharePoint 構成ウィザード**
{{% /alert %}}

{{% alert color="primary" %}}

**ウィザードが完了したら、現在のところレポートサーバーボックスで行うべきことはすべてです。ReportServer URL に戻ると、別のエラーが表示されますが、それは中央管理者を通じて構成していないためです。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- レポートサーバーエラー**
{{% /alert %}}