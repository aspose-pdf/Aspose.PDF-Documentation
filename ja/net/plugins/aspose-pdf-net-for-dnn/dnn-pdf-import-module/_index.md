---
title: DNN PDFインポートモジュール
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/dnn-pdf-import-module/
description: DotNetNuke用のPDFインポートモジュールのインストールと使用方法を学ぶ
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "DNN PDF Import Module",
    "alternativeHeadline": "Effortless PDF Content Import for DotNetNuke",
    "abstract": "DNN PDFインポートモジュールは、Aspose.PDF for .NET技術を活用して、PDFドキュメントからのコンテンツをDotNetNuke内でシームレスに抽出および表示し、Adobe Acrobatのような追加のソフトウェアを必要としません。この革新的なモジュールは、直感的なインターフェースを使用してドキュメントインポートプロセスを簡素化し、ユーザーがファイルを簡単にブラウズし、PDFコンテンツをウェブページにインポートできるようにします。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "878",
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
    "url": "/net/dnn-pdf-import-module/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/dnn-pdf-import-module/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## はじめに

Aspose .NET PDFインポートモジュールは、開発者がAdobe AcrobatやPDFリーダーなどの他のソフトウェアを必要とせずにPDFドキュメントの内容を取得/読み取ることを可能にします。

### モジュールの特徴

このモジュールは、[Aspose.PDF](https://products.aspose.com/pdf/net/)が提供する強力なインポート機能を示しています。モジュールが追加されたページには、シンプルなファイルブラウザコントロール、コンテンツペインの選択、および**PDFからインポート**ボタンが追加されます。ボタンをクリックすると、ドキュメントの内容がすぐに画面に表示されます。

## システム要件とサポートされているプラットフォーム

### システム要件

Aspose .NET PDFインポートモジュールをセットアップするには、以下の要件を満たす必要があります。

- DNN 7.0以上。

他のバージョンのDNNにこのモジュールをインストールしたい場合は、お気軽にお問い合わせください。

### サポートされているプラットフォーム

Aspose .NET PDFインポートモジュールは現在、以下をサポートしています。

- DNN 7.0以上。

他のバージョンのDNNにこのモジュールをインストールしたい場合は、お気軽にお問い合わせください。

## ダウンロード

以下のいずれかの場所からAspose .NET PDFインポートモジュールをダウンロードできます。

- [Github](https://github.com/asposemarketplace/Aspose_for_DNN/releases)。
- [Sourceforge](https://sourceforge.net/projects/asposednn/files/)。
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-dnn/downloads)。

## インストール

ダウンロードが完了したら、以下の手順に従ってモジュールをDNNウェブサイトにインストールしてください。

1. **ホスト**または他のスーパーユーザーアカウントとしてサイトにログインします。
1. ホストメニューに移動し、**拡張機能**を選択します。
1. **拡張機能インストールウィザード**をクリックします。
1. 指示に従ってダウンロードしたzipファイルの場所を参照し、選択して**開く**をクリックします。
1. **次へ**をクリックし、ライセンスに同意し、インストールを続行します。完了したら、**戻る**ボタンをクリックします。

詳細については、DNNの[このモジュールインストールビデオ](http://www.dnnsoftware.com/community/learn/video-library/view-video/video/542/view/details/how-to-install-a-module-in-dotnetnuke-7)を確認してください。

**注意:** モジュールのアップロード中にエラーが発生した場合、これはDNNインストールのweb.configのmaxRequestLength制限によるものです。web.configを開き、**maxRequestLength=”20480″**に設定してmaxRequestLengthを20MBに更新し、再度モジュールをアップロードしてください。

## 使用方法

Aspose .NET PDFインポートモジュールをインストールした後、ウェブサイトでの使用は非常に簡単です。以下の簡単な手順に従って始めてください。

1. DNNにホストまたは管理者レベルのアカウントでログインしていることを確認します。
1. インポートモジュールを追加したいページに移動します。
1. 上部のリボンから**モジュール** -> **新しいモジュールを追加**を選択します。

1. リストから**Aspose .NET PDFインポート for DNN**を選択し、ページ上の任意の場所にドラッグします。

Aspose .NET PDFインポートモジュールをページに正常に追加しました。ファイルブラウズと**PDFからインポート**というタイトルのボタンがページに表示され、コンテンツペインの選択ドロップダウンも表示されます。誰でもPDFファイルを選択し、**PDFからインポート**ボタンをクリックして、選択したドキュメントの内容をページにリスト表示できます。

## ビデオデモ

モジュールの動作を確認するには、以下の[ビデオ](https://www.youtube.com/watch?v=Q3z22RQgOe8)をご覧ください。

## サポート、拡張、貢献

### **サポート**

Asposeの初期の頃から、私たちは顧客に良い製品を提供するだけでは不十分であることを知っていました。良いサービスも提供する必要がありました。私たち自身が開発者であり、技術的な問題やソフトウェアの不具合が必要なことを妨げるときのフラストレーションを理解しています。私たちは問題を解決するためにここにいます。

これが、私たちが無料サポートを提供する理由です。私たちの製品を使用するすべての人は、購入したか評価版を使用しているかに関わらず、私たちの完全な注意と尊重に値します。

Aspose .NET PDFインポートモジュールに関連する問題や提案は、以下のプラットフォームのいずれかを使用してログできます。

- [Github](https://github.com/asposemarketplace/Aspose_for_DNN/issues)。
- [Sourceforge](https://sourceforge.net/p/asposednn/tickets/)。
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-dnn/issues?status=new&status=open)。

### 拡張と貢献

Aspose .NET PDFインポートモジュールはオープンソースであり、そのソースコードは以下の主要なソーシャルコーディングサイトで入手できます。開発者は、ソースコードをダウンロードし、自分の要件に応じて機能を拡張することが奨励されています。

#### ソースコード

最新のソースコードは以下のいずれかの場所から入手できます。

- [Github](https://github.com/asposemarketplace/Aspose_for_DNN)。
- [Sourceforge](https://sourceforge.net/p/asposednn/code/ci/master/tree/)。
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-dnn/src)。

#### ソースコードの設定方法

ソースコードを開いて拡張するには、以下をインストールする必要があります。

- Visual Studio 2010以上。
- [DNN開発テンプレート](https://docs.aspose.com/total/net/aspose-dnn-module-development-template/#downloading)。

以下の簡単な手順に従って始めてください。

1. ソースコードをダウンロード/クローンします。
1. Visual Studio 2010を開き、**ファイル** > **プロジェクトを開く**を選択します。
1. ダウンロードした最新のソースコードを参照し、**AsposeDNNPdfImport.csproj**を開きます。