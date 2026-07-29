---
title: Introduction
linktitle: Introduction
type: docs
weight: 10
url: /ja/reportingservices/introduction/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services は、長年にわたり SQL Reporting Services を介した PDF 生成で非常に優れた実績があり、SQL Reporting Services ではデフォルトでサポートされていない多様な構成およびパラメータ化オプションを提供します。最近、Aspose.PDF for Reporting Services の SharePoint との統合に関するリクエストを受けました。本記事では MS SharePoint 2010 に焦点を当てます。先に進む前提として、すでに SharePoint Farm がセットアップされているものとします。この例ではフル SharePoint Cloud を使用しますが、手順は SharePoint Foundation Server でも同様です。

{{% /alert %}}

{{% alert color="primary" %}}

先に進む前に、この記事の作成中に参照した参考トピックを見てみましょう。

- [Reporting Services と SharePoint テクノロジー統合の概要](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [SharePoint 統合モードにおける Reporting Services の展開トポロジー](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [SharePoint 2010 統合のための Reporting Services の構成](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## 環境設定

当社のセットアップは 4 台のサーバーで構成されています。ドメイン コントローラー、SQL Server、SharePoint Server、そして Reporting Services 用のサーバーが含まれます。SharePoint と Reporting Services を同じサーバー上に配置することも可能で、これによりやや簡素化できます。その際の違いについていくつか指摘します。

## インストール前提条件

{{% alert color="primary" %}}

Reporting Services Add-In for SharePoint は、統合を適切に機能させるための重要なコンポーネントの一つです。Add‑In は、SharePoint ファーム内の任意の Web Front End (WFE) と Central Admin サーバーの両方にインストールする必要があります。SQL 2008 R2 & SharePoint 2010 の新たな変更点のひとつは、2008 R2 Add‑In が SharePoint インストールの前提条件となったことです。これにより、SharePoint をインストールする際に RS Add‑In が自動的に配置されます。以下の図に示しハイライトされています。この方式により、Add‑In のインストール時に SP 2007 と RS 2008 で見られた多くの問題が実際に回避されます。

![todo:image_alt_text](introduction_1.png)

**Image1 :- Share Point 用 Reporting Services アドイン**
{{% /alert %}}

## SharePoint 認証

**RS 統合のパーツに入る前に、SharePoint ファームについて指摘したいことがあります。それはサイトの設定方法です。特にサイトの認証方法の構成です。Classic か Claims のどちらかです。この選択は最初に重要です。一度設定するとこのオプションを変更できるとは思っていません。もし変更できたとしても、簡単なプロセスではありません。**

NOTE: ***Reporting Services 2008 R2 は Claims に対応していません***

たとえ SharePoint サイトで Claims を使用するように設定しても、Reporting Services 自体は Claims を認識していません。ただし、これにより Reporting Services の認証動作に影響があります。では、Reporting Services の観点からどのような違いがあるのでしょうか？ポイントは、ユーザー資格情報をデータ ソースに転送するかどうかです。Classic:- Kerberos を使用でき、ユーザーの資格情報をバックエンド データ ソースに転送できます（そのためには Kerberos が必要です）。Claims:- Claims トークンが使用され、Windows トークンではありません。RS は常に Trusted Authentication を使用し、このシナリオでは SPUser トークンへのアクセスしか持ちません。データ ソース内に資格情報を保存する必要があります。

Classic :- Kerberos を使用でき、ユーザーの資格情報をバックエンド データ ソースに転送できます（そのためには Kerberos が必要です）。

Claims :- Claims トークンが使用され、Windows トークンではありません。RS は常に Trusted Authentication を使用し、このシナリオでは SPUser トークンへのアクセスしか持ちません。データ ソース内に資格情報を保存する必要があります。

今のところ、私たちはRSのセットアップに集中したいだけです。現時点でSharePointは私のSharePoint Boxにインストールされ、ポート80のClassic Authサイトとして設定されています。RSサーバーではReporting Servicesをインストールしただけです。
