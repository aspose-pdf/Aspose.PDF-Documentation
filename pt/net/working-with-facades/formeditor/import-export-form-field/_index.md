---
title: Importar e Exportar Campo de Formulário
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /pt/net/import-export-form-field/
description: Preencher campos de formulário usando DataTable com a Classe FormEditor por Aspose.PDF for .NET
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Form Field",
    "alternativeHeadline": "Streamline PDF Form Management with Import/Export Features",
    "abstract": "O recurso de Importar e Exportar Campo de Formulário em Aspose.PDF for .NET permite que os usuários preencham e manipulem campos de formulário PDF de forma contínua usando várias fontes de dados, como FDF, XFDF, XML e até mesmo objetos System.Data.DataTable. Esta poderosa API permite o manuseio automatizado de dados, aumentando a eficiência da gestão de formulários PDF e otimizando o processo de entrada de dados.",
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
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

Aspose.PDF for .NET oferece grandes capacidades para criar/manipular campos de formulário dentro de documentos PDF. Usando esta API, você pode preencher programaticamente campos de formulário dentro de um arquivo PDF, preencher campos de formulário por [Importar Dados de FDF para um Arquivo PDF](/pdf/net/import-and-export-data/), [Importar Dados de XFDF para um Arquivo PDF](/pdf/net/import-and-export-data/), [Importar Dados de XML para um Arquivo PDF](/pdf/net/import-and-export-data/) ou até mesmo você pode importar dados de um objeto [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1).

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

## Exportar Dados de FDF para um Arquivo PDF

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