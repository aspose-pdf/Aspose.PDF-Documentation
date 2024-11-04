---
title: Aspose.Pdf for SharePoint ライセンスのアンインストール
type: docs
weight: 30
url: /sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: PDF SharePoint API ライセンスをアンインストールするための手順については、この記事の手順に従ってください。
---

## アンインストール手順

{{% alert color="primary" %}}

Aspose.PDF for SharePoint ライセンスをアンインストールするには、サーバーコンソールから以下の手順を使用してください。

1. ファームからライセンスソリューションをリトラクトします:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. 管理タイマージョブを実行してリトラクトを即座に完了させます:

  stsadm.exe -o execadmsvcjobs

3. リトラクトが完了するまで待ちます。Central Administration を使用して、Central Administration -> Operations -> Solution Management でリトラクトが完了したかどうかを確認できます。

4. SharePoint ソリューションストアからソリューションを削除します:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}