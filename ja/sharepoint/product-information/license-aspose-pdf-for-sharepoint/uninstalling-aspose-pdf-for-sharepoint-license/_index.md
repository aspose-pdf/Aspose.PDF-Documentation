---
title: Aspose.PDF for SharePoint ライセンスのアンインストール
linktitle: Aspose.PDF for SharePoint ライセンスのアンインストール
type: docs
weight: 30
url: /ja/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: PDF SharePoint API ライセンスをアンインストールするには、この記事に記載されている手順に従ってください。
---

## アンインストール手順

{{% alert color="primary" %}}

Aspose.PDF for SharePoint ライセンスをアンインストールするには、サーバー コンソールから次の手順を実行してください。

1. ファームからライセンス ソリューションを撤回します。

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. 管理タイマー ジョブを実行して、撤回をただちに完了します。

  stsadm.exe -o execadmsvcjobs

3. 撤回が完了するまで待ちます。セントラルを使用できます   

  管理者は、[サーバーの全体管理] -> [操作] -> [ソリューション管理] で撤回が完了したかどうかを確認します。

4. SharePoint ソリューション ストアからソリューションを削除します。

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}

