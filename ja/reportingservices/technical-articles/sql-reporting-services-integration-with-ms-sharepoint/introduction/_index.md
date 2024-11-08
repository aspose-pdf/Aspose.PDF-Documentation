---
title: Introduction
type: docs
weight: 10
url: /ja/reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Servicesは、SQL Reporting Servicesを通じたPDF生成において非常に優れたものであり、多年にわたりデフォルトではSQL Reporting Servicesでサポートされていない多様な設定およびパラメータ化オプションを提供しています。最近、SharePointとの統合に関するいくつかの要求を受けました。この記事では、MS SharePoint 2010に焦点を当てます。先に進む前に、すでにSharePointファームが設定されていることを前提とします。この例では、完全なSharePointクラウドを使用します。ただし、手順はSharePoint Foundation Serverの場合と似ています。

{{% /alert %}}

{{% alert color="primary" %}}

先に進む前に、この記事の準備中に参考にしたトピックを見てみましょう。

- [Reporting ServicesとSharePointテクノロジー統合の概要](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [Deployment Topologies for Reporting Services in SharePoint Integrated Mode](http://msdn.microsoft.com/en-us/library/bb510781.aspx)  
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)  

{{% /alert %}}  

## 環境セットアップ  

セットアップは4台のサーバーで構成されています。ドメインコントローラー、SQLサーバー、SharePointサーバー、Reporting Services用のサーバーが含まれています。SharePointとReporting Servicesを同じマシンに置くこともでき、その場合は少し簡略化されますが、いくつかの違いを指摘します。  

## インストール前提条件  

{{% alert color="primary" %}}  

SharePoint用のReporting Servicesアドインは、統合を適切に機能させるための主要なコンポーネントの1つです。 The Add-In needs to be installed on any of the Web Front Ends (WFE) that is in your SharePoint farm along with the Central Admin server. One of the new changes with SQL 2008 R2 & SharePoint 2010 is that the 2008 R2 Add-In is now a pre-requisite for the SharePoint Install. This means that the RS Add-In will be laid down when you go to install SharePoint. It has been shown and highlighted in figure below. This actually avoids a lot of issues we saw with SP 2007 and RS 2008 when installing the Add-In.

SharePointファームにある任意のWebフロントエンド（WFE）と中央管理サーバーにアドインをインストールする必要があります。SQL 2008 R2とSharePoint 2010の新しい変更点の1つは、2008 R2アドインがSharePointインストールの前提条件になったことです。これは、SharePointをインストールする際にRSアドインが配置されることを意味します。このことは、以下の図で示され、ハイライトされています。これは実際に、SP 2007とRS 2008でアドインをインストールする際に見られた多くの問題を回避します。

![todo:image_alt_text](introduction_1.png)

**Image1 :- Reporting Services Add-in for Share Point**
{{% /alert %}}

## SharePoint Authentication

**Before we jump into the RS Integration pieces, one thing I want to point out about the SharePoint Farm is how you setup the Site.

## SharePoint認証

**RS統合部分に進む前に、SharePointファームについて1つ指摘したいのは、サイトのセットアップ方法です。 もっと具体的に言うと、サイトの認証をどのように設定するかです。それがクラシックかクレームか。この選択は最初に重要です。一度設定すると、このオプションを変更できるとは思えません。もし変更できるとしても、簡単なプロセスではないでしょう。

注意: ***Reporting Services 2008 R2 はクレーム対応ではありません***

たとえSharePointサイトでクレームを使用するように選択しても、Reporting Services自体はクレーム対応ではありません。とはいえ、それはReporting Servicesでの認証の動作に影響します。では、Reporting Servicesの観点から何が違うのでしょうか？それは、データソースにユーザーの資格情報を転送したいかどうかにかかっています。 クラシック:- Kerberosを使用して、ユーザーの資格情報をバックエンドのデータソースに転送できます（そのためにはKerberosを使用する必要があります）。 クレーム:- クレームトークンが使用され、Windowsトークンは使用されません。このシナリオではRSは常に信頼された認証を使用し、SPUserトークンへのアクセスのみが可能です。データソース内に資格情報を保存する必要があります。

クラシック:- Kerberosを使用して、ユーザーの資格情報をバックエンドのデータソースに転送できます（そのためにはKerberosを使用する必要があります）。
Claims :- クレームトークンが使用され、Windowsトークンは使用されません。このシナリオではRSは常に信頼できる認証を使用し、SPUserトークンのみアクセスできます。データソース内に資格情報を保存する必要があります。

現時点では、RSのセットアップに集中したいと思います。この時点で、SharePointは私のSharePointボックスにインストールされ、ポート80のクラシック認証サイトでセットアップされています。RSサーバーにはReporting Servicesをインストールしただけです。