---
title: Замена текста в PDF
linktitle: Замена текста в PDF
type: docs
weight: 40
url: /ru/net/replace-text-in-pdf/
description: Узнайте больше о различных способах замены и удаления текста из библиотеки Aspose.PDF для .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Замена текста в PDF",
    "alternativeHeadline": "Замена и удаление текста в файле PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, замена текста, удаление текста",
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
    "url": "/net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-in-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Узнайте больше о различных способах замены и удаления текста из библиотеки Aspose.PDF для .NET."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Замена текста на всех страницах PDF документа

{{% alert color="primary" %}}

Вы можете попробовать найти и заменить текст в документе с помощью Aspose.PDF и получить результаты онлайн по этой [ссылке](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Чтобы заменить текст на всех страницах PDF документа, вам сначала нужно использовать TextFragmentAbsorber для поиска конкретной фразы, которую вы хотите заменить. После этого вам нужно пройти по всем TextFragments, чтобы заменить текст и изменить любые другие атрибуты. Как только вы это сделаете, вам остается только сохранить выходной PDF с помощью метода Save объекта Document. Следующий фрагмент кода показывает, как заменить текст на всех страницах PDF документа.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ReplaceTextAll.pdf");

// Создать объект TextAbsorber для поиска всех вхождений искомой фразы
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// Принять absorber для всех страниц
pdfDocument.Pages.Accept(textFragmentAbsorber);

// Получить извлеченные фрагменты текста
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// Пройти по фрагментам
foreach (TextFragment textFragment in textFragmentCollection)
{
    // Обновить текст и другие свойства
    textFragment.Text = "TEXT";
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}

dataDir = dataDir + "ReplaceTextAll_out.pdf";
// Сохранить результат в PDF документ.
pdfDocument.Save(dataDir);
```
## Замена текста в определенной области страницы

Для замены текста в определенной области страницы сначала необходимо создать объект TextFragmentAbsorber, указать область страницы с помощью свойства TextSearchOptions.Rectangle и затем пройти через все TextFragments для замены текста. После выполнения этих операций остается только сохранить выходной PDF с помощью метода Save объекта Document. Следующий пример кода показывает, как заменить текст на всех страницах PDF-документа.

```csharp
// загрузить PDF файл
Aspose.PDF.Document pdf  = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// создать объект TextFragment Absorber
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// искать текст в пределах страницы
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// указать область страницы для TextSearch Options
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// искать текст на первой странице PDF файла
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// пройтись по каждому TextFragment
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // обновить текст на пустые символы
    tf.Text = "";
}

// сохранить обновленный PDF файл после замены текста
pdf.Save("c:/pdftest/TextUpdated.pdf");
```
## Замена текста на основе регулярного выражения

Если вы хотите заменить некоторые фразы на основе регулярного выражения, вам сначала нужно найти все фразы, соответствующие этому регулярному выражению, используя TextFragmentAbsorber. Вам нужно передать регулярное выражение в качестве параметра конструктору TextFragmentAbsorber. Вам также необходимо создать объект TextSearchOptions, который указывает, используется ли регулярное выражение или нет. После того как вы получите соответствующие фразы в TextFragments, вам нужно пройтись по всем им и обновить по мере необходимости. Наконец, вам нужно сохранить обновленный PDF с помощью метода Save объекта Document. Следующий фрагмент кода показывает, как заменить текст на основе регулярного выражения.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// Создать объект TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // Например, 1999-2000

// Установить опцию поиска текста для указания использования регулярного выражения
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// Применить absorber для одной страницы
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

Aspose.PDF для .NET поддерживает возможность замены текста в PDF-документе. Однако иногда возникает необходимость заменить только используемый шрифт в документе PDF. Таким образом, вместо замены текста заменяется только используемый шрифт. Один из перегруженных конструкторов TextFragmentAbsorber принимает объект TextEditOptions в качестве аргумента, и мы можем использовать значение RemoveUnusedFonts из перечисления TextEditOptions.FontReplace для выполнения наших требований. Следующий фрагмент кода показывает, как заменить шрифт в документе PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Загрузка исходного PDF-файла
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// Поиск текстовых фрагментов и установка опции редактирования как удаление неиспользуемых шрифтов
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// Принять absorber для всех страниц
pdfDocument.Pages.Accept(absorber);
// Перебор всех текстовых фрагментов
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // Если имя шрифта ArialMT, замените имя шрифта на Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// Сохранить обновленный документ
pdfDocument.Save(dataDir);
```
## Автоматическое перераспределение содержимого страницы при замене текста

Aspose.PDF для .NET поддерживает функцию поиска и замены текста внутри PDF-файла. Однако недавно некоторые клиенты столкнулись с проблемами во время замены текста, когда определенный TextFragment заменяется на меньший по размеру контент, и в результате в PDF появляются лишние пробелы, или, в случае замены TextFragment на более длинную строку, слова налагаются на существующее содержимое страницы. Поэтому возникла необходимость ввести механизм, который после замены текста в документе PDF автоматически перераспределял бы содержимое.

Для решения вышеописанных сценариев Aspose.PDF для .NET был улучшен таким образом, чтобы при замене текста внутри PDF-файла подобные проблемы не возникали. Следующий фрагмент кода показывает, как заменить текст внутри PDF-файла, и содержимое страницы должно быть автоматически перераспределено.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Загрузить исходный PDF-файл
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// Создать объект TextFragment Absorber с регулярным выражением
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// Заменить каждый TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // Установить шрифт заменяемого текстового фрагмента
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // Установить размер шрифта
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // Заменить текст на более длинную строку, чем заполнитель
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// Сохранить результирующий PDF
doc.Save(dataDir);
```
## Рендеринг заменяемых символов при создании PDF

Заменяемые символы - это специальные символы в текстовой строке, которые можно заменить соответствующим содержимым во время выполнения. Заменяемые символы, которые в настоящее время поддерживаются новой моделью объектов документа пространства имен Aspose.PDF, это `$P`, `$p`, `\n`, `\r`. Символы `$p` и `$P` используются для управления нумерацией страниц во время выполнения. `$p` заменяется на номер страницы, на которой находится текущий класс Paragraph. `$P` заменяется на общее количество страниц в документе. При добавлении `TextFragment` в коллекцию абзацев документов PDF не поддерживается вставка перевода строки в текст. Однако для добавления текста с переводом строки используйте `TextFragment` с `TextParagraph`:

- используйте "\r\n" или Environment.NewLine в TextFragment вместо одиночного "\n";
- создайте объект TextParagraph. Он добавит текст с разделением строк;
- добавьте TextFragment с помощью TextParagraph.AppendLine;
- добавьте TextParagraph с помощью TextBuilder.AppendParagraph.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// Инициализируйте новый TextFragment с текстом, содержащим необходимые маркеры новой строки
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Имя заявителя: " + Environment.NewLine + " Джо Смо");

// Установите свойства фрагмента текста, если это необходимо
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// Создайте объект TextParagraph
TextParagraph par = new TextParagraph();

// Добавьте новый TextFragment в абзац
par.AppendLine(textFragment);

// Установите позицию абзаца
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// Создайте объект TextBuilder
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// Добавьте TextParagraph с помощью TextBuilder
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```
## Заменяемые символы в области верхнего/нижнего колонтитула

Заменяемые символы также можно разместить внутри секции верхнего или нижнего колонтитула PDF файла. Пожалуйста, ознакомьтесь с следующим примером кода для деталей о том, как добавить заменяемый символ в секцию нижнего колонтитула.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// Назначаем экземпляр marginInfo свойству Margin секции PageInfo
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// Создаем текстовый параграф, который будет содержать контент для отображения в верхнем колонтитуле
TextFragment t1 = new TextFragment("название отчета");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("Report_Name");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// Создаем объект HeaderFooter для секции
HeaderFooter hfFoot = new HeaderFooter();
// Устанавливаем объект HeaderFooter для нечетных и четных нижних колонтитулов
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// Добавляем текстовый параграф, содержащий текущий номер страницы из общего количества страниц
TextFragment t3 = new TextFragment("Создано на тестовую дату");
TextFragment t4 = new TextFragment("название отчета ");
TextFragment t5 = new TextFragment("Страница $p из $P");

// Создаем объект таблицы
Table tab2 = new Table();

// Добавляем таблицу в коллекцию параграфов желаемой секции
hfFoot.Paragraphs.Add(tab2);

// Устанавливаем ширину столбцов таблицы
tab2.ColumnWidths = "165 172 165";

// Создаем строки в таблице, а затем ячейки в строках
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

Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// Добавляем таблицу в коллекцию параграфов желаемой секции
page.Paragraphs.Add(table);

// Устанавливаем границу ячеек по умолчанию с помощью объекта BorderInfo
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// Устанавливаем границу таблицы с помощью другого настроенного объекта BorderInfo
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// Создаем строки в таблице, затем ячейки в строках
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
            c1 = row.Cells.Add("Aspose.Total for Java является компиляцией всех компонентов Java, предлагаемых Aspose. Она компилируется" + CRLF + "ежедневно, чтобы обеспечить наличие самых актуальных версий каждого из наших компонентов Java. " + CRLF + "ежедневно, чтобы обеспечить наличие самых актуальных версий каждого из наших компонентов Java. " + CRLF + "С помощью Aspose.Total для Java разработчики могут создавать широкий спектр приложений.");
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
## Удаление неиспользуемых шрифтов из файла PDF

Aspose.PDF для .NET поддерживает функцию встраивания шрифтов при создании документа PDF, а также возможность встраивания шрифтов в существующие файлы PDF. Начиная с версии Aspose.PDF для .NET 7.3.0, также появилась возможность удаления дублирующихся или неиспользуемых шрифтов из документов PDF.

Для замены шрифтов используйте следующий подход:

1. Вызовите класс [TextFragmentAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragmentabsorber).
1. Вызовите параметр TextFragmentAbsorber класса TextEditOptions.FontReplace.RemoveUnusedFonts. (Это удаляет шрифты, которые стали неиспользуемыми во время замены шрифтов).
1. Установите шрифт индивидуально для каждого текстового фрагмента.

Следующий фрагмент кода заменяет шрифт для всех текстовых фрагментов всех страниц документа и удаляет неиспользуемые шрифты.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по адресу https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Загрузка исходного файла PDF
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// Итерация по всем TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// Сохранение обновленного документа
doc.Save(dataDir);
```
## Удаление всего текста из документа PDF

### Удаление всего текста с помощью операторов

В некоторых операциях с текстом вам может потребоваться удалить весь текст из документа PDF, и для этого обычно нужно установить найденный текст как пустую строку. Важно, что изменение текста для множества текстовых фрагментов вызывает ряд операций проверки и корректировки позиции текста. Они необходимы в сценариях редактирования текста. Проблема в том, что вы не можете определить, сколько текстовых фрагментов будет удалено в сценарии, где они обрабатываются в цикле.

Поэтому мы рекомендуем использовать другой подход для сценария удаления всего текста со страниц PDF. Пожалуйста, рассмотрите следующий фрагмент кода, который работает очень быстро.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Открыть документ
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// Пройти по всем страницам PDF документа
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

