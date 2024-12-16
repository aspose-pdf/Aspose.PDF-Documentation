---
title: Добавление текста в PDF с использованием C++
linktitle: Добавление текста в PDF
type: docs
weight: 10
url: /ru/cpp/add-text-to-pdf-file/
description: Эта статья описывает различные аспекты работы с текстом в Aspose.PDF. Узнайте, как добавить текст в PDF, добавить HTML-фрагменты или использовать пользовательские шрифты OTF.
lastmod: "2021-12-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавление текста

Чтобы добавить текст в существующий PDF-файл:

1. Откройте входной PDF с помощью объекта Document.
2. Получите конкретную страницу, на которую вы хотите добавить текст.
3. Создайте объект TextFragment с входным текстом и другими свойствами текста. Объект TextBuilder, созданный из этой конкретной страницы, на которую вы хотите добавить текст, позволяет вам добавить объект TextFragment на страницу с помощью метода AppendText.
4. Вызовите метод Save объекта Document и сохраните выходной PDF-файл.

Следующий фрагмент кода показывает, как добавить текст в существующий PDF-файл.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddingText() {
    
    String _dataDir("C:\\Samples\\");

    // String for input file name
    String inputFileName("sample.pdf");
    // String for output file name
    String outputFileName("AddingText_out.pdf");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // get particular page
    auto pdfPage = document->get_Pages()->idx_get(1);

    // create text fragment
    auto textFragment = MakeObject<TextFragment>("Aspose.PDF");
    textFragment->set_Position(MakeObject<Position>(80, 700));

    // set text properties
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
    textFragment->get_TextState()->set_FontSize(14);
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());

    // create TextBuilder object
    auto textBuilder = MakeObject<TextBuilder>(pdfPage);
    // append the text fragment to the PDF page
    textBuilder->AppendText(textFragment);

    // Save resulting PDF document.
    document->Save(_dataDir + outputFileName);
}
```

## Загрузка шрифта из потока

Следующий фрагмент кода показывает, как загрузить шрифт из объекта Stream при добавлении текста в PDF-документ.

```cpp
void LoadingFontFromStream() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("sample.pdf");
    String outputFileName("LoadingFontFromStream_out.pdf");

    String fontFile("C:\\Windows\\Fonts\\Arial.ttf");

    // Загрузить входной PDF-файл
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Создать объект построителя текста для первой страницы документа
    auto textBuilder = MakeObject<TextBuilder>(document->get_Pages()->idx_get(1));
    // Создать фрагмент текста с примером строки
    auto textFragment = MakeObject<TextFragment>("Hello world");

    if (!fontFile.IsNullOrEmpty()) {
        // Загрузить шрифт TrueType в объект потока
        auto fontStream = System::IO::File::OpenRead(fontFile);
        // Установить имя шрифта для текстовой строки
        textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
        // Указать позицию для текстового фрагмента
        textFragment->set_Position(MakeObject<Position>(10, 10));
        // Добавить текст в TextBuilder, чтобы он мог быть размещен на PDF-файле
        textBuilder->AppendText(textFragment);

        // Сохранить результирующий PDF-документ.
        document->Save(_dataDir + outputFileName);
    }
}
```

## Добавить текст с использованием TextParagraph

Следующий фрагмент кода показывает, как добавить текст в PDF-документ с использованием класса [TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph).

```cpp
void AddTextUsingTextParagraph() {

    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>();

    String outputFileName("AddTextUsingTextParagraph_out.pdf");

    // Добавить страницу в коллекцию страниц объекта Document
    auto page = document->get_Pages()->Add();
    auto builder = MakeObject<TextBuilder>(page);

    // Создать текстовый абзац
    auto paragraph = MakeObject<TextParagraph>();

    // Установить отступ для последующих строк
    paragraph->set_SubsequentLinesIndent(20);

    // Указать местоположение для добавления TextParagraph
    paragraph->set_Rectangle(MakeObject<Rectangle>(100, 300, 200, 700));

    // Указать режим переноса слов
    paragraph->get_FormattingOptions()->set_WrapMode(TextFormattingOptions::WordWrapMode::ByWords);

    // Создать текстовый фрагмент
    auto fragment1 = MakeObject<TextFragment>("the quick brown fox jumps over the lazy dog");
    fragment1->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    fragment1->get_TextState()->set_FontSize(12);
    // Добавить фрагмент в абзац
    paragraph->AppendLine(fragment1);
    // Добавить абзац
    builder->AppendParagraph(paragraph);

    // Сохранить результирующий PDF-документ.
    document->Save(_dataDir + outputFileName);
}

```

## Добавить гиперссылку к TextSegment

Страница PDF может состоять из одного или нескольких объектов TextFragment, где каждый объект TextFragment может иметь один или несколько экземпляров TextSegment. Для установки гиперссылки для TextSegment можно использовать свойство Hyperlink класса [TextSegment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_segment), предоставляя объект экземпляра Aspose.Pdf.WebHyperlink. Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования.

```cpp
void AddHyperlinkToTextSegment() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("AddHyperlinkToTextSegment_out.pdf");

    // Создать экземпляр документа
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц PDF файла
    auto page1 = document->get_Pages()->Add();

    // Создать экземпляр TextFragment
    auto tf = MakeObject<TextFragment>("Sample Text Fragment");
    // Установить горизонтальное выравнивание для TextFragment
    tf->set_HorizontalAlignment(HorizontalAlignment::Right);

    // Создать текстовый сегмент с примером текста
    auto segment = MakeObject<TextSegment>(" ... Text Segment 1...");
    // Добавить сегмент в коллекцию сегментов TextFragment
    tf->get_Segments()->Add(segment);

    // Создать новый TextSegment
    segment = MakeObject<TextSegment>("Link to Google");
    // Добавить сегмент в коллекцию сегментов TextFragment

    tf->get_Segments()->Add(segment);

    // Установить гиперссылку для TextSegment
    segment->set_Hyperlink(MakeObject<Aspose::Pdf::WebHyperlink>("www.aspose.com"));

    // Установить цвет переднего плана для текстового сегмента
    segment->get_TextState()->set_ForegroundColor(Color::get_Blue());

    // Установить форматирование текста как курсив
    segment->get_TextState()->set_FontStyle(FontStyles::Italic);

    // Создать другой объект TextSegment
    segment = MakeObject<TextSegment>(u"TextSegment without hyperlink");

    // Добавить сегмент в коллекцию сегментов TextFragment
    tf->get_Segments()->Add(segment);

    // Добавить TextFragment в коллекцию параграфов объекта страницы
    page1->get_Paragraphs()->Add(tf);

    // Сохранить результирующий PDF документ.
    document->Save(_dataDir + outputFileName);

}
```

## Использовать OTF Шрифт

Aspose.PDF для C++ предлагает возможность использовать пользовательские/TrueType шрифты при создании/манипуляции содержимым PDF файла, чтобы содержимое отображалось с использованием шрифтов, отличных от системных по умолчанию.

```cpp
void UseOTFFont() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("OTFFont_out.pdf");

    // Создать новый экземпляр документа
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    // Создать экземпляр TextFragment с образцом текста
    auto fragment = MakeObject<TextFragment>("Пример текста в OTF шрифте");

    // Или вы можете даже указать путь к OTF шрифту в системной директории
    fragment->get_TextState()->set_Font(FontRepository::OpenFont(u"C:\\Samples\\Fonts\\Montserrat-Black.otf"));
    // Указать встраивание шрифта в PDF файл, чтобы он отображался правильно,
    // даже если конкретный шрифт не установлен/отсутствует на целевой машине
    fragment->get_TextState()->get_Font()->set_IsEmbedded(true);
    // Добавить TextFragment в коллекцию параграфов экземпляра страницы
    page->get_Paragraphs()->Add(fragment);
    // Сохранить полученный PDF документ.
    document->Save(_dataDir + outputFileName);
}
```

## Добавление HTML строки с использованием DOM

Класс Aspose.Pdf.Generator.Text содержит свойство под названием IsHtmlTagSupported, которое позволяет добавлять HTML теги/содержимое в PDF файлы. Добавленное содержимое отображается в виде нативных HTML тегов, а не просто как текстовая строка. Чтобы поддерживать аналогичную функцию в новой модели объектов документа (DOM) пространства имен Aspose.Pdf, был введен класс HtmlFragment.

Экземпляр [HtmlFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_fragment) может быть использован для указания HTML содержимого, которое должно быть размещено внутри PDF файла. Подобно TextFragment, HtmlFragment является объектом уровня абзаца и может быть добавлен в коллекцию абзацев объекта Page. Следующие фрагменты кода показывают шаги по размещению HTML содержимого внутри PDF файла с использованием подхода DOM.

```cpp
void AddingHtmlString() {
    
    String _dataDir("C:\\Samples\\");

    // String для имени входного файла
    String inputFileName("sample.pdf");

    // String для имени выходного файла
    String outputFileName("sample_html_out.pdf");

    // создать экземпляр Document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    // Создать объект HtmlFragment с HTML содержимым
    auto title = MakeObject<HtmlFragment>("<h1 style=\"color:blue\"><strong>HTML String Demo</strong></h1>");

    // установить MarginInfo для деталей полей
    auto margin = MakeObject<MarginInfo>();
    margin->set_Bottom(10);
    margin->set_Top(200);
    // Установить информацию о полях
    title->set_Margin(margin);

    // Добавить HTML фрагмент в коллекцию абзацев страницы
    page->get_Paragraphs()->Add(title);
    // Сохранить PDF файл
    document->Save(_dataDir + outputFileName);
}
```

Следующий фрагмент кода демонстрирует шаги по добавлению упорядоченных списков HTML в документ:

```cpp
void AddHTMLOrderedListIntoDocuments() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла
    String outputFileName("AddHTMLOrderedListIntoDocuments_out.pdf");

    // Создание объекта Document    
    auto document = MakeObject<Document>();

    // Создание объекта HtmlFragment с соответствующим HTML фрагментом
    auto htmlFragment = MakeObject<HtmlFragment>(
        "<div style=\"font-family: sans-serif\"><ul><li>First</li><li>Second</li><li>Third</li><li>Fourth</li><li>Fifth</li></ul><p>Text after the list.</p><p>Next line<br/>Last line</p></div>");
    // Добавление страницы в коллекцию страниц
    auto page = document->get_Pages()->Add();

    // Добавление HtmlFragment на страницу
    page->get_Paragraphs()->Add(htmlFragment);

    // Сохранение результирующего PDF файла
    document->Save(_dataDir + outputFileName);
}
```

Вы также можете установить форматирование строки HTML, используя объект TextState следующим образом:

```cpp
void AddHTMLStringFormatting() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла
    String outputFileName("sample_html_out.pdf");

    // Создание объекта Document    
    auto document = MakeObject<Document>();

    // Добавление страницы в коллекцию страниц
    auto page = document->get_Pages()->Add();

    // Создание HtmlFragment с содержимым HTML
    auto title = MakeObject<HtmlFragment>("<h1><strong>HTML String Demo</strong></h1>");

    auto textState = MakeObject<TextState>(12);

    textState->set_Font(FontRepository::FindFont(u"Calibri"));
    textState->set_ForegroundColor(Color::get_Green());
    textState->set_BackgroundColor(Color::get_Coral());
    title->set_TextState(textState);

    // Добавление HTML-фрагмента к коллекции абзацев страницы
    page->get_Paragraphs()->Add(title);
    // Сохранение PDF файла
    document->Save(_dataDir + outputFileName);
}
```

Если вы задаете значения атрибутов текста через HTML разметку, а затем предоставляете те же значения в свойствах TextState, они перезапишут HTML параметры значениями из экземпляра TextState. Следующие фрагменты кода демонстрируют описанное поведение.

```cpp
void AddHTMLUsingDOMAndOverwrite() {

    String _dataDir("C:\\Samples\\");
    // Строка для имени выходного файла
    String outputFileName("AddHTMLUsingDOMAndOverwrite_out.pdf");

    // Создание объекта Document    
    auto document = MakeObject<Document>();

    // Добавление страницы в коллекцию страниц
    auto page = document->get_Pages()->Add();

    // Создание HtmlFragment с HTML содержимым
    auto title = MakeObject<HtmlFragment>("<p style='font-family: Verdana'><b><i>Table contains text</i></b></p>");

    // Семейство шрифтов из 'Verdana' будет сброшено на 'Arial'
    title->set_TextState(new TextState(u"Arial Black"));
    title->set_TextState(new TextState(20));

    // Установка информации о нижнем поле
    title->get_Margin()->set_Bottom(10);
    // Установка информации о верхнем поле
    title->get_Margin()->set_Top(400);
    // Добавление HTML-фрагмента в коллекцию абзацев страницы
    page->get_Paragraphs()->Add(title);
    // Сохранение PDF файла
    document->Save(_dataDir + outputFileName);
}
```

## FootNotes and EndNotes (DOM)

Сноски указывают на примечания в тексте вашего документа, используя последовательные надстрочные номера. Фактическое примечание отступает и может быть представлено в виде сноски внизу страницы.

### Добавление сноски

В системе ссылок с сносками укажите ссылку, выполняя следующие действия:

- поставьте маленький номер над строкой текста непосредственно после исходного материала. Этот номер называется идентификатором примечания. Он находится немного выше строки текста.
- поставьте тот же номер, за которым следует ссылка на ваш источник, внизу страницы. Сноски должны быть числовыми и хронологическими: первая ссылка — 1, вторая — 2 и так далее.

Преимущество сносок в том, что читатель может просто опустить взгляд вниз по странице, чтобы узнать источник ссылки, которая его интересует.

Следуйте следующим шагам:

- Создайте экземпляр [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
- Создайте объект [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page)

- Создайте объект [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)
- Создайте экземпляр Note и передайте его значение свойству TextFragment [FootNote](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#abe1663009fbceed84a0a392527463219)
- Добавьте TextFragment в коллекцию абзацев экземпляра страницы

```cpp
void AddFootNote() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла
    String inputFileName("sample.pdf");
    String outputFileName("sample_footnote_out.pdf");

    // Создайте экземпляр объекта Document    
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Добавьте страницу в коллекцию страниц
    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>();
    note->set_Text(u"Демо");
    t->set_FootNote(note);

    // создайте экземпляр TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // установите значение FootNote для TextFragment
    text->set_FootNote(MakeObject<Note>("примечание для тестового текста 1"));
    // добавьте TextFragment в коллекцию абзацев первой страницы документа
    page->get_Paragraphs()->Add(text);
    // создайте второй TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // установите FootNote для второго текстового фрагмента
    text->set_FootNote(MakeObject<Note>("примечание для тестового текста 2"));
    // добавьте второй текстовый фрагмент в коллекцию абзацев PDF файла
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Пользовательский стиль линии для FootNote

Следующий пример демонстрирует, как добавить сноски в нижнюю часть страницы PDF и определить пользовательский стиль линии.

```cpp
void CustomFootNote_Line() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла    
    String outputFileName("customFootNote_Line.pdf");

    // Создать экземпляр документа
    auto document = MakeObject<Document>();

    // добавить страницу в коллекцию страниц PDF
    auto page = document->get_Pages()->Add();
    
    // создать объект GraphInfo
    auto graph = MakeObject<GraphInfo>();
    // установить ширину линии как 2
    graph->set_LineWidth(2);
    // установить цвет для объекта графа
    graph->set_Color(Color::get_Red());
    // установить значение массива тире как 3
    graph->set_DashArray(MakeArray<int>(3));
    // установить фазу тире как 1
    graph->set_DashPhase(1);
    // установить стиль линии сноски для страницы как граф
    page->set_NoteLineStyle(graph);

    // создать экземпляр TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // установить значение сноски для TextFragment
    text->set_FootNote(MakeObject<Note>("сноска для тестового текста 1"));
    // добавить TextFragment в коллекцию абзацев первой страницы документа
    page->get_Paragraphs()->Add(text);
    // создать второй TextFragment
    text = MakeObject<TextFragment>("Aspose.Pdf for Java");
    // установить сноску для второго текстового фрагмента
    text->set_FootNote(MakeObject<Note>("сноска для тестового текста 2"));
    // добавить второй текстовый фрагмент в коллекцию абзацев PDF-файла
    page->get_Paragraphs()->Add(text);
    // сохранить PDF-файл
    document->Save(_dataDir + outputFileName);
}
```

Мы можем установить форматирование метки сноски (идентификатор примечания) с использованием объекта TextState следующим образом:

```csharp
void AddCustomFootNoteLabel() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для имени входного файла    
    String inputFileName("sample.pdf");

    // Строка для имени выходного файла    
    String outputFileName("sample_footnote.pdf");

    // Создать экземпляр документа
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto page = document->get_Pages()->idx_get(1);

    auto tfa = MakeObject<TextFragmentAbsorber>("Portable Document Format");
    tfa->Visit(page);

    auto t = tfa->get_TextFragments()->idx_get(1);
    auto note = MakeObject<Note>("Demo");
    t->set_FootNote(note);

    // создать экземпляр TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // установить значение FootNote для TextFragment
    text->set_FootNote(MakeObject<Note>("сноска для тестового текста 1"));
    text->get_FootNote()->set_Text(u"21");

    auto ts = MakeObject<TextState>();
    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_FontStyle(FontStyles::Italic);
    text->get_FootNote()->set_TextState(ts);

    // добавить TextFragment в коллекцию абзацев первой страницы документа
    page->get_Paragraphs()->Add(text);
    // создать второй TextFragment
    text = MakeObject<TextFragment>(u"Aspose.Pdf for C++");
    // установить FootNote для второго текстового фрагмента
    text->set_FootNote(MakeObject<Note>("сноска для тестового текста 2"));
    // добавить второй текстовый фрагмент в коллекцию абзацев PDF файла
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

### Настройка метки сноски

По умолчанию номер сноски увеличивается, начиная с 1. Однако у нас может возникнуть требование установить пользовательскую метку сноски. Чтобы выполнить это требование, попробуйте использовать следующий фрагмент кода

```cpp
void CustomFootNote_Label() {

    String _dataDir("C:\\Samples\\");
    // Строка для имени выходного файла    
    String outputFileName("CustomizeFootNoteLabel_out.pdf");

    // Создать экземпляр Document
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц PDF
    auto page = document->get_Pages()->Add();

    // Создать объект GraphInfo
    auto graph = MakeObject<GraphInfo>();

    // Установить ширину линии как 2
    graph->set_LineWidth(2);

    // Установить цвет для объекта графика
    graph->set_Color(Color::get_Red());

    // Установить массив штрихов как 3
    graph->set_DashArray(MakeArray<int>(3));

    // Установить фазу штрихов как 1
    graph->set_DashPhase(1);

    // Установить стиль линии сноски для страницы как график
    page->set_NoteLineStyle(graph);

    // Создать экземпляр TextFragment
    auto text = MakeObject<TextFragment>("Hello World");
    // Установить значение сноски для TextFragment
    text->set_FootNote(MakeObject<Note>("foot note for test text 1"));
    // Указать пользовательскую метку для сноски
    text->get_FootNote()->set_Text(u" Aspose(2021)");
    // Добавить TextFragment в коллекцию абзацев первой страницы документа
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Добавление изображения и таблицы в сноску

Следующий фрагмент кода показывает шаги по добавлению [сноски](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment#a017ff999979d9f799b8e3cd32ab95722) к объекту [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment), а затем добавление объектов изображения и таблицы в коллекцию абзацев раздела сноски.

```cpp

void AddingImageAndTableToFootnote() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла    
    String outputFileName("AddImageAndTableToFootNote_out.pdf");

    // Создание экземпляра документа
    auto document = new Document();
    // Добавление страницы в коллекцию страниц PDF
    auto page = document->get_Pages()->Add();

    // Создание экземпляра TextFragment
    auto text = MakeObject<TextFragment>("Hello World");

    page->get_Paragraphs()->Add(text);

    text->set_FootNote(MakeObject<Note>());
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.jpg");
    image->set_FixHeight(20);

    text->get_FootNote()->get_Paragraphs()->Add(image);

    auto footNote = MakeObject<TextFragment>("footnote text");
    footNote->get_TextState()->set_FontSize(20);
    footNote->set_IsInLineParagraph(true);
    text->get_FootNote()->get_Paragraphs()->Add(footNote);
    
    auto table = MakeObject<Table>();
    table->get_Rows()->Add()->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Row 1 Cell 1"));
    text->get_FootNote()->get_Paragraphs()->Add(table);

    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Как создать концовки

Концовка — это ссылка на источник, которая направляет читателей к определенному месту в конце документа, где они могут найти источник информации или слов, процитированных или упомянутых в документе. При использовании концовок за вашей цитируемой, пересказанной или обобщенной фразой следует надстрочный номер.

Следующий пример демонстрирует, как добавить концовку на страницу PDF.

```cpp
void HowToCreateEndNotes() {
    
    String _dataDir("C:\\Samples\\");

    // String for output file name    
    String outputFileName("endNote_out.pdf");

    // Create Document instance
    auto document = new Document();
    // Add page to pages collection of PDF
    auto page = document->get_Pages()->Add();

    // create TextFragment instance
    auto text = MakeObject<TextFragment>("Hello World");

    // set FootNote value for TextFragment
    text->set_EndNote(MakeObject<Note>("sample End note"));

    // specify custom label for FootNote
    text->get_EndNote()->set_Text(u" Aspose(2021)");
    // add TextFragment to paragraphs collection of first page of document
    page->get_Paragraphs()->Add(text);
    // save the PDF file
    document->Save(_dataDir + outputFileName);
}
```

## Текст и изображение как встроенный абзац

Макет по умолчанию для PDF-файла — это потоковый макет (слева направо и сверху вниз). Поэтому каждый новый элемент, добавляемый в PDF-файл, добавляется в поток справа внизу. Однако у нас может быть требование отобразить различные элементы страницы, такие как изображение и текст, на одном уровне (один за другим). Один из подходов может заключаться в создании экземпляра таблицы и добавлении обоих элементов в отдельные объекты ячеек. Однако другой подход может быть встроенным абзацем. Установив свойство IsInLineParagraph для изображения и текста в значение true, эти абзацы будут отображаться как встроенные с другими элементами страницы.

Следующий фрагмент кода показывает, как добавить текст и изображение как встроенные абзацы в PDF-файл.

```cpp
void TextAndImageAsInLineParagraph() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("TextAndImageAsParagraph_out.pdf");

    // Создать экземпляр документа
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц экземпляра документа
    auto page = document->get_Pages()->Add();

    // Создать TextFragmnet
    auto text = MakeObject<TextFragment>("Hello World.. ");
    // Добавить фрагмент текста в коллекцию абзацев объекта страницы
    page->get_Paragraphs()->Add(text);

    // Создать экземпляр изображения
    auto image = MakeObject<Image>();

    // Установить изображение как встроенный абзац, чтобы оно появлялось сразу после
    // предыдущего объекта абзаца (TextFragment)
    image->set_IsInLineParagraph(true);

    // Указать путь к файлу изображения
    image->set_File(_dataDir + u"aspose-logo.jpg");
    // Установить высоту изображения (опционально)
    image->set_FixHeight(30);
    // Установить ширину изображения (опционально)
    image->set_FixWidth(100);
    // Добавить изображение в коллекцию абзацев объекта страницы
    page->get_Paragraphs()->Add(image);
    // Повторно инициализировать объект TextFragment с другим содержимым
    text = MakeObject<TextFragment>(" Hello Again..");
    // Установить TextFragment как встроенный абзац
    text->set_IsInLineParagraph(true);
    // Добавить вновь созданный TextFragment в коллекцию абзацев страницы
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Указать межсимвольный интервал при добавлении текста

Текст может быть добавлен в коллекцию абзацев PDF с использованием экземпляра TextFragment или объекта TextParagraph, и даже можно штамповать текст внутри PDF, используя класс TextStamp. При добавлении текста может потребоваться указать интервал между символами для текстовых объектов. Для выполнения этого требования было введено новое свойство под названием Property CharacterSpacing.

Пожалуйста, рассмотрите следующие подходы для выполнения этого требования.

Следующие подходы показывают шаги для указания межсимвольного интервала при добавлении текста в документ PDF.

### Использование TextBuilder и TextFragment

```cpp
// Указать межсимвольный интервал при добавлении текста с использованием TextBuilder и TextFragment
void CharacterSpacing_TextFragment() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Создать экземпляр документа
    auto document = MakeObject<Document>();
    // Добавить страницу в коллекцию страниц документа
    auto page = document->get_Pages()->Add();

    // Создать экземпляр TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Создать экземпляр текстового фрагмента с образцом содержимого
    auto wideFragment = MakeObject<TextFragment>("Text with increased character spacing");
    wideFragment->get_TextState()->ApplyChangesFrom(MakeObject<TextState>("Arial", 12));

    // Указать межсимвольный интервал для TextFragment
    wideFragment->get_TextState()->set_CharacterSpacing(2.0f);

    // Указать позицию TextFragment
    wideFragment->set_Position(MakeObject<Position>(100, 650));

    // Добавить TextFragment в экземпляр TextBuilder
    builder->AppendText(wideFragment);

    // Сохранить результирующий PDF-документ.
    document->Save(_dataDir + outputFileName);
}
```

### Использование TextParagraph

```cpp
void CharacterSpacing_TextParagraph() {
    
    String _dataDir("C:\\Samples\\");

    // Строка для выходного имени файла    
    String outputFileName("CharacterSpacingUsingTextBuilderAndFragment_out.pdf");

    // Создание экземпляра документа
    auto document = MakeObject<Document>();

    // Добавление страницы в коллекцию страниц документа
    auto page = document->get_Pages()->Add();

    // Создание экземпляра TextBuilder
    auto builder = MakeObject<TextBuilder>(page);

    // Создание экземпляра TextParagraph
    auto paragraph = MakeObject<TextParagraph>();

    // Создание экземпляра TextState для указания имени и размера шрифта
    auto state = MakeObject<TextState>("Arial", 12);

    // Указание межсимвольного интервала
    state->set_CharacterSpacing(1.5f);

    // Добавление текста в объект TextParagraph
    paragraph->AppendLine(u"Это абзац с межсимвольным интервалом", state);

    // Указание позиции для TextParagraph
    paragraph->set_Position(MakeObject<Position>(100, 550));

    // Добавление TextParagraph в экземпляр TextBuilder
    builder->AppendParagraph(paragraph);

    // Сохранение итогового PDF документа.
    document->Save(_dataDir + outputFileName);
}
```

### Использование TextStamp

```cpp
void CharacterSpacing_TextStamp() {
    
    String _dataDir("C:\\Samples\\");
    String outputFileName("CharacterSpacingUsingTextStamp_out.pdf");
    // Создать экземпляр документа
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц документа    
    auto page = document->get_Pages()->Add();

    // Создать экземпляр TextStamp с примерным текстом
    auto stamp = MakeObject<TextStamp>("Это текстовый штамп с межсимвольным интервалом");

    // Указать имя шрифта для объекта Stamp
    stamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    // Указать размер шрифта для TextStamp
    stamp->get_TextState()->set_FontSize(12);
    // Указать межсимвольный интервал как 1f
    stamp->get_TextState()->set_CharacterSpacing(1.0f);
    // Установить XIndent для Stamp
    stamp->set_XIndent(100);
    // Установить YIndent для Stamp
    stamp->set_YIndent(500);
    // Добавить текстовый штамп на страницу
    stamp->Put(page);
    // Сохранить итоговый PDF документ.
    document->Save(_dataDir + outputFileName);
}
```

## Создание многостолбцового PDF документа

Эта тема показывает, как вы можете создать многостолбцовый PDF, используя Aspose.Pdf для C++.

Сегодня мы чаще всего видим новости, отображаемые в нескольких столбцах на отдельных страницах, а не в книгах, где абзацы текста в основном печатаются на всех страницах слева направо. Многие приложения для обработки документов, такие как Microsoft Word и Adobe Acrobat Writer, позволяют пользователям создавать несколько столбцов на одной странице, а затем добавлять в них данные. 

Aspose.Pdf для C++ также предлагает возможность создавать несколько столбцов на страницах PDF документа. Чтобы создать PDF с несколькими столбцами, мы можем использовать класс [Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box), так как он предоставляет свойство ColumnInfo.ColumnCount для указания количества столбцов внутри FloatingBox, и мы также можем указать расстояние между столбцами и ширину столбцов, используя ColumnInfo.ColumnSpacing и ColumnInfo.ColumnWidths соответственно.

Ниже приведен пример, демонстрирующий создание двух столбцов с объектами Graphs (Line), которые добавляются в коллекцию абзацев FloatingBox, а затем добавляются в коллекцию абзацев экземпляра Page.

```cpp
void CreateMultiColumn() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("CreateMultiColumnPdf_out.pdf");

    // Создать новый экземпляр документа    
    auto document = MakeObject<Document>();

    // Указать информацию о левом поле для PDF файла
    document->get_PageInfo()->get_Margin()->set_Left(40);

    // Указать информацию о правом поле для PDF файла
    document->get_PageInfo()->get_Margin()->set_Right(40);

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    auto graph1 = MakeObject<Aspose::Pdf::Drawing::Graph>(500, 2);

    // Добавить линию в коллекцию абзацев объекта секции
    page->get_Paragraphs()->Add(graph1);

    // Указать координаты для линии
    auto posArr = MakeArray<float>({ 1, 2, 500, 2 });
    auto l1 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr);
    graph1->get_Shapes()->Add(l1);

    // Создать строковые переменные с текстом, содержащим HTML теги
    String s ("<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">\
<strong> Как избежать денежных мошенничеств</<strong> </span>");

    // Создать текстовые абзацы, содержащие HTML текст

    auto heading_text = MakeObject<HtmlFragment>(s);
    page->get_Paragraphs()->Add(heading_text);

    auto box = MakeObject<FloatingBox>();

    // Добавить четыре колонки в секцию
    box->get_ColumnInfo()->set_ColumnCount(2);
    // Установить расстояние между колонками
    box->get_ColumnInfo()->set_ColumnSpacing(u"5");

    box->get_ColumnInfo()->set_ColumnWidths(u"105 105");
    auto text1 = MakeObject<TextFragment>("От Google (Официальный блог Google)");
    text1->get_TextState()->set_FontSize(8);
    text1->get_TextState()->set_LineSpacing(2);
    text1->get_TextState()->set_FontSize(10);
    text1->get_TextState()->set_FontStyle(FontStyles::Italic);

    box->get_Paragraphs()->Add(text1);

    // Создать объект графиков для рисования линии
    auto graph2 = MakeObject<Aspose::Pdf::Drawing::Graph>(50, 10);
    // Указать координаты для линии
    auto posArr2 = MakeArray<float>({ 1, 10, 100, 10 });

    auto l2 = MakeObject<Aspose::Pdf::Drawing::Line>(posArr2);
    graph2->get_Shapes()->Add(l2);

    // Добавить линию в коллекцию абзацев объекта секции
    box->get_Paragraphs()->Add(graph2);

    auto text2 = MakeObject<TextFragment>(
        "Сед аугэ tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. \
        Сед quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue.\
        Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur \
        ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean \
        posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. \
        Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, \
        risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam \
        luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, \
        sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, \
        pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,\
        iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus \
        mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla.\
        Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,\
        iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique\
        ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.\
        Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. \
        Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box->get_Paragraphs()->Add(text2);

    page->get_Paragraphs()->Add(box);

    // Сохранить PDF файл
    document->Save(_dataDir + outputFileName);
}
```

## Работа с пользовательскими Табуляторами

Табулятор - это точка остановки для табуляции. В текстовых процессорах каждая строка содержит несколько табуляторов, расположенных на регулярных интервалах (например, каждые полдюйма). Однако их можно изменить, поскольку большинство текстовых процессоров позволяют устанавливать табуляторы там, где вы хотите. Когда вы нажимаете клавишу Tab, курсор или точка вставки перемещаются к следующему табулятору, который сам по себе невидим. Хотя табуляторы не существуют в текстовом файле, текстовый процессор отслеживает их, чтобы правильно реагировать на нажатие клавиши Tab.

Вот пример, как установить пользовательские табуляторы.

## Как добавить прозрачный текст в PDF

PDF 1.4 (формат файла, поддерживаемый Acrobat 5) была первой версией PDF, поддерживающей прозрачность. Этот PDF появился на рынке примерно в то же время, что и Adobe Illustrator 9.

PDF-файл содержит объекты изображения, текста, графики, вложений, аннотаций, и при создании TextFragment вы можете задать информацию о переднем и заднем планах, а также форматирование текста. Aspose.PDF для C++ поддерживает возможность добавления текста с альфа-каналом цвета. Следующий пример кода показывает, как добавить текст с прозрачным цветом.

```cpp
void AddTransparentText() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("AddTransparentText_out.pdf");

    // Создать экземпляр документа
    auto document = MakeObject<Document>();    
    // Создать страницу для коллекции страниц PDF-файла
    auto page = document->get_Pages()->Add();

    // Создать объект графики
    auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

    // Создать экземпляр прямоугольника с определенными размерами
    auto rect = MakeObject<Aspose::Pdf::Drawing::Rectangle>(100, 100, 400, 400);
    // Создать объект цвет из альфа-канала цвета
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;

    auto alphaColor = Color::FromArgb(alpha, red, green, blue);

    rect->get_GraphInfo()->set_FillColor(alphaColor);

    // Добавить прямоугольник в коллекцию форм объекта графики
    canvas->get_Shapes()->Add(rect);

    // Добавить объект графики в коллекцию абзацев объекта страницы
    page->get_Paragraphs()->Add(canvas);

    // Установить значение, чтобы не изменять позицию для объекта графики
    canvas->set_IsChangePosition(false);

    // Создать экземпляр TextFragment с примерным значением
    auto text = MakeObject<TextFragment>(
        "прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст ");
    // Создать объект цвет из альфа-канала
    alpha = 30;
    alphaColor = Color::FromArgb(alpha, red, green, blue);
    // Установить информацию о цвете для экземпляра текста
    text->get_TextState()->set_ForegroundColor(alphaColor);
    // Добавить текст в коллекцию абзацев экземпляра страницы
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);
}
```

## Указание межстрочного интервала для шрифтов

Класс [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) имеет перечисление [LineSpacingMode](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91), которое предназначено для специфических шрифтов, например, входной шрифт "HPSimplified.ttf". Также класс [Aspose.Pdf.Text.TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options) имеет свойство [LineSpacing](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a240276fd8a270b7c134d3355c5fb1c91a9e120eead36071a90367e425c96b5eaf) типа LineSpacingMode. Вам просто нужно установить LineSpacing в LineSpacingMode.FullSize. Фрагмент кода, чтобы шрифт отображался правильно, будет выглядеть следующим образом:

```cpp
void SpecifyLineSpacingForFonts() {

    String _dataDir("C:\\Samples\\");
    String outputFileName("SpecifyLineSpacing_out.pdf");

    String fontFile ("hp-simplified-265.ttf");

    // Загрузить входной PDF файл
    auto document = MakeObject<Document>();
    
    // Создать TextFormattingOptions с LineSpacingMode.FullSize
    auto formattingOptions = MakeObject<TextFormattingOptions>();
    formattingOptions->set_LineSpacing(TextFormattingOptions::LineSpacingMode::FullSize);
    
    // Создать текстовый фрагмент с примером строки
    auto textFragment = MakeObject<TextFragment>("Hello world");

    // Загрузить шрифт TrueType в объект потока
    auto fontStream = System::IO::File::OpenRead(_dataDir + fontFile);
    
    // Установить имя шрифта для текстовой строки
    textFragment->get_TextState()->set_Font(FontRepository::OpenFont(fontStream, FontTypes::TTF));
    // Указать позицию для текстового фрагмента
    textFragment->set_Position(MakeObject<Position>(100, 600));
    // Установить TextFormattingOptions текущего фрагмента в предопределенные (которые указывают на
    // LineSpacingMode.FullSize)
    textFragment->get_TextState()->set_FormattingOptions(formattingOptions);
    
    // Добавить текст в TextBuilder, чтобы он мог быть размещен поверх PDF файла    
    auto page = document->get_Pages()->Add();
    page->get_Paragraphs()->Add(textFragment);

    // Сохранить полученный PDF документ
    document->Save(_dataDir + outputFileName);
}
```

## Получение ширины текста динамически

Класс [Aspose.Pdf.Text.TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state) показывает, как получить ширину текста динамически в PDF документе.

Иногда требуется получить ширину текста динамически. Aspose.PDF для C++ включает два метода для измерения ширины строки. Вы можете вызвать метод [MeasureString](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state#a084c1781028cd3483c82b4fd4cec4967) классов Aspose.Pdf.Text.Font или Aspose.Pdf.Text.TextState (или обоих). Пример кода ниже показывает, как использовать эту функциональность.

```cpp
void GetTextWidthDynamicaly() {
    auto font = FontRepository::FindFont(u"Arial");
    auto ts = MakeObject<TextState>();

    ts->set_Font(font);
    ts->set_FontSize(14);

    if (Math::Abs(font->MeasureString(u"A", 14) - 9.337) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    if (Math::Abs(ts->MeasureString(u"z") - 7.0) > 0.001)
        Console::WriteLine(u"Unexpected font string measure!");

    for (char c = 'A'; c <= 'z'; c++) {
        String v(c);
        double fnMeasure = font->MeasureString(v, 14);
        double tsMeasure = ts->MeasureString(v);

        if (Math::Abs(fnMeasure - tsMeasure) > 0.001)
            Console::WriteLine(u"Font and state string measuring doesn't match!");
    }
}
```