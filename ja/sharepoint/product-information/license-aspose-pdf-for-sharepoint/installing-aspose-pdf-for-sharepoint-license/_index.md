---
title: Aspose.Pdf for SharePoint ライセンスのインストール
linktitle: Aspose.Pdf for SharePoint ライセンスのインストール
type: docs
weight: 10
url: /ja/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: 評価に満足したら、PDF SharePoint API のライセンスを購入し、インストール手順に従って適用できます。
---

{{% alert color="primary" %}}

評価に満足したら、あなたは [ライセンスを購入する](https://purchase.aspose.com/buy). 購入前に、ライセンスのサブスクリプション条件を理解し、同意していることを確認してください。

{{% /alert %}}

{{% alert color="primary" %}}

注文の支払いが完了した後、ライセンスはメールで送付されます。ライセンスは通常の SharePoint ソリューション パッケージを含む .zip アーカイブです。

このアーカイブには次が含まれます:

- Aspose.PDF.SharePoint.License.wsp

SharePoint ソリューション パッケージ ファイル。Aspose.PDF for SharePoint ライセンスは、サーバーファーム全体での展開/撤回を容易にするために SharePoint ソリューションとしてパッケージ化されています。

- readme.txt

ライセンスインストール手順。ライセンスのインストールはサーバーコンソールから stsadm.exe を使用して実行されます。ライセンスをインストールするために必要な手順は以下に示されています。

**Note:** パスは明確さのために省略されています。実行時に stsadm.exe および/またはソリューションファイルへの実際のパスを追加する必要がある場合があります。

1. SharePoint ソリューション ストアにソリューションを追加するために stsadm を実行します:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. ファーム内のすべてのサーバーにソリューションをデプロイします:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 管理タイマー ジョブを実行して、デプロイをすぐに完了させます。

stsadm.exe -o execadmsvcjobs

**Note:** Windows SharePoint Services Administration サービスが開始されていない状態でデプロイ手順を実行すると、警告が表示されます。Stsadm.exe はこのサービスと Windows SharePoint Timer Service に依存して、ファーム全体でソリューション データを複製します。これらのサービスがサーバー ファームで実行されていない場合、各サーバーにライセンスをデプロイする必要があるかもしれません。


{{% /alert %}}
