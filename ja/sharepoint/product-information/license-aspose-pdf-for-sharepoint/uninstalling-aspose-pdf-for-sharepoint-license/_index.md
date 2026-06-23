---
title: Aspose.Pdf for SharePoint ライセンスのアンインストール
linktitle: Aspose.Pdf for SharePoint ライセンスのアンインストール
type: docs
weight: 30
url: /ja/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: PDF SharePoint API ライセンスをアンインストールするには、この記事に記載されている手順に従ってください。
---

## アンインストール手順

{{% alert color="primary" %}}

Aspose.PDF for SharePoint ライセンスをアンインストールするには、サーバーコンソールから以下の手順をご利用ください。

1. ファームからライセンス ソリューションを取り下げます:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. 管理タイマージョブを実行して、リトラクションを直ちに完了させます:

  stsadm.exe -o execadmsvcjobs

3. リトラクションが完了するのを待ちます。Central を使用できます   

  Administration を使用して、Central Administration の下でリトラクションが完了したかどうかを確認します -> Operations -> Solution Management

4. SharePoint ソリューションストアからソリューションを削除します:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
