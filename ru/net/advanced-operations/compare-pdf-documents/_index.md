---
title: Сравнение PDF документов
linktitle: Сравнить PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /ru/net/compare-pdf-documents/
description: С версии 24.7 теперь возможно сравнивать содержимое PDF документов с аннотациями и выводом рядом
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "Новая функция сравнения PDF в Aspose.PDF for .NET позволяет пользователям эффективно выявлять различия между двумя PDF документами, как по конкретным страницам, так и по всему содержимому. С боковыми выводами и настраиваемыми опциями, такими как дополнительные маркеры изменений и различные режимы сравнения, этот мощный инструмент улучшает сотрудничество, упрощая отслеживание и обзор правок.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "1108",
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
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

Обратите внимание, что все инструменты сравнения доступны в библиотеке [Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/).

## Способы сравнения PDF документов

При работе с PDF документами иногда необходимо сравнить содержимое двух документов, чтобы выявить различия. Библиотека Aspose.PDF for .NET предоставляет мощный набор инструментов для этой цели. В этой статье мы рассмотрим, как сравнивать PDF документы, используя несколько простых фрагментов кода.

Функциональность сравнения в Aspose.PDF позволяет сравнивать два PDF документа постранично. Вы можете выбрать, чтобы сравнить либо конкретные страницы, либо целые документы. Результирующий документ сравнения подчеркивает различия, что упрощает выявление изменений между двумя файлами.

Вот список возможных способов сравнения PDF документов с использованием библиотеки Aspose.PDF для .NET:

1. **Сравнение конкретных страниц** - Сравните первые страницы двух PDF документов.

1. **Сравнение целых документов** - Сравните все содержимое двух PDF документов.

1. **Сравнить PDF документы графически**:

- Сравнить PDF с методом GetDifference - отдельные изображения, где изменения отмечены.

- Сравнить PDF с методом CompareDocumentsToPdf - PDF документ с изображениями, где изменения отмечены.

## Сравнение конкретных страниц

Первый фрагмент кода демонстрирует, как сравнить первые страницы двух PDF документов.

1. Инициализация документа.
Код начинается с инициализации двух PDF документов с использованием их соответствующих путей к файлам (documentPath1 и documentPath2). Пути в данный момент указаны как пустые строки, но на практике вы замените их на фактические пути к файлам.

2. Процесс сравнения.

- Выбор страниц - сравнение ограничивается первой страницей каждого документа ('Pages[1]').
- Опции сравнения:

'AdditionalChangeMarks = true' - эта опция гарантирует, что дополнительные маркеры изменений отображаются. Эти маркеры подчеркивают различия, которые могут присутствовать на других страницах, даже если они не находятся на текущей странице, которая сравнивается.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - этот режим говорит сравнивателю игнорировать пробелы в тексте, сосредоточившись только на изменениях внутри слов.

3. Результирующий документ сравнения, который подчеркивает различия между двумя страницами, сохраняется по пути файла, указанному в 'resultPdfPath'.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## Сравнение целых документов

Второй фрагмент кода расширяет область для сравнения всего содержимого двух PDF документов.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

Результаты сравнения, сгенерированные этими фрагментами кода, являются PDF документами, которые вы можете открыть в просмотрщике, таком как Adobe Acrobat. Если вы используете двухстраничный вид в Adobe Acrobat, вы увидите изменения рядом:

- Удаления - они отмечены на левой странице.
- Вставки - они отмечены на правой странице.

Установив 'AdditionalChangeMarks' в 'true', вы также можете увидеть маркеры для изменений, которые могут происходить на других страницах, даже если эти изменения не находятся на текущей странице, которую вы просматриваете.

**Aspose.PDF for .NET** предоставляет надежные инструменты для сравнения PDF документов, независимо от того, нужно ли вам сравнить конкретные страницы или целые документы. Используя такие опции, как 'AdditionalChangeMarks' и различные настройки 'ComparisonMode', вы можете адаптировать процесс сравнения под ваши конкретные нужды. Результирующий документ предоставляет четкий, боковой вид изменений, что упрощает отслеживание правок и обеспечивает точность документа.

## Сравнение PDF документов с использованием GraphicalPdfComparer

При сотрудничестве над документами, особенно в профессиональной среде, вы часто получаете несколько версий одного и того же файла.

Вы можете использовать класс [GraphicalPdfComparer](https://reference.aspose.com/pdf/ru/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/) для сравнения PDF документов и страниц. Класс подходит для сравнения изменений в графическом содержимом страницы.

С Aspose.PDF for .NET возможно сравнивать документы и страницы и выводить результат сравнения в PDF документ или файл изображения.

Вы можете установить следующие свойства класса:

- Разрешение - разрешение в единицах DPI для выходных изображений, а также для изображений, создаваемых во время сравнения.
- Цвет - цвет маркеров изменений.
- Порог - порог изменений в процентах. Значение по умолчанию равно нулю. Установка значения, отличного от нуля, позволяет игнорировать графические изменения, которые для вас незначительны.

Класс имеет метод, который позволяет получить различия изображений страниц в форме, подходящей для дальнейшей обработки: **ImagesDifference GetDifference(Page page1, Page page2)**.

Этот метод возвращает объект класса [ImagesDifference](https://reference.aspose.com/pdf/ru/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/), который содержит изображение первой сравниваемой страницы и массив различий. Массив различий и оригинальное изображение имеют формат пикселей **RGB24bpp**.

ImagesDifference позволяет вам сгенерировать другое изображение и получить изображение второй сравниваемой страницы, добавив массив различий к оригинальному изображению. Для этого используйте методы **ImagesDifference.GetDestinationImage и ImagesDifference.DifferenceToImage**.

### Сравнить PDF с методом GetDifference

Предоставленный код определяет метод [GetDifference](https://reference.aspose.com/pdf/ru/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods), который сравнивает два PDF документа и генерирует визуальные представления различий между ними.

Этот метод сравнивает первые страницы двух PDF файлов и генерирует два PNG изображения:

- Одно изображение (diffPngFilePath) подчеркивает различия между страницами красным цветом.
- Другое изображение (destPngFilePath) является визуальным представлением целевой (второй) страницы PDF.

Этот процесс может быть полезен для визуального сравнения изменений или различий между двумя версиями документа.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod2.pdf"))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
                }
            }
        }
    }
}
```

### Сравнить PDF с методом CompareDocumentsToPdf

Предоставленный фрагмент кода использует метод [CompareDocumentsToPdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/), который сравнивает два документа и генерирует PDF отчет о результатах сравнения.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```