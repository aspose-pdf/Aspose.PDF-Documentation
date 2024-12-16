---
title: Aspose.Pdf for SharePointのインストール
type: docs
weight: 20
url: /ja/sharepoint/installing-aspose-pdf-for-sharepoint/
lastmod: "2020-12-16"
description: PDF SharePoint APIは、サーバーファームの展開、削除、アクティベーション、非アクティベーションを簡素化するためにSharePointソリューションとしてパッケージ化されています。
---

{{% alert color="primary" %}}

Aspose.PDF for SharePointは、Aspose.PDF.SharePoint.zipアーカイブとしてダウンロード可能です。

{{% /alert %}}

**このアーカイブには以下が含まれています:**

- Aspose.PDF.SharePoint.wsp
  SharePointソリューションファイル。Aspose.PDF for SharePointは、サーバーファーム全体での展開/削除と機能のアクティベーション/非アクティベーションを容易にするためにSharePointソリューションとしてパッケージ化されています。
- Aspose_LicenseAgreement.rtf

**エンドユーザーライセンス契約書:**

- Aspose.PDF for SharePoint.pdf

**ユーザー文書:**

- Aspose.PDF for SharePoint Documentation.chm

**公開APIリファレンス付きユーザー文書:**

- setup.exe

**セットアッププログラム:**

- setup.exe.config

**セットアップ構成ファイル:**

セットアッププログラムは、以下の条件を確認してから進みます:

- SharePoint 2010 がインストールされています。
- ユーザーには SharePoint ソリューションをインストールする権限があります。
- SharePoint データベースがオンラインです。
- SharePoint 管理サービスが開始されています。
- SharePoint タイマーサービスが開始されています。サーバーファーム内のすべてのサーバーに伝播するために、いくつかのセットアップアクションはタイマージョブに依存しているため、SharePoint 管理サービスおよびタイマーサービスが必要です。

**Aspose.PDF for SharePoint をインストールするには:**

- Aspose.PDF.SharePoint の zip をローカルドライブに解凍します。
- setup.exe を実行し、画面の指示に従います。

**セットアッププログラムは次のアクションを実行します:**

- インストールの前提条件を確認します。チェックに失敗した場合、セットアップは続行されません。

![todo:image_alt_text](installing-aspose-pdf-for-sharepoint_1.png)



- エンドユーザー使用許諾契約書を表示します。ユーザーは進行するために契約に同意する必要があります。

![todo:image_alt_text](installing-aspose-pdf-for-sharepoint_2.png)



- デプロイメントターゲット選択ダイアログを表示します。
 The user selects web applications and site collections where the feature shall be activated. See the figure below.

![todo:image_alt_text](installing-aspose-pdf-for-sharepoint_3.png)

- ユーザーは、機能を有効化するWebアプリケーションとサイトコレクションを選択します。下の図を参照してください。

- Deploy the feature to the server farm.

![todo:image_alt_text](installing-aspose-pdf-for-sharepoint_4.png)

- 機能をサーバーファームに展開します。

- Activate the feature for the selected site collections and configure their parent web applications.
- Display a list of web applications and site collections where the feature has been deployed and activated.

![todo:image_alt_text](installing-aspose-pdf-for-sharepoint_5.png)

- 選択したサイトコレクションの機能を有効化し、それらの親Webアプリケーションを設定します。
- 機能が展開され、有効化されたWebアプリケーションとサイトコレクションのリストを表示します。