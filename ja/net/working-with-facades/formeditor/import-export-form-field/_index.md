---
title: フォームフィールドのインポートとエクスポート
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /ja/net/import-export-form-field/
description: FormEditorクラスを使用してDataTableでフォームフィールドを埋める Aspose.PDF for .NET
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Form Field",
    "alternativeHeadline": "Streamline PDF Form Management with Import/Export Features",
    "abstract": "Aspose.PDF for .NETのフォームフィールドのインポートとエクスポート機能により、ユーザーはFDF、XFDF、XML、さらにはSystem.Data.DataTableオブジェクトなどのさまざまなデータソースを使用してPDFフォームフィールドをシームレスに埋めたり操作したりできます。この強力なAPIは自動データ処理を可能にし、PDFフォーム管理の効率を向上させ、データ入力プロセスを合理化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "252",
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
    "url": "/net/import-export-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

Aspose.PDF for .NETは、PDFドキュメント内のフォームフィールドを作成/操作するための優れた機能を提供します。このAPIを使用すると、プログラム的にPDFファイル内のフォームフィールドを埋めたり、[FDFからPDFファイルにデータをインポートする](/pdf/ja/net/import-and-export-data/)、[XFDFからPDFファイルにデータをインポートする](/pdf/ja/net/import-and-export-data/)、[XMLからPDFファイルにデータをインポートする](/pdf/ja/net/import-and-export-data/)ことができます。また、[System.Data.DataTable](https://reference.aspose.com/pdf/ja/net/aspose.pdf.table/importdatatable/methods/1)オブジェクトからデータをインポートすることもできます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ImportData()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Import data fdf
        using (var xfdfInputStream  = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            form.ImportFdf(xfdfInputStream);
        }
                
        // Import data XML
        using (var xfdfInputStream  = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            form.ImportXml(xfdfInputStream);
        }
                
        // Import data XFDF
        using (var xfdfInputStream  = new FileStream(dataDir + "input.xfdf", FileMode.Open))
        {
            form.ImportXfdf(xfdfInputStream);
        }
                
        // Save PDF document
        form.Save(dataDir + "ImportDataUpdated_out.pdf");
    }
}
```

## FDFからPDFファイルにデータをエクスポートする

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void ExportData()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");
                
        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "data_out.fdf", FileMode.Create))
        {
            form.ExportXfdf(fdfOutputStream);
        }
                
        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "data_out.xml", FileMode.Create))
        {
            form.ExportXfdf(xmlOutputStream);
        }
            
        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "data_out.xfdf", FileMode.Create))
        {
            form.ExportXfdf(xfdfOutputStream);
        }              
    }
} 
```