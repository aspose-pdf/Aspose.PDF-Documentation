---
title: Aspose.PDF DOM APIの基本
linktitle: DOM APIの基本
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /ja/net/basics-of-dom-api/
description: Aspose.PDF for .NETは、オブジェクトの観点からPDFドキュメントの構造を表現するためにDOMのアイデアを使用しています。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Basics of Aspose.PDF DOM API",
    "alternativeHeadline": "Enhanced PDF Manipulation with Aspose.PDF DOM API in C#",
    "abstract": "新しいAspose.PDF for .NET DOM APIは、PDFドキュメントの構造を階層的なツリーとして表現することにより、PDFドキュメントを操作するための堅牢なオブジェクト指向アプローチを提供します。この機能により、開発者はPDF要素に簡単にアクセス、更新、エクスポートでき、直感的なプログラミングインターフェースを通じてドキュメント操作に対する柔軟性と制御を強化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "891",
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
    "url": "/net/basics-of-dom-api/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/basics-of-dom-api/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## DOM APIの紹介

ドキュメントオブジェクトモデル（DOM）は、構造化されたドキュメントをオブジェクト指向モデルとして表現する形式です。DOMは、プラットフォームや言語に依存しない方法で構造化されたドキュメントを表現するための公式なWorld Wide Web Consortium（W3C）標準です。

簡単に言えば、DOMはドキュメントの構造を表すオブジェクトのツリーです。Aspose.PDF for .NETも、オブジェクトの観点からPDFドキュメントの構造を表現するためにDOMのアイデアを使用しています。ただし、DOMの要素（その要素など）は、使用中のプログラミング言語の構文内で操作されます。DOMの公開インターフェースは、そのアプリケーションプログラミングインターフェース（API）で指定されています。

### PDFドキュメントの紹介

ポータブルドキュメントフォーマット（PDF）は、ドキュメント交換のためのオープンスタンダードです。PDFドキュメントは、テキストとバイナリデータの組み合わせです。テキストエディタで開くと、ドキュメントの構造と内容を定義する生のオブジェクトが表示されます。

PDFファイルの論理構造は階層的であり、表示アプリケーションがドキュメントのページとその内容を描画する順序を決定します。PDFは、オブジェクト、ファイル構造、ドキュメント構造、コンテンツストリームの4つのコンポーネントで構成されています。

### PDFドキュメント構造

PDFファイルの構造は階層的であるため、Aspose.PDF for .NETも同じ方法で要素にアクセスします。以下の階層は、PDFドキュメントが論理的にどのように構造化されているか、そしてAspose.PDF for .NET DOM APIがそれをどのように構築するかを示しています。

![PDFドキュメント構造](../images/structure.png)

### PDFドキュメント要素へのアクセス

Documentオブジェクトはオブジェクトモデルのルートレベルにあります。Aspose.PDF for .NET DOM APIを使用すると、Documentオブジェクトを作成し、階層内の他のすべてのオブジェクトにアクセスできます。Pagesのようなコレクションや、Pageなどの個々の要素にアクセスできます。DOM APIは、PDFドキュメントを操作するための単一のエントリポイントとエグジットポイントを提供します。以下のように操作します：

- PDFドキュメントを開く。
- DOMスタイルでPDFドキュメント構造にアクセスする。
- PDFドキュメント内のデータを更新する。
- PDFドキュメントを検証する。
- PDFドキュメントを異なるフォーマットにエクスポートする。
- 最後に、更新されたPDFドキュメントを保存する。

## 新しいAspose.PDF for .NET APIの使用方法

このトピックでは、新しいAspose.PDF for .NET APIを説明し、迅速かつ簡単に始めるためのガイドを提供します。特定の機能の使用に関する詳細はこの記事の一部ではないことに注意してください。

Aspose.PDF for .NETは、2つの部分で構成されています：

- Aspose.PDF for .NET DOM API。
- Aspose.Pdf.Facades（旧Aspose.PDF.Kit for .NET）。

これらの各領域の詳細は以下に示します。

### Aspose.PDF for .NET DOM API

Aspose.PDF for .NET DOM APIは、PDFドキュメント構造に対応しており、ファイルおよびドキュメントレベルだけでなく、オブジェクトレベルでもPDFドキュメントを操作するのに役立ちます。開発者がPDFドキュメントのすべての要素とオブジェクトにアクセスできるように、より柔軟性を提供しました。Aspose.PDF DOM APIのクラスを使用すると、ドキュメント要素とフォーマットにプログラム的にアクセスできます。この新しいDOM APIは、以下のようなさまざまな名前空間で構成されています：

### Aspose.PDF

この名前空間は、PDFドキュメントを開いて保存するためのDocumentクラスを提供します。Licenseクラスもこの名前空間の一部です。また、Page、PageCollection、FileSpecification、EmbeddedFileCollection、OutlineItemCollection、OutlineCollectionなどのPDFページ、添付ファイル、ブックマークに関連するクラスも提供します。

#### Aspose.Text

この名前空間は、テキストとそのさまざまな側面を操作するのに役立つクラスを提供します。例えば、Font、FontCollection、FontRepository、FontStyles、TextAbsorber、TextFragment、TextFragmentAbsorber、TextFragmentCollection、TextFragmentState、TextSegment、TextSegmentCollectionなどです。

#### Aspose.Text.TextOptions

この名前空間は、テキストの検索、編集、置換のためのさまざまなオプションを設定するためのクラスを提供します。例えば、TextEditOptions、TextReplaceOptions、TextSearchOptionsなどです。

#### Aspose.InteractiveFeatures

この名前空間には、PDFドキュメントのインタラクティブ機能を操作するのに役立つクラスが含まれています。例えば、ドキュメントの操作やその他のアクションに関するクラスが含まれています。この名前空間には、GoToAction、GoToRemoteAction、GoToURIActionなどのクラスがあります。

#### Aspose.InteractiveFeatures.Annotations

注釈は、PDFドキュメントのインタラクティブ機能の一部です。注釈用の名前空間を専用に設けています。この名前空間には、Annotation、AnnotationCollection、CircleAnnotation、LinkAnnotationなどの注釈を操作するのに役立つクラスが含まれています。

#### Aspose.InteractiveFeatures.Forms

この名前空間には、PDFフォームおよびフォームフィールドを操作するのに役立つクラスが含まれています。例えば、Form、Field、TextBoxField、OptionCollectionなどです。

#### Aspose.Pdf.Devices

PDFドキュメントに対してさまざまな操作を実行できます。例えば、PDFドキュメントをさまざまな画像フォーマットに変換することができます。ただし、そのような操作はDocumentオブジェクトには属さず、そのような操作のためにDocumentクラスを拡張することはできません。だからこそ、新しいDOM APIではDeviceの概念を導入しました。

#### Aspose.Pdf.Facades

Aspose.PDF for .NET以前は、既存のPDFファイルを操作するためにAspose.PDF.Kit for .NETが必要でした。古いAspose.PDF.Kitコードを実行するには、Aspose.PDF.Facades名前空間を使用できます。