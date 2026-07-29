---
title: Reporting Services Server で SharePoint を設定する
linktitle: Reporting Services Server で SharePoint を設定する
type: docs
weight: 30
url: /ja/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

現在、SharePoint WFE で行ったのと同様の手順を実行する必要があります。まず最初に Prereq uisites のインストールを実行し、完了したら SharePoint のセットアップを開始します。

{{% /alert %}}

セットアップでは、SharePoint のスタンドアロン インストールを望まず、Server Farm を選択し、SharePoint Box に合わせた完全インストールを行います。

## SharePoint 構成

{{% alert color="primary" %}}

**SharePoint 構成ウィザードでは、既存のファームに接続したいです。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- SharePoint 設定ウィザード**
{{% /alert %}}

{{% alert color="primary" %}}

**次に、ファームが使用している SharePoint_Config データベースを指すように設定します。場所が分からない場合は、Central Admin の System Settings -> Manager Servers でこのファーム内の場所を確認できます。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- データベース構成設定を指定**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- SharePoint 設定ウィザード**
{{% /alert %}}

{{% alert color="primary" %}}

**ウィザードが完了したら、現時点で Report Server ボックスで行う必要があるのはそれだけです。ReportServer の URL に戻ると、別のエラーが表示されますが、これは Central Administrator で設定していないためです。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- レポートサーバーエラー**
{{% /alert %}}
