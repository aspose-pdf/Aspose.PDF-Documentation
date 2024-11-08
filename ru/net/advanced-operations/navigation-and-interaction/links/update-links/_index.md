---
title: Обновление ссылок в PDF
linktitle: Обновление ссылок
type: docs
weight: 20
url: /ru/net/update-links/
description: Обновление ссылок в PDF программно. Это руководство о том, как обновить ссылки в PDF на языке C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Обновление ссылок в PDF",
    "alternativeHeadline": "Как обновить ссылки в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, обновление ссылок в pdf",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2022-02-04",
    "description": "Обновление ссылок в PDF программно. Это руководство о том, как обновить ссылки в PDF на языке C#."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Обновление ссылок в PDF файле

Как обсуждалось в разделе Добавление гиперссылки в PDF файл, класс [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) позволяет добавлять ссылки в PDF файл. Существует также похожий класс, используемый для получения существующих ссылок из PDF файлов. Используйте это, если вам нужно обновить существующую ссылку. Чтобы обновить существующую ссылку:

1. Загрузите PDF файл.
1. Перейдите на определенную страницу в PDF файле.
1. Укажите место назначения ссылки с помощью свойства Destination объекта [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction).
1. Страница назначения указывается с помощью конструктора [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination).

### Установка цели ссылки на страницу в том же документе

Следующий фрагмент кода показывает, как обновить ссылку в PDF файле и установить ее цель на вторую страницу документа.
Следующий фрагмент кода показывает, как обновить ссылку в файле PDF и установить её цель на вторую страницу документа.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Загрузить файл PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
// Получить первую аннотацию ссылки с первой страницы документа
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Модификация ссылки: изменение места назначения
GoToAction goToAction = (GoToAction)linkAnnot.Action;
// Указать место назначения для объекта ссылки
// Первый параметр - это объект документа, второй - номер страницы назначения.
// Пятый аргумент - это коэффициент масштабирования при отображении соответствующей страницы. При использовании 2 страница будет отображаться с увеличением 200%
goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);
dataDir = dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf";
// Сохранить документ с обновленной ссылкой
doc.Save(dataDir);
```
### Установить адрес ссылки на веб-адрес

Для обновления гиперссылки, чтобы она указывала на веб-адрес, создайте объект [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) и передайте его в свойство Action аннотации LinkAnnotation. Следующий фрагмент кода показывает, как обновить ссылку в файле PDF и установить ее целью веб-адрес.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Загрузить файл PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");

// Получить первую аннотацию ссылки с первой страницы документа
LinkAnnotation linkAnnot = (LinkAnnotation)doc.Pages[1].Annotations[1];
// Модификация ссылки: изменить действие ссылки и установить целью веб-адрес
linkAnnot.Action = new GoToURIAction("www.aspose.com");

dataDir = dataDir + "SetDestinationLink_out.pdf";
// Сохранить документ с обновленной ссылкой
doc.Save(dataDir);
```
### Установить цель ссылки на другой PDF-файл

Следующий фрагмент кода показывает, как обновить ссылку в PDF-файле и установить её цель на другой PDF-файл.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Загрузить PDF-файл
Document document = new Document(dataDir + "UpdateLinks.pdf");

LinkAnnotation linkAnnot = (LinkAnnotation)document.Pages[1].Annotations[1];

GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.Action;
// Следующая строка обновляет назначение, не обновляйте файл
goToR.Destination = new XYZExplicitDestination(2, 0, 0, 1.5);
// Следующая строка обновляет файл
goToR.File = new FileSpecification(dataDir +  "input.pdf");

dataDir = dataDir + "SetTargetLink_out.pdf";
// Сохранить документ с обновленной ссылкой
document.Save(dataDir);
```

### Обновить цвет текста LinkAnnotation

Аннотация ссылки не содержит текста.
Аннотация ссылки не содержит текста.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Загрузка файла PDF
Document doc = new Document(dataDir + "UpdateLinks.pdf");
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    if (annotation is LinkAnnotation)
    {
        // Поиск текста под аннотацией
        TextFragmentAbsorber ta = new TextFragmentAbsorber();
        Rectangle rect = annotation.Rect;
        rect.LLX -= 10;
        rect.LLY -= 10;
        rect.URX += 10;
        rect.URY += 10;
        ta.TextSearchOptions = new TextSearchOptions(rect);
        ta.Visit(doc.Pages[1]);
        // Изменение цвета текста.
        foreach (TextFragment tf in ta.TextFragments)
        {
            tf.TextState.ForegroundColor = Color.Red;
        }
    }

}
dataDir = dataDir + "UpdateLinkTextColor_out.pdf";
// Сохранение документа с обновленной ссылкой
doc.Save(dataDir);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки .NET",
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
                "contactType": "продажи",
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
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
```

