---
title: Работа со слоями PDF с использованием C#
linktitle: Работа со слоями PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ru/net/work-with-pdf-layers/
description: Следующая задача объясняет, как заблокировать слой PDF, извлечь элементы слоя PDF, сгладить многоуровневый PDF-файл и объединить все слои внутри PDF в один.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Work with PDF layers using C#",
    "alternativeHeadline": "Manage PDF layers effortlessly with C#",
    "abstract": "Испытайте улучшенное управление PDF-документами с новой функцией Aspose.PDF для .NET, которая позволяет пользователям эффективно работать со слоями PDF. Эта функция включает блокировку и разблокировку слоёв, извлечение элементов в отдельные файлы, выравнивание многослойного содержимого и объединение нескольких слоёв в один, обеспечивая больший контроль над видимостью и организацией документов. Раскройте потенциал своих PDF-документов и оптимизируйте рабочие процессы с помощью этих мощных инструментов",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF layers, lock PDF layer, extract PDF layer elements, flatten layered PDF, merge PDF layers, Aspose.PDF for .NET, layer.Lock(), layer.Flatten(), layer.Save()",
    "wordcount": "501",
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
    "url": "/net/work-with-pdf-layers/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/work-with-pdf-layers/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

Слои PDF позволяют документу PDF содержать различные наборы содержимого, которые можно выборочно просматривать или скрывать. Каждый слой в PDF может включать текст, изображения или графику, и пользователи могут включать или отключать эти слои в зависимости от своих потребностей. Слои часто используются в сложных документах, где необходимо упорядочить или разделить различное содержимое.

## Блокировка слоя PDF

С помощью Aspose.PDF for .NET вы можете открыть PDF-файл, заблокировать определённый слой на первой странице и сохранить документ с изменениями.

Эта функция была реализована начиная с версии 24.5.

Были добавлены два новых метода и одно свойство:

- Layer.Lock(); — блокирует слой.
- Layer.Unlock(); — разблокирует слой.
- Layer.Locked; — свойство, указывающее состояние блокировки слоя.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LockLayerInPDF()
{
	// The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Layers();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page and the first layer
        var page = document.Pages[1];
        var layer = page.Layers[0];

        // Lock the layer
        layer.Lock();

        // Save PDF document
        document.Save(dataDir + "LockLayerInPDF_out.pdf");
    }
}
```

## Извлечение элементов слоя PDF

Библиотека Aspose.PDF for .NET позволяет извлекать каждый слой из первой страницы и сохранять каждый слой в отдельный файл.

Чтобы создать новый PDF-файл из слоя, можно использовать следующий фрагмент кода:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output path
        foreach (var layer in layers)
        {
            layer.Save(dataDir + "Layers_out.pdf");
        }
    }
}
```

В выпуске 24.9 эта функция была обновлена.

Можно извлечь элементы слоя PDF и сохранить их в новом потоке PDF-файлов:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SaveLayersToOutputStream(Stream outputStream)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get layers from the first page
        var layers = document.Pages[1].Layers;

        // Save each layer to the output stream
        foreach (var layer in layers)
        {
            layer.Save(outputStream);
        }
    }
}
```

## Выравнивание многоуровневого PDF-файла

Библиотека Aspose.PDF for .NET открывает PDF-файл, перебирает каждый слой на первой странице и выравнивает каждый слой, делая его постоянным на странице.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenLayersInPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Flatten each layer on the page
        foreach (var layer in page.Layers)
        {
            layer.Flatten(true);
        }
    }
}
```

Метод 'Layer.Flatten(bool cleanupContentStream)' принимает логический параметр, который указывает, следует ли удалять необязательные маркеры группы содержимого из потока содержимого. Установка параметра cleanupContentStream в значение false ускоряет процесс выравнивания.

## Объединение всех слоёв внутри PDF-файла в один

Библиотека Aspose.PDF for .NET позволяет объединить либо все слои PDF, либо конкретный слой на первой странице в новый слой и сохраняет обновлённый документ.

Для объединения всех слоёв на странице были добавлены два метода:

- void MergeLayers(string newLayerName).
- void MergeLayers(string newLayerName, string newOptionalContentGroupId).

Второй параметр позволяет переименовать необязательный маркер группы содержимого. Значение по умолчанию — «oc1» (/OC /oc1 BDC).

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MergeLayersInPdf(string newLayerName, string optionalLayerName = null)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the first page
        var page = document.Pages[1];

        // Merge layers with a new layer name
        if (optionalLayerName != null)
        {
            page.MergeLayers(newLayerName, optionalLayerName);
        }
        else
        {
            page.MergeLayers(newLayerName);
        }

        // Save PDF document
        document.Save(dataDir + "MergeLayersInPdf_out.pdf");
    }
}
```