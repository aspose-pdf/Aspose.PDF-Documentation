---
title: OneClick PDFドキュメントジェネレーターの使用
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/using-oneclick-pdf-document-generator/
description: Microsoft DynamicsでAspose.PDF OneClick PDFドキュメントジェネレーターを使用する方法を学ぶ
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "Aspose.PDF OneClick PDFドキュメントジェネレーターを使用して、Microsoft Dynamicsでシームレスなドキュメント生成を実現します。この革新的な機能により、ユーザーはCRM内でカスタマイズ可能なPDFテンプレートを直接作成し、ワンクリックで効率的にドキュメントを生成し、フォームにOneClickボタンを簡単に統合してアクセスを効率化できます。この強力なツールを使用してデータ管理能力を向上させ、生産性を改善しましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## テンプレートを作成しCRMに追加する

- Wordを開き、テンプレートを作成します。
- CRMからのデータ用にMailMergeフィールドを挿入します。

![MailMergeフィールドを挿入](using-oneclick-pdf-document-generator_1.png)

- フィールド名がCRMフィールドと正確に一致することを確認してください。
- テンプレートは個々のエンティティで使用するために特定されています。

![デモテンプレート](using-oneclick-pdf-document-generator_2.png)

- テンプレートが作成されたら、CRMでOneClick PDF設定エンティティを開き、新しいレコードを作成します。
- テンプレートの名前を付け、テンプレートが定義されているエンティティを選択し、作成したドキュメントを添付します。

![テンプレートを選択](using-oneclick-pdf-document-generator_3.png)

## リボンボタンからドキュメントを生成する

- ドキュメントを生成したいレコードを開きます。（そのエンティティの設定にテンプレートがすでに添付されていることを確認してください）
- リボンからOneClick PDFボタンをクリックします。

![OneClick PDFをクリック](using-oneclick-pdf-document-generator_4.png)

- ポップアップから：テンプレート、ファイル名、アクションを選択し、生成をクリックします。
- 選択に基づいてダウンロードしたファイルまたはノートを確認します。

## OneClickボタンを設定し使用する

- フォームからOneClickボタンを直接使用するために、フォームのカスタマイズを開きます。
- OneClickボタンを追加したい場所にWebResourceを挿入します。
- WebResourceでOpenButtonPageを選択し、名前を付けます。
- 次のサンプルのデータフィールドでボタンを設定します。

![WebResourceプロパティ](using-oneclick-pdf-document-generator_5.png)

- 各ボタンに対して別の行を使用し、次の構文を使用します：
  - 構文：テンプレート名 |<アクション：ダウンロード/ノート>|出力ファイル名
  - 例：デモ|ダウンロード|私のダウンロードファイル
- カスタマイズを保存して公開します。
- ボタンがフォームに表示されます。

![ボタンがフォームに表示されます](using-oneclick-pdf-document-generator_6.png)