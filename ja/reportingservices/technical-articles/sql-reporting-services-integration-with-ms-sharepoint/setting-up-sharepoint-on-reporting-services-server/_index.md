---
title: Reporting Services Server に SharePoint を設定する
linktitle: Reporting Services Server に SharePoint を設定する
type: docs
weight: 30
url: /ja/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

SharePoint WFE で行ったのと同様の手順を実行する必要があります。まず、Prereq uisites のインストールを実行し、完了したら SharePoint のセットアップを起動します。

{{% /alert %}}

セットアップでは、Server Farm を選択し、SharePoint Box に合わせて完全インストールを行います。SharePoint のスタンドアロンインストールは希望しません。

## SharePoint 設定

{{% alert color="primary" %}}

**SharePoint 構成ウィザードでは、既存のファームに接続したいです。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- SharePoint 構成ウィザード**
{{% /alert %}}

{{% alert color="primary" %}}

**次に、ファームが使用している SharePoint_Config データベースを指定します。場所がわからない場合は、Central Admin の System Settings → Manager Servers からこのファームで確認できます。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- データベース構成設定を指定**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- SharePoint 構成ウィザード**
{{% /alert %}}

{{% alert color="primary" %}}

**ウィザードが完了したら、今のところ Report Server ボックスで行う必要があることはそれだけです。ReportServer の URL に戻ると、別のエラーが表示されますが、これは Central Administrator で構成していないためです。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- レポートサーバーエラー**
{{% /alert %}}

