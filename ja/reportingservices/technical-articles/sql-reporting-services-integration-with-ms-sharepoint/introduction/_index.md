---
title: 導入
linktitle: 導入
type: docs
weight: 10
url: /reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services は、SQL Reporting Services を介した PDF 生成において長年にわたって非常に注目されており、SQL Reporting Services ではデフォルトではサポートされていない多様な構成およびパラメーター化オプションを提供します。最近、Reporting Services を SharePoint と統合するための Aspose.PDF に関するリクエストをいくつか受け取りました。この記事では、MS SharePoint 2010 に焦点を当てます。先に進む前に、SharePoint ファームがすでにセットアップされていることを前提としています。この例では、完全な SharePoint Cloud を使用します。ただし、SharePoint Foundation Server の場合でも手順は似ています。

{{% /alert %}}

{{% alert color="primary" %}}

先に進む前に、この記事の準備中に参考にした参考トピックを見てみましょう。

- [Reporting Services と SharePoint テクノロジの統合の概要](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [SharePoint 統合モードでの Reporting Services の展開トポロジ](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [SharePoint 2010 統合用の Reporting Services の構成](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## 環境設定

セットアップは 4 つのサーバーで構成されます。これには、ドメイン コントローラー、SQL サーバー、SharePoint サーバー、および Reporting Services 用のサーバーが含まれます。 SharePoint と Reporting Services を同じボックスに入れることを選択することもできます。これにより、これが少し簡素化され、いくつかの違いを指摘します。

## インストールの前提条件

{{% alert color="primary" %}}

SharePoint 用 Reporting Services アドインは、統合を適切に機能させるための重要なコンポーネントの 1 つです。アドインは、中央管理サーバーとともに SharePoint ファーム内のいずれかの Web フロント エンド (WFE) にインストールする必要があります。 SQL 2008 R2 および SharePoint 2010 の新しい変更点の 1 つは、2008 R2 アドインが SharePoint インストールの前提条件になったことです。これは、SharePoint をインストールするときに RS アドインが配置されることを意味します。それは以下の図に示され、強調表示されています。これにより、アドインのインストール時に SP 2007 および RS 2008 で発生した多くの問題が実際に回避されます。

![Introduction](introduction_1.png)

**画像 1 :- Share Point 用 Reporting Services アドイン**
{{% /alert %}}

## SharePoint認証

**RS 統合の説明に入る前に、SharePoint ファームについて指摘しておきたいのは、サイトのセットアップ方法です。より具体的には、サイトの認証を構成する方法です。クラシックかクレームか。この選択は最初は重要です。このオプションは一度完了すると変更できないと思います。変更できるとしても、それは簡単なプロセスではありません。

注: ***Reporting Services 2008 R2 はクレームに対応していません***

SharePoint サイトで Claims を使用することを選択した場合でも、Reporting Services 自体は Claims を認識しません。ただし、Reporting Services での認証の動作には影響します。では、Reporting Services の観点から見た違いは何でしょうか?結局のところ、ユーザー資格情報をデータ ソースに転送するかどうかが決まります。クラシック:- Kerberos を使用し、ユーザーの資格情報をバックエンド データソースに転送できます (そのためには Kerberos を使用する必要があります)。クレーム:- Windows トークンではなく、クレーム トークンが使用されます。 RS は、このシナリオでは常に信頼された認証を使用し、SPUser トークンにのみアクセスできます。資格情報をデータ ソース内に保存する必要があります。

クラシック:- Kerberos を使用し、ユーザーの資格情報をバックエンド データソースに転送できます (そのためには Kerberos を使用する必要があります)。

Claims :- Windows トークンではなく、Claims トークンが使用されます。このシナリオでは、RS は常に信頼された認証を使用し、SPUser トークンにのみアクセスできます。資格情報をデータ ソース内に保存する必要があります。

今のところ、RS のセットアップに焦点を当てたいと思います。この時点で、SharePoint は SharePoint ボックスにインストールされ、ポート 80 でクラシック認証サイトがセットアップされています。RS サーバーには、Reporting Services をインストールしただけです。それだけです。
