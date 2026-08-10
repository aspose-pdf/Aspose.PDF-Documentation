---
title: Aspose.Pdf for SharePoint ライセンスのインストール
linktitle: Aspose.Pdf for SharePoint ライセンスのインストール
type: docs
weight: 10
url: /ja/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-08-10"
description: 評価に満足したら、PDF SharePoint API のライセンスを購入し、適用するためのインストール手順に従うことができます。
---

{{% alert color="primary" %}}

評価に満足したら、次のことができます [ライセンスを購入する](https://purchase.aspose.com/buy). 購入する前に、ライセンス サブスクリプションの条件を理解し、同意していることを確認してください。

{{% /alert %}}

{{% alert color="primary" %}}

注文が支払われた後、ライセンスがメールで送信されます。ライセンスは通常の SharePoint ソリューション パッケージを含む .zip アーカイブです。

このアーカイブには以下が含まれます：

- Aspose.PDF.SharePoint.License.wsp

SharePoint ソリューション パッケージ ファイル。Aspose.PDF for SharePoint ライセンスは、サーバーファーム全体での展開/取り消しを容易にするために SharePoint ソリューションとしてパッケージ化されています。

- readme.txt

ライセンスインストール手順。ライセンスのインストールはサーバーコンソールから stsadm.exe を使用して実行されます。ライセンスをインストールするために必要な手順は以下に示します。

**注:** パスは明瞭さのため省略されています。実行時に stsadm.exe および/またはソリューションファイルへの実際のパスを追加する必要がある場合があります。

1. stsadm を実行してソリューションを SharePoint ソリューションストアに追加します:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. ソリューションをファーム内のすべてのサーバーにデプロイします:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 管理タイマージョブを実行して、デプロイをすぐに完了させます。

stsadm.exe -o execadmsvcjobs

**Note:** Windows SharePoint Services Administration サービスが開始されていない場合、デプロイ手順の実行時に警告が表示されます。Stsadm.exe はこのサービスおよび Windows SharePoint Timer Service に依存して、ファーム全体でソリューション データを複製します。これらのサービスがサーバーファームで実行されていない場合、各サーバーにライセンスをデプロイする必要があるかもしれません。

{{% /alert %}}
