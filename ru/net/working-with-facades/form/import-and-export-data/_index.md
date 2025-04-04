---
title: Импорт и экспорт данных
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ru/net/import-and-export-data/
description: Этот раздел объясняет, как импортировать и экспортировать данные с помощью Aspose.PDF Facades, используя класс Form.
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data",
    "alternativeHeadline": "Effortless Data Import and Export for PDF Forms",
    "abstract": "Функция импорта и экспорта данных в Aspose.PDF for .NET позволяет бесшовную интеграцию управления данными документов, позволяя пользователям импортировать и экспортировать данные форм PDF, используя форматы XML, FDF, XFDF и JSON. Эта функциональность улучшает возможности обработки данных, упрощая автоматизацию рабочих процессов и поддержание точных записей непосредственно из PDF документов.",
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
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

[Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form) класс позволяет вам импортировать данные из XML файла в PDF файл, используя метод [ImportXml](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.form/importxml/methods/1). Для импорта данных из XML вам нужно создать объект класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form), а затем вызвать метод [ImportXml](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/importxml/index), используя объект FileStream. Наконец, вы можете сохранить PDF файл, используя метод [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/save) класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form). Следующий фрагмент кода показывает, как импортировать данные из XML файла.

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

## Экспорт данных в XML из PDF файла

[Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form) класс позволяет вам экспортировать данные в XML файл из PDF файла, используя метод [ExportXml](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/exportxml). Для экспорта данных в XML вам нужно создать объект класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form), а затем вызвать метод [ExportXml](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/exportxml), используя объект FileStream. Наконец, вы можете закрыть объект FileStream и освободить объект Form. Следующий фрагмент кода показывает, как экспортировать данные в XML файл.

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

## Импорт данных из FDF в PDF файл

[Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form) класс позволяет вам импортировать данные из FDF файла в PDF файл, используя метод [ImportFdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/importfdf). Для импорта данных из FDF вам нужно создать объект класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form), а затем вызвать метод [ImportFdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/importfdf), используя объект FileStream. Наконец, вы можете сохранить PDF файл, используя метод [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/save) класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form). Следующий фрагмент кода показывает, как импортировать данные из FDF файла.

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

## Экспорт данных в FDF из PDF файла

[Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form) класс позволяет вам экспортировать данные в FDF файл из PDF файла, используя метод [ExportFdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/exportfdf). Для экспорта данных в FDF вам нужно создать объект класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form), а затем вызвать метод [ExportFdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/exportfdf), используя объект FileStream. Наконец, вы можете сохранить PDF файл, используя метод [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/save) класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form). Следующий фрагмент кода показывает, как экспортировать данные в FDF файл.

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

## Импорт данных из XFDF в PDF файл

[Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form) класс позволяет вам импортировать данные из XFDF файла в PDF файл, используя метод [ImportXfdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/importxfdf). Для импорта данных из XFDF вам нужно создать объект класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form), а затем вызвать метод [ImportXfdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/importxfdf), используя объект FileStream. Наконец, вы можете сохранить PDF файл, используя метод [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/save) класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form). Следующий фрагмент кода показывает, как импортировать данные из XFDF файла.

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

## Экспорт данных в XFDF из PDF файла

[Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form) класс позволяет вам экспортировать данные в XFDF файл из PDF файла, используя метод [ExportXfdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/exportxfdf). Для экспорта данных в XFDF вам нужно создать объект класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form), а затем вызвать метод [ExportXfdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/form/methods/exportxfdf), используя объект FileStream. Наконец, вы можете сохранить PDF файл, используя метод [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formeditor/methods/save) класса [Form](https://reference.aspose.com/pdf/ru/net/aspose.pdf.forms/form). Следующий фрагмент кода показывает, как экспортировать данные в XFDF файл.

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

## Экспорт значений из полей в JSON файл

Aspose.Pdf.Facades предоставляет альтернативный API для работы с полями форм. Этот фрагмент демонстрирует, как экспортировать и импортировать значения полей, используя этот API.

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

## Импорт значений в поля из JSON файла

Этот фрагмент кода демонстрирует, как импортировать значения в поля формы PDF документа из JSON файла, используя API Aspose.Pdf.Facades. Объект FileStream используется для обработки JSON файла.

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