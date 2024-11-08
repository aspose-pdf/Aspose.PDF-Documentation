---
title: Reporting Services and SharePoint configuration
type: docs
weight: 40
url: /ja/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

SharePoint が RS サーバーにインストールされ構成され、Reporting Services Configuration Manager を通じて RS がセットアップおよび設定されたので、Central Admin 内での構成に進むことができます。RS 2008 R2 はこのプロセスを本当に簡素化しました。これが機能するために実行しなければならなかった 3 ステップのプロセスがありましたが、今では 1 ステップだけになりました。

{{% /alert %}}

{{% alert color="primary" %}}

Central Administrator Web サイトに移動し、General Application Settings に入ります。下の方に Reporting Services が表示されます。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- SharePoint 構成ダイアログ

"Reporting Services Integration" リンクを選択します。次の画面が表示されます。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- レポート サービスの統合資格情報を指定する

{{% /alert %}}

## Web Service URL:

**レポート サーバーの URL は、レポート サービス構成マネージャーで見つけたものを提供します。**

## Authentication Mode:

**また、認証モードを選択します。次の MSDN リンクは、これらが何であるかを詳細に説明しています。
SharePoint 統合モードでのレポート サービスのセキュリティ概要**

{{% alert color="primary" %}}

**簡単に言えば、サイトがクレーム認証を使用している場合、ここで何を選択しても常に信頼された認証を使用することになります。Windows 資格情報を渡したい場合は、Windows 認証を選択します。信頼された認証の場合、SPUser トークンを渡し、Windows 資格情報には依存しません。クラシック モードのサイトを NTLM 用に構成し、RS が NTLM 用に設定されている場合は、信頼された認証も使用する必要があります。Windows 認証を使用してデータ ソースにそれを渡すには、Kerberos が必要です。**

{{% /alert %}}

## 機能を有効化する:

{{% alert color="primary" %}}

**これにより、すべてのサイトコレクションでレポートサービスを有効化するオプションが提供されます。または、どのサイトで有効化するかを選択することもできます。これは、どのサイトがレポートサービスを使用できるかを意味します。完了すると、次の結果が表示されるはずです**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**画像3:**- SharePoint環境とのレポートサービスの統合が成功しました
{{% /alert %}}

{{% alert color="primary" %}}

ReportServer URL に戻ると、以下のようなものが表示されるはずです

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**画像4:**- レポートサービスがSharePoint環境と正常に接続されました

**注意:** ***SharePointサイトがSSL用に構成されている場合、このリストには表示されません。これは既知の問題であり、問題があることを意味するわけではありません。レポートは引き続き動作するはずです。***
{{% /alert %}}

これで両製品の統合が成功したので、SharePoint 2010でReporting Servicesを使用する準備が整いました。前のバージョンと同様に、「サイトコレクション機能」でReporting Services統合を設定すると機能が有効になります。また、インストールにより、サイトに追加するための3つのコンテンツタイプが追加されました。イメージ7では、カスタムレポートを作成するためにドキュメントライブラリに追加された2つのコンテンツタイプを見ることができます。以下のイメージ5で確認できます。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**イメージ5:**- レポートビルダー
{{% alert color="primary" %}}

「レポートビルダー」はActiveXコントロールなので、サーバー経由でダウンロードする必要があります。以下のイメージ6で確認できます。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**イメージ6:**- レポートビルダーのダウンロードとインストール
{{% /alert %}}

{{% alert color="primary" %}}

ダウンロードプロセスが完了したら、「レポートビルダー」コントロールをロードします。これで、以下のイメージ7に示すように、最初のレポートを設計する準備が整いました。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- レポートビルダー – 新しいレポート生成ウィザード
{{% /alert %}}

{{% alert color="primary" %}}

レポートを作成した後、SharePoint 2010 にレポートを配置するために作成されたドキュメントライブラリに保存することができます。もう一つのコンテンツタイプは、共有接続をデータソースとして作成し、それを SharePoint のドキュメントライブラリに保存するために使用されます。ドキュメントライブラリを作成し、このコンテンツタイプを追加することで、レポートのデータソースを変更するための接続を利用可能にすることができます。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Aspose.PDF for Reporting Services と MS SharePoint の統合成功
{{% /alert %}}