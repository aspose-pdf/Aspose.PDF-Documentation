---
title: Aspose.PDF for SharePoint ライセンスのアンインストール
linktitle: Aspose.PDF for SharePoint ライセンスのアンインストール
type: docs
weight: 30
url: /ja/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-08-10"
description: この記事に記載されている手順に従って、PDF SharePoint API ライセンスをアンインストールしてください。
---

## アンインストール手順

{{% alert color="primary" %}}

Aspose.PDF for SharePoint ライセンスをアンインストールするには、サーバーコンソールから以下の手順を使用してください。

1. ファームからライセンス ソリューションを取り消す：

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. リトラクションを直ちに完了させるために、管理タイマージョブを実行します:

  stsadm.exe -o execadmsvcjobs

3. リトラクションが完了するまで待ちます。Central を使用できます   

  Administration を使用して、Central Administration → Operations → Solution Management の下でリトラクションが完了したか確認できます

4. SharePoint ソリューションストアからソリューションを削除します:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
