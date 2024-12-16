---
title: Замена текста в PDF с помощью Python
linktitle: Замена текста в PDF
type: docs
weight: 40
url: /ru/python-net/replace-text-in-pdf/
description: Узнайте больше о различных способах замены и удаления текста с помощью библиотеки Aspose.PDF для Python через .NET.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Замена текста в PDF",
    "alternativeHeadline": "Замена и удаление текста в PDF файле",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, python, замена текста, удаление текста",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/replace-text-in-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "Узнайте больше о различных способах замены и удаления текста с помощью библиотеки Aspose.PDF для Python через .NET."
}
</script>


## Замена текста на всех страницах PDF документа

{{% alert color="primary" %}}

Вы можете попробовать найти и заменить текст в документе, используя Aspose.PDF, и получить результаты онлайн по этой [ссылке](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Чтобы заменить текст на всех страницах PDF документа, вам сначала нужно использовать [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) для поиска конкретной фразы, которую вы хотите заменить. После этого вам нужно пройтись по всем TextFragment, чтобы заменить текст и изменить любые другие атрибуты. Когда вы это сделаете, вам нужно только сохранить выходной PDF, используя метод Save объекта Document. Следующий фрагмент кода показывает, как заменить текст на всех страницах PDF документа.

```python

    import aspose.pdf as ap

    # Открываем документ
    document = ap.Document(input_pdf)

    # Создаем объект TextAbsorber, чтобы найти все экземпляры входной поисковой фразы
    absorber = ap.text.TextFragmentAbsorber("format")

    # Применяем абсорбер для всех страниц
    document.pages.accept(absorber)

    # Получаем извлеченные фрагменты текста
    collection = absorber.text_fragments

    # Перебираем фрагменты
    for text_fragment in collection:
        # Обновляем текст и другие свойства
        text_fragment.text = "FORMAT"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
        text_fragment.text_state.font_size = 22
        text_fragment.text_state.foreground_color = ap.Color.blue
        text_fragment.text_state.background_color = ap.Color.green

    # Сохраняем документ
    document.save(output_pdf)
```


## Замена текста в определенном регионе страницы

Чтобы заменить текст в определенном регионе страницы, сначала нужно создать объект TextFragmentAbsorber, задать регион страницы с помощью свойства TextSearchOptions.Rectangle, а затем перебрать все TextFragments для замены текста. После выполнения этих операций нам нужно только сохранить выходной PDF, используя метод Save объекта Document. Следующий фрагмент кода показывает, как заменить текст на всех страницах PDF-документа.

```python
// загрузить файл PDF
Aspose.PDF.Document pdf = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// создать объект TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// искать текст в пределах границ страницы
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// задать регион страницы для параметров поиска текста
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// искать текст на первой странице PDF-файла
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// перебрать отдельные TextFragment
foreach (Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // обновить текст на пустые символы
    tf.Text = "";
}

// сохранить обновленный PDF-файл после замены текста
pdf.Save("c:/pdftest/TextUpdated.pdf");
```


## Замена текста на основе регулярного выражения

Если вы хотите заменить некоторые фразы на основе регулярного выражения, вам сначала нужно найти все фразы, соответствующие этому регулярному выражению, используя TextFragmentAbsorber. Необходимо передать регулярное выражение в качестве параметра конструктору TextFragmentAbsorber. Также нужно создать объект TextSearchOptions, который указывает, используется ли регулярное выражение или нет. Когда вы получите соответствующие фразы в TextFragments, вам нужно будет пройтись по всем из них и обновить по мере необходимости. Наконец, вам нужно сохранить обновленный PDF, используя метод Save объекта Document. Следующий фрагмент кода показывает, как заменить текст на основе регулярного выражения.

```python
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// Создать объект TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Например, 1999-2000

// Установить параметр поиска текста для использования регулярного выражения
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Применить поглотитель для одной страницы
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// Получить извлеченные текстовые фрагменты
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Пройтись по фрагментам
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Обновить текст и другие свойства
    textFragment.Text = "New Phrase";
    // Установить в экземпляр объекта.
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```


## Замена шрифтов в существующем PDF-файле

Aspose.PDF для Python через .NET поддерживает возможность замены текста в PDF-документе. Однако иногда возникает необходимость только заменить шрифт, используемый внутри PDF-документа. Вместо замены текста заменяется только используемый шрифт. Один из перегруженных конструкторов TextFragmentAbsorber принимает объект TextEditOptions в качестве аргумента, и мы можем использовать значение RemoveUnusedFonts из перечисления TextEditOptions.FontReplace для выполнения наших требований. Следующий фрагмент кода показывает, как заменить шрифт внутри PDF-документа.

```python
// Для получения полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Загрузить исходный PDF-файл
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// Поиск фрагментов текста и установка параметра редактирования как удаление неиспользуемых шрифтов
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// Принять абсорбер для всех страниц
pdfDocument.Pages.Accept(absorber);
// Перебрать все TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // Если имя шрифта ArialMT, заменить имя шрифта на Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```


## Замена текста должна автоматически перестраивать содержимое страницы

Aspose.PDF для Python через .NET поддерживает функцию поиска и замены текста внутри PDF файла. Однако недавно некоторые клиенты столкнулись с проблемами при замене текста, когда конкретный TextFragment заменяется на более короткое содержимое и некоторые лишние пробелы отображаются в итоговом PDF, или в случае, если TextFragment заменяется на более длинную строку, то слова накладываются на существующее содержимое страницы. Поэтому возникла необходимость ввести механизм, который бы после замены текста в документе PDF перестраивал содержимое.

Для решения вышеуказанных сценариев, Aspose.PDF для Python через .NET был улучшен таким образом, чтобы такие проблемы не возникали при замене текста внутри PDF файла. Следующий фрагмент кода демонстрирует, как заменить текст внутри PDF файла и чтобы содержимое страницы автоматически перестраивалось.

```python
// Для полных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Загрузить исходный PDF файл
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// Создать объект TextFragment Absorber с регулярным выражением
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// Заменить каждый TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // Установить шрифт для заменяемого текстового фрагмента
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // Установить размер шрифта
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // Заменить текст на более длинную строку, чем заполнитель
    textFragment.Text = "Это более длинная строка для тестирования этой проблемы";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// Сохранить итоговый PDF
doc.Save(dataDir);
```


## Рендеринг заменяемых символов при создании PDF

Заменяемые символы - это специальные символы в строке текста, которые могут быть заменены соответствующим содержимым во время выполнения. Заменяемые символы, которые в настоящее время поддерживаются новой моделью объектов документа Aspose.PDF, это `$P`, `$p,` `\n`, `\r`. Символы `$p` и `$P` используются для работы с нумерацией страниц во время выполнения. `$p` заменяется на номер страницы, на которой находится текущий объект класса Paragraph. `$P` заменяется на общее количество страниц в документе. При добавлении `TextFragment` в коллекцию абзацев PDF-документов, он не поддерживает перенос строки внутри текста. Однако, чтобы добавить текст с переносом строки, пожалуйста, используйте `TextFragment` с `TextParagraph`:

- используйте "\r\n" или Environment.NewLine в TextFragment вместо одиночного "\n";
- создайте объект TextParagraph. Он добавит текст с разбиением на строки;
- добавьте TextFragment с помощью TextParagraph.AppendLine;
- добавьте TextParagraph с помощью TextBuilder.AppendParagraph.

```python
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Инициализация нового TextFragment с текстом, содержащим необходимые маркеры новой строки
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Имя заявителя: " + Environment.NewLine + " Joe Smoe");

// Установите свойства текстового фрагмента, если необходимо
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Создание объекта TextParagraph
TextParagraph par = new TextParagraph();

// Добавление нового TextFragment в абзац
par.AppendLine(textFragment);

// Установите позицию абзаца
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Создание объекта TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Добавление TextParagraph с помощью TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```


## Заменяемые символы в области заголовка/подвала

Заменяемые символы также могут быть помещены в раздел заголовка/подвала PDF-файла. Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы узнать, как добавить заменяемый символ в разделе подвала.

```python
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// Назначьте экземпляр marginInfo свойству Margin секции sec1.PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// Создаем текстовый абзац, который будет содержать содержимое для отображения в качестве заголовка
TextFragment t1 = new TextFragment("название отчета");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Имя_Отчета");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// Создаем объект HeaderFooter для секции
HeaderFooter hfFoot = new HeaderFooter();
// Установите объект HeaderFooter в нечетный и четный нижний колонтитул
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// Добавляем текстовый абзац, содержащий текущий номер страницы из общего количества страниц
TextFragment t3 = new TextFragment("Создано на тестовой дате");
TextFragment t4 = new TextFragment("имя отчета ");
TextFragment t5 = new TextFragment("Страница $p из $P");

// Создаем объект таблицы
Table tab2 = new Table();

// Добавляем таблицу в коллекцию абзацев нужной секции
hfFoot.Paragraphs.Add(tab2);

// Устанавливаем ширину колонок таблицы
tab2.ColumnWidths = "165 172 165";

// Создаем строки в таблице и затем ячейки в строках
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// Устанавливаем вертикальное выравнивание текста как центрированное
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

// Sec1.Paragraphs.Add(New Text("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL #$NP" + "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a#$NL" + "daily basis to ensure it contains the most up to date versions of each of our Java components. #$NL " + "Using Aspose.Total for Java developers can create a wide range of applications. #$NL #$NL"))
Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// Добавляем таблицу в коллекцию абзацев нужной секции
page.Paragraphs.Add(table);

// Устанавливаем границу ячейки по умолчанию, используя объект BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// Устанавливаем границу таблицы, используя другой настроенный объект BorderInfo
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// Создаем строки в таблице и затем ячейки в строках
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a" + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "daily basis to ensure it contains the most up to date versions of each of our Java components. " + CRLF + "Using Aspose.Total for Java developers can create a wide range of applications.");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```


## Удаление неиспользуемых шрифтов из PDF файла

Aspose.PDF для Python через .NET поддерживает функцию встраивания шрифтов при создании PDF документа, а также возможность встраивания шрифтов в существующие PDF файлы. Начиная с Aspose.PDF для Python через .NET 7.3.0, вы также можете удалять дублирующие или неиспользуемые шрифты из PDF документов.

Чтобы заменить шрифты, используйте следующий подход:

1. Вызовите класс [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Вызовите параметр TextEditOptions.FontReplace.RemoveUnusedFonts класса TextFragmentAbsorber. (Это удаляет шрифты, которые стали неиспользуемыми в процессе замены шрифтов).
1. Установите шрифт индивидуально для каждого текстового фрагмента.

Следующий фрагмент кода заменяет шрифт для всех текстовых фрагментов всех страниц документа и удаляет неиспользуемые шрифты.

```python
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Загрузите исходный PDF файл
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// Переберите все текстовые фрагменты
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// Сохраните обновленный документ
doc.Save(dataDir);
```


## Удаление всего текста из PDF документа

### Удаление всего текста с использованием операторов

В некоторых текстовых операциях вам может понадобиться удалить весь текст из PDF документа, и для этого обычно необходимо установить найденный текст как пустую строку. Суть в том, что изменение текста для множества текстовых фрагментов вызывает ряд проверок и операций по корректировке положения текста. Они необходимы в сценариях редактирования текста. Трудность заключается в том, что невозможно определить, сколько текстовых фрагментов будет удалено в сценарии, когда они обрабатываются в цикле.

Поэтому мы рекомендуем использовать другой подход для сценария удаления всего текста со страниц PDF. Пожалуйста, рассмотрите следующий фрагмент кода, который работает очень быстро.

```python
// Для полноценных примеров и файлов данных, пожалуйста, посетите https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// Перебрать все страницы PDF документа
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // Выбрать весь текст на странице
    page.Contents.Accept(operatorSelector);
    // Удалить весь текст
    page.Contents.Delete(operatorSelector.Selected);
}
// Сохранить документ
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для Python через .NET библиотека",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "Библиотека для манипуляции PDF для Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>