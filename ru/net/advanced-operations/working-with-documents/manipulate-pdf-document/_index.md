---
title: Манипулирование документом PDF в C#
linktitle: Манипулирование документом PDF
type: docs
weight: 20
url: /ru/net/manipulate-pdf-document/
description: Эта статья содержит информацию о том, как проверить документ PDF на соответствие стандарту PDF A, как работать с оглавлением, как установить срок действия PDF и т.д.
keywords: "manipulate pdf c#"
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Манипулирование документом PDF",
    "alternativeHeadline": "Как манипулировать файлом PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, dotnet, manipulate pdf file",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья содержит информацию о том, как проверить документ PDF на соответствие стандарту PDF A, как работать с оглавлением, как установить срок действия PDF и т.д."
}
</script>
## **Работа с PDF документами в C#**

## Проверка PDF документа на соответствие стандарту PDF A (A 1A и A 1B)

Для проверки PDF документа на соответствие стандартам PDF/A-1a или PDF/A-1b используйте метод Validate класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Этот метод позволяет указать имя файла, в котором будет сохранен результат, и требуемый тип валидации, перечисление [PdfFormat](https://reference.aspose.com/pdf/net/aspose.pdf/pdfformat): PDF_A_1A или PDF_A_1B.

{{% alert color="primary" %}}

Выходной формат XML - это пользовательский формат Aspose. XML содержит коллекцию тегов с названием Problem; каждый тег содержит детали конкретной проблемы. Атрибут ObjectID тега Problem представляет собой ID конкретного объекта, с которым связана эта проблема. Атрибут Clause представляет соответствующее правило в спецификации PDF.

{{% /alert %}}

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Следующий фрагмент кода показывает, как проверить PDF документ на соответствие PDF/A-1A.
Следующий фрагмент кода показывает, как проверить документ PDF на соответствие PDF/A-1A.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Проверка PDF на соответствие PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);
```

Следующий фрагмент кода показывает, как проверить документ PDF на соответствие PDF/A-1b.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Проверка PDF на соответствие PDF/A-1b
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```
{{% alert color="primary" %}}

Aspose.PDF для .NET может использоваться для определения, является ли загруженный документ действительным PDF, а также [зашифрован он или нет](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/). Для дальнейшего расширения возможностей класса Document, было добавлено свойство *IsPdfaCompliant*, позволяющее определить соответствие входного файла PDF/A, и свойство *PdfaFormat*, для идентификации формата PDF/A.

{{% /alert %}}

## Работа с оглавлением

### Добавление оглавления в существующий PDF

API Aspose.PDF позволяет добавлять оглавление при создании PDF или в существующий файл. Класс ListSection в пространстве имен Aspose.Pdf.Generator позволяет создавать оглавление при создании PDF с нуля. Для добавления заголовков, которые являются элементами оглавления, используйте класс Aspose.Pdf.Generator.Heading.

Чтобы добавить оглавление в существующий файл PDF, используйте класс Heading в пространстве имен Aspose.Pdf.
Чтобы добавить оглавление в существующий PDF-файл, используйте класс Heading в пространстве имен Aspose.Pdf.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Загрузить существующий PDF-файл
Document doc = new Document(dataDir + "AddTOC.pdf");

// Получить доступ к первой странице PDF-файла
Page tocPage = doc.Pages.Insert(1);

// Создать объект для представления информации оглавления
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Содержание");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;

// Установить заголовок для оглавления
tocInfo.Title = title;
tocPage.TocInfo = tocInfo;

// Создать строковые объекты, которые будут использоваться как элементы оглавления
string[] titles = new string[4];
titles[0] = "Первая страница";
titles[1] = "Вторая страница";
titles[2] = "Третья страница";
titles[3] = "Четвертая страница";
for (int i = 0; i < 2; i++)
{
    // Создать объект Heading
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);

    // Указать целевую страницу для объекта заголовка
    heading2.DestinationPage = doc.Pages[i + 2];

    // Целевая страница
    heading2.Top = doc.Pages[i + 2].Rect.Height;

    // Целевая координата
    segment2.Text = titles[i];

    // Добавить заголовок на страницу, содержащую оглавление
    tocPage.Paragraphs.Add(heading2);
}
dataDir = dataDir + "TOC_out.pdf";
// Сохранить обновленный документ
doc.Save(dataDir);
```
### Установка различных типов TabLeaderType для разных уровней оглавления

Aspose.PDF также позволяет устанавливать различные TabLeaderType для разных уровней оглавления. Вам необходимо установить свойство LineDash массива FormatArray с соответствующим значением перечисления TabLeaderType следующим образом.

```csharp
 string outFile = "TOC.pdf";

Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();

//установка LeaderType
tocInfo.LineDash = TabLeaderType.Solid;
TextFragment title = new TextFragment("Оглавление");
title.TextState.FontSize = 30;
tocInfo.Title = title;

//Добавление раздела списка в коллекцию разделов документа PDF
tocPage.TocInfo = tocInfo;
//Определение формата четырех уровней списка, установка левых отступов
//и
//настройки формата текста каждого уровня

tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Left = 0;
tocInfo.FormatArray[0].Margin.Right = 30;
tocInfo.FormatArray[0].LineDash = TabLeaderType.Dot;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 10;
tocInfo.FormatArray[1].Margin.Right = 30;
tocInfo.FormatArray[1].LineDash = TabLeaderType.None;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].Margin.Left = 20;
tocInfo.FormatArray[2].Margin.Right = 30;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].LineDash = TabLeaderType.Solid;
tocInfo.FormatArray[3].Margin.Left = 30;
tocInfo.FormatArray[3].Margin.Right = 30;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;

//Создание раздела в документе PDF
Page page = doc.Pages.Add();

//Добавление четырех заголовков в раздел
for (int Level = 1; Level <= 4; Level++)
{

    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(Level);
    TextSegment segment2 = new TextSegment();
    heading2.Segments.Add(segment2);
    heading2.IsAutoSequence = true;
    heading2.TocPage = tocPage;
    segment2.Text = "Пример заголовка" + Level;
    heading2.TextState.Font = FontRepository.FindFont("Arial Unicode MS");

    //Добавление заголовка в оглавление.
    heading2.IsInList = true;
    page.Paragraphs.Add(heading2);
}

// сохранение PDF

doc.Save(outFile);
```
### Скрыть номера страниц в оглавлении

Если вы не хотите отображать номера страниц вместе с заголовками в оглавлении, вы можете использовать свойство [IsShowPageNumbers](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) класса [TOCInfo](https://reference.aspose.com/pdf/net/aspose.pdf/tocinfo) как false. Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы скрыть номера страниц в оглавлении:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "HiddenPageNumbers_out.pdf";
Document doc = new Document();
Page tocPage = doc.Pages.Add();
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Оглавление");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
tocInfo.Title = title;
//Добавьте раздел списка в коллекцию разделов документа PDF
tocPage.TocInfo = tocInfo;
//Определите формат четырех уровней списка, установив левые отступы и
//настройки формата текста каждого уровня

tocInfo.IsShowPageNumbers = false;
tocInfo.FormatArrayLength = 4;
tocInfo.FormatArray[0].Margin.Right = 0;
tocInfo.FormatArray[0].TextState.FontStyle = FontStyles.Bold | FontStyles.Italic;
tocInfo.FormatArray[1].Margin.Left = 30;
tocInfo.FormatArray[1].TextState.Underline = true;
tocInfo.FormatArray[1].TextState.FontSize = 10;
tocInfo.FormatArray[2].TextState.FontStyle = FontStyles.Bold;
tocInfo.FormatArray[3].TextState.FontStyle = FontStyles.Bold;
Page page = doc.Pages.Add();
//Добавьте четыре заголовка в раздел
for (int Level = 1; Level != 5; Level++)

{ Heading heading2 = new Heading(Level); TextSegment segment2 = new TextSegment(); heading2.TocPage = tocPage; heading2.Segments.Add(segment2); heading2.IsAutoSequence = true; segment2.Text = "это заголовок уровня " + Level; heading2.IsInList = true; page.Paragraphs.Add(heading2); }
doc.Save(outFile);
```
### Настройка номеров страниц при добавлении оглавления

Часто требуется настроить нумерацию страниц в оглавлении при добавлении оглавления в документ PDF. Например, может потребоваться добавить префикс перед номером страницы, например P1, P2, P3 и так далее. В таком случае Aspose.PDF для .NET предоставляет свойство PageNumbersPrefix класса TocInfo, которое можно использовать для настройки номеров страниц, как показано в следующем примере кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string inFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824.pdf";
string outFile = RunExamples.GetDataDir_AsposePdf_WorkingDocuments() + "42824_out.pdf";
// Загружаем существующий файл PDF
Document doc = new Document(inFile);
// Получаем доступ к первой странице файла PDF
Aspose.Pdf.Page tocPage = doc.Pages.Insert(1);
// Создаем объект для представления информации оглавления
TocInfo tocInfo = new TocInfo();
TextFragment title = new TextFragment("Оглавление");
title.TextState.FontSize = 20;
title.TextState.FontStyle = FontStyles.Bold;
// Устанавливаем заголовок для оглавления
tocInfo.Title = title;
tocInfo.PageNumbersPrefix = "P";
tocPage.TocInfo = tocInfo;
for (int i = 1; i < doc.Pages.Count; i++)
{
    // Создаем объект для заголовка
    Aspose.Pdf.Heading heading2 = new Aspose.Pdf.Heading(1);
    TextSegment segment2 = new TextSegment();
    heading2.TocPage = tocPage;
    heading2.Segments.Add(segment2);
    // Указываем целевую страницу для объекта заголовка
    heading2.DestinationPage = doc.Pages[i + 1];
    // Целевая страница
    heading2.Top = doc.Pages[i + 1].Rect.Height;
    // Координата назначения
    segment2.Text = "Страница " + i.ToString();
    // Добавляем заголовок на страницу с оглавлением
    tocPage.Paragraphs.Add(heading2);
}

// Сохраняем обновленный документ
doc.Save(outFile);
```
## Как установить срок действия PDF

Мы применяем привилегии доступа к файлам PDF, чтобы определенная группа пользователей могла получить доступ к определенным функциям/объектам документов PDF. Чтобы ограничить доступ к файлу PDF, мы обычно применяем шифрование и у нас может возникнуть необходимость установить срок действия файла PDF, чтобы пользователь, просматривающий документ, получил соответствующее уведомление о истечении срока действия файла PDF.

Для выполнения вышеуказанных требований мы можем использовать объект *JavascriptAction*. Пожалуйста, обратите внимание на следующий фрагмент кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Создаем объект документа
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
// Добавляем страницу в коллекцию страниц PDF файла
doc.Pages.Add();
// Добавляем текстовый фрагмент в коллекцию параграфов объекта страницы
doc.Pages[1].Paragraphs.Add(new TextFragment("Hello World..."));
// Создаем объект JavaScript для установки срока действия PDF
JavascriptAction javaScript = new JavascriptAction(
"var year=2017;"
+ "var month=5;"
+ "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
+ "expiry = new Date(year, month);"
+ "if (today.getTime() > expiry.getTime())"
+ "app.alert('The file is expired. You need a new one.');");
// Устанавливаем JavaScript как действие при открытии PDF
doc.OpenAction = javaScript;

dataDir = dataDir + "SetExpiryDate_out.pdf";
// Сохраняем документ PDF
doc.Save(dataDir);
```
## Определение Прогресса Генерации PDF Файла

Клиент попросил добавить функцию, позволяющую разработчикам определять прогресс генерации PDF файла. Вот ответ на этот запрос.

Поле [CustomerProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) класса [DocSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) позволяет определить, как идет генерация PDF. Обработчик имеет следующие типы:

- DocSaveOptions.ConversionProgessEventHandler
- DocSaveOptions.ProgressEventHandlerInfo
- DocSaveOptions.ProgressEventType

Приведенные ниже фрагменты кода показывают, как использовать CustomerProgressHandler.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "AddTOC.pdf");
DocSaveOptions saveOptions = new DocSaveOptions();
saveOptions.CustomProgressHandler = new UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

dataDir = dataDir + "DetermineProgress_out.pdf";
pdfDocument.Save(dataDir, saveOptions);
Console.ReadLine();
```
```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public static void ShowProgressOnConsole(DocSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case DocSaveOptions.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Прогресс конвертации : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.SourcePageAnalized:
            Console.WriteLine(String.Format("{0}  - Анализ страницы источника {1} из {2} выполнен.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Создана компоновка страницы результата {1} из {2}.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case DocSaveOptions.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Экспортирована страница результата {1} из {2}.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }

}
```
## Сглаживание заполняемого PDF в C#

Документы PDF часто включают формы с интерактивными заполняемыми виджетами, такими как радиокнопки, флажки, текстовые поля, списки и т.д. Чтобы сделать их неизменяемыми для различных целей приложения, нам нужно сгладить файл PDF.
Aspose.PDF предоставляет функцию для сглаживания вашего PDF в C# всего несколькими строками кода:

```csharp

// Загрузка исходной PDF формы
Document doc = new Document(dataDir + "input.pdf");

// Сглаживание заполняемого PDF
if (doc.Form.Fields.Count() > 0)
{
    foreach (var item in doc.Form.Fields)
    {
        item.Flatten();
    }
}

dataDir = dataDir + "FlattenForms_out.pdf";
// Сохранение обновленного документа
doc.Save(dataDir);
```

