---
title: Добавление текста в PDF файл
linktitle: Добавление текста в PDF файл
type: docs
weight: 10
url: /ru/java/add-text-to-pdf-file/
description: Эта статья описывает различные аспекты работы с текстом в Aspose.PDF. Узнайте, как добавить текст в PDF, добавить HTML-фрагменты или использовать пользовательские шрифты OTF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Чтобы добавить текст в существующий PDF файл:

1. Откройте входной PDF, используя объект Document.
2. Получите конкретную страницу, на которую хотите добавить текст.
3. Создайте объект TextFragment с входным текстом и другими свойствами текста. Объект TextBuilder, созданный из этой конкретной страницы, на которую вы хотите добавить текст, позволяет вам добавить объект TextFragment на страницу, используя метод AppendText.
4. Вызовите метод Save объекта Document и сохраните выходной PDF файл.

## Добавление текста

Следующий фрагмент кода показывает, как добавить текст в существующий PDF файл.

```java
public static void AddingText() {
    // Загрузить PDF файл
    Document document = new Document(_dataDir + "sample.pdf");

    // получить конкретную страницу
    Page pdfPage = document.getPages().get_Item(1);
    // создать текстовый фрагмент
    TextFragment textFragment = new TextFragment("Aspose.PDF");
    textFragment.setPosition(new Position(80, 700));

    // задать свойства текста
    textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
    textFragment.getTextState().setFontSize(14);
    textFragment.getTextState().setForegroundColor(Color.getBlue());
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());

    // создать объект TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // добавить текстовый фрагмент на страницу PDF
    textBuilder.appendText(textFragment);

    // Сохранить получившийся PDF документ.
    document.save(_dataDir + "AddText_out.pdf");
}
```


## Загрузка шрифта из потока

Следующий фрагмент кода показывает, как загрузить шрифт из объекта потока при добавлении текста в документ PDF.

```java
import com.aspose.pdf.*;
import com.aspose.pdf.text.FontTypes;

import java.io.FileInputStream;
import java.io.FileNotFoundException;  
//...
public static void LoadingFontFromStream() throws FileNotFoundException{
    
    String fontFile = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf";

    // Загрузить входной PDF файл
    Document doc = new Document(_dataDir + "input.pdf");
    // Создать объект построителя текста для первой страницы документа
    TextBuilder textBuilder = new TextBuilder(doc.getPages().get_Item(1));
    // Создать фрагмент текста с примером строки
    TextFragment textFragment = new TextFragment("Hello world");
    
    if (fontFile != "")
    {
        // Загрузить шрифт TrueType в объект потока
        FileInputStream fontStream=new FileInputStream(fontFile);            
        // Установить имя шрифта для текстовой строки
        textFragment.getTextState().setFont (FontRepository.openFont(fontStream, FontTypes.TTF));
        // Указать позицию для текстового фрагмента
        textFragment.setPosition(new Position(10, 10));
        // Добавить текст в TextBuilder, чтобы он мог быть размещен на PDF файле
        textBuilder.appendText(textFragment);
        
        _dataDir = _dataDir + "LoadingFontFromStream_out.pdf";
    
        // Сохранить результирующий PDF документ.
        doc.save(_dataDir); 
    }       
}
```


## Добавление текста с использованием TextParagraph

Следующий фрагмент кода показывает, как добавить текст в PDF-документ с использованием класса [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph).

```java
public static void AddTextUsingTextParagraph() {
    // Открыть документ
    Document doc = new Document();
    // Добавить страницу в коллекцию страниц объекта Document
    Page page = doc.getPages().add();
    TextBuilder builder = new TextBuilder(page);
    // Создать текстовый абзац
    TextParagraph paragraph = new TextParagraph();
    // Установить отступ для последующих строк
    paragraph.setSubsequentLinesIndent (20);
    // Указать местоположение для добавления TextParagraph
    paragraph.setRectangle(new Rectangle(100, 300, 200, 700));
    // Указать режим переноса слов
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    // Создать текстовый фрагмент
    TextFragment fragment1 = new TextFragment("the quick brown fox jumps over the lazy dog");
    fragment1.getTextState().setFont (FontRepository.findFont("Times New Roman"));
    fragment1.getTextState().setFontSize (12);
    // Добавить фрагмент в абзац
    paragraph.appendLine(fragment1);
    // Добавить абзац
    builder.appendParagraph(paragraph);

    _dataDir = _dataDir + "AddTextUsingTextParagraph_out.pdf";

    // Сохранить полученный PDF-документ.
    doc.save(_dataDir);        
}
```


## Добавление гиперссылки к TextSegment

Страница PDF может состоять из одного или нескольких объектов TextFragment, где каждый объект TextFragment может иметь один или несколько экземпляров TextSegment. Чтобы установить гиперссылку для TextSegment, можно использовать свойство Hyperlink класса TextSegment, предоставляя объект экземпляра Aspose.Pdf.WebHyperlink. Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования.

```java
public static void AddHyperlinkToTextSegment() {
    // Создать экземпляр документа
    Document doc = new Document();
    // Добавить страницу в коллекцию страниц PDF файла
    Page page1 = doc.getPages().add();

    // Создать экземпляр TextFragment
    TextFragment tf = new TextFragment("Пример текстового фрагмента");
    // Установить выравнивание по горизонтали для TextFragment
    tf.setHorizontalAlignment(HorizontalAlignment.Right);

    // Создать текстовый сегмент с примером текста
    TextSegment segment = new TextSegment(" ... Текстовый сегмент 1...");
    // Добавить сегмент в коллекцию сегментов TextFragment
    tf.getSegments().add(segment);

    // Создать новый TextSegment
    segment = new TextSegment("Ссылка на Google");
    // Добавить сегмент в коллекцию сегментов TextFragment

    tf.getSegments().add(segment);

    // Установить гиперссылку для TextSegment
    segment.setHyperlink(new com.aspose.pdf.WebHyperlink("www.aspose.com"));

    // Установить цвет переднего плана для текстового сегмента
    segment.getTextState().setForegroundColor(com.aspose.pdf.Color.getBlue());

    // Установить форматирование текста как курсив
    segment.getTextState().setFontStyle(FontStyles.Italic);

    // Создать другой объект TextSegment
    segment = new TextSegment("TextSegment без гиперссылки");

    // Добавить сегмент в коллекцию сегментов TextFragment
    tf.getSegments().add(segment);

    // Добавить TextFragment в коллекцию параграфов объекта страницы
    page1.getParagraphs().add(tf);

    _dataDir = _dataDir + "AddHyperlinkToTextSegment_out.pdf";

    // Сохранить полученный PDF документ.
    doc.save(_dataDir);

}
```


## Использование шрифта OTF

Aspose.PDF для Java предлагает возможность использовать пользовательские/TrueType шрифты при создании/манипулировании содержимым PDF файла, чтобы содержимое файла отображалось с использованием шрифтов, отличных от стандартных системных шрифтов. Начиная с выпуска Aspose.PDF для Java 10.4.0, мы предоставили поддержку шрифтов Open Type.

```java
public static void UseOTFFont() {
    // Создать новый экземпляр документа
    Document pdfDocument = new Document();
    // Добавить страницу в коллекцию страниц PDF файла
    Page page = pdfDocument.getPages().add();
    // Создать экземпляр TextFragment с примером текста
    TextFragment fragment = new TextFragment("Пример текста в шрифте OTF");
    // Или вы даже можете указать путь к шрифту OTF в системном каталоге
    fragment.getTextState().setFont(FontRepository.openFont("/home/aspose/.fonts/Montserrat-Black.otf"));
    // Указать включение шрифта внутрь PDF, чтобы он отображался правильно,
    // Даже если конкретный шрифт не установлен/отсутствует на целевой машине
    fragment.getTextState().getFont().setEmbedded(true);
    // Добавить TextFragment в коллекцию параграфов экземпляра страницы
    page.getParagraphs().add(fragment);
    // Сохранить полученный PDF документ.
    pdfDocument.save(_dataDir + "OTFFont_out.pdf");
}
```


## Добавление HTML строки с использованием DOM

Класс Aspose.Pdf.Generator.Text содержит свойство под названием IsHtmlTagSupported, которое позволяет добавлять HTML теги/контент в PDF файлы. Добавленный контент отображается в виде нативных HTML тегов, а не как простая текстовая строка. Чтобы поддержать аналогичную функцию в новой модели Объектного Документа (DOM) из пространства имен Aspose.Pdf, был введен класс HtmlFragment.

Экземпляр [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlFragment) может быть использован для указания HTML содержимого, которое должно быть помещено внутрь PDF файла. Подобно TextFragment, HtmlFragment является объектом уровня абзаца и может быть добавлен в коллекцию абзацев объекта Page. Следующие фрагменты кода показывают шаги для размещения HTML содержимого внутри PDF файла с использованием подхода DOM.

```java
public static void AddingHtmlString() {
    // Создать объект Document
    Document doc = new Document();
    // Добавить страницу в коллекцию страниц PDF файла
    Page page = doc.getPages().add();
    // Создать HtmlFragment с содержимым HTML
    HtmlFragment title = new HtmlFragment("<h1 style=\"color:blue\"><strong>Демонстрация HTML строки</strong></h1>");
    // задать MarginInfo для деталей полей
    MarginInfo Margin = new MarginInfo();
    Margin.setBottom(10);
    Margin.setTop(200);
    // Установить информацию о полях
    title.setMargin(Margin);
    // Добавить HTML фрагмент в коллекцию абзацев страницы
    page.getParagraphs().add(title);
    // Сохранить PDF файл
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


Следующий фрагмент кода демонстрирует шаги по добавлению упорядоченных HTML-списков в документ:

```java
public static void AddHTMLOrderedListIntoDocuments() {
    // Создать экземпляр объекта Document
    Document doc = new Document();
    // Создать экземпляр объекта HtmlFragment с соответствующим HTML-фрагментом
    HtmlFragment t = new HtmlFragment(
            "<div style=\"font-family: sans-serif\"><ul><li>Первый</li><li>Второй</li><li>Третий</li><li>Четвертый</li><li>Пятый</li></ul><p>Текст после списка.</p><p>Следующая строка<br/>Последняя строка</p></div>");
    // Добавить страницу в коллекцию страниц
    Page page = doc.getPages().add();
    // Добавить HtmlFragment на страницу
    page.getParagraphs().add(t);
    // Сохранить результирующий PDF файл
    doc.save(_dataDir + "AddHTMLOrderedListIntoDocuments_out.pdf");
}
```

Вы также можете установить форматирование строки HTML, используя объект TextState следующим образом:

```java
public static void AddHTMLStringFormatting() {
    // Создать экземпляр объекта Document
    Document doc = new Document();
    // Добавить страницу в коллекцию страниц PDF файла
    Page page = doc.getPages().add();
    // Создать экземпляр HtmlFragment с HTML содержимым
    HtmlFragment title = new HtmlFragment("<h1><strong>Демонстрация строки HTML</strong></h1>");
    TextState textState = new TextState(12);
    textState.setFont(FontRepository.findFont("Calibri"));
    textState.setForegroundColor(Color.getGreen());
    textState.setBackgroundColor(Color.getCoral());
    title.setTextState(textState);

    // Добавить HTML-фрагмент в коллекцию параграфов страницы
    page.getParagraphs().add(title);
    // Сохранить PDF файл
    doc.save(_dataDir + "sample_html_out.pdf");
}
```


В случае, если вы устанавливаете значения атрибутов текста через HTML-разметку, а затем предоставляете те же значения в свойствах TextState, они перезапишут HTML-параметры значениями из экземпляра TextState. Следующие фрагменты кода демонстрируют описанное поведение.

```java
public static void AddHTMLUsingDOMAndOverwrite() {
    // Создание объекта Document
    Document doc = new Document();
    // Добавление страницы в коллекцию страниц PDF-файла
    Page page = doc.getPages().add();
    // Создание HtmlFragment с содержимым HTML
    HtmlFragment title = new HtmlFragment("<p style='font-family: Verdana'><b><i>Таблица содержит текст</i></b></p>");
    // Семейство шрифтов из 'Verdana' будет сброшено на 'Arial'
    title.setTextState(new TextState("Arial Black"));
    title.setTextState(new TextState(20));
    // Установка информации о нижнем отступе
    title.getMargin().setBottom(10);
    // Установка информации о верхнем отступе
    title.getMargin().setTop(400);
    // Добавление HTML-фрагмента в коллекцию абзацев страницы
    page.getParagraphs().add(title);
    // Сохранение PDF-файла
    doc.save(_dataDir + "AddHTMLUsingDOMAndOverwrite_out.pdf");
}
```


## FootNotes и EndNotes (DOM)

FootNotes указывают на примечания в тексте вашего документа, используя последовательные надстрочные цифры. Само примечание отступает и может быть представлено как сноска внизу страницы.

### Добавление FootNote

В системе ссылок на сноски укажите ссылку, выполнив следующее:

- поставьте маленький номер над строкой текста сразу после исходного материала. Этот номер называется идентификатором примечания. Он располагается немного выше строки текста.
- поставьте тот же номер, за которым следует цитата вашего источника, внизу страницы. Сноски должны быть числовыми и хронологическими: первая ссылка — это 1, вторая — 2 и так далее.

Преимущество сносок заключается в том, что читатель может просто опустить взгляд вниз по странице, чтобы узнать источник ссылки, которая их интересует.

Пожалуйста, выполните следующие шаги, чтобы создать FootNote:

- Создайте экземпляр Document
- Создайте объект Page
- Создайте объект TextFragment

- Создайте экземпляр Note и передайте его значение свойству TextFragment.FootNote
- Добавьте TextFragment в коллекцию абзацев экземпляра страницы

### Пользовательский стиль линии для FootNote

Следующий пример демонстрирует, как добавить сноски в нижнюю часть страницы PDF и определить пользовательский стиль линии.

```java
public static void AddFootNote() {
    // создать экземпляр Document
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Демо");
    t.setFootNote(note);

    // создать экземпляр TextFragment
    TextFragment text = new TextFragment("Привет, мир");
    // установить значение FootNote для TextFragment
    text.setFootNote(new Note("сноска для тестового текста 1"));
    // добавить TextFragment в коллекцию абзацев первой страницы документа
    page.getParagraphs().add(text);
    // создать второй TextFragment
    text = new TextFragment("Aspose.Pdf for Java");
    // установить FootNote для второго текстового фрагмента
    text.setFootNote(new Note("сноска для тестового текста 2"));
    // добавить второй текстовый фрагмент в коллекцию абзацев PDF файла
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


Мы можем установить форматирование метки сноски (идентификатор заметки) с использованием объекта TextState следующим образом:

```java
public static void AddCustomFootNoteLabel() {
    // создать экземпляр документа
    Document document = new Document(_dataDir + "sample.pdf");

    Page page = document.getPages().get_Item(1);
    TextFragmentAbsorber tfa = new TextFragmentAbsorber("Portable Document Format");
    tfa.visit(page);

    TextFragment t = tfa.getTextFragments().get_Item(1);
    Note note = new Note();
    note.setText("Демо");
    t.setFootNote(note);

    // создать экземпляр TextFragment
    TextFragment text = new TextFragment("Привет, мир");
    // установить значение сноски для TextFragment
    text.setFootNote(new Note("сноска для тестового текста 1"));
    text.getFootNote().setText("21");
    TextState ts = new TextState();
    ts.setForegroundColor(Color.getBlue());
    ts.setFontStyle(FontStyles.Italic);
    text.getFootNote().setTextState(ts);

    // добавить TextFragment в коллекцию абзацев первой страницы документа
    page.getParagraphs().add(text);
    // создать второй TextFragment
    text = new TextFragment("Aspose.Pdf для Java");
    // установить сноску для второго текстового фрагмента
    text.setFootNote(new Note("сноска для тестового текста 2"));
    // добавить второй текстовый фрагмент в коллекцию абзацев PDF файла
    page.getParagraphs().add(text);

    document.save(_dataDir + "sample_footnote.pdf");
}
```


### Настройка метки сноски

По умолчанию номер сноски увеличивается, начиная с 1. Однако у нас может быть требование установить пользовательскую метку сноски. Чтобы выполнить это требование, попробуйте использовать следующий фрагмент кода

```java
public static void CustomFootNote_Label() {
    // Создайте экземпляр Document
    Document document = new Document();
    // Добавьте страницу в коллекцию страниц PDF
    Page page = document.getPages().add();
    // Создайте объект GraphInfo
    GraphInfo graph = new GraphInfo();
    // Установите ширину линии равной 2
    graph.setLineWidth(2);
    // Установите цвет для объекта graph
    graph.setColor(Color.getRed());
    // Установите значение массива тире равным 3
    graph.setDashArray(new int[] { 3 });
    // Установите значение фазы тире равным 1
    graph.setDashPhase(1);
    // Установите стиль линии сноски для страницы как graph
    page.setNoteLineStyle(graph);

    // Создайте экземпляр TextFragment
    TextFragment text = new TextFragment("Hello World");
    // Установите значение сноски для TextFragment
    text.setFootNote(new Note("сноска для тестового текста 1"));
    // Укажите пользовательскую метку для сноски
    text.getFootNote().setText(" Aspose(2021)");
    // Добавьте TextFragment в коллекцию абзацев первой страницы документа
    page.getParagraphs().add(text);

    document.save(_dataDir + "CustomizeFootNoteLabel_out.pdf");
}
```


## Добавление изображения и таблицы в сноску

В более ранних версиях поддержка сносок была предоставлена, но она применялась только к объекту TextFragment. Однако, начиная с версии Aspose.PDF for Java 10.7.0, вы также можете добавлять сноски к другим объектам внутри PDF-документа, таким как таблицы, ячейки и т. д. Следующий фрагмент кода показывает шаги для добавления сноски к объекту TextFragment, а затем добавления изображения и объекта таблицы в коллекцию абзацев раздела сноски.

```java
public static void AddingImageAndTableToFootnote() {
    // Создайте экземпляр документа
    Document document = new Document();
    // Добавьте страницу в коллекцию страниц PDF
    Page page = document.getPages().add();
    // Создайте экземпляр TextFragment
    TextFragment text = new TextFragment("Hello World");

    page.getParagraphs().add(text);

    text.setFootNote(new Note());
    Image image = new Image();
    image.setFile(_dataDir + "aspose-logo.jpg");
    image.setFixHeight(20);
    text.getFootNote().getParagraphs().add(image);
    TextFragment footNote = new TextFragment("footnote text");
    footNote.getTextState().setFontSize(20);
    footNote.setInLineParagraph(true);
    text.getFootNote().getParagraphs().add(footNote);
    Table table = new Table();
    table.getRows().add().getCells().add().getParagraphs().add(new TextFragment("Row 1 Cell 1"));
    text.getFootNote().getParagraphs().add(table);

    page.getParagraphs().add(text);

    document.save(_dataDir + "AddImageAndTable_out.pdf");
}
```


## Как создать Концевые Сноски

Концевая сноска — это ссылка на источник, которая отсылает читателей к определенному месту в конце работы, где они могут узнать источник информации или слов, процитированных или упомянутых в работе. При использовании концевых сносок цитируемое или перефразированное предложение или обобщенный материал сопровождаются верхним индексом.

Следующий пример демонстрирует, как добавить концевую сноску на страницу PDF.

```java
public static void HowToCreateEndNotes() {
    Document doc = new Document();
    // добавить страницу в коллекцию страниц PDF
    Page page = doc.getPages().add();
    // создать экземпляр TextFragment
    TextFragment text = new TextFragment("Hello World");
    // установить значение концевой сноски для TextFragment
    text.setEndNote(new Note("пример концевой сноски"));
    // указать пользовательскую метку для концевой сноски
    text.getEndNote().setText(" Aspose(2021)");
    // добавить TextFragment в коллекцию абзацев первой страницы документа
    page.getParagraphs().add(text);
    // сохранить PDF файл
    doc.save(_dataDir + "EndNote.pdf");
}
```


## Текст и изображение как встроенный абзац

Макет PDF-файла по умолчанию — потоковый макет (слева направо, сверху вниз). Следовательно, каждый новый элемент, добавляемый в PDF-файл, добавляется в нижнем правом потоке. Однако может возникнуть необходимость отображать различные элементы страницы, такие как изображение и текст, на одном уровне (один за другим). Один из подходов заключается в создании экземпляра таблицы и добавлении обоих элементов в отдельные ячейки. Однако другой подход может заключаться в использовании встроенного абзаца. Установив для свойства IsInLineParagraph изображение и текст значение true, эти абзацы будут отображаться как встроенные с другими элементами страницы.

Следующий фрагмент кода показывает, как добавить текст и изображение как встроенные абзацы в PDF-файл.

```java
 public static void TextAndImageAsInLineParagraph() {
    // Создать экземпляр Document
    Document doc = new Document();
    // Добавить страницу в коллекцию страниц экземпляра Document
    Page page = doc.getPages().add();
    // Создать TextFragment
    TextFragment text = new TextFragment("Hello World.. ");
    // Добавить текстовый фрагмент в коллекцию абзацев объекта Page
    page.getParagraphs().add(text);
    // Создать экземпляр изображения
    Image image = new Image();
    // Установить изображение как встроенный абзац, чтобы оно появилось сразу после
    // предыдущего объекта абзаца (TextFragment)
    image.setInLineParagraph (true);
    // Указать путь к файлу изображения
    image.setFile(_dataDir + "aspose-logo.jpg");
    // Установить высоту изображения (необязательно)
    image.setFixHeight(30);
    // Установить ширину изображения (необязательно)
    image.setFixWidth(100);
    // Добавить изображение в коллекцию абзацев объекта страницы
    page.getParagraphs().add(image);
    // Повторно инициализировать объект TextFragment с другим содержимым
    text = new TextFragment(" Hello Again..");
    // Установить TextFragment как встроенный абзац
    text.setInLineParagraph (true);
    // Добавить вновь созданный TextFragment в коллекцию абзацев страницы
    page.getParagraphs().add(text);
    
    doc.save(_dataDir+"TextAndImageAsParagraph_out.pdf");
}
```


## Указание межсимвольного интервала при добавлении текста

Текст можно добавить в коллекцию абзацев PDF-файла, используя экземпляр TextFragment или объект TextParagraph, и даже можно поставить текст в PDF, используя класс TextStamp. При добавлении текста может возникнуть необходимость указать межсимвольный интервал для текстовых объектов. Для выполнения этого требования введено новое свойство под названием CharacterSpacing. Пожалуйста, ознакомьтесь со следующими подходами для выполнения этого требования.

Следующие подходы показывают шаги по указанию межсимвольного интервала при добавлении текста в PDF-документ.

## Использование TextBuilder и TextFragment

```java
 public static void CharacterSpacing_TextFragment(){
    // Создать экземпляр документа
    Document pdfDocument = new Document();
    // Добавить страницу в коллекцию страниц документа
    Page page = pdfDocument.getPages().add();
    // Создать экземпляр TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // Создать экземпляр текстового фрагмента с примерным содержимым
    TextFragment wideFragment = new TextFragment("Текст с увеличенным межсимвольным интервалом");
    wideFragment.getTextState().applyChangesFrom(new TextState("Arial", 12));
    // Указать межсимвольный интервал для TextFragment
    wideFragment.getTextState().setCharacterSpacing(2.0f);
    // Указать позицию TextFragment
    wideFragment.setPosition(new Position(100, 650));
    // Добавить TextFragment в экземпляр TextBuilder
    builder.appendText(wideFragment);        
    // Сохранить получившийся PDF-документ.
    pdfDocument.save(_dataDir+ "CharacterSpacingUsingTextBuilderAndFragment_out.pdf");
}
```


## Использование TextBuilder и TextParagraph

```java
public static void CharacterSpacing_TextParagraph() {
    // Создание экземпляра документа
    Document pdfDocument = new Document();
    // Добавление страницы в коллекцию страниц документа
    Page page = pdfDocument.getPages().add();
    // Создание экземпляра TextBuilder
    TextBuilder builder = new TextBuilder(page);
    // Создание экземпляра TextParagraph
    TextParagraph paragraph = new TextParagraph();
    // Создание экземпляра TextState для указания имени и размера шрифта
    TextState state = new TextState("Arial", 12);
    // Указание межсимвольного интервала
    state.setCharacterSpacing (1.5f);
    // Добавление текста в объект TextParagraph
    paragraph.appendLine("Это абзац с межсимвольным интервалом", state);
    // Указание позиции для TextParagraph
    paragraph.setPosition (new Position(100, 550));
    // Добавление TextParagraph в экземпляр TextBuilder
    builder.appendParagraph(paragraph);
    // Сохранение итогового PDF документа.
    pdfDocument.save(_dataDir + "CharacterSpacingUsingTextBuilderAndParagraph_out.pdf");
}
```


## Использование TextStamp

```java
public static void CharacterSpacing_TextStamp() {
    // Создать экземпляр документа
    Document pdfDocument = new Document();
    // Добавить страницу в коллекцию страниц документа
    Page page = pdfDocument.getPages().add();
    // Создать экземпляр TextStamp с образцом текста
    TextStamp stamp = new TextStamp("Это текстовый штамп с межсимвольным интервалом");
    // Указать имя шрифта для объекта Stamp
    stamp.getTextState().setFont(FontRepository.findFont("Arial"));
    // Указать размер шрифта для TextStamp
    stamp.getTextState().setFontSize(12);
    // Указать межсимвольный интервал как 1f
    stamp.getTextState().setCharacterSpacing(1f);
    // Установить отступ по оси X для штампа
    stamp.setXIndent(100);
    // Установить отступ по оси Y для штампа
    stamp.setYIndent(500);
    // Добавить текстовый штамп на страницу
    stamp.put(page);        
    // Сохранить результирующий PDF документ.
    pdfDocument.save(_dataDir+"CharacterSpacingUsingTextStamp_out.pdf");        
}
```

## Создание PDF документа с несколькими колонками

В журналах и газетах чаще всего мы видим, что новости отображаются в нескольких колонках на одной странице, в отличие от книг, где текстовые абзацы обычно печатаются на всей странице от левого до правого края.
 Многие приложения для обработки документов, такие как Microsoft Word и Adobe Acrobat Writer, позволяют пользователям создавать несколько колонок на одной странице и затем добавлять в них данные.

Aspose.PDF for Java также предлагает возможность создавать несколько колонок на страницах PDF-документов. Для создания PDF-файла с несколькими колонками мы можем использовать класс Aspose.Pdf.FloatingBox, так как он предоставляет свойство ColumnInfo.ColumnCount для указания количества колонок внутри FloatingBox, а также можем указать расстояние между колонками и ширину колонок, используя свойства ColumnInfo.ColumnSpacing и ColumnInfo.ColumnWidths соответственно. Обратите внимание, что FloatingBox является элементом внутри модели объекта документа, и он может иметь устаревшее позиционирование по сравнению с относительным позиционированием (например, Текст, Графика, Изображение и т.д.).
Column spacing означает пространство между колонками, и по умолчанию расстояние между колонками составляет 1,25 см. Если ширина колонок не указана, то Aspose.PDF for Java автоматически рассчитывает ширину для каждой колонки в зависимости от размера страницы и расстояния между колонками.

Ниже приведен пример, демонстрирующий создание двух колонок с объектами Graphs (Line), которые добавляются в коллекцию параграфов FloatingBox, который затем добавляется в коллекцию параграфов экземпляра Page.

```java
public static void CreateMultiColumn() {
    Document doc = new Document();
    // Указываем информацию о левом поле для PDF файла
    doc.getPageInfo().getMargin().setLeft(40);
    
    // Указываем информацию о правом поле для PDF файла
    doc.getPageInfo().getMargin().setRight(40);
    
    Page page = doc.getPages().add();

    com.aspose.pdf.drawing.Graph graph1 = new com.aspose.pdf.drawing.Graph(500, 2);
    
    // Добавляем линию в коллекцию параграфов объекта раздела
    page.getParagraphs().add(graph1);

    // Указываем координаты для линии
    float[] posArr = new float[] { 1, 2, 500, 2 };
    com.aspose.pdf.drawing.Line l1 = new com.aspose.pdf.drawing.Line(posArr);
    graph1.getShapes().add(l1);
    
    // Создаем строковые переменные с текстом, содержащим html теги
    String s = "<span style=\"font-family: \"Times New Roman\", Times, serif;\" font-size=\"14pt\" \">"
                +"<strong> Как избежать денежных мошенничеств</<strong> </span>";
    
    // Создаем текстовые параграфы, содержащие HTML текст

    HtmlFragment heading_text = new HtmlFragment(s);
    page.getParagraphs().add(heading_text);

    FloatingBox box = new FloatingBox();
    
    // Добавляем четыре колонки в раздел
    box.getColumnInfo().setColumnCount(2);
    // Устанавливаем расстояние между колонками
    box.getColumnInfo().setColumnSpacing("5");

    box.getColumnInfo().setColumnWidths("105 105");
    TextFragment text1 = new TextFragment("Автор: Googler (Официальный блог Google)");
    text1.getTextState().setFontSize (8);
    text1.getTextState().setLineSpacing (2);
    text1.getTextState().setFontSize (10);
    text1.getTextState().setFontStyle (FontStyles.Italic);

    box.getParagraphs().add(text1);
    
    // Создаем объект графиков для рисования линии
    com.aspose.pdf.drawing.Graph graph2 = new com.aspose.pdf.drawing.Graph(50, 10);
    // Указываем координаты для линии
    float[] posArr2 = new float[] { 1, 10, 100, 10 };
    com.aspose.pdf.drawing.Line l2 = new com.aspose.pdf.drawing.Line(posArr2);
    graph2.getShapes().add(l2);

    // Добавляем линию в коллекцию параграфов объекта раздела
    box.getParagraphs().add(graph2);

    TextFragment text2 = new TextFragment("Сед augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. "
    +"Сед quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue."
    +"Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur "
    +"ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean "
    +"posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. "
    +"Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, "
    +"risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam "
    +"luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, "
    +"sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, "
    +"pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut,"
    +"iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus "
    +"mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla."
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam,"
    +"iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique"
    +"ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    +"Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. "
    +"Praesent porttitor turpis eleifend ante. Morbi sodales.");
    box.getParagraphs().add(text2);

    page.getParagraphs().add(box);

    // Сохраняем PDF файл
    doc.save(_dataDir + "CreateMultiColumnPdf_out.pdf");        
}
```


## Работа с пользовательскими табуляторами

Табуляция — это остановка для табуляции. В текстовых редакторах каждая строка содержит несколько табуляций, расположенных через регулярные интервалы (например, каждые полдюйма). Однако они могут быть изменены, так как большинство текстовых редакторов позволяют устанавливать табуляции в любом месте. Когда вы нажимаете клавишу Tab, курсор или точка вставки переходит к следующей табуляции, которая сама по себе невидима. Хотя табуляции не существуют в текстовом файле, текстовый редактор отслеживает их, чтобы правильно реагировать на клавишу Tab.

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) позволяет разработчикам использовать пользовательские табуляции в PDF-документах. Класс Aspose.Pdf.Text.TabStop используется для установки пользовательских остановок TAB в классе [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment).

[Aspose.PDF for Java](https://docs.aspose.com/pdf/java/) также предлагает некоторые предопределенные типы лидеров табуляции в виде перечисления, названного TabLeaderType, чьи предопределенные значения и их описания приведены ниже:

|**Tab Leader Type**|**Описание**|
| :- | :- |
|None|Без лидера табуляции|
|Solid|Сплошной лидер табуляции|
|Dash|Штриховой лидер табуляции|
|Dot|Точечный лидер табуляции|

Вот пример, как установить пользовательские остановки табуляции.

```java
public static void CustomTabStops() {
    Document pdfdocument = new Document();
    Page page = pdfdocument.getPages().add();

    com.aspose.pdf.TabStops ts = new com.aspose.pdf.TabStops();
    com.aspose.pdf.TabStop ts1 = ts.add(100);
    ts1.setAlignmentType(TabAlignmentType.Right);
    ts1.setLeaderType (TabLeaderType.Solid);
    
    com.aspose.pdf.TabStop ts2 = ts.add(200);
    ts2.setAlignmentType(TabAlignmentType.Center);
    ts2.setLeaderType (TabLeaderType.Dash);

    com.aspose.pdf.TabStop ts3 = ts.add(300);
    ts3.setAlignmentType(TabAlignmentType.Left);
    ts3.setLeaderType (TabLeaderType.Dot);

    TextFragment header = new TextFragment("Это пример формирования таблицы с остановками табуляции", ts);
    TextFragment text0 = new TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts);

    TextFragment text1 = new TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts);
    TextFragment text2 = new TextFragment("#$TABdata21 ", ts);
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data22 "));
    text2.getSegments().add(new TextSegment("#$TAB"));
    text2.getSegments().add(new TextSegment("data23"));

    page.getParagraphs().add(header);
    page.getParagraphs().add(text0);
    page.getParagraphs().add(text1);
    page.getParagraphs().add(text2);
    
    pdfdocument.save(_dataDir + "CustomTabStops_out.pdf"); 
}
```


## Как добавить прозрачный текст в PDF

Файл PDF содержит объекты Изображение, Текст, График, Вложения, Аннотации, и при создании TextFragment вы можете установить информацию о переднем и заднем фоне, а также форматирование текста. Aspose.PDF для Java поддерживает возможность добавления текста с альфа-каналом цвета. Следующий фрагмент кода показывает, как добавить текст с прозрачным цветом.

```java
  public static void AddTransparentText() {
    // Создать экземпляр документа
    Document pdfdocument = new Document();
    // Создать страницу для коллекции страниц PDF-файла
    Page page = pdfdocument.getPages().add();

    // Создать объект Graph
    Graph canvas = new Graph(100, 400);
    // Создать экземпляр прямоугольника с определенными размерами
    com.aspose.pdf.drawing.Rectangle rect = new com.aspose.pdf.drawing.Rectangle(100, 100, 400, 400);
    // Создать объект цвета из альфа-канала цвета
    int alpha = 10;
    int green = 0;
    int red = 100;
    int blue = 0;
    Color alphaColor = Color.fromArgb(alpha, red, green, blue);
    rect.getGraphInfo().setFillColor(alphaColor);
    // Добавить прямоугольник в коллекцию фигур объекта Graph
    canvas.getShapes().add(rect);
    // Добавить объект графа в коллекцию параграфов объекта страницы
    page.getParagraphs().add(canvas);
    // Установить значение, чтобы не изменять позицию для объекта графа
    canvas.setChangePosition(false);

    // Создать экземпляр TextFragment с примерным значением
    TextFragment text = new TextFragment(
            "прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст ");
    // Создать объект цвета из альфа-канала
    alpha = 30;
    alphaColor = Color.fromArgb(alpha, red, green, blue);
    // Установить информацию о цвете для экземпляра текста
    text.getTextState().setForegroundColor (alphaColor);
    // Добавить текст в коллекцию параграфов экземпляра страницы
    page.getParagraphs().add(text);
    
    pdfdocument.save(_dataDir + "AddTransparentText_out.pdf");
}
```


## Указание межстрочного интервала для шрифтов

У каждого шрифта есть абстрактный квадрат, высота которого является предполагаемым расстоянием между строками текста в одном и том же размере шрифта. Этот квадрат называется `em square`, и это сетка дизайна, на которой определены контуры глифов. Многие буквы входного шрифта имеют точки, которые расположены за пределами `em square` шрифта, поэтому для правильного отображения шрифта необходимо использовать специальную настройку. Объект TextFragment имеет набор параметров форматирования текста, которые доступны через метод [TextState.getFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentState#getFormattingOptions--).
Этот метод возвращает класс [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions).
 Этот класс имеет перечисление [LineSpacingMode](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions.LineSpacingMode), которое предназначено для определенных шрифтов, например, входного шрифта "HPSimplified.ttf". Также класс [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions) имеет метод [setLineSpacing](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions#setLineSpacing-int-) типа LineSpacingMode. Вам просто нужно установить LineSpacing в LineSpacingMode.FullSize. Пример кода для правильного отображения шрифта будет следующим:

```java
public static void SpecifyLineSpacingForFonts() {
    String fontFile = _dataDir + "hp-simplified.ttf";
    // Загрузить входной PDF файл
    Document doc = new Document();
    // Создать TextFormattingOptions с LineSpacingMode.FullSize
    TextFormattingOptions formattingOptions = new TextFormattingOptions();
    formattingOptions.setLineSpacing(TextFormattingOptions.LineSpacingMode.FullSize);

    // Создать объект построителя текста для первой страницы документа
    // TextBuilder textBuilder = new TextBuilder(doc.Pages[1]);
    // Создать фрагмент текста с примером строки
    TextFragment textFragment = new TextFragment("Hello world");

    // Загрузить шрифт TrueType в объект потока
    FileInputStream fontStream;
    try {
        fontStream = new FileInputStream(fontFile);
    } catch (FileNotFoundException e) {
        e.printStackTrace();
        return;
    }

    // Установить имя шрифта для текстовой строки
    textFragment.getTextState().setFont(FontRepository.openFont(fontStream, FontTypes.TTF));
    // Указать позицию для текстового фрагмента
    textFragment.setPosition(new Position(100, 600));
    // Установить TextFormattingOptions текущего фрагмента в предопределенный (указывающий на
    // LineSpacingMode.FullSize)
    textFragment.getTextState().setFormattingOptions(formattingOptions);
    // Добавить текст в TextBuilder, чтобы он мог быть размещен поверх PDF файла
    // textBuilder.AppendText(textFragment);
    Page page = doc.getPages().add();
    page.getParagraphs().add(textFragment);

    // Сохранить результирующий PDF документ
    doc.save(_dataDir + "SpecifyLineSpacing_out.pdf");
}
```

## Получение ширины текста динамически

Иногда требуется динамически получить ширину текста. Aspose.PDF для Java включает два метода для измерения ширины строки. Вы можете вызвать метод [MeasureString](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState#measureString--) из классов com.aspose.pdf.Font или com.aspose.pdf.TextState (или обоих). Пример кода ниже показывает, как использовать эту функциональность.

```java
public static void GetTextWidthDynamicaly() {
    Font font = FontRepository.findFont("Arial");
    TextState ts = new TextState();
        ts.setFont(font);
        ts.setFontSize(14);
        if (Math.abs(font.measureString("A", 14) - 9.337) > 0.001)
            System.out.println("Неожиданное измерение строки шрифта!");

        if (Math.abs(ts.measureString("z") - 7.0) > 0.001)
        System.out.println("Неожиданное измерение строки шрифта!");

        for (char c = 'A'; c <= 'z'; c++)
        {
            double fnMeasure = font.measureString(String.valueOf(c), 14);
            double tsMeasure = ts.measureString(String.valueOf(c));

            if (Math.abs(fnMeasure - tsMeasure) > 0.001)
                System.out.println("Измерение строки шрифта и состояния не совпадает!");
        }
}
```