---
title: Aspose.PDF for SharePoint ライセンスのインストール
linktitle: Aspose.PDF for SharePoint ライセンスのインストール
type: docs
weight: 10
url: /ja/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: 評価に満足したら、PDF SharePoint API のライセンスを購入し、インストール手順に従って適用できます。
---

{{% alert color="primary" %}}

評価に満足したら、 [ライセンスを購入する](https://purchase.aspose.com/buy)。購入する前に、必ずライセンス サブスクリプション条項を理解し、同意してください。

{{% /alert %}}

{{% alert color="primary" %}}

ライセンスは、注文の支払い後に電子メールで送信されます。ライセンスは、通常の SharePoint ソリューション パッケージを含む .zip アーカイブです。

このアーカイブには以下が含まれます。

- Aspose.PDF.SharePoint.License.wsp

SharePoint ソリューション パッケージ ファイル。 Aspose.PDF for SharePoint ライセンスは、サーバー ファーム全体での展開/撤回を容易にする SharePoint ソリューションとしてパッケージ化されています。

- readme.txt

ライセンスのインストール手順。ライセンスのインストールは、stsadm.exe を介してサーバー コンソールから実行されます。ライセンスをインストールするために必要な手順は以下のとおりです。

**注:** わかりやすくするためにパスは省略されています。 stsadm.exe やソリューション ファイルを実行するときに、実際のパスを追加する必要がある場合があります。

1. stsadm を実行して、ソリューションを SharePoint ソリューション ストアに追加します。

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. ファーム内のすべてのサーバーにソリューションを展開します。

stsadm.exe -odeploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 管理タイマー ジョブを実行して、展開をただちに完了します。

stsadm.exe -o execadmsvcjobs

**注意:** Windows SharePoint Services Administration サービスが開始されていない場合、展開手順を実行するときに警告が表示されます。 Stsadm.exe は、このサービスと Windows SharePoint タイマー サービスを利用して、ファーム全体にソリューション データをレプリケートします。これらのサービスがサーバー ファームで実行されていない場合は、各サーバーでライセンスを展開する必要がある場合があります。

{{% /alert %}}

