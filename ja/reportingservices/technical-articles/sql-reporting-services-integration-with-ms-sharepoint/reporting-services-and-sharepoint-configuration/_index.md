---
title: Reporting Services と SharePoint の構成
linktitle: Reporting Services と SharePoint の構成
type: docs
weight: 40
url: /ja/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

SharePoint が RS サーバーにインストールされ構成され、Reporting Services Configuration Manager を通じて RS の設定が完了したので、Central Admin 内の構成に進むことができます。RS 2008 R2 はこのプロセスを本当に簡素化しました。以前はこれを実行するために 3 段階の手順が必要でしたが、現在は 1 つの手順だけです。

{{% /alert %}}

{{% alert color="primary" %}}

Central Administrator Web サイトにアクセスし、次に General Application Settings に進みます。下部に Reporting Services が表示されます。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- SharePoint 構成ダイアログ

「Reporting Services Integration」リンクを選択します。次の画面が表示されます。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- Reporting Services の統合クレデンシャルを指定します

{{% /alert %}}

## Web サービス URL:

**Reporting Services Configuration Manager で見つけたレポートサーバーの URL を提供します。**

## 認証モード:

**認証モードも選択します。以下のMSDNリンクでは、これらが何であるか詳細に説明されています。
SharePoint 統合モードにおける Reporting Services のセキュリティ概要**

{{% alert color="primary" %}}

**要するに、サイトがクレーム認証を使用している場合、ここで何を選択しても常に信頼された認証が使用されます。Windows の資格情報を渡したい場合は、Windows 認証を選択してください。信頼された認証では、Windows の資格情報に依存せず SPUser トークンを渡します。Classic モードのサイトを NTLM 用に構成し、RS が NTLM 用に設定されている場合も、信頼された認証を使用することをお勧めします。Windows 認証とデータ ソースへの転送には Kerberos が必要になります。**

{{% /alert %}}

## 機能を有効化:

{{% alert color="primary" %}}

**これにより、すべてのサイト コレクションで Reporting Services を有効化するオプションが提供されるか、または有効化したいものだけを選択できます。これは実際には、どのサイトが Reporting Services を使用できるかを意味します。完了すると、以下の結果が表示されます**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3:**- Reporting Services と SharePoint 環境の統合に成功しました
{{% /alert %}}

{{% alert color="primary" %}}

ReportServer の URL に戻ると、次のようなものが表示されるはずです

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4:**- Reporting Services が SharePoint 環境に正常に接続されました

**NOTE:** ***SharePoint サイトが SSL 用に構成されている場合、このリストに表示されません。これは既知の問題であり、問題があることを意味するわけではありません。レポートは引き続き機能するはずです。***
{{% /alert %}}

{{% alert color="primary" %}}

両方の製品を正常に統合したので、Reporting Services を SharePoint 2010 で使用できるようになりました。前のバージョンと同様に、Reporting Services Integration を構成した際に有効になる “Site Collection Feature” があります。また、インストール時にサイトに追加する 3 つのコンテンツタイプが追加されました。Image 7 では、ドキュメント ライブラリに追加された 2 つのコンテンツタイプがカスタム レポートを作成するために使用されているのが確認できます（下の Image5 を参照）。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- Report Builder

“Reporter Builder” は ActiveX コントロールなので、サーバー経由でダウンロードする必要があります。下の Image 6 を参照してください。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- Report Builder のダウンロードとインストール
{{% /alert %}}

{{% alert color="primary" %}}

ダウンロードプロセスが完了したら、“Report Builder” コントロールをロードします。これで、以下の Image7 に示すように、最初のレポートを設計する準備が整いました。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – 新規レポート生成ウィザード
{{% /alert %}}

{{% alert color="primary" %}}

レポートを作成した後、SharePoint 2010 のレポートを配置するために作成したドキュメント ライブラリに保存できます。他のコンテンツ タイプは、データ ソースとして共有接続を作成し、SharePoint のドキュメント ライブラリに保存するために使用する必要があります。ドキュメント ライブラリを作成し、このコンテンツ タイプを追加すれば、レポートのデータ ソースを変更できるように接続を利用できるようになります。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Aspose.PDF for Reporting Services と MS SharePoint の統合が成功
{{% /alert %}}


