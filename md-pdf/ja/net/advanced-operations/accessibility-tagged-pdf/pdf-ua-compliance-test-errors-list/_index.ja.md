---
title: PDF-UA 準拠テスト - エラーリスト
linktitle: PDF-UA 準拠テスト - エラーリスト
type: docs
weight: 50
url: /net/pdf-ua-compliance-test-errors-list/
description: この記事では、Aspose.PDF APIおよびC#またはVBを使用したPDF/UA準拠テスト中に発生する可能性のあるエラーのリストを示しています。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF-UA 準拠テスト - エラーリスト",
    "alternativeHeadline": "APIを使用したPDF/UA準拠テスト",
    "author": {
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, ドキュメント生成",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/pdf-ua-compliance-test-errors-list/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-ua-compliance-test-errors-list/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF APIおよびC#またはVBを使用したPDF/UA準拠テスト中に発生する可能性のあるエラーのリストを示しています。"
}
</script>
Aspose.PDF APIを使用してPDF/UA準拠テストを行う際には、発生する可能性のあるエラーメッセージを知りたいと思うかもしれません。これらのエラーには一般的なもの、テキスト、フォント、見出し、その他いくつかのタイプがあります。このようなエラーに関する情報は、エラーの正確な原因とその処理方法を知るのに役立ちます。

この記事では、APIを使用したPDF/UA準拠テスト中に発生する可能性のあるエラーをリストアップします。

## **一般**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|5:1|エラー|PDF/UA識別子がありません|
|6.2:1.1|エラー|構造親ツリー：一貫性のないエントリが見つかりました|
|7.1:1.1(14.8.1)|エラー|ドキュメントがタグ付けされているとマークされていません|
|7.1:1.1(14.8)|エラー|[OBJECT_NAME] オブジェクトがタグ付けされていません|
|7.1:1.2(14.8.2.2)|エラー|タグ付けされた内容の内部にアーティファクトが存在します|
|7.1:1.3(14.8.2.2)|エラー|アーティファクトの内部にタグ付けされた内容が存在します|
|7.1:2.1|警告|構造ツリーがありません|
|7.1:2.2|警告|ルート要素ではない「ドキュメント」構造要素が見つかりました|
|7.1:2.3|警告|ルート要素として使用される「[ELEMENT_NAME]」構造要素|
|7.1:2.3|Warning|「[ELEMENT_NAME]」構造要素がルート要素として使用されています|
|7.1:2.4.1|Warning|「[ELEMENT_NAME]」構造要素の使用が不適切かもしれません|
|7.1:2.4.2|Error|「[ELEMENT_NAME]」構造要素の無効な使用|
|7.1:2.5|Warning|StructTreeRoot内での「[ELEMENT_NAME]」構造要素の誤ったネスト可能性|
|7.1:3(14.8.4)|Error|非標準構造型「[TYPE_NAME]」が標準構造型にも他の非標準構造型にもマップされていません|
|7.1:4(14.8.4)|Warning|標準構造型「[TYPE_NAME]」が「[TYPE_NAME]」に再マップされています|
|7.1:5|Need check manual|色のコントラスト|
|7.1:6.1|Error|文書にXMPメタデータがありません|
|7.1:6.2|Error|文書のXMPメタデータにタイトルがありません|
|7.1:6.3|Warning|文書のXMPメタデータでタイトルが空です|
|7.1:7.1(12.2)|Warning|「ViewerPreferences」辞書がありません|
|7.1:7.2(12.2)|Error|「DisplayDocTitle」エントリが設定されていません|
|7.1:8(14.7.1)|Error|「Suspects」エントリが設定されています|
|7.1:9.1(14.7)|Error|ページに「StructParents」キーがありません|
|7.1:9.2(14.7)|Error|注釈に「StructParent」エントリがありません|
|7.1:9.2(14.7)|Error|「StructParent」エントリが注釈で見つかりません|
|7.1:9.3(14.7)|Error|指定された「StructParents」のエントリが見つかりません|

## **テキスト**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.2:1|手動チェックが必要|論理的な読み取り順序|
|7.2:2(14.8.2.4.2)|Error|テキストオブジェクトの文字をUnicodeにマッピングできません|
|7.2:3.1(14.9.2.2)|Error|テキストオブジェクトの自然言語を特定できません|
|7.2:3.2(14.9.2.2)|Error|代替テキストの自然言語を特定できません|
|7.2:3.3(14.9.2.2)|Error|実際のテキストの自然言語を特定できません|
|7.2:3.4(14.9.2.2)|Error|展開テキストの自然言語を特定できません|
|7.2:4(14.9.4)|Error|伸縮可能な文字がActualTextを使用してタグ付けされていません|

## **フォント**

|**条項**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.21.3.1|Error|CIDFontの文字コレクションが内部CMapの文字コレクションと互換性がありません|
|7.21.3.2|Error|フォント「[FONT_NAME]」のCIDToGIDMapが埋め込まれていないか不完全です|
|7.21.3.2|Error|フォント「[FONT_NAME]」のCMapが埋め込まれていません|
|7.21.3.2|エラー|フォント「[FONT_NAME]」にCMapが埋め込まれていません|
|7.21.4.2|エラー|フォント「[FONT_NAME]」のCIDSetが欠落しているか不完全です|
|7.21.4.2|エラー|埋め込まれたフォント「[FONT_NAME]」にグリフが欠けています|
|7.21.6|エラー|非シンボリックTrueTypeフォント「[FONT_NAME]」にcmapエントリーがありません|
|7.21.6|エラー|シンボリックTrueTypeフォント「[FONT_NAME]」にエンコーディングエントリーが禁止されています|
|7.21.6|エラー|TrueTypeフォント「[FONT_NAME]」に間違ったエンコーディングが使用されています|
|7.21.6|エラー|非シンボリックTrueTypeフォント「[FONT_NAME]」の「Differences」配列が正しくありません|

## **グラフィックス**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.3:1(14.8.4.5)|エラー|単一ページに境界ボックスのない「[ELEMENT_NAME]」要素|
|7.3:2|エラー|「[ELEMENT_NAME]」構造要素の代替テキストがありません|
|7.3:3|エラー|図に付随するキャプションがありません|
|7.3:4(14.8.4.5)|エラー|BTとETオペレータの間にグラフィックスオブジェクトが表示されます|

## **見出し**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.4.2:1|エラー|最初の見出しは最初のレベルにありません|
|7.4.2:2|エラー|番号付き見出しが1つ以上の見出しレベルをスキップしています|
|7.4.2:2|エラー|番号付き見出しが1つ以上の見出しレベルをスキップしています|
|7.4.4:1|エラー|「H」と「Hn」構造要素が見つかりました|
|7.4.4:2|エラー|親構造要素内に「H」構造要素が複数存在します|

## **テーブル**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.5:1|警告|不規則なテーブル行|
|7.5:2|エラー|テーブルヘッダーセルに関連するサブセルがありません|
|7.5:3.1|警告|テーブルヘッダーがありません|
|7.5:3.2|警告|テーブルサマリーがありません|

## **リスト**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.6:1|エラー|「LI」構造要素は「L」要素の子でなければなりません|
|7.6:2|エラー|「Lbl」と「LBody」構造要素は「LI」要素の子でなければなりません|

## **注釈と参照**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.9:2.1|エラー|「Note」構造要素にIDがありません|
|7.9:2.2|エラー|「Note」構造要素のIDエントリーが一意ではありません|

## **オプショナルコンテンツ**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.10:1|エラー|オプショナルコンテンツ設定辞書に「Name」がありません|
|7.10:1|Error|オプショナルコンテンツ設定辞書に「Name」がありません|
|7.10:2|Error|オプショナルコンテンツ設定辞書に「AS」キーが含まれています|

## **埋め込まれたファイル**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.11:1|Error|ファイル仕様に「F」または「UF」キーがありません|
|7.11:2|Warning|ファイル仕様に「Desc」キーがありません|

## **デジタル署名**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.13:1|Error|署名フォームフィールド「[FIELD_NAME]」が仕様に準拠していません|
|7.13:2.1|Error|フォームフィールド「[FIELD_NAME]」の代替名の自然言語を特定できません|
|7.13:2.2|Error|フォームフィールド「[FIELD_NAME]」に代替フィールド名エントリーがありません|

## **非対話型フォーム**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.14:1|Error|非対話型フォームアイテムに「PrintField」属性がありません|

## **XFA**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.15:1|Error|PDFに動的XFAフォームが含まれています|

## **セキュリティ**

|**コード**|**重大度**|**メッセージ**|
|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.16:1(7.6.3.2)|エラー|セキュリティ設定が支援技術の文書内容へのアクセスをブロックしています|
|7.16:2(7.6.3.2)|エラー|許可の制限により変換が許可されていません|

## **ナビゲーション**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.17:1|エラー|文書のアウトラインのエラー|
|7.17:2|エラー|アウトラインの自然言語を特定できます|
|7.17:3|手動チェックが必要|意味的に適切なページラベル|

## **注釈**

|**コード**|**重大度**|**メッセージ**|
| :- | :- | :- |
|7.18.1:1|エラー|コンテンツエントリの自然言語を特定できません|
|7.18.1:2|エラー|注釈のための代替説明がありません|
|7.18.1:3|エラー|注釈が「Annot」構造要素内にネストされていません|
|7.18.2:1|エラー|ISO 32000で未定義のサブタイプを持つ注釈が7.18.1を満たしていません|
|7.18.2:2|エラー|サブタイプTrapNetの注釈が存在します|
|7.18.3:1|エラー|注釈が含まれるページのタブ順序エントリが'S'（構造）に設定されていません|
|7.18.4:1|エラー|「Widget」注釈が「Form」構造要素内にネストされていません|
|7.18.4:1|Error|「Widget」アノテーションが「Form」構造要素の中にネストされていません|
|7.18.5:1|Error|「Link」アノテーションが「Link」構造要素の中にネストされていません|
|7.18.6.2:1|Error|メディアクリップデータ辞書からCTキーが欠けています|
|7.18.6.2:2|Error|メディアクリップデータ辞書からAltキーが欠けています|
|7.18.7:1|Error|ファイル添付アノテーション。「F」または「UF」キーがファイル仕様にありません|
|7.18.7:2|Warning|ファイル添付アノテーション。「Desc」キーがファイル仕様にありません|
|7.18.8:1|Error|PrinterMarkアノテーションが論理構造に含まれています|
|7.18.8:2|Error|PrinterMarkアノテーションの外観ストリームがアーティファクトとしてマークされていません|

## **Actions**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.19:1|Need check manual|アクションが見つかりました。PDF/UAの仕様に従って手動でアクションを確認する必要があります|

## **XObjects**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|7.20:1|Error|適合するPDF/UAファイルでは参照XObjectは使用できません|
|7.20:2|Error|Form XObjectの内容が構造要素に組み込まれていません|
|7.20:2|エラー|Form XObject のコンテンツは構造要素に組み込まれていません|

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
                "areaServed": "AU",
                "availableLanguage": "英語"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET 用 PDF 操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

