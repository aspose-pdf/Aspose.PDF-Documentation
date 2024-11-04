---
title: Форматирование текста внутри PDF
linktitle: Форматирование текста внутри PDF
type: docs
weight: 30
url: /java/text-formatting-inside-pdf/
description: Эта страница объясняет, как форматировать текст внутри вашего PDF файла. Это включает добавление отступа строки, добавление границы текста, подчеркивание текста, добавление границы вокруг добавленного текста, выравнивание текста для содержимого плавающего блока и т.д.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Как добавить отступ строки в PDF

Aspose.PDF для Java предлагает свойство SubsequentLinesIndent в классе [TextFormattingOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFormattingOptions). Которое может использоваться для указания отступа строки в сценариях генерации PDF с использованием TextFragment и коллекции Paragraphs.

Пожалуйста, используйте следующий фрагмент кода для использования этого свойства:

```java
public static void AddLineIndentToPDF() {
        // Создать новый объект документа
        Document document = new Document();
        Page page = document.getPages().add();

        TextFragment text = new TextFragment(
                "A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

        // Инициализировать TextFormattingOptions для текстового фрагмента и указать
        // значение SubsequentLinesIndent
        TextFormattingOptions textOptions = new TextFormattingOptions();
        textOptions.setSubsequentLinesIndent(20);
        text.getTextState().setFormattingOptions(textOptions);

        page.getParagraphs().add(text);

        text = new TextFragment("Line2");
        page.getParagraphs().add(text);

        text = new TextFragment("Line3");
        page.getParagraphs().add(text);

        text = new TextFragment("Line4");
        page.getParagraphs().add(text);

        text = new TextFragment("Line5");
        page.getParagraphs().add(text);

        document.save(_dataDir + "SubsequentIndent_out.pdf");
    }
```


## Как добавить границу к тексту

Следующий фрагмент кода показывает, как добавить границу к тексту, используя TextBuilder и установку метода DrawTextRectangleBorder из TextState:

```java
public static void AddTextBorder() {
    // Создать новый объект документа
    Document pdfDocument = new Document();
    // Получить конкретную страницу
    Page pdfPage = pdfDocument.getPages().add();
    // Создать текстовый фрагмент
    TextFragment textFragment = new TextFragment("основной текст");
    textFragment.setPosition(new Position(100, 600));
    // Установить свойства текста
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());
    // Используйте setStrokingColor для рисования границы (обводки) вокруг текстового прямоугольника
    textFragment.getTextState().setStrokingColor (Color.getDarkRed());
    // Используйте метод setDrawTextRectangleBorder, чтобы установить значение true
    textFragment.getTextState().setDrawTextRectangleBorder(true);
    TextBuilder tb = new TextBuilder(pdfPage);
    tb.appendText(textFragment);
    // Сохранить документ
    pdfDocument.save(_dataDir + "PDFWithTextBorder_out.pdf");
}
```


## Как добавить подчеркнутый текст

Следующий фрагмент кода показывает, как добавить подчеркнутый текст при создании нового PDF файла.

```java
public static void AddUnderlineText(){
    // Создать объект документации
    Document pdfDocument = new Document();
    // Добавить страницу в PDF документ
    Page page = pdfDocument.getPages().add();
    // Создать TextBuilder для первой страницы
    TextBuilder tb = new TextBuilder(page);
    // TextFragment с примером текста
    TextFragment fragment = new TextFragment("Текст с подчеркиванием");
    // Установить шрифт для TextFragment
    fragment.getTextState().setFont (FontRepository.findFont("Arial"));
    fragment.getTextState().setFontSize (10);
    // Установить форматирование текста как подчеркнутое
    fragment.getTextState().setUnderline(true);
    // Указать позицию, где должен быть размещен TextFragment
    fragment.setPosition (new Position(10, 800));
    // Добавить TextFragment в PDF файл
    tb.appendText(fragment);

    // Сохранить полученный PDF документ.
    pdfDocument.save(_dataDir + "AddUnderlineText_out.pdf");
}
```


## Как добавить рамку вокруг добавленного текста

Вы можете контролировать внешний вид добавленного текста. Пример ниже показывает, как добавить рамку вокруг текста, который вы добавили, нарисовав вокруг него прямоугольник. Узнайте больше о классе [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor).

```java
public static void AddBorderAroundAddedText() {
    PdfContentEditor editor = new PdfContentEditor();
    editor.bindPdf(_dataDir + "input.pdf");
    LineInfo lineInfo = new LineInfo();
    lineInfo.setLineWidth(2);
    lineInfo.setVerticeCoordinate (new float[] { 0, 0, 100, 100, 50, 100 });
    lineInfo.setVisibility(true);
    editor.createPolygon(lineInfo, 1, new java.awt.Rectangle(0, 0, 0, 0), "");

    // Сохранить результирующий PDF документ.
    editor.save(_dataDir + "AddingBorderAroundAddedText_out.pdf");
}
```

## Как добавить перевод строки

TextFragment не поддерживает перевод строки внутри текста.
 Однако, чтобы добавить текст с переводом строки, используйте TextFragment с TextParagraph:

- используйте "\r\n" или Environment.NewLine в TextFragment вместо одиночного “\n”;
- создайте объект TextParagraph. Это добавит текст с разделением строк;
- добавьте TextFragment с TextParagraph.AppendLine;
- добавьте TextParagraph с TextBuilder.AppendParagraph.
Пожалуйста, используйте приведенный ниже фрагмент кода.

```java
public static void AddNewLineFeed() {        
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    // Инициализируйте новый TextFragment с текстом, содержащим необходимые маркеры новой строки
    TextFragment textFragment = new TextFragment("Applicant Name: " + System.lineSeparator() + " Joe Smoe");

    // Установите свойства фрагмента текста, если необходимо
    textFragment.getTextState().setFontSize (12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor (Color.getLightGray());
    textFragment.getTextState().setForegroundColor (Color.getRed());

    // Создайте объект TextParagraph
    TextParagraph par = new TextParagraph();

    // Добавьте новый TextFragment в абзац
    par.appendLine(textFragment);

    // Установите позицию абзаца
    par.setPosition (new Position(100, 600));

    // Создайте объект TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // Добавьте TextParagraph, используя TextBuilder
    textBuilder.appendParagraph(par);

    // Сохраните результирующий PDF-документ.
    pdfDocument.save(_dataDir + "AddNewLineFeed_out.pdf");
}
```

## Как добавить зачеркнутый текст

Класс TextState предоставляет возможности для установки форматирования для TextFragments, размещаемых внутри PDF документа. Вы можете использовать этот класс, чтобы устанавливать форматирование текста как жирный, курсив, подчеркивание, и начиная с этого релиза, API предоставил возможность отмечать форматирование текста как зачеркнутое. Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы добавить TextFragment с форматированием зачеркнутого текста.

Пожалуйста, используйте полный фрагмент кода:

```java
public static void AddStrikeOutText(){
    // Открыть документ
    Document pdfDocument = new Document();
    // Получить конкретную страницу
    Page pdfPage = (Page)pdfDocument.getPages().add();

    // Создать фрагмент текста
    TextFragment textFragment = new TextFragment("main text");
    textFragment.setPosition (new Position(100, 600));

    // Установить свойства текста
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("DejaVu Serif"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());
    // использовать метод setStrikeOut для включения зачеркнутого текста
    textFragment.getTextState().setStrikeOut(true);
    // Отметить текст как жирный
    textFragment.getTextState().setFontStyle(FontStyles.Bold);

    // Создать объект TextBuilder
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // Добавить фрагмент текста на страницу PDF
    textBuilder.appendText(textFragment);

    // Сохранить итоговый PDF документ.
    pdfDocument.save(_dataDir + "AddStrikeOutText_out.pdf");        
}
```


## Применение градиентной заливки к тексту

Форматирование текста было дополнительно улучшено в API для сценариев редактирования текста, и теперь вы можете добавлять текст с цветовым пространством шаблона внутри PDF-документа. Класс com.aspose.pdf.Color был дополнительно улучшен путем введения нового метода `setPatternColorSpace`, который можно использовать для указания цветов заливки для текста. Этот новый метод добавляет различную градиентную заливку к тексту, например, аксиальную заливку, радиальную (тип 3) заливку, как показано в следующем фрагменте кода:

```java
public static void ApplyGradientShading() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("always print correctly");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientAxialShading(Color.getRed(), Color.getBlue()));

    // Создаем новый цвет с цветовыми пространствами шаблона
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```


Для применения радиального градиента, вы можете использовать метод `setPatternColorSpace`, равный `GradientRadialShading(startingColor, endingColor)` в указанном выше фрагменте кода.

```java
public static void ApplyGradientShadingRadial() {
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("всегда печатайте правильно");
    pdfDocument.getPages().accept(absorber);

    TextFragment textFragment = absorber.getTextFragments().get_Item(1);

    Color foregroundColor = new com.aspose.pdf.Color();
    foregroundColor.setPatternColorSpace(new GradientRadialShading(Color.getRed(), Color.getBlue()));

    // Создать новый цвет с шаблонным цветовым пространством
    textFragment.getTextState().setForegroundColor (foregroundColor);

    textFragment.getTextState().setUnderline(true);

    pdfDocument.save(_dataDir + "text_out.pdf");
}
```

## Как выровнять текст относительно плавающего содержимого

Aspose.PDF поддерживает установку выравнивания текста для содержимого внутри элемента Floating Box.
 Свойства выравнивания экземпляра Aspose.Pdf.FloatingBox могут быть использованы для достижения этого, как показано в следующем примере кода.

```java
public static void AlignTextToFloatContent() {
    Document pdfDocument = new Document();
    Page page = pdfDocument.getPages().add();

    FloatingBox floatBox = new FloatingBox(100, 100);
    floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
    floatBox.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
    floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
    
    page.getParagraphs().add(floatBox);

    FloatingBox floatBox1 = new FloatingBox(100, 100);
    floatBox1.setVerticalAlignment(VerticalAlignment.Center);
    floatBox1.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox1.getParagraphs().add(new TextFragment("FloatingBox_center"));
    floatBox1.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox1);

    FloatingBox floatBox2 = new FloatingBox(100, 100);
    floatBox2.setVerticalAlignment(VerticalAlignment.Top);
    floatBox2.setHorizontalAlignment (HorizontalAlignment.Right);
    floatBox2.getParagraphs().add(new TextFragment("FloatingBox_top"));
    floatBox2.setBorder (new BorderInfo(BorderSide.All, Color.getBlue()));
    page.getParagraphs().add(floatBox2);

    pdfDocument.save(_dataDir + "FloatingBox_alignment_review_out.pdf");        
}
```