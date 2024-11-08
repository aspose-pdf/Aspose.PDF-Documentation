---
title: Использование текстовой аннотации для PDF
linktitle: Текстовая аннотация
type: docs
weight: 10
url: /ru/net/text-annotation/
description: Aspose.PDF для .NET позволяет добавлять, получать и удалять текстовую аннотацию из вашего PDF документа.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Использование текстовой аннотации для PDF",
    "alternativeHeadline": "Как добавить текстовую аннотацию в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, c#, текстовая аннотация",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для .NET позволяет добавлять, получать и удалять текстовую аннотацию из вашего PDF документа."
}
</script>
## Как добавить текстовую аннотацию в существующий PDF-файл

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Текстовая аннотация - это аннотация, прикрепленная к определенному месту в документе PDF. Когда закрыта, аннотация отображается в виде иконки; когда открыта, должно отображаться всплывающее окно, содержащее текст заметки выбранным читателем шрифтом и размером.

Аннотации содержатся в коллекции [Annotations](https://reference.aspose.com/pdf/net/aspose.pdf.annotations) определенной страницы. Эта коллекция содержит аннотации только для этой конкретной страницы; каждая страница имеет свою собственную коллекцию Annotations.

Чтобы добавить аннотацию на определенную страницу, добавьте ее в коллекцию Annotations этой страницы с помощью метода [Add](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection/methods/add).

1. Сначала создайте аннотацию, которую хотите добавить в PDF.
1. Затем откройте входной PDF.
1.
1.

Следующий пример кода показывает, как добавить аннотацию на страницу PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Открыть документ
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");

// Создать аннотацию
TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
textAnnotation.Title = "Название аннотации";
textAnnotation.Subject = "Тема";
textAnnotation.State = AnnotationState.Accepted;
textAnnotation.Contents = "Пример содержимого для аннотации";
textAnnotation.Open = true;
textAnnotation.Icon = TextIcon.Key;

Border border = new Border(textAnnotation);
border.Width = 5;
border.Dash = new Dash(1, 1);
textAnnotation.Border = border;
textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

// Добавить аннотацию в коллекцию аннотаций страницы
pdfDocument.Pages[1].Annotations.Add(textAnnotation);
dataDir = dataDir + "AddAnnotation_out.pdf";
// Сохранить выходной файл
pdfDocument.Save(dataDir);
```
## Как добавить аннотацию всплывающего окна

Аннотация всплывающего окна отображает текст во всплывающем окне для ввода и редактирования. Она не должна появляться сама по себе, а должна быть связана с аннотацией разметки, своей родительской аннотацией, и должна использоваться для редактирования текста родителя.

Она не должна иметь собственного потока внешнего вида или связанных действий и должна быть идентифицирована по записи Popup в словаре аннотаций родителя.

Следующий фрагмент кода показывает, как добавить [Аннотацию всплывающего окна](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) на страницу PDF с использованием примера добавления родительской [Аннотации линии](/pdf/ru/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file).

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // Путь к каталогу документов.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // Загрузить файл PDF
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // Создать аннотацию линии
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "Джон Смит",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // Добавить аннотацию на страницу
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```

## Как добавить (или создать) новую аннотацию свободного текста

Аннотация свободного текста отображает текст непосредственно на странице. Метод [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) позволяет создавать этот тип аннотации. В следующем фрагменте мы добавляем аннотацию свободного текста над первым вхождением строки.

```csharp
private static void AddFreeTextAnnotationDemo()
{
    _document = new Document(@"C:\tmp\pdf-sample.pdf");
    var pdfContentEditor = new PdfContentEditor(_document);

    tfa.Visit(_document.Pages[1]);
    if (tfa.TextFragments.Count <= 0) return;
    var rect = new System.Drawing.Rectangle
    {
        X = (int)tfa.TextFragments[1].Rectangle.LLX,
        Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
        Height = 18,
        Width = 100
    };

    pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // последний параметр - номер страницы
    pdfContentEditor.Save(@"C:\tmp\pdf-sample-0.pdf");
}
```

### Установить свойство Callout для FreeTextAnnotation
### Установка свойства Callout для FreeTextAnnotation

Для более гибкой настройки аннотации в PDF-документе, Aspose.PDF для .NET предоставляет свойство [Callout](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation/properties/callout) класса [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation), которое позволяет указывать массив точек линии выноски. Следующий фрагмент кода показывает, как использовать эту функциональность:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Document doc = new Document();
Page page = doc.Pages.Add();
DefaultAppearance da = new DefaultAppearance();
da.TextColor = System.Drawing.Color.Red;
da.FontSize = 10;
FreeTextAnnotation fta = new FreeTextAnnotation(page, new Rectangle(422.25, 645.75, 583.5, 702.75), da);
fta.Intent = FreeTextIntent.FreeTextCallout;
fta.EndingStyle = LineEnding.OpenArrow;
fta.Callout = new Point[]
{
    new Point(428.25,651.75), new Point(462.75,681.375), new Point(474,681.375)
};
page.Annotations.Add(fta);
fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">Это образец</span></p></body>";
doc.Save(dataDir + "SetCalloutProperty.pdf");
```
### Установка свойства Callout для файла XFDF

Если вы используете импорт из файла XFDF, пожалуйста, используйте имя callout-line вместо простого Callout. Следующий пример кода показывает, как использовать эту функциональность:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document pdfDocument = new Document(dataDir + "AddAnnotation.pdf");
StringBuilder Xfdf = new StringBuilder();
Xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");
CreateXfdf(ref Xfdf);
Xfdf.AppendLine("</annots></xfdf>");
pdfDocument.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(Xfdf.ToString())));
pdfDocument.Save(dataDir + "SetCalloutPropertyXFDF.pdf");
```

Следующий метод используется для создания XFDF:

```csharp
/// <summary>
/// Создать XFDF
/// </summary>
/// <param name="pXfdf"></param>

static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">Это пример</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```
### Сделать текстовую аннотацию невидимой

Иногда необходимо создать водяной знак, который не виден в документе при его просмотре, но должен быть видим при печати. Для этого используйте флаги аннотаций. Следующий фрагмент кода показывает как это сделать.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Открыть документ
Document doc = new Document(dataDir + "input.pdf");

FreeTextAnnotation annotation = new FreeTextAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(50, 600, 250, 650), new DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red));
annotation.Contents = "ABCDEFG";
annotation.Characteristics.Border = System.Drawing.Color.Red;
annotation.Flags = AnnotationFlags.Print | AnnotationFlags.NoView;
doc.Pages[1].Annotations.Add(annotation);

dataDir = dataDir + "InvisibleAnnotation_out.pdf";
// Сохранить выходной файл
doc.Save(dataDir);
```
### Форматирование свободного текста в аннотации

Эта часть рассматривает форматирование текста в аннотации свободного текста.

Аннотации содержатся в коллекции [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). При добавлении [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) в документ PDF, вы можете указать информацию о форматировании, такую как шрифт, размер, цвет и т.д., используя класс [DefaultAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/defaultappearance/methods/index). Также возможно указать информацию о форматировании с помощью свойства TextStyle. Кроме того, вы можете обновить форматирование любой FreeTextAnnotation, уже находящейся в документе PDF.

Класс [TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) поддерживает работу с стандартной записью стиля.
[TextStyle](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/textstyle) класс поддерживает работу со стандартным стилем.

- Свойство FontName получает или устанавливает название шрифта (string).
- Свойство FontSize получает и устанавливает стандартный размер текста (double).
- Свойство System.Drawing.Color получает и устанавливает цвет текста (color).
- Свойство TextAlignment получает и устанавливает выравнивание текста аннотации (alignment).

Следующий фрагмент кода показывает, как добавить FreeTextAnnotation с определенным форматированием текста.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-SetFreeTextAnnotationFormatting-SetFreeTextAnnotationFormatting.cs" >}}

{{% alert color="primary" %}}

Когда вы изменяете содержимое или стиль текста свободной текстовой аннотации, внешний вид аннотации регенерируется, чтобы отразить изменения.

{{% /alert %}}

### Зачеркивание слов с помощью StrikeOutAnnotation

Aspose.PDF для .NET позволяет добавлять, удалять и обновлять аннотации в PDF документах.
Aspose.PDF для .NET позволяет добавлять, удалять и обновлять аннотации в документах PDF.

Для зачеркивания определенного TextFragment:

1. Найти TextFragment в файле PDF.
1. Получить координаты объекта TextFragment.
1. Использовать координаты для создания объекта StrikeOutAnnotation.

Следующий фрагмент кода показывает, как найти конкретный TextFragment и добавить к этому объекту StrikeOutAnnotation.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Annotations-StrikeOutWords-StrikeOutWords.cs" >}}

{{% alert color="primary" %}}

Эта функция поддерживается начиная с версии 19.6 или выше.

{{% /alert %}}

## Удалить все аннотации со страницы PDF файла

Коллекция [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) содержит все аннотации для этой конкретной страницы.
Объект [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) содержит коллекцию [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection), которая включает все аннотации данной страницы.

Следующий фрагмент кода показывает, как удалить все аннотации с конкретной страницы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Открыть документ
Document pdfDocument = new Document(dataDir + "DeleteAllAnnotationsFromPage.pdf");

// Удалить конкретную аннотацию
pdfDocument.Pages[1].Annotations.Delete();

dataDir = dataDir + "DeleteAllAnnotationsFromPage_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```

## Удаление конкретной аннотации из PDF файла

{{% alert color="primary" %}}

Вы можете проверить качество Aspose.PDF и получить результаты онлайн по этой ссылке:
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF позволяет удалять конкретную аннотацию из файла PDF. Эта тема объясняет как это сделать.

Для удаления конкретной аннотации из PDF вызовите [метод Delete коллекции AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations.annotationcollection/delete/methods/1). Эта коллекция принадлежит объекту [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page). Метод Delete требует указания индекса аннотации, которую вы хотите удалить. Затем сохраните обновленный файл PDF. Следующий фрагмент кода показывает, как удалить конкретную аннотацию.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Открыть документ
Document pdfDocument = new Document(dataDir + "DeleteParticularAnnotation.pdf");

// Удалить конкретную аннотацию
pdfDocument.Pages[1].Annotations.Delete(1);

dataDir = dataDir + "DeleteParticularAnnotation_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```
## Получение всех аннотаций со страницы PDF-документа

Aspose.PDF позволяет получать аннотации из всего документа или с конкретной страницы. Чтобы получить все аннотации со страницы в PDF-документе, переберите коллекцию [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) ресурсов желаемой страницы. Следующий фрагмент кода показывает, как получить все аннотации страницы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetAllAnnotationsFromPage.pdf");

// Перебрать все аннотации
foreach (MarkupAnnotation annotation in pdfDocument.Pages[1].Annotations)
{
    // Получить свойства аннотации
    Console.WriteLine("Название : {0} ", annotation.Title);
    Console.WriteLine("Тема : {0} ", annotation.Subject);
    Console.WriteLine("Содержание : {0} ", annotation.Contents);
}
```
Обратите внимание, что для получения всех аннотаций из всего PDF-документа необходимо пройти через коллекцию класса PageCollection, прежде чем переходить к коллекции класса AnnotationCollection. Вы можете получить каждую аннотацию коллекции в базовом типе аннотации, называемом классом MarkupAnnotation, а затем показать его свойства.

## Получение конкретной аннотации из PDF-файла

Аннотации связаны с отдельными страницами и хранятся в коллекции [AnnotationCollection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).
Аннотации связаны с отдельными страницами и хранятся в коллекции [AnnotationCOllection](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationcollection) объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetParticularAnnotation.pdf");

// Получить конкретную аннотацию
TextAnnotation textAnnotation = (TextAnnotation)pdfDocument.Pages[1].Annotations[1];

// Получить свойства аннотации
Console.WriteLine("Название : {0} ", textAnnotation.Title);
Console.WriteLine("Тема : {0} ", textAnnotation.Subject);
Console.WriteLine("Содержание : {0} ", textAnnotation.Contents);
```

## Получение ресурса аннотации

Aspose.PDF позволяет получать ресурс аннотации из всего документа или с конкретной страницы.
Aspose.PDF позволяет получить ресурс аннотации из всего документа или с конкретной страницы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Открыть документ
Document doc = new Document(dataDir + "AddAnnotation.pdf");
// Создать аннотацию
ScreenAnnotation sa = new ScreenAnnotation(doc.Pages[1], new Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
doc.Pages[1].Annotations.Add(sa);
// Сохранить документ
doc.Save(dataDir + "GetResourceOfAnnotation_Out.pdf");

// Открыть документ
Document doc1 = new Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

// Получить действие аннотации
RenditionAction action = (doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction;

// Получить рендишн (видео-сценарий) из действия рендишн
Rendition rendition = ((doc.Pages[1].Annotations[1] as ScreenAnnotation).Action as RenditionAction).Rendition;

// Медиа клип
MediaClip clip = (rendition as MediaRendition).MediaClip;
FileSpecification data = (clip as MediaClipData).Data;
MemoryStream ms = new MemoryStream();
byte[] buffer = new byte[1024];
int read = 0;
// Данные медиа доступны в FileSpecification.Contents
Stream source = data.Contents;
while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
{
    ms.Write(buffer, 0, read);
}
Console.WriteLine(rendition.Name);
Console.WriteLine(action.RenditionOperation);
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET библиотеки",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
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

