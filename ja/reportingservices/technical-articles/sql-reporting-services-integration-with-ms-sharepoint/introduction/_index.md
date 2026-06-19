---
title: イントロダクション
linktitle: イントロダクション
type: docs
weight: 10
url: /ja/reportingservices/introduction/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services は、長年にわたり SQL Reporting Services を通じた PDF 生成で非常に優れた製品であり、SQL Reporting Services の標準ではサポートされていない多様な構成およびパラメータ化オプションを提供します。最近、Aspose.PDF for Reporting Services と SharePoint の統合に関する要望を受け取りました。本稿では MS SharePoint 2010 に焦点を当てます。さらに進む前に、既に SharePoint Farm が設定されていることを前提とします。この例ではフル SharePoint Cloud を使用します。ただし、手順は SharePoint Foundation Server でも同様です。

{{% /alert %}}

{{% alert color="primary" %}}

さらに進む前に、この記事の作成にあたって参照したトピックを確認してみましょう。

- [Reporting Services と SharePoint テクノロジー統合の概要](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [SharePoint 統合モードにおける Reporting Services の展開トポロジー](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [SharePoint 2010 統合用 Reporting Services の構成](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## 環境設定

当社のセットアップは 4 台のサーバーで構成されています。ドメインコントローラ、SQL Server、SharePoint Server、そして Reporting Services 用サーバーが含まれます。SharePoint と Reporting Services を同一サーバーにすることも選択でき、その場合は設定が少し簡素化されますので、いくつかの違いを指摘します。

## インストール前提条件

{{% alert color="primary" %}}

Reporting Services Add-In for SharePoint は、統合を適切に機能させるための重要なコンポーネントの一つです。Add-In は、SharePoint ファーム内の任意の Web Front End (WFE) と Central Admin サーバーの両方にインストールする必要があります。SQL 2008 R2 \u0026 SharePoint 2010 の新しい変更点の一つは、2008 R2 Add-In が SharePoint インストールの前提条件となったことです。これは、SharePoint をインストールする際に RS Add-In が自動的に配置されることを意味します。以下の図に示され、ハイライトされています。これにより、Add-In をインストールする際に経験した SP 2007 と RS 2008 の多くの問題が実際に回避されます。

![todo:image_alt_text](introduction_1.png)

**Image1 :- Share Point 用 Reporting Services アドイン**
{{% /alert %}}

## SharePoint 認証

**RS 統合のパーツに入る前に、SharePoint ファームについて指摘したいことがあります。それはサイトの設定方法です。特に、サイトの認証を Classic にするか Claims にするかです。この選択は最初に重要です。一度設定すると変更できないと考えています。もし変更できたとしても、簡単なプロセスではありません。**

NOTE: ***Reporting Services 2008 R2 は Claims 非対応です***

SharePoint サイトで Claims を使用するように選択した場合でも、Reporting Services 自体は Claims を認識しません。とはいえ、これは Reporting Services の認証方法に影響します。では、Reporting Services の観点からの違いは何でしょうか？ それはユーザー資格情報をデータ ソースに転送するかどうかに依存します。 Classic:- Kerberos を使用でき、ユーザーの資格情報をバックエンド データ ソースに転送できます（そのためには Kerberos が必要です）。 Claims:- Claims トークンが使用され、Windows トークンではありません。このシナリオでは RS は常に Trusted Authentication を使用し、SPUser トークンのみにアクセスできます。データ ソース内に資格情報を保存する必要があります。

Classic :- Kerberos を使用でき、ユーザーの資格情報をバックエンド データ ソースに転送できます（そのためには Kerberos が必要です）。

Claims :- Claims トークンが使用され、Windows トークンではありません。このシナリオでは RS は常に Trusted Authentication を使用し、SPUser トークンのみにアクセスできます。データ ソース内に資格情報を保存する必要があります。

まずは RS のセットアップに集中したいだけです。現時点では SharePoint が私の SharePoint Box にインストールされ、ポート 80 の Classic Auth サイトとして設定されています。RS サーバーでは Reporting Services をインストールしただけで、他には何もありません。

