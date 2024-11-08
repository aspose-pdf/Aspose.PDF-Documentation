 ---
title: Форматирование документа PDF с использованием C#
linktitle: Форматирование документа PDF
type: docs
weight: 11
url: /ru/net/formatting-pdf-document/
description: Создайте и отформатируйте документ PDF с помощью Aspose.PDF для .NET. Используйте следующий фрагмент кода для решения ваших задач.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Форматирование документа PDF с использованием C#",
    "alternativeHeadline": "Как отформатировать документ PDF в .NET",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, dotnet, форматирование документов pdf",
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
    "url": "/net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/formatting-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Создайте и отформатируйте документ PDF с помощью Aspose.PDF для .NET. Используйте следующий фрагмент кода для решения ваших задач."
}
</script>
## Форматирование PDF документа

### Получение свойств окна документа и отображения страниц

Эта тема поможет вам понять, как получить свойства окна документа, приложения для просмотра и как отображаются страницы. Для установки этих свойств:

Откройте PDF файл с помощью класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Теперь вы можете установить свойства объекта Document, такие как

- CenterWindow – Центрировать окно документа на экране. По умолчанию: false.
- Direction – Порядок чтения. Определяет, как страницы располагаются при их отображении рядом. По умолчанию: слева направо.
- DisplayDocTitle – Отображать название документа в заголовке окна документа. По умолчанию: false (название отображается).
- HideMenuBar – Скрыть или отобразить строку меню окна документа. По умолчанию: false (строка меню отображается).
- HideToolBar – Скрыть или отобразить панель инструментов окна документа. По умолчанию: false (панель инструментов отображается).
- HideWindowUI – Скрыть или отобразить элементы окна документа, такие как полосы прокрутки.
- HideWindowUI – Скрыть или отобразить элементы окна документа, такие как полосы прокрутки.
- NonFullScreenPageMode – Как отображается документ, когда он не показан в полностраничном режиме.
- PageLayout – Макет страницы.
- PageMode – Как документ отображается при первом открытии. Варианты: показать миниатюры, полноэкранный режим, показать панель вложений.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Следующий фрагмент кода показывает, как получить свойства с использованием класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetDocumentWindow.pdf");

// Получить различные свойства документа
// Позиция окна документа - по умолчанию: false
Console.WriteLine("CenterWindow : {0}", pdfDocument.CenterWindow);
  
// Преобладающий порядок чтения; определяет позицию страницы
// При отображении бок о бок - по умолчанию: L2R
Console.WriteLine("Direction : {0}", pdfDocument.Direction);

// Должна ли строка заголовка окна отображать название документа
// Если false, строка заголовка отображает имя файла PDF - по умолчанию: false
Console.WriteLine("DisplayDocTitle : {0}", pdfDocument.DisplayDocTitle);

// Должно ли окно документа изменять размер для соответствия размеру
// Первой отображаемой страницы - по умолчанию: false
Console.WriteLine("FitWindow : {0}", pdfDocument.FitWindow);

// Скрыть ли меню бар приложения просмотра - по умолчанию: false
Console.WriteLine("HideMenuBar : {0}", pdfDocument.HideMenubar);

// Скрыть ли панель инструментов приложения просмотра - по умолчанию: false
Console.WriteLine("HideToolBar : {0}", pdfDocument.HideToolBar);

// Скрыть ли элементы пользовательского интерфейса, такие как полосы прокрутки
// И оставить только содержимое страницы - по умолчанию: false
Console.WriteLine("HideWindowUI : {0}", pdfDocument.HideWindowUI);

// Режим страницы документа. Как отображать документ при выходе из полноэкранного режима.
Console.WriteLine("NonFullScreenPageMode : {0}", pdfDocument.NonFullScreenPageMode);

// Макет страницы, например, одна страница, одна колонка
Console.WriteLine("PageLayout : {0}", pdfDocument.PageLayout);

// Как должен отображаться документ при открытии
// Например, показать миниатюры, полноэкранный режим, показать панель вложений
Console.WriteLine("pageMode : {0}", pdfDocument.PageMode);
```
### Настройка свойств окна документа и отображения страницы

Эта тема объясняет, как настроить свойства окна документа, приложения для просмотра и отображения страницы. Для настройки этих различных свойств:

1. Откройте PDF-файл с помощью класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Установите свойства объекта Document.
1. Сохраните обновленный PDF-файл с помощью метода Save.

Доступные свойства:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Каждое свойство используется и описывается в приведенном ниже коде. Следующий фрагмент кода показывает, как настроить свойства с помощью класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SetDocumentWindow.pdf");

// Установить различные свойства документа
// Указать позицию окна документа - По умолчанию: false
pdfDocument.CenterWindow = true;

// Преобладающий порядок чтения; определяет позицию страницы
// При отображении бок о бок - По умолчанию: L2R
pdfDocument.Direction = Direction.R2L;

// Указать, должна ли строка заголовка окна отображать название документа
// Если false, в строке заголовка отображается имя файла PDF - По умолчанию: false
pdfDocument.DisplayDocTitle = true;

// Указать, следует ли изменить размер окна документа для соответствия размеру
// Первой отображаемой страницы - По умолчанию: false
pdfDocument.FitWindow = true;

// Указать, следует ли скрыть строку меню приложения для просмотра - По умолчанию: false
pdfDocument.HideMenubar = true;

// Указать, следует ли скрыть панель инструментов приложения для просмотра - По умолчанию: false
pdfDocument.HideToolBar = true;

// Указать, следует ли скрыть элементы пользовательского интерфейса, такие как полосы прокрутки
// И оставить отображаемым только содержимое страницы - По умолчанию: false
pdfDocument.HideWindowUI = true;

// Режим страницы документа. Указывает, как отображать документ при выходе из полноэкранного режима.
pdfDocument.NonFullScreenPageMode = PageMode.UseOC;

// Указать макет страницы, т.е. одна страница, один столбец
pdfDocument.PageLayout = PageLayout.TwoColumnLeft;

// Указать, как должен отображаться документ при открытии
// Т.е. показать эскизы, полноэкранный режим, показать панель вложений
pdfDocument.PageMode = PageMode.UseThumbs;

dataDir = dataDir + "SetDocumentWindow_out.pdf";
// Сохранить обновленный PDF файл
pdfDocument.Save(dataDir);
```
### Встраивание шрифтов в существующий файл PDF

PDF-читатели поддерживают [ядро из 14 шрифтов](https://en.wikipedia.org/wiki/PDF#Text), чтобы документы отображались одинаково независимо от платформы, на которой они просматриваются. Когда PDF содержит шрифт, который не является одним из 14 основных шрифтов, встройте шрифт в файл PDF, чтобы избежать замены шрифта.

Aspose.PDF для .NET поддерживает встраивание шрифтов в существующие файлы PDF. Вы можете встроить полный шрифт или его подмножество. Чтобы встроить шрифт, откройте файл PDF с использованием класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Затем используйте класс [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/net/aspose.pdf.text), чтобы встроить шрифт в файл PDF. Чтобы встроить полный шрифт, используйте свойство IsEmbeded класса Font; для использования подмножества шрифта используйте свойство IsSubset.

{{% alert color="primary" %}}

Подмножество шрифта встраивает только используемые символы и полезно там, где шрифты используются для коротких фраз или слоганов, например, когда корпоративный шрифт используется для логотипа, но не для основного текста.
Подмножество шрифтов встраивает только используемые символы и является полезным в случаях, когда шрифты используются для коротких предложений или слоганов, например, когда корпоративный шрифт используется для логотипа, но не для основного текста.

{{% /alert %}}

Следующий фрагмент кода показывает, как встроить шрифт в файл PDF.

### Встраивание стандартных шрифтов Type 1

Некоторые документы PDF содержат шрифты из специального набора Adobe. Шрифты из этого набора называются "Стандартные шрифты Type 1". Этот набор включает 14 шрифтов, и встраивание таких шрифтов требует использования специальных флагов, например [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/embedstandardfonts). Ниже приведен фрагмент кода, который можно использовать для получения документа со всеми встроенными шрифтами, включая стандартные шрифты Type 1:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Загрузка существующего документа PDF
Document pdfDocument = new Document(dataDir + "input.pdf");
// Установка свойства EmbedStandardFonts документа
pdfDocument.EmbedStandardFonts = true;
foreach (Aspose.Pdf.Page page in pdfDocument.Pages)
{
    if (page.Resources.Fonts != null)
    {
        foreach (Aspose.Pdf.Text.Font pageFont in page.Resources.Fonts)
        {
// Проверка, встроен ли уже шрифт
if (!pageFont.IsEmbedded)
{
    pageFont.IsEmbedded = true;
}
        }
    }
}
pdfDocument.Save(dataDir + "EmbeddedFonts-updated_out.pdf");
```
### Встраивание шрифтов при создании PDF

Если вам нужно использовать шрифт, отличный от 14 базовых шрифтов, поддерживаемых Adobe Reader, вы должны встроить описание шрифта при генерации файла Pdf. Если информация о шрифте не встроена, Adobe Reader возьмет её из операционной системы, если она установлена в системе, или создаст замещающий шрифт в соответствии с дескриптором шрифта в Pdf.

>Обратите внимание, что встроенный шрифт должен быть установлен на хост-машине, т.е. в случае следующего кода шрифт ‘Univers Condensed’ установлен в системе.

Мы используем свойство IsEmbedded класса Font для встраивания информации о шрифте в файл Pdf. Установка значения этого свойства в ‘True’ встроит полный файл шрифта в Pdf, учитывая, что это увеличит размер файла Pdf. Ниже приведен фрагмент кода, который можно использовать для встраивания информации о шрифте в Pdf.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создание объекта Pdf путем вызова его пустого конструктора
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();

// Создание раздела в объекте Pdf
Aspose.Pdf.Page page = doc.Pages.Add();

Aspose.Pdf.Text.TextFragment fragment = new Aspose.Pdf.Text.TextFragment("");

Aspose.Pdf.Text.TextSegment segment = new Aspose.Pdf.Text.TextSegment(" Это образец текста с использованием пользовательского шрифта.");
Aspose.Pdf.Text.TextState ts = new Aspose.Pdf.Text.TextState();
ts.Font = FontRepository.FindFont("Arial");
ts.Font.IsEmbedded = true;
segment.TextState = ts;
fragment.Segments.Add(segment);
page.Paragraphs.Add(fragment);

dataDir = dataDir + "EmbedFontWhileDocCreation_out.pdf";
// Сохранение документа PDF
doc.Save(dataDir);
```
### Установка имени шрифта по умолчанию при сохранении в PDF

Когда документ PDF содержит шрифты, которые недоступны в самом документе и на устройстве, API заменяет эти шрифты шрифтом по умолчанию. Когда шрифт доступен (установлен на устройстве или встроен в документ), выходной PDF должен использовать тот же шрифт (не должен быть заменен на шрифт по умолчанию). Значение шрифта по умолчанию должно содержать имя шрифта (не путь к файлам шрифта). Мы реализовали функцию установки имени шрифта по умолчанию при сохранении документа в формате PDF. Следующий фрагмент кода может быть использован для установки шрифта по умолчанию:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
// Загрузка существующего PDF-документа с отсутствующим шрифтом
string documentName = dataDir + "input.pdf";
string newName = "Arial";
using (System.IO.FileStream fs = new System.IO.FileStream(documentName, System.IO.FileMode.Open))
using (Document document = new Document(fs))
{
    PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();
    // Указание имени шрифта по умолчанию
    pdfSaveOptions.DefaultFontName = newName;
    document.Save(dataDir + "output_out.pdf", pdfSaveOptions);
}
```
### Получение всех шрифтов из PDF-документа

Если вы хотите получить все шрифты из PDF-документа, вы можете использовать метод FontUtilities.GetAllFonts(), предоставленный в классе [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Пожалуйста, проверьте следующий фрагмент кода, чтобы получить все шрифты из существующего PDF-документа:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

### Получение предупреждений о замене шрифтов

Aspose.PDF для .NET предоставляет методы для получения уведомлений о замене шрифтов для обработки случаев замены шрифтов. Ниже приведены фрагменты кода, которые показывают, как использовать соответствующую функциональность.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

Document doc = new Document(dataDir + "input.pdf");

doc.FontSubstitution += new Document.FontSubstitutionHandler(OnFontSubstitution);
```
**Метод OnFontSubstitution** перечислен ниже.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Console.WriteLine(string.Format("Шрифт '{0}' был заменен другим шрифтом '{1}'",
oldFont.FontName, newFont.FontName));
```

### Улучшение встраивания шрифтов с использованием FontSubsetStrategy

Возможность встраивания шрифтов как подмножества может быть достигнута с использованием свойства IsSubset, но иногда вы хотите уменьшить полностью встроенный набор шрифтов до только подмножеств, используемых в документе. У Aspose.Pdf.Document есть свойство FontUtilities, которое включает метод SubsetFonts(FontSubsetStrategy subsetStrategy). В методе SubsetFonts(), параметр subsetStrategy помогает настроить стратегию подмножества. FontSubsetStrategy поддерживает два следующих варианта подмножества шрифтов.

- SubsetAllFonts - Это будет подмножество всех шрифтов, используемых в документе.
- SubsetEmbeddedFontsOnly - Это будет подмножество только тех шрифтов, которые полностью встроены в документ.

Следующий фрагмент кода показывает, как установить FontSubsetStrategy:
Следующий фрагмент кода показывает, как установить FontSubsetStrategy:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
// Все шрифты будут встроены как подмножество в документ в случае SubsetAllFonts.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetAllFonts);
// Подмножество шрифтов будет встроено для полностью встроенных шрифтов, но шрифты, которые не встроены в документ, не будут затронуты.
doc.FontUtilities.SubsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
doc.Save(dataDir + "Output_out.pdf");
```

### Получение и установка коэффициента масштабирования файла PDF

Иногда вам может понадобиться определить текущий коэффициент масштабирования документа PDF. С помощью Aspose.Pdf вы можете узнать текущее значение, а также установить его.

Свойство Destination класса [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) позволяет получить значение масштабирования, связанное с файлом PDF.
Свойство Destination класса [GoToAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotoaction) позволяет получить значение увеличения, связанное с файлом PDF.

#### Установить коэффициент масштабирования

Следующий фрагмент кода показывает, как установить коэффициент масштабирования файла PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создать новый объект Document
Document doc = new Document(dataDir + "SetZoomFactor.pdf");

GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0, 0, .5));
doc.OpenAction = action;
dataDir = dataDir + "Zoomed_pdf_out.pdf";
// Сохранить документ
doc.Save(dataDir);
```

#### Получить коэффициент масштабирования

Следующий фрагмент кода показывает, как получить коэффициент масштабирования файла PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создать новый объект Document
Document doc = new Document(dataDir + "Zoomed_pdf.pdf");

// Создать объект GoToAction
GoToAction action = doc.OpenAction as GoToAction;

// Получить коэффициент масштабирования файла PDF
System.Console.WriteLine((action.Destination as XYZExplicitDestination).Zoom); // Значение увеличения документа;
```
### Настройка свойств предустановок диалога печати

Aspoose.PDF позволяет настраивать свойства предустановок диалога печати документа PDF. Вы можете изменить свойство DuplexMode для документа PDF, которое по умолчанию установлено как simplex. Это можно сделать двумя различными методами, как показано ниже.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

using (Document doc = new Document())
{
    doc.Pages.Add();
    doc.Duplex = PrintDuplex.DuplexFlipLongEdge;
    doc.Save(dataDir + "35297_out.pdf", SaveFormat.Pdf);
}
```

### Настройка свойств предустановок диалога печати с использованием редактора содержимого PDF

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

string outputFile = dataDir + "input.pdf";
using (PdfContentEditor ed = new PdfContentEditor())
{
    ed.BindPdf(outputFile);
    if ((ed.GetViewerPreference() & ViewerPreference.DuplexFlipShortEdge) > 0)
    {
        Console.WriteLine("Файл имеет двустороннюю короткую кромку");
    }

    ed.ChangeViewerPreference(ViewerPreference.DuplexFlipShortEdge);
    ed.Save(dataDir + "SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
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
    "applicationCategory": "Библиотека для работы с PDF в .NET",
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

