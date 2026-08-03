---
title: Reporting Services サーバーでの SharePoint のセットアップ
linktitle: Reporting Services サーバーでの SharePoint のセットアップ
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

次に、SharePoint WFE の場合と同様の手順を実行する必要があります。まず、前提条件のインストールを実行し、それが完了したら、SharePoint セットアップを起動します。

{{% /alert %}}

SharePoint のスタンドアロン インストールを望まないため、セットアップにはサーバー ファームを選択し、SharePoint Box に一致する完全なインストールを選択します。

## SharePointの構成

{{% alert color="primary" %}}

**SharePoint 構成ウィザードでは、既存のファームに接続したいと考えています。**

![SharePoint 構成ウィザード](setting-up-sharepoint-on-reporting-services-server_1.png)

**画像1:- SharePoint構成ウィザード**
{{% /alert %}}

{{% alert color="primary" %}}

**次に、ファームが使用している SharePoint_Config データベースを指すようにします。これがどこにあるのかわからない場合は、中央管理からシステム設定 -> このファームのマネージャー サーバーを選択して確認できます。**

![SharePoint 構成データベース](setting-up-sharepoint-on-reporting-services-server_2.png)

**画像 2:- データベース構成設定を指定します**

![SharePoint 構成ウィザード](setting-up-sharepoint-on-reporting-services-server_3.png)

**画像3:- SharePoint構成ウィザード**
{{% /alert %}}

{{% alert color="primary" %}}

**ウィザードが完了したら、現時点でレポート サーバー ボックスで行う必要があるのはこれだけです。 ReportServer URL に戻ると、別のエラーが表示されます。これは、Central Administrator を使用して構成していないためです。**

![SharePoint 構成エラー](setting-up-sharepoint-on-reporting-services-server_4.png)

**画像4:- レポートサーバーエラー**
{{% /alert %}}
