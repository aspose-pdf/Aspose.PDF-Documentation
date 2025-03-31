---
title: Importar e Exportar Dados
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /pt/net/import-and-export-data/
description: Esta seção explica como importar e exportar dados com Aspose.PDF Facades usando a classe Form.
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data",
    "alternativeHeadline": "Effortless Data Import and Export for PDF Forms",
    "abstract": "O recurso de Importação e Exportação de Dados em Aspose.PDF for .NET permite a integração perfeita da gestão de dados de documentos, permitindo que os usuários importem e exportem dados de formulários PDF utilizando formatos XML, FDF, XFDF e JSON. Essa funcionalidade aprimora as capacidades de manipulação de dados, facilitando a automação de fluxos de trabalho e a manutenção de registros precisos diretamente de documentos PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1085",
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
    "url": "/net/import-and-export-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

A classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) permite que você importe dados de um arquivo XML para o arquivo PDF usando o método [ImportXml](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.form/importxml/methods/1). Para importar dados de XML, você precisa criar um objeto da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) e, em seguida, chamar o método [ImportXml](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/importxml/index) usando o objeto FileStream. Finalmente, você pode salvar o arquivo PDF usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/formeditor/methods/save) da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form). O seguinte trecho de código mostra como importar dados de um arquivo XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open xml file
        using (var xmlInputStream = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXml(xmlInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXML_out.pdf");
        }
    }
}
```

## Exportar Dados para XML de um Arquivo PDF

A classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) permite que você exporte dados para um arquivo XML a partir do arquivo PDF usando o método [ExportXml](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/exportxml). Para exportar dados para XML, você precisa criar um objeto da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) e, em seguida, chamar o método [ExportXml](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/exportxml) usando o objeto FileStream. Finalmente, você pode fechar o objeto FileStream e descartar o objeto Form. O seguinte trecho de código mostra como exportar dados para um arquivo XML.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXml(xmlOutputStream);
        }
    }
}
```

## Importar Dados de FDF para um Arquivo PDF

A classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) permite que você importe dados de um arquivo FDF para o arquivo PDF usando o método [ImportFdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/importfdf). Para importar dados de FDF, você precisa criar um objeto da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) e, em seguida, chamar o método [ImportFdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/importfdf) usando o objeto FileStream. Finalmente, você pode salvar o arquivo PDF usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/formeditor/methods/save) da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form). O seguinte trecho de código mostra como importar dados de um arquivo FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromPdfIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");
        
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportFdf(fdfInputStream);         

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromPdf_out.pdf");
        }
    }
}
```

## Exportar Dados para FDF de um Arquivo PDF

A classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) permite que você exporte dados para um arquivo FDF a partir do arquivo PDF usando o método [ExportFdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/exportfdf). Para exportar dados para FDF, você precisa criar um objeto da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) e, em seguida, chamar o método [ExportFdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/exportfdf) usando o objeto FileStream. Finalmente, você pode salvar o arquivo PDF usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/formeditor/methods/save) da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form). O seguinte trecho de código mostra como exportar dados para um arquivo FDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdfFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportFdf(fdfOutputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToPdf_out.pdf"); 
        }
    }
}
```

## Importar Dados de XFDF para um Arquivo PDF

A classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) permite que você importe dados de um arquivo XFDF para o arquivo PDF usando o método [ImportXfdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/importxfdf). Para importar dados de XFDF, você precisa criar um objeto da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) e, em seguida, chamar o método [ImportXfdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/importxfdf) usando o objeto FileStream. Finalmente, você pode salvar o arquivo PDF usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/formeditor/methods/save) da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form). O seguinte trecho de código mostra como importar dados de um arquivo XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXFDIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open XFDF file
        using (var xfdfInputStream = new FileStream(dataDir + "test2.xfdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXfdf(xfdfInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXFDF_out.pdf");
        }
    }
}
```

## Exportar Dados para XFDF de um Arquivo PDF

A classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) permite que você exporte dados para um arquivo XFDF a partir do arquivo PDF usando o método [ExportXfdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/exportxfdf). Para exportar dados para XFDF, você precisa criar um objeto da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form) e, em seguida, chamar o método [ExportXfdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/form/methods/exportxfdf) usando o objeto FileStream. Finalmente, você pode salvar o arquivo PDF usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/formeditor/methods/save) da classe [Form](https://reference.aspose.com/pdf/pt/net/aspose.pdf.forms/form). O seguinte trecho de código mostra como exportar dados para um arquivo XFDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDFFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "out.xfdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXfdf(xfdfOutputStream);

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToXFDF_out.pdf");
        }
    }
}
```

## Exportar valores dos campos para o arquivo JSON

Aspose.Pdf.Facades fornece uma API alternativa para trabalhar com campos de formulário. Este trecho demonstra como exportar e importar valores de campos usando esta API.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportValuesFromFieldsToJSON()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    
    using (var form = new Aspose.Pdf.Facades.Form())
    {       
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Create JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Create))
        {
            // Export data
            form.ExportJson(jsonStream);
        }
    }
}
```

## Importar valores para os campos a partir do arquivo JSON

Este trecho de código demonstra como importar valores para os campos de formulário de um documento PDF a partir de um arquivo JSON usando a API Aspose.Pdf.Facades. O FileStream é usado para manipular o arquivo JSON.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportValuesFromJsonToForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {        
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Import from JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Open))
        {
            // Export data
            form.ImportJson(jsonStream);
        }
    }
}
```