---
title: Sitefinity PDF インポート
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/sitefinity-pdf-import/
description: Sitefinity 用の PDF インポートモジュールのインストールと使用方法を学ぶ
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Sitefinity PDF Import",
    "alternativeHeadline": "Effortless PDF Content Import for Sitefinity Users",
    "abstract": "Sitefinity PDF インポート機能を紹介します。これにより、開発者は PDF ドキュメントからコンテンツを簡単に抽出し、Sitefinity ウェブサイト内で直接表示できます。このオープンソースのアドオンは、シンプルなファイルブラウザと PDF からのインポートボタンを統合することで、追加のソフトウェアなしで文書操作のプロセスを簡素化し、コンテンツ管理を強化します。この強力なインポート機能でコンテンツの可能性を引き出しましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1145",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/sitefinity-pdf-import/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sitefinity-pdf-import/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF は、シンプルで簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## はじめに

### はじめに

#### Sitefinity とは？

Sitefinity は、ビジネスプロフェッショナル向けに直感的なウェブコンテンツ管理と堅牢な開発環境を提供する、最新の ASP.NET ベースのウェブコンテンツ管理システム (CMS) です。ここでは、この人気の CMS のために作成したプロジェクトを紹介します。

#### Aspose.PDF for .NET

Aspose.PDF for .NET は、.NET アプリケーションが Adobe Acrobat を使用せずに既存の PDF ドキュメントを読み書きし、操作できる PDF ドキュメント作成および操作コンポーネントです。また、PDF ドキュメントに埋め込まれたフォームを作成し、フォームフィールドを管理することもできます。

Aspose.PDF for .NET は手頃な価格で、PDF 圧縮オプション、テーブルの作成と操作、グラフオブジェクトのサポート、広範なハイパーリンク機能、拡張セキュリティ制御、カスタムフォント処理、データソースとの統合、ブックマークの追加または削除、目次の作成、添付ファイルや注釈の追加、更新、削除、PDF フォームデータのインポートまたはエクスポート、テキストや画像の追加、置換、削除、ページの分割、連結、抽出または挿入、ページを画像に変換、PDF ドキュメントの印刷など、驚くべき機能を提供します。

#### Aspose .NET PDF インポート for Sitefinity

Sitefinity PDF インポートは、開発者が他のソフトウェアを必要とせずに任意の PDF ドキュメントの内容を取得/読み取ることを可能にする、[Aspose](http://www.aspose.com/) のオープンソースアドオンです。このアドオンは、[Aspose.PDF](https://products.aspose.com/pdf/net/) によって提供される強力なインポート機能を示しています。アドオンが追加されたページにシンプルなファイルブラウザコントロールと **PDF からインポート** ボタンが追加されます。ボタンをクリックすると、ファイルから文書の内容が取得され、すぐに画面に表示されます。

### システム要件とサポートされているプラットフォーム

#### **システム要件**

Aspose.PDF .NET for Sitefinity アドオンをセットアップするには、以下の要件を満たす必要があります。

- ASP.NET 4.0 で動作する Sitefinity CMS。

Sitefinity アドオンのセットアップに問題がある場合は、お気軽にお問い合わせください。

#### サポートされているプラットフォーム

アドオンは、以下のすべてのバージョンでサポートされています。

- ASP.NET 4.0 で動作する Sitefinity CMS。

### サポート、拡張、貢献

#### サポート

Aspose の最初の日から、私たちは顧客に良い製品を提供するだけでは不十分であることを知っていました。良いサービスも提供する必要がありました。私たちは開発者であり、技術的な問題やソフトウェアの不具合があなたの作業を妨げるときのフラストレーションを理解しています。私たちは問題を解決するためにここにいます。

これが、私たちが無料サポートを提供する理由です。私たちの製品を使用するすべての人、購入したか評価版を使用しているかにかかわらず、私たちの完全な注意と尊重に値します。

Aspose.PDF .NET for Sitefinity モジュールに関連する問題や提案は、以下のプラットフォームのいずれかを使用してログできます。

- [Github](https://github.com/asposemarketplace/Aspose_for_Sitefinity/issues).
- [Sourceforge](https://sourceforge.net/p/asposesitefinity/tickets/?source=navbar).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-sitefinity/issues?status=new&status=open).

#### 拡張と貢献

Aspose .NET PDF インポート for Sitefinity はオープンソースであり、そのソースコードは以下の主要なソーシャルコーディングサイトで入手できます。開発者は、ソースコードをダウンロードし、自分の要件に応じて機能を拡張することを奨励されています。

#### ソースコード

最新のソースコードは、以下のいずれかの場所から取得できます。

- [Github](https://github.com/asposemarketplace/Aspose_for_Sitefinity).
- [Sourceforge](https://sourceforge.net/p/asposesitefinity/code/ci/master/tree/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-sitefinity/src).

#### ソースコードの構成方法

ソースコードを開いて拡張するには、以下のものをインストールする必要があります。

- Visual Studio 2010 以降。

以下の簡単な手順に従って、始めてください。

1. ソースコードをダウンロード/クローンします。
1. Visual Studio 2010 を開き、`ファイル > プロジェクトを開く`を選択します。
1. ダウンロードした最新のソースコードを参照し、**Aspose.SiteFinity.PDFImport.sln** を開きます。

## インストールと使用

### ダウンロードとインストール

#### ダウンロード

以下のいずれかの場所から Sitefinity 用の Aspose .NET Pdf インポートをダウンロードできます。

- [Github](https://github.com/asposemarketplace/Aspose_for_Sitefinity/releases).
- [Sourceforge](https://sourceforge.net/projects/asposesitefinity/files/).
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-sitefinity/downloads).

#### インストール

ダウンロードが完了したら、以下の手順に従ってアドオンを Sitefinity ウェブサイトにインストールしてください。

##### ステップ 1: ファイルを Sitefinity インストールにコピーする

ダウンロードした ZIP ファイルを解凍してください。次の操作を行うには、FTP またはサーバー上の Sitefinity インストールフォルダーへの直接アクセスが必要です。

1. Aspose.PDF.dll と Aspose.SiteFinity.PDFImport.dll を Sitefinity インストールの **bin** フォルダーにコピーします。
1. **bin** フォルダーがある Sitefinity インストールのルートに **Addons** フォルダーをコピーします。

##### ステップ 2: Sitefinity に Aspose .NET PDF インポート for Sitefinity アドオンを登録する

1. **管理者** アカウントで Sitefinity CMS にログインします。ログインページには <http://www.mywebsite.com/sitefinity> からアクセスできます。
1. **管理** をクリックし、次に **設定** をクリックします。
   基本設定ページが表示されます。
1. **詳細リンクをクリックします。**。
   設定ページが表示されます。
1. 左側のペインで **ツールボックス** をクリックし、次に **ツールボックス**、**ページコントロール**、**セクション**、**コンテンツツールボックスセクション**、次に **ツール** をクリックします。
1. **新規作成** をクリックします。
   ウィジェット登録フォームが表示されます。
1. フォームフィールドに以下のように入力します：
   1. **有効** が選択されていることを確認します。
   1. **Control CLR Type or Virtual Path** フィールドに ~/Addons/AsposePDFImport/AsposePDFImport.ascx を追加します。
   1. **名前**、**タイトル**、**説明** を以下のように追加します：
      AsposePDFImport
      Aspose PDF インポート
      Aspose .NET PDF インポートを使用して Sitefinity に PDF ドキュメントをインポート
   1. 他のすべてのフィールドはそのままにしておいて構いません。
1. 完了したら、**変更を保存** をクリックします。
   ウィジェットがツールボックスに登録され、Sitefinity で使用できるようになります。設定は以下の画像にも表示されます。

### 使用とビデオデモ

#### 使用

Aspose .NET PDF インポート for Sitefinity アドオンをインストールして構成した後、ウェブサイトでの使用は非常に簡単です。以下の簡単な手順に従って始めてください：

1. 管理者レベルのアカウントで Sitefinity にログインしていることを確認します。
1. Sitefinity PDF インポートアドオンを追加したいページに移動します。ページが編集モードで開いていることを確認してください。
1. 右側の **ウィジェットをドラッグ** メニューから **Aspose PDF インポート** を選択し、位置にドラッグします。

Aspose .NET PDF インポート for Sitefinity アドオンをページに正常に追加しました。ファイルブラウズと **PDF からインポート** というタイトルのボタンがページに表示されます。誰でも任意の PDF ドキュメントを選択し、PDF からインポートボタンをクリックして、選択したドキュメントの内容をページに表示できます。

#### ビデオデモ

以下の [ビデオ](https://www.youtube.com/watch?v=kKk2p--lXFI) をチェックして、モジュールの動作を確認してください。