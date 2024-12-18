---
title: Добавление текста в PDF с использованием C#
linktitle: Добавление текста в PDF
type: docs
weight: 10
url: /ru/net/add-text-to-pdf-file/
description: Эта статья описывает различные аспекты работы с текстом в Aspose.PDF. Узнайте, как добавить текст в PDF, добавить HTML-фрагменты или использовать пользовательские OTF-шрифты.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/add-text-to-a-pdf-file/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление текста в PDF с использованием C#",
    "alternativeHeadline": "Как добавить текст в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, добавление текста в pdf",
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
    "url": "/net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-to-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта статья описывает различные аспекты работы с текстом в Aspose.PDF. Узнайте, как добавить текст в PDF, добавить HTML-фрагменты или использовать пользовательские OTF-шрифты."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Для добавления текста в существующий файл PDF:

1. Откройте входной PDF с помощью объекта Document.
2. Получите конкретную страницу, на которую вы хотите добавить текст.
3. Создайте объект TextFragment с входным текстом вместе с другими свойствами текста. Объект TextBuilder, созданный из этой конкретной страницы – на которую вы хотите добавить текст – позволяет добавить объект TextFragment на страницу с помощью метода AppendText.
4. Вызовите метод Save объекта Document и сохраните выходной файл PDF.

## Добавление текста

Следующий фрагмент кода показывает, как добавить текст в существующий файл PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "input.pdf");

// Получить конкретную страницу
Page pdfPage = (Page)pdfDocument.Pages[1];

// Создать фрагмент текста
TextFragment textFragment = new TextFragment("основной текст");
textFragment.Position = new Position(100, 600);

// Установить свойства текста
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.LightGray);
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Red);

// Создать объект TextBuilder
TextBuilder textBuilder = new TextBuilder(pdfPage);

// Добавить фрагмент текста на страницу PDF
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddText_out.pdf";

// Сохранить результирующий документ PDF.
pdfDocument.Save(dataDir);
```
## Загрузка шрифта из потока

Следующий фрагмент кода показывает, как загрузить шрифт из объекта Stream при добавлении текста в документ PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string fontFile = "";

// Загрузите входной файл PDF
Document doc = new Document( dataDir + "input.pdf");
// Создайте объект конструктора текста для первой страницы документа
TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Создайте текстовый фрагмент с образцом строки
TextFragment textFragment = new TextFragment("Hello world");

if (fontFile != "")
{
    // Загрузите шрифт TrueType в объект потока
    using (FileStream fontStream = File.OpenRead(fontFile))
    {
        // Установите имя шрифта для текстовой строки
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Укажите позицию для текстового фрагмента
        textFragment.Position = new Position(10, 10);
        // Добавьте текст в TextBuilder, чтобы он мог быть размещен в файле PDF
        textBuilder.AppendText(textFragment);
    }

    dataDir = dataDir + "LoadingFontFromStream_out.pdf";

    // Сохраните результирующий документ PDF.
    doc.Save(dataDir);
}
```
## Добавление текста с использованием TextParagraph

Приведенный ниже фрагмент кода показывает, как добавить текст в документ PDF с использованием класса [TextParagraph](https://reference.aspose.com/pdf/net/aspose.pdf.text/textparagraph).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Открыть документ
Document doc = new Document();
// Добавить страницу в коллекцию страниц объекта Document
Page page = doc.Pages.Add();
TextBuilder builder = new TextBuilder(page);
// Создать текстовый параграф
TextParagraph paragraph = new TextParagraph();
// Установить отступ для последующих строк
paragraph.SubsequentLinesIndent = 20;
// Указать местоположение для добавления TextParagraph
paragraph.Rectangle = new Aspose.Pdf.Rectangle(100, 300, 200, 700);
// Указать режим переноса слов
paragraph.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;
// Создать фрагмент текста
TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
fragment1.TextState.Font = FontRepository.FindFont("Times New Roman");
fragment1.TextState.FontSize = 12;
// Добавить фрагмент в параграф
paragraph.AppendLine(fragment1);
// Добавить параграф
builder.AppendParagraph(paragraph);

dataDir = dataDir + "AddTextUsingTextParagraph_out.pdf";

// Сохранить результирующий PDF документ.
doc.Save(dataDir);
```
## Добавление гиперссылки к TextSegment

Страница PDF может состоять из одного или нескольких объектов TextFragment, где каждый объект TextFragment может иметь один или несколько экземпляров TextSegment. Чтобы установить гиперссылку для TextSegment, можно использовать свойство Hyperlink класса [TextSegment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textsegment), предоставляя объект Aspose.Pdf.WebHyperlink. Пожалуйста, используйте следующий фрагмент кода для выполнения этой задачи.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создание экземпляра документа
Document doc = new Document();
// Добавление страницы в коллекцию страниц PDF файла
Page page1 = doc.Pages.Add();
// Создание экземпляра TextFragment
TextFragment tf = new TextFragment("Пример текстового фрагмента");
// Установка горизонтального выравнивания для TextFragment
tf.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
// Создание textsegment с образцом текста
TextSegment segment = new TextSegment(" ... Текстовый сегмент 1...");
// Добавление сегмента в коллекцию сегментов TextFragment
tf.Segments.Add(segment);
// Создание нового TextSegment
segment = new TextSegment("Ссылка на Google");
// Добавление сегмента в коллекцию сегментов TextFragment
tf.Segments.Add(segment);
// Установка гиперссылки для TextSegment
segment.Hyperlink = new Aspose.Pdf.WebHyperlink("www.google.com");
// Установка цвета переднего плана для текстового сегмента
segment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
// Установка форматирования текста как курсив
segment.TextState.FontStyle = FontStyles.Italic;
// Создание другого объекта TextSegment
segment = new TextSegment("TextSegment без гиперссылки");
// Добавление сегмента в коллекцию сегментов TextFragment
tf.Segments.Add(segment);
// Добавление TextFragment в коллекцию абзацев объекта страницы
page1.Paragraphs.Add(tf);

dataDir = dataDir + "AddHyperlinkToTextSegment_out.pdf";

// Сохранение результирующего документа PDF.
doc.Save(dataDir);
```
## Использование шрифта OTF

Aspose.PDF для .NET предлагает функциональность использования пользовательских/шрифтов TrueType при создании/манипулировании содержимым файлов PDF, так что содержимое отображается с использованием шрифтов, отличных от системных по умолчанию. Начиная с релиза Aspose.PDF для .NET 10.3.0, мы добавили поддержку шрифтов Open Type.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создать новый экземпляр документа
Document pdfDocument = new Document();
// Добавить страницу в коллекцию страниц PDF файла
Aspose.Pdf.Page page = pdfDocument.Pages.Add();
// Создать экземпляр TextFragment с образцом текста
TextFragment fragment = new TextFragment("Пример текста в шрифте OTF");
// Найти шрифт в системной директории шрифтов
// Fragment.TextState.Font = FontRepository.FindFont("HelveticaNeueLT Pro 45 Lt");
// Или вы можете указать путь к шрифту OTF в системной директории
fragment.TextState.Font = FontRepository.OpenFont(dataDir + "space age.otf");
// Указать внедрение шрифта в PDF файл, чтобы он правильно отображался,
// даже если конкретный шрифт не установлен/присутствует на целевом устройстве
fragment.TextState.Font.IsEmbedded = true;
// Добавить TextFragment в коллекцию параграфов экземпляра страницы
page.Paragraphs.Add(fragment);

dataDir = dataDir + "OTFFont_out.pdf";

// Сохранить результатирующий PDF документ.
pdfDocument.Save(dataDir);
```
## Добавление HTML-строки с использованием DOM

Класс Aspose.Pdf.Generator.Text содержит свойство с именем IsHtmlTagSupported, которое позволяет добавлять HTML-теги/содержимое в файлы PDF. Добавленное содержимое отображается с использованием нативных HTML-тегов, вместо того чтобы появляться как простая текстовая строка. Для поддержки аналогичной функции в новой модели объектов документа (DOM) пространства имен Aspose.Pdf был введен класс HtmlFragment.

Экземпляр [HtmlFragment](https://reference.aspose.com/pdf/net/aspose.pdf/htmlfragment) может быть использован для указания HTML-содержимого, которое должно быть размещено внутри файла PDF. Аналогично TextFragment, HtmlFragment является объектом уровня абзаца и может быть добавлен в коллекцию абзацев объекта Page. Следующие примеры кода показывают шаги размещения HTML-содержимого в файле PDF с использованием подхода DOM.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создание объекта документа
Document doc = new Document();
// Добавление страницы в коллекцию страниц PDF файла
Page page = doc.Pages.Add();
// Создание HtmlFragment с HTML содержимым
HtmlFragment title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");
// Установка информации о нижнем отступе
title.Margin.Bottom = 10;
// Установка информации о верхнем отступе
title.Margin.Top = 200;
// Добавление HTML Fragment в коллекцию абзацев страницы
page.Paragraphs.Add(title);

dataDir = dataDir + "AddHTMLUsingDOM_out.pdf";
// Сохранение файла PDF
doc.Save(dataDir);
```
Следующий фрагмент кода демонстрирует шаги добавления упорядоченных списков HTML в документ:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Путь к выходному документу.
string outFile = dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf";
// Создание объекта документа
Document doc = new Document();
// Создание объекта HtmlFragment с соответствующим фрагментом HTML
HtmlFragment t = new HtmlFragment("`<body style='line-height: 100px;'><ul><li>Первый</li><li>Второй</li><li>Третий</li><li>Четвертый</li><li>Пятый</li></ul>Текст после списка.<br/>Следующая строка<br/>Последняя строка</body>`");
// Добавление страницы в коллекцию страниц
Page page = doc.Pages.Add();
// Добавление HtmlFragment на страницу
page.Paragraphs.Add(t);
// Сохранение результата в PDF файл
doc.Save(outFile);
```

Вы также можете установить форматирование строк HTML с использованием объекта TextState следующим образом:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
HtmlFragment html = new HtmlFragment("некоторый текст");
html.TextState = new TextState();
html.TextState.Font = FontRepository.FindFont("Calibri");
```
Если вы устанавливаете значения атрибутов текста через HTML-разметку, а затем предоставляете те же значения в свойствах TextState, они перезапишут параметры HTML свойствами из экземпляра TextState. Следующие примеры кода демонстрируют описанное поведение.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создаем объект документа
Document doc = new Document();
// Добавляем страницу в коллекцию страниц PDF файла
Page page = doc.Pages.Add();
// Создаем HtmlFragment с HTML содержимым
HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Таблица содержит текст</i></b></p>");
// Шрифт 'Verdana' будет сброшен на 'Arial'
title.TextState = new TextState("Arial");
title.TextState.FontSize = 20;
// Устанавливаем информацию о нижнем отступе
title.Margin.Bottom = 10;
// Устанавливаем информацию о верхнем отступе
title.Margin.Top = 400;
// Добавляем HTML Fragment в коллекцию параграфов страницы
page.Paragraphs.Add(title);
// Сохраняем PDF файл
dataDir = dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf";
// Сохраняем PDF файл
doc.Save(dataDir);
```
## Сноски и концевые сноски (DOM)

Сноски указывают на заметки в тексте вашей работы с использованием последовательных надстрочных номеров. Сама заметка имеет отступ и может находиться в виде сноски внизу страницы.

### Добавление сноски

В системе ссылок сносками указывают на ссылку следующим образом:

- помещая маленький номер над строкой текста непосредственно после исходного материала. Этот номер называется идентификатором заметки. Он находится немного выше строки текста.
- помещая тот же номер, за которым следует цитата вашего источника, внизу страницы. Сноски должны быть числовыми и хронологическими: первая ссылка - 1, вторая - 2 и так далее.

Преимущество сносок заключается в том, что читатель может просто опустить взгляд на страницу, чтобы узнать источник интересующей его ссылки.

Пожалуйста, следуйте указанным ниже шагам, чтобы создать сноску:

- Создайте экземпляр документа
- Создайте объект страницы
- Создайте объект фрагмента текста
- Создайте экземпляр заметки и передайте его значение в свойство TextFragment.FootNote
- Создайте экземпляр Note и передайте его значение в свойство TextFragment.FootNote
- Добавьте TextFragment в коллекцию абзацев страницы

### Пользовательский стиль линии для сноски

Следующий пример демонстрирует, как добавить сноски в нижнюю часть страницы PDF и определить пользовательский стиль линии.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создать экземпляр документа
Document doc = new Document();
// Добавить страницу в коллекцию страниц PDF
Page page = doc.Pages.Add();
// Создать объект GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Установить ширину линии равной 2
graph.LineWidth = 2;
// Установить цвет для объекта графики
graph.Color = Aspose.Pdf.Color.Red;
// Установить значение массива пунктира равным 3
graph.DashArray = new int[] { 3 };
// Установить значение фазы пунктира равным 1
graph.DashPhase = 1;
// Установить стиль линии сноски для страницы как graph
page.NoteLineStyle = graph;
// Создать экземпляр TextFragment
TextFragment text = new TextFragment("Hello World");
// Установить значение FootNote для TextFragment
text.FootNote = new Note("сноска для тестового текста 1");
// Добавить TextFragment в коллекцию абзацев первой страницы документа
page.Paragraphs.Add(text);
// Создать второй TextFragment
text = new TextFragment("Aspose.Pdf for .NET");
// Установить FootNote для второго текстового фрагмента
text.FootNote = new Note("сноска для тестового текста 2");
// Добавить второй текстовый фрагмент в коллекцию абзацев файла PDF
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomLineStyleForFootNote_out.pdf";

// Сохранить результат в PDF документ.
doc.Save(dataDir);
```
Мы можем установить форматирование метки сноски (идентификатор заметки) с использованием объекта TextState следующим образом:

```csharp
TextFragment text = new TextFragment("тестовый текст 1");
text.FootNote = new Note("сноска для тестового текста 1");
text.FootNote.Text = "21";
text.FootNote.TextState = new TextState();
text.FootNote.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
text.FootNote.TextState.FontStyle = FontStyles.Italic;
```

### Настройка метки сноски

По умолчанию номер FootNote увеличивается, начиная с 1. Однако у нас может возникнуть потребность установить пользовательскую метку FootNote. Для достижения этой цели, пожалуйста, попробуйте использовать следующий фрагмент кода

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создать экземпляр документа
Document doc = new Document();
// Добавить страницу в коллекцию страниц PDF
Page page = doc.Pages.Add();
// Создать объект GraphInfo
Aspose.Pdf.GraphInfo graph = new Aspose.Pdf.GraphInfo();
// Установить ширину линии как 2
graph.LineWidth = 2;
// Установить цвет для объекта графики
graph.Color = Aspose.Pdf.Color.Red;
// Установить значение массива тире как 3
graph.DashArray = new int[] { 3 };
// Установить фазовое значение тире как 1
graph.DashPhase = 1;
// Установить стиль линии сноски для страницы как граф
page.NoteLineStyle = graph;
// Создать экземпляр TextFragment
TextFragment text = new TextFragment("Привет Мир");
// Установить значение FootNote для TextFragment
text.FootNote = new Note("сноска для тестового текста 1");
// Указать пользовательскую метку для FootNote
text.FootNote.Text = " Aspose(2015)";
// Добавить TextFragment в коллекцию абзацев первой страницы документа
page.Paragraphs.Add(text);

dataDir = dataDir + "CustomizeFootNoteLabel_out.pdf";
```
## Добавление изображения и таблицы в сноску

В предыдущих версиях поддержка сносок была предоставлена, но она применялась только к объекту TextFragment. Однако, начиная с версии Aspose.PDF для .NET 10.7.0, вы также можете добавлять сноски к другим объектам внутри документа PDF, таким как таблицы, ячейки и т.д. Следующий фрагмент кода показывает шаги по добавлению сноски к объекту TextFragment, а затем добавлению объекта изображения и таблицы в коллекцию абзацев раздела сноски.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();
TextFragment text = new TextFragment("некоторый текст");
page.Paragraphs.Add(text);

text.FootNote = new Note();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = dataDir + "aspose-logo.jpg";
image.FixHeight = 20;
text.FootNote.Paragraphs.Add(image);
TextFragment footNote = new TextFragment("текст сноски");
footNote.TextState.FontSize = 20;
footNote.IsInLineParagraph = true;
text.FootNote.Paragraphs.Add(footNote);
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.Rows.Add().Cells.Add().Paragraphs.Add(new TextFragment("Ряд 1 Ячейка 1"));
text.FootNote.Paragraphs.Add(table);

dataDir = dataDir + "AddImageAndTable_out.pdf";

// Сохранить результирующий PDF документ.
doc.Save(dataDir);
```
## Как создать концевые сноски

Концевая сноска — это ссылка на источник, которая направляет читателей в определённое место в конце документа, где они могут найти источник информации или слов, цитируемых или упомянутых в документе. При использовании концевых сносок ваша цитируемая или перефразированная фраза или сводный материал сопровождается номером в виде верхнего индекса.

Следующий пример демонстрирует, как добавить концевую сноску на страницу PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создать экземпляр документа
Document doc = new Document();
// Добавить страницу в коллекцию страниц PDF
Page page = doc.Pages.Add();
// Создать экземпляр TextFragment
TextFragment text = new TextFragment("Hello World");
// Установить значение FootNote для TextFragment
text.EndNote = new Note("пример концевой сноски");
// Указать пользовательскую метку для FootNote
text.EndNote.Text = " Aspose(2015)";
// Добавить TextFragment в коллекцию параграфов первой страницы документа
page.Paragraphs.Add(text);

dataDir = dataDir + "CreateEndNotes_out.pdf";
// Сохранить результат в PDF документ.
doc.Save(dataDir);
```
## Текст и изображение как встроенный абзац

Стандартная компоновка файла PDF представляет собой потоковую разметку (сверху слева вниз вправо). Поэтому каждый новый элемент, добавленный в файл PDF, размещается в потоке внизу справа. Однако может возникнуть потребность отображать различные элементы страницы, например Изображение и Текст, на одном уровне (один за другим). Один из подходов может заключаться в создании экземпляра Таблицы и добавлении обоих элементов в отдельные ячейки. Тем не менее, другой подход может быть использование встроенного абзаца. Установив свойство IsInLineParagraph для Изображения и Текста в значение true, эти абзацы будут отображаться как встроенные по отношению к другим элементам страницы.

Следующий фрагмент кода показывает, как добавить текст и изображение как встроенные абзацы в файл PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// Создать экземпляр документа
Document doc = new Document();
// Добавить страницу в коллекцию страниц экземпляра Документа
Page page = doc.Pages.Add();
// Создать фрагмент текста
TextFragment text = new TextFragment("Привет мир.. ");
// Добавить фрагмент текста в коллекцию абзацев объекта Страницы
page.Paragraphs.Add(text);
// Создать экземпляр изображения
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
// Установить изображение как встроенный абзац, чтобы оно отображалось сразу после
// предыдущего абзаца (фрагмента текста)
image.IsInLineParagraph = true;
// Указать путь к файлу изображения
image.File = dataDir + "aspose-logo.jpg";
// Установить высоту изображения (необязательно)
image.FixHeight = 30;
// Установить ширину изображения (необязательно)
image.FixWidth = 100;
// Добавить изображение в коллекцию абзацев объекта Страницы
page.Paragraphs.Add(image);
// Переинициализировать объект фрагмента текста с другим содержимым
text = new TextFragment(" Снова привет..");
// Установить фрагмент текста как встроенный абзац
text.IsInLineParagraph = true;
// Добавить вновь созданный фрагмент текста в коллекцию абзацев страницы
page.Paragraphs.Add(text);

dataDir = dataDir + "TextAndImageAsParagraph_out.pdf";
doc.Save(dataDir);
```
## Указание интервала между символами при добавлении текста

Текст может быть добавлен в коллекцию абзацев PDF-файлов с использованием экземпляра TextFragment или с помощью объекта TextParagraph, а также вы можете добавить текст в PDF с помощью класса TextStamp. При добавлении текста может возникнуть необходимость указать интервал между символами для текстовых объектов. Для достижения этой цели было введено новое свойство с именем CharacterSpacing. Пожалуйста, ознакомьтесь с следующими подходами для выполнения этой задачи.

Следующие подходы показывают шаги по указанию интервала между символами при добавлении текста в документ PDF.

### Использование TextBuilder и TextFragment

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создать экземпляр документа
Document pdfDocument = new Document();
// Добавить страницу в коллекцию страниц документа
Page page = pdfDocument.Pages.Add();
// Создать экземпляр TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Создать экземпляр текстового фрагмента с образцом содержимого
TextFragment wideFragment = new TextFragment("Текст с увеличенным интервалом между символами");
wideFragment.TextState.ApplyChangesFrom(new TextState("Arial", 12));
// Указать интервал между символами для TextFragment
wideFragment.TextState.CharacterSpacing = 2.0f;
// Указать позицию TextFragment
wideFragment.Position = new Position(100, 650);
// Добавить TextFragment в экземпляр TextBuilder
builder.AppendText(wideFragment);
dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndFragment_out.pdf";
// Сохранить результат в PDF-документ.
pdfDocument.Save(dataDir);
```
### Использование TextParagraph

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создать экземпляр документа
Document pdfDocument = new Document();
// Добавить страницу в коллекцию страниц документа
Page page = pdfDocument.Pages.Add();
// Создать экземпляр TextBuilder
TextBuilder builder = new TextBuilder(pdfDocument.Pages[1]);
// Создать экземпляр TextParagraph
TextParagraph paragraph = new TextParagraph();
// Создать экземпляр TextState для указания имени шрифта и размера
TextState state = new TextState("Arial", 12);
// Указать межсимвольный интервал
state.CharacterSpacing = 1.5f;
// Добавить текст в объект TextParagraph
paragraph.AppendLine("Это абзац с межсимвольным интервалом", state);
// Указать позицию для TextParagraph
paragraph.Position = new Position(100, 550);
// Добавить TextParagraph в экземпляр TextBuilder
builder.AppendParagraph(paragraph);

dataDir = dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf";
// Сохранить результат в PDF документ.
pdfDocument.Save(dataDir);
```
### Использование TextStamp

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создать экземпляр документа
Document pdfDocument = new Document();
// Добавить страницу в коллекцию страниц документа
Page page = pdfDocument.Pages.Add();
// Создать экземпляр TextStamp с образцом текста
TextStamp stamp = new TextStamp("This is text stamp with character spacing");
// Указать имя шрифта для объекта Stamp
stamp.TextState.Font = FontRepository.FindFont("Arial");
// Указать размер шрифта для TextStamp
stamp.TextState.FontSize = 12;
// Указать расстояние между символами как 1f
stamp.TextState.CharacterSpacing = 1f;
// Установить XIndent для Stamp
stamp.XIndent = 100;
// Установить YIndent для Stamp
stamp.YIndent = 500;
// Добавить текстовый штамп на страницу
stamp.Put(page);
dataDir = dataDir + "CharacterSpacingUsingTextStamp_out.pdf";
// Сохранить результат в PDF документ.
pdfDocument.Save(dataDir);
```
## Создание многостолбцового PDF-документа

В журналах и газетах мы часто видим, что новости выводятся в нескольких столбцах на одной странице, в отличие от книг, где текстовые абзацы обычно печатаются на целой странице слева направо. Многие приложения для обработки документов, такие как Microsoft Word и Adobe Acrobat Writer, позволяют пользователям создавать несколько столбцов на одной странице и затем добавлять в них данные.

[Aspose.PDF для .NET](https://docs.aspose.com/pdf/net/) также предлагает функцию создания нескольких столбцов внутри страниц PDF-документов.
[Aspose.PDF для .NET](https://docs.aspose.com/pdf/net/) также предлагает функцию создания нескольких колонок внутри страниц PDF-документов.

Расстояние между колонками означает пространство между колонками, и по умолчанию расстояние между колонками составляет 1,25 см. Если ширина колонки не указана, то [Aspose.PDF для .NET](https://docs.aspose.com/pdf/net/) автоматически рассчитывает ширину каждой колонки в соответствии с размером страницы и расстоянием между колонками.

Ниже приведен пример, демонстрирующий создание двух колонок с объектами графиков (Линия), которые добавляются в коллекцию абзацев FloatingBox, которая затем добавляется в коллекцию абзацев экземпляра страницы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
// Указываем информацию о левом отступе для файла PDF
doc.PageInfo.Margin.Left = 40;
// Указываем информацию о правом отступе для файла PDF
doc.PageInfo.Margin.Right = 40;
Page page = doc.Pages.Add();

Aspose.Pdf.Drawing.Graph graph1 = new Aspose.Pdf.Drawing.Graph(500, 2);
// Добавляем линию в коллекцию абзацев объекта раздела
page.Paragraphs.Add(graph1);

// Указываем координаты для линии
float[] posArr = new float[] { 1, 2, 500, 2 };
Aspose.Pdf.Drawing.Line l1 = new Aspose.Pdf.Drawing.Line(posArr);
graph1.Shapes.Add(l1);
// Создаем строковые переменные с текстом, содержащим теги html

string s = "<font face=\"Times New Roman\" size=4>" +

"<strong> Как избежать денежных мошенничеств</<strong> "
+ "</font>";
// Создаем текстовые абзацы, содержащие HTML текст

HtmlFragment heading_text = new HtmlFragment(s);
page.Paragraphs.Add(heading_text);

Aspose.Pdf.FloatingBox box = new Aspose.Pdf.FloatingBox();
// Добавляем четыре колонки в раздел
box.ColumnInfo.ColumnCount = 2;
// Устанавливаем расстояние между колонками
box.ColumnInfo.ColumnSpacing = "5";

box.ColumnInfo.ColumnWidths = "105 105";
TextFragment text1 = new TextFragment("От Googler (Официальный блог Google)");
text1.TextState.FontSize = 8;
text1.TextState.LineSpacing = 2;
box.Paragraphs.Add(text1);
text1.TextState.FontSize = 10;

text1.TextState.FontStyle = FontStyles.Italic;
// Создаем объект графиков для рисования линии
Aspose.Pdf.Drawing.Graph graph2 = new Aspose.Pdf.Drawing.Graph(50, 10);
// Указываем координаты для линии
float[] posArr2 = new float[] { 1, 10, 100, 10 };
Aspose.Pdf.Drawing.Line l2 = new Aspose.Pdf.Drawing.Line(posArr2);
graph2.Shapes.Add(l2);

// Добавляем линию в коллекцию абзацев объекта раздела
box.Paragraphs.Add(graph2);

TextFragment text2 = new TextFragment(@"Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.");
box.Paragraphs.Add(text2);

page.Paragraphs.Add(box);

dataDir = dataDir + "CreateMultiColumnPdf_out.pdf";
// Сохраняем файл PDF
doc.Save(dataDir);
```
## Работа с пользовательскими табуляциями

Табуляция - это точка остановки для табуляции. В текстовой обработке каждая строка содержит несколько точек табуляции, расположенных на регулярных интервалах (например, каждые полдюйма). Однако их можно изменить, поскольку большинство текстовых процессоров позволяют устанавливать табуляции там, где вы хотите. Когда вы нажимаете клавишу Tab, курсор или точка вставки перескакивает на следующую табуляцию, которая сама по себе невидима. Хотя табуляции не существуют в текстовом файле, текстовый процессор отслеживает их, чтобы правильно реагировать на клавишу Tab.

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) позволяет разработчикам использовать пользовательские табуляции в документах PDF. Класс Aspose.Pdf.Text.TabStop используется для установки пользовательских ТАБ-остановок в классе [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment).

[Aspose.PDF for .NET](https://docs.aspose.com/pdf/net/) также предлагает некоторые предопределенные типы табуляции как перечисление с именем TabLeaderType, значения и описания которых приведены ниже:
[Aspose.PDF для .NET](https://docs.aspose.com/pdf/net/) также предлагает некоторые предопределенные типы табуляции в виде перечисления под названием TabLeaderType, значения и описания которых приведены ниже:

|**Тип табулятора**|**Описание**|
| :- | :- |
|None|Без табулятора|
|Solid|Сплошная линия табулятора|
|Dash|Пунктирная линия табулятора|
|Dot|Точечная линия табулятора|

Вот пример того, как установить пользовательские табуляции.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document _pdfdocument = new Document();
Page page = _pdfdocument.Pages.Add();

Aspose.Pdf.Text.TabStops ts = new Aspose.Pdf.Text.TabStops();
Aspose.Pdf.Text.TabStop ts1 = ts.Add(100);
ts1.AlignmentType = TabAlignmentType.Right;
ts1.LeaderType = TabLeaderType.Solid;
Aspose.Pdf.Text.TabStop ts2 = ts.Add(200);
ts2.AlignmentType = TabAlignmentType.Center;
ts2.LeaderType = TabLeaderType.Dash;
Aspose.Pdf.Text.TabStop ts3 = ts.Add(300);
ts3.AlignmentType = TabAlignmentType.Left;
ts3.LeaderType = TabLeaderType.Dot;

TextFragment header = new TextFragment("Это пример формирования таблицы с табуляциями", ts);
TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data22 "));
text2.Segments.Add(new TextSegment("#$TAB"));
text2.Segments.Add(new TextSegment("data23"));

page.Paragraphs.Add(header);
page.Paragraphs.Add(text0);
page.Paragraphs.Add(text1);
page.Paragraphs.Add(text2);

dataDir = dataDir + "CustomTabStops_out.pdf";
_pdfdocument.Save(dataDir);
```
## Как добавить прозрачный текст в PDF

Файл PDF содержит объекты изображений, текста, графиков, вложений, аннотаций, и при создании TextFragment вы можете установить информацию о переднем и фоновом цвете, а также форматирование текста. Aspose.PDF для .NET поддерживает функцию добавления текста с альфа-каналом цвета. Следующий фрагмент кода показывает, как добавить текст с прозрачным цветом.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Создать экземпляр документа
Document doc = new Document();
// Создать страницу в коллекции страниц PDF файла
Aspose.Pdf.Page page = doc.Pages.Add();

// Создать объект Graph
Aspose.Pdf.Drawing.Graph canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
// Создать экземпляр прямоугольника с определенными размерами
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 400, 400);
// Создать объект цвета из альфа-канала цвета
rect.GraphInfo.FillColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.FromArgb(128, System.Drawing.Color.FromArgb(12957183)));
// Добавить прямоугольник в коллекцию форм объекта Graph
canvas.Shapes.Add(rect);
// Добавить объект графика в коллекцию параграфов объекта страницы
page.Paragraphs.Add(canvas);
// Установить значение, чтобы не изменять позицию для объекта графика
canvas.IsChangePosition = false;

// Создать экземпляр TextFragment с примером значения
TextFragment text = new TextFragment("прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст ");
// Создать объект цвета из альфа-канала
Aspose.Pdf.Color color = Aspose.Pdf.Color.FromArgb(30, 0, 255, 0);
// Установить информацию о цвете для экземпляра текста
text.TextState.ForegroundColor = color;
// Добавить текст в коллекцию параграфов экземпляра страницы
page.Paragraphs.Add(text);

dataDir = dataDir + "AddTransparentText_out.pdf";
doc.Save(dataDir);
```
## Указать межстрочный интервал для шрифтов

Каждый шрифт имеет абстрактный квадрат, высота которого является предполагаемым расстоянием между строками текста одного и того же размера шрифта.
Каждый шрифт имеет абстрактный квадрат, высота которого предназначена для расстояния между строками текста того же размера.

```csharp
// Для получения полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string fontFile = dataDir + "HPSimplified.TTF";
// Загрузить входной PDF файл
Document doc = new Document();
// Создать TextFormattingOptions с LineSpacingMode.FullSize
TextFormattingOptions formattingOptions = new TextFormattingOptions();
formattingOptions.LineSpacing = TextFormattingOptions.LineSpacingMode.FullSize;

// Создать объект строителя текста для первой страницы документа
//TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
// Создать текстовый фрагмент с образцом строки
TextFragment textFragment = new TextFragment("Привет мир");

if (fontFile != "")
{
    // Загрузить шрифт TrueType в объект потока
    using (FileStream fontStream = System.IO.File.OpenRead(fontFile))
    {
        // Установить имя шрифта для текстовой строки
        textFragment.TextState.Font = FontRepository.OpenFont(fontStream, FontTypes.TTF);
        // Указать позицию для текстового фрагмента
        textFragment.Position = new Position(100, 600);
        // Установить TextFormattingOptions текущего фрагмента на предопределенный (указывающий на LineSpacingMode.FullSize)
        textFragment.TextState.FormattingOptions = formattingOptions;
        // Добавить текст в TextBuilder, чтобы он мог быть размещен на PDF файле
        //textBuilder.AppendText(textFragment);
        var page = doc.Pages.Add();
        page.Paragraphs.Add(textFragment);
    }

    dataDir = dataDir + "SpecifyLineSpacing_out.pdf";
    // Сохранить результирующий PDF документ
    doc.Save(dataDir);
}
```
## Динамическое определение ширины текста

Иногда требуется динамически получить ширину текста. Aspose.PDF для .NET включает два метода для измерения ширины строки. Вы можете вызвать метод [MeasureString](https://reference.aspose.com/pdf/net/aspose.pdf.text/font/methods/measurestring) классов Aspose.Pdf.Text.Font или Aspose.Pdf.Text.TextState (или обоих). Ниже приведен пример кода, который показывает, как использовать эту функциональность.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Text.Font font = FontRepository.FindFont("Arial");
TextState ts = new TextState();
ts.Font = font;
ts.FontSize = 14;

if (Math.Abs(font.MeasureString("A", 14) - 9.337) > 0.001)
    Console.WriteLine("Неожиданное измерение ширины строки шрифта!");

if (Math.Abs(ts.MeasureString("z") - 7.0) > 0.001)
    Console.WriteLine("Неожиданное измерение ширины строки шрифта!");

for (char c = 'A'; c <= 'z'; c++)
{
    double fnMeasure = font.MeasureString(c.ToString(), 14);
    double tsMeasure = ts.MeasureString(c.ToString());

    if (Math.Abs(fnMeasure - tsMeasure) > 0.001)
        Console.WriteLine("Измерение ширины строки шрифта и состояния не совпадают!");
}
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

