---
title: COM相互運用を介したPHP
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/php-via-com-interop/
description: COM Interopを使用してAspose.PDF for .NETをPHPアプリケーションに統合します。ワークフローに強力なPDF処理機能を追加します。
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PHP via COM Interop",
    "alternativeHeadline": "Seamlessly Integrate PHP with Aspose.PDF for .NET via COM",
    "abstract": "PHPアプリケーション内でAspose.PDF for .NETをシームレスに統合するPHP via COM Interop機能を紹介します。この機能により、開発者はPHPを使用してPDFファイルを作成および操作でき、PHPスクリプトから直接.NETの強力な機能を活用することで生産性が向上します。この革新的な相互運用ソリューションを使用して、効率的なPDFからExcelへの変換などを体験してください。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PHP, COM Interop, Aspose.PDF, PDF file creation, Excel conversion, Aspose.License, COM interoperability, PHP integration, SaveFormat enum, .NET integration",
    "wordcount": "192",
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
    "url": "/net/php-via-com-interop/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/php-via-com-interop/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 前提条件

{{% alert color="primary" %}}
COMで動作するようにPHPを設定してください。詳細については、<http://www.php.net/manual/en/ref.com.php>を参照してください。さらに詳しい情報は、[COM Interopを介して.NET用のAspose.pdfを使用する](/pdf/net/use-aspose-pdf-for-net-via-com-interop/)という記事をご覧ください。

{{% /alert %}}

## Hello World! の例

{{% alert color="primary" %}}
これは、新しいPDFファイルを作成し、COM Interopを介してPHPで[Aspose.PDF for .NET](/pdf/net/)を使用してPDFファイルにテキストを追加する方法を示すシンプルなアプリケーションです。

{{% /alert %}}

```php
<?php
echo "<h2>Calling Aspose.PDF for .NET from PHP using COM Interoperatibility</h2>";
echo "<h3>PDF to Excel Conversion</h3>";

// Set license
$lic = new COM("Aspose.Pdf.License");
$lic->SetLicense("Aspose.Total.lic");

// Open PDF document
$input = "HelloWorld.pdf";
$helper = new COM("Aspose.Pdf.ComHelper");

$pdf = $helper->OpenFile($input);

// Save PDF document to desired file format by passing  SaveFormat enum value for the format in this case we pass 9 for excel.
$output = "test_php.xls";
$pdf->Save_4($output, 9);
?>
```