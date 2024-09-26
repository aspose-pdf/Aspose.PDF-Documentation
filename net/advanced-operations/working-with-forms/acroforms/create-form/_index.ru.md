---
title: Создание AcroForm - Создание заполняемого PDF в C#
linktitle: Создание AcroForm
type: docs
weight: 10
url: /net/create-form/
description: С помощью Aspose.PDF для .NET вы можете создать форму с нуля в вашем PDF-файле
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Создание AcroForm",
    "alternativeHeadline": "Как создать AcroForm в PDF",
    "author": {
        "@type": "Person",
        "name": "Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, создание acroform",
    "wordcount": "302",
    "proficiencyLevel": "Начинающий",
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
    "url": "/net/create-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-form/"
    },
    "dateModified": "2022-02-04",
    "description": "С помощью Aspose.PDF для .NET вы можете создать форму с нуля в вашем PDF-файле"
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Создание формы с нуля

### Добавление поля формы в документ PDF

Класс [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) предоставляет коллекцию с именем [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form), которая помогает управлять полями форм в документе PDF.

Для добавления поля формы:

1. Создайте поле формы, которое хотите добавить.
1. Вызовите метод Add коллекции [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form).

### Добавление TextBoxField

Ниже приведен пример того, как добавить [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по адресу https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Открыть документ
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// Создать поле
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "Текстовое поле";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// Добавить поле в документ
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// Сохранить измененный PDF
pdfDocument.Save(dataDir);
```
### Добавление RadioButtonField

Следующие фрагменты кода показывают, как добавить [RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield) в документ PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Создание объекта документа
Document pdfDocument = new Document();
// Добавление страницы в файл PDF
pdfDocument.Pages.Add();
// Создание объекта RadioButtonField с номером страницы в качестве аргумента
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// Добавление первой опции радиокнопки и указание её положения с помощью объекта Rectangle
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// Добавление второй опции радиокнопки
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// Добавление радиокнопки в форму объекта документа
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// Сохранение файла PDF
pdfDocument.Save(dataDir);
```
Следующий фрагмент кода показывает шаги добавления RadioButtonField с тремя опциями и размещения их в ячейках таблицы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "120 120 120";
page.Paragraphs.Add(table);
Row r1 = table.Rows.Add();
Cell c1 = r1.Cells.Add();
Cell c2 = r1.Cells.Add();
Cell c3 = r1.Cells.Add();

RadioButtonField rf = new RadioButtonField(page);
rf.PartialName = "radio";
doc.Form.Add(rf, 1);

RadioButtonOptionField opt1 = new RadioButtonOptionField();
RadioButtonOptionField opt2 = new RadioButtonOptionField();
RadioButtonOptionField opt3 = new RadioButtonOptionField();

opt1.OptionName = "Item1";
opt2.OptionName = "Item2";
opt3.OptionName = "Item3";

opt1.Width = 15;
opt1.Height = 15;
opt2.Width = 15;
opt2.Height = 15;
opt3.Width = 15;
opt3.Height = 15;

rf.Add(opt1);
rf.Add(opt2);
rf.Add(opt3);

opt1.Border = new Border(opt1);
opt1.Border.Width = 1;
opt1.Border.Style = BorderStyle.Solid;
opt1.Characteristics.Border = System.Drawing.Color.Black;
opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt1.Caption = new TextFragment("Item1");
opt2.Border = new Border(opt1);
opt2.Border.Width = 1;
opt2.Border.Style = BorderStyle.Solid;
opt2.Characteristics.Border = System.Drawing.Color.Black;
opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt2.Caption = new TextFragment("Item2");
opt3.Border = new Border(opt1);
opt3.Border.Width = 1;
opt3.Border.Style = BorderStyle.Solid;
opt3.Characteristics.Border = System.Drawing.Color.Black;
opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt3.Caption = new TextFragment("Item3");
c1.Paragraphs.Add(opt1);
c2.Paragraphs.Add(opt2);
c3.Paragraphs.Add(opt3);

dataDir = dataDir + "RadioButtonWithOptions_out.pdf";
// Сохранить файл PDF
doc.Save(dataDir);
```
### Добавление подписи к RadioButtonField

Приведенный ниже фрагмент кода показывает, как добавить подпись, которая будет ассоциирована с RadioButtonField:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Загрузить исходную PDF форму
Aspose.Pdf.Facades.Form form1 = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf");
Document PDF_Template_PDF_HTML = new Document(dataDir + "RadioButtonField.pdf");
foreach (var item in form1.FieldNames)
{
    Console.WriteLine(item.ToString());
    Dictionary<string, string> radioOptions = form1.GetButtonOptionValues(item);
    if (item.Contains("radio1"))
    {
        Aspose.Pdf.Forms.RadioButtonField field0 = PDF_Template_PDF_HTML.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
        Aspose.Pdf.Forms.RadioButtonOptionField fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
        fieldoption.OptionName = "Yes";
        fieldoption.PartialName = "Yesname";

        var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
        updatedFragment.TextState.Font = FontRepository.FindFont("Arial");
        updatedFragment.TextState.FontSize = 10;
        updatedFragment.TextState.LineSpacing = 6.32f;

        // Создать объект TextParagraph
        TextParagraph par = new TextParagraph();

        // Задать позицию абзаца
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // Указать режим переноса слов
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // Добавить новый TextFragment в абзац
        par.AppendLine(updatedFragment);

        // Добавить TextParagraph с помощью TextBuilder
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```
### Добавление поля ComboBox

Следующие примеры кода показывают, как добавить поле ComboBox в PDF документ.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Создание объекта документа
Document doc = new Document();

// Добавление страницы к объекту документа
doc.Pages.Add();

// Создание объекта поля ComboBox
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// Добавление опций в ComboBox
combo.AddOption("Red");
combo.AddOption("Yellow");
combo.AddOption("Green");
combo.AddOption("Blue");

// Добавление объекта ComboBox в коллекцию полей формы объекта документа
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// Сохранение PDF документа
doc.Save(dataDir);
```

### Добавление всплывающей подсказки к полю формы

Класс Document содержит коллекцию с именем Form, которая управляет полями формы в PDF документе.
Класс Document содержит коллекцию с именем Form, которая управляет полями формы в документе PDF.

Следующие примеры кода показывают, как добавить всплывающую подсказку к полю формы, сначала используя C#, а затем Visual Basic.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Загрузка исходной PDF формы
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// Установка всплывающей подсказки для текстового поля
(doc.Form["textbox1"] as Field).AlternateName = "Всплывающая подсказка текстового поля";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// Сохранение обновленного документа
doc.Save(dataDir);
```

