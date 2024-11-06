---
title: Работа с действиями в PDF
linktitle: Действия
type: docs
weight: 20
url: ru/net/actions/
description: Этот раздел объясняет, как программно добавлять действия в документ и поля формы с помощью C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с действиями в PDF",
    "alternativeHeadline": "Как добавить действия в PDF",
    "author": {
        "@type": "Person",
        "name":"Андрий Андруховский",
        "givenName": "Андрий",
        "familyName": "Андруховский",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, действия в pdf",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел объясняет, как программно добавлять действия в документ и поля формы с помощью C#."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Добавление гиперссылки в файл PDF

Возможно добавить гиперссылки в файлы PDF, чтобы читатели могли переходить к другой части PDF или к внешнему контенту.

Для добавления веб-гиперссылок в документы PDF:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Получите класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page), на который вы хотите добавить ссылку.
1. Создайте объект [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation), используя объекты Page и [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle). Объект прямоугольника используется для указания местоположения на странице, где должна быть добавлена ссылка.
1. Установите свойство Action на объект [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction), который указывает местоположение удаленного URI.
1. Добавить свободный текст:

- Создайте объект [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation). Он также принимает объекты Page и Rectangle в качестве аргументов, так что можно указать те же значения, что и для конструктора LinkAnnotation.
- Используя свойство Contents объекта [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), укажите строку, которая должна отображаться в выходном PDF.
- При желании установите ширину границы объектов [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) и FreeTextAnnotation равной 0, чтобы они не отображались в документе PDF.
- После того как объекты [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) и [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) будут определены, добавьте эти ссылки в коллекцию Annotations объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- После того как объекты [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) и [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) были определены, добавьте эти ссылки в коллекцию аннотаций объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
- Наконец, сохраните обновленный PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Следующий фрагмент кода показывает, как добавить гиперссылку в файл PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Открыть документ
Document document = new Document(dataDir + "AddHyperlink.pdf");
// Создать ссылку
Page page = document.Pages[1];
// Создать объект аннотации ссылки
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// Создать объект границы для LinkAnnotation
Border border = new Border(link);
// Установить значение ширины границы как 0
border.Width = 0;
// Установить границу для LinkAnnotation
link.Border = border;
// Указать тип ссылки как удаленный URI
link.Action = new GoToURIAction("www.aspose.com");
// Добавить аннотацию ссылки в коллекцию аннотаций первой страницы файла PDF
page.Annotations.Add(link);

// Создать аннотацию свободного текста
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// Текст для добавления как свободный текст
textAnnotation.Contents = "Ссылка на сайт Aspose";
// Установить границу для аннотации свободного текста
textAnnotation.Border = border;
// Добавить аннотацию свободного текста в коллекцию аннотаций первой страницы документа
document.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddHyperlink_out.pdf";
// Сохранить обновленный документ
document.Save(dataDir);
```
## Создание гиперссылки на страницы в том же PDF

Aspose.PDF для .NET предоставляет отличные возможности для создания PDF, а также его манипуляции. Также предоставляется возможность добавления ссылок на страницы PDF, и ссылка может вести на страницы в другом файле PDF, веб-URL, запускать приложение или даже ссылаться на страницы в том же файле PDF. Для добавления локальных гиперссылок (ссылок на страницы в том же файле PDF) в пространство имен Aspose.PDF добавлен класс [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink), который имеет свойство с именем TargetPageNumber, используемое для указания целевой/назначаемой страницы для гиперссылки.

Для добавления локальной гиперссылки необходимо создать TextFragment, чтобы ссылка могла быть связана с TextFragment. Класс [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) имеет свойство с именем Hyperlink, которое используется для ассоциации экземпляра LocalHyperlink. Следующий фрагмент кода показывает шаги для выполнения этой задачи.

```csharp
```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Создать экземпляр документа
Document doc = new Document();
// Добавить страницу в коллекцию страниц PDF файла
Page page = doc.Pages.Add();
// Создать экземпляр текстового фрагмента
Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment("тест ссылки на страницу номер 7");
// Создать экземпляр локальной гиперссылки
Aspose.Pdf.LocalHyperlink link = new Aspose.Pdf.LocalHyperlink();
// Установить целевую страницу для экземпляра ссылки
link.TargetPageNumber = 7;
// Установить гиперссылку текстового фрагмента
text.Hyperlink = link;
// Добавить текст в коллекцию абзацев страницы
page.Paragraphs.Add(text);
// Создать новый экземпляр текстового фрагмента
text = new TextFragment("тест ссылки на страницу номер 1");
// Текстовый фрагмент должен быть добавлен на новую страницу
text.IsInNewPage = true;
// Создать другой экземпляр локальной гиперссылки
link = new LocalHyperlink();
// Установить целевую страницу для второй гиперссылки
link.TargetPageNumber = 1;
// Установить ссылку для второго текстового фрагмента
text.Hyperlink = link;
// Добавить текст в коллекцию абзацев объекта страницы
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateLocalHyperlink_out.pdf";
// Сохранить обновленный документ
doc.Save(dataDir);
```
## Получение URL-адреса гиперссылки в PDF

Ссылки представлены в виде аннотаций в PDF-файле, их можно добавлять, обновлять или удалять. Aspose.PDF для .NET также поддерживает получение адреса (URL) гиперссылки в PDF-файле.

Для получения URL-адреса ссылки:

1. Создайте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Получите [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page), с которой вы хотите извлечь ссылки.
1. Используйте класс [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) для извлечения всех объектов [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) с указанной страницы.
1. Передайте объект [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) методу Accept объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
1. Наконец, извлеките действие LinkAnnotation как GoToURIAction.

Следующий фрагмент кода показывает, как получить адреса гиперссылок (URL) из файла PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Загрузка файла PDF
Document document = new Document(dataDir + "input.pdf");

// Проходим через все страницы PDF
foreach (Aspose.Pdf.Page page in document.Pages)
{
    // Получаем аннотации ссылок с конкретной страницы
    AnnotationSelector selector = new AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // Создаем список, содержащий все ссылки
    IList<Annotation> list = selector.Selected;
    // Итерируем через каждый элемент в списке
    foreach (LinkAnnotation a in list)
    {
        // Выводим URL назначения
        Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
    }
}
```
## Получение текста гиперссылки

Гиперссылка состоит из двух частей: текст, который отображается в документе, и URL-адрес назначения. В некоторых случаях нам нужен именно текст, а не URL.

Текст и аннотации/действия в файле PDF представлены разными сущностями. Текст на странице - это просто набор слов и символов, в то время как аннотации приносят некоторую интерактивность, например, как в гиперссылке.

Чтобы найти содержимое URL, вам нужно работать как с аннотацией, так и с текстом. Объект [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) сам по себе не содержит текст, но располагается под текстом на странице. Так что для получения текста Annotation указывает границы URL, в то время как объект Text дает содержимое URL. Пожалуйста, смотрите следующий фрагмент кода.

```csharp
  {
        public static void Run()
        {
            try
            {
                // ExStart:GetHyperlinkText
                // Путь к директории документов.
                string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
                // Загрузить PDF-файл
                Document document = new Document(dataDir + "input.pdf");
                // Перебор каждой страницы PDF
                foreach (Page page in document.Pages)
                {
                    // Показать аннотацию ссылки
                    ShowLinkAnnotations(page);
                }
                // ExEnd:GetHyperlinkText
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
        // ExStart:ShowLinkAnnotations
        public static void ShowLinkAnnotations(Page page)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annot in page.Annotations)
            {
                if (annot is LinkAnnotation)
                {
                    // Вывести URL каждой аннотации ссылки
                    Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
                    TextAbsorber absorber = new TextAbsorber();
                    absorber.TextSearchOptions.LimitToPageBounds = true;
                    absorber.TextSearchOptions.Rectangle = annot.Rect;
                    page.Accept(absorber);
                    string extractedText = absorber.Text;
                    // Вывести текст, связанный с гиперссылкой
                    Console.WriteLine(extractedText);
                }

            }
        }
        // ExEnd:ShowLinkAnnotations
    }
}
```
## Удаление действия открытия документа из файла PDF

[Как указать страницу PDF при просмотре документа](#how-to-specify-pdf-page-when-viewing-document) объяснило, как настроить документ для открытия на другой странице, а не на первой. При объединении нескольких документов, если у одного или нескольких из них установлено действие GoTo, возможно, вы захотите их удалить. Например, если объединить два документа и второй имеет действие GoTo, которое переводит на вторую страницу, итоговый документ будет открываться на второй странице второго документа, а не на первой странице объединенного документа. Чтобы избежать этого поведения, удалите команду действия открытия.

Для удаления действия открытия:

1. Установите свойство [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) в значение null.
1. Сохраните обновленный PDF с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) объекта Document.

Следующий фрагмент кода показывает, как удалить действие открытия документа из файла PDF.
Следующий фрагмент кода показывает, как удалить действие открытия документа из файла PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Открыть документ
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// Удалить действие открытия документа
document.OpenAction = null;
dataDir = dataDir + "RemoveOpenAction_out.pdf";
// Сохранить обновленный документ
document.Save(dataDir);
```

## Как указать страницу PDF при просмотре документа {#how-to-specify-pdf-page-when-viewing-document}

При просмотре файлов PDF в таких PDF-просмотрщиках, как Adobe Reader, файлы обычно открываются на первой странице. Однако можно настроить файл так, чтобы он открывался на другой странице.

Класс [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) позволяет указать страницу в файле PDF, которую вы хотите открыть.
Класс [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) позволяет указать страницу в файле PDF, которую вы хотите открыть.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Загрузить файл PDF
Document doc = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// Получить экземпляр второй страницы документа
Page page2 = doc.Pages[2];
// Создать переменную для установки коэффициента масштабирования целевой страницы
double zoom = 1;
// Создать экземпляр GoToAction
GoToAction action = new GoToAction(doc.Pages[2]);
// Перейти на 2 страницу
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// Установить действие открытия документа
doc.OpenAction = action;
// Сохранить обновленный документ
doc.Save(dataDir + "goto2page_out.pdf");
```

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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
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

