---
title: Замена текста в PDF
linktitle: Замена текста в PDF
type: docs
weight: 40
url: /ru/java/replace-text-in-a-pdf-document/
description: Узнайте больше о различных способах замены и удаления текста из PDF. Aspose.PDF позволяет заменять текст в определенной области или с использованием регулярного выражения.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Замена текста на всех страницах PDF-документа

{{% alert color="primary" %}}

Вы можете попробовать найти и заменить текст в документе с помощью Aspose.PDF и получить результаты онлайн по этой [ссылке](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Чтобы заменить текст на всех страницах PDF-документа с использованием [Aspose.PDF для Java](https://products.aspose.com/pdf/java):

1. Сначала используйте [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber), чтобы найти конкретную фразу для замены.

1. Затем, пройдите через все [TextFragments](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber#getTextFragments--) для замены текста и изменения любых других атрибутов.
1. Наконец, сохраните выходной PDF, используя метод [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save--) класса Document.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleReplaceText {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    public static void ReplaceTextOnAllPages() {
        Document pdfDocument = new Document(_dataDir+"sample.pdf");

        // Создайте объект TextAbsorber для поиска всех экземпляров входной поисковой фразы
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Web");
        
        // Примените абсорбер для первой страницы документа
        pdfDocument.getPages().accept(textFragmentAbsorber);
        
        // Получите извлеченные текстовые фрагменты в коллекцию
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
        
        // Пройдитесь по фрагментам
        for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
            // Обновите текст и другие свойства
            textFragment.setText("World Wide Web");
            textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
            textFragment.getTextState().setFontSize(12);
            textFragment.getTextState().setForegroundColor(Color.getBlue());
            textFragment.getTextState().setBackgroundColor(Color.getGray());
        }
        // Сохраните обновленный PDF файл
        pdfDocument.save(_dataDir+"Updated_Text.pdf");
    }
}
```


## Заменить текст в определенной области страницы

Чтобы заменить текст в определенной области страницы, сначала нам нужно создать объект TextFragmentAbsorber, указать область страницы, используя [TextSearchOptions.setRectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions#setRectangle-com.aspose.pdf.Rectangle-), а затем пройтись по всем TextFragments для замены текста. После завершения этих операций нам нужно только сохранить выходной PDF, используя метод save объекта Document.

Следующий фрагмент кода показывает, как заменить текст на всех страницах PDF-документа.

```java
 public static void ReplaceTextInParticularRegion(){
    // загрузить PDF файл
    Document pdfDocument = new Document(_dataDir+"sample.pdf");

    // создать объект TextFragment Absorber
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("PDF");

    // искать текст в пределах границ страницы
    textFragmentAbsorber.getTextSearchOptions().setLimitToPageBounds(true);

    // указать область страницы для параметров поиска текста
    textFragmentAbsorber.getTextSearchOptions().setRectangle(new Rectangle(100, 700, 400, 770));

    // искать текст с первой страницы PDF файла
    pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);

    // пройтись по отдельным TextFragment
    for(TextFragment tf : textFragmentAbsorber.getTextFragments())
    {
        // заменить текст на "---"
        tf.setText("---");
    }

    // Сохранить обновленный PDF файл
    pdfDocument.save(_dataDir+"Updated_Text.pdf");
}
```


## Замена текста на основе регулярного выражения

Если вы хотите заменить некоторые фразы на основе регулярного выражения, сначала необходимо найти все фразы, соответствующие этому регулярному выражению, используя TextFragmentAbsorber. Вам нужно будет передать регулярное выражение в качестве параметра конструктору TextFragmentAbsorber. Также необходимо создать объект TextSearchOptions, который указывает, используется ли регулярное выражение. Получив совпадающие фразы в TextFragments, вам нужно пройти через все из них и обновить по мере необходимости. Наконец, вам нужно сохранить обновленный PDF, используя метод Save объекта Document.

Следующий фрагмент кода показывает, как заменить текст на основе регулярного выражения.

```java
public static void ReplaceTextWithRegularExpression() {
    // загрузить PDF файл
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    // Создать объект TextAbsorber для поиска всех экземпляров входной поисковой фразы
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); 
    // как 1999-2000

    // Установить параметр поиска текста для указания использования регулярного выражения
    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

    // Принять абсорбер для первой страницы документа
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Получить извлеченные текстовые фрагменты в коллекцию
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Перебрать фрагменты
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Обновить текст и другие свойства
        textFragment.setText("ABCD-EFGH");
        textFragment.getTextState().setFont(FontRepository.findFont("Verdana"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }

    // Сохранить обновленный PDF файл
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


## Замена шрифтов в существующем PDF файле

Aspose.PDF для Java поддерживает возможность замены текста в PDF документе. Однако иногда требуется заменить только шрифт, используемый внутри PDF документа. Вместо замены текста заменяется только используемый шрифт. Один из перегруженных конструкторов TextFragmentAbsorber принимает объект TextEditOptions в качестве аргумента, и мы можем использовать значение RemoveUnusedFonts из перечисления TextEditOptions.FontReplace для достижения наших требований.

Следующий фрагмент кода показывает, как заменить шрифт внутри PDF документа.

```java
public static void ReplaceFonts() {
    // Создать экземпляр объекта Document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Найти фрагменты текста и установить параметры редактирования как удаление неиспользуемых шрифтов
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(
            new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

    // Принять абсорбер для всех страниц документа
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Перебрать все TextFragments
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection)
    {
        String fontName = textFragment.getTextState().getFont().getFontName();
        // если имя шрифта ArialMT, заменить имя шрифта на Arial
        if (fontName.equals("ArialMT")) {
            textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        }
    }

    // Сохранить обновленный PDF файл
    pdfDocument.save(_dataDir + "Updated_Text.pdf");
}
```


### Используйте шрифт на неанглийском языке (японский) при замене текста

Следующий фрагмент кода показывает, как заменить текст японскими символами. Обратите внимание, что для добавления японского текста необходимо использовать шрифт, который поддерживает японские символы (например, MSGothic).

```java
public static void UseNonEnglishFontWhenReplacingText() {

    // Создайте объект Document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Давайте изменим каждое слово "page" на некоторый японский текст с определенным шрифтом
    // TakaoMincho, который может быть установлен в ОС
    // Также это может быть другой шрифт, который поддерживает иероглифы
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("page");

    // Создайте экземпляр параметров поиска текста
    TextSearchOptions searchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(searchOptions);

    // Примите абсорбер для всех страниц документа
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Получите извлеченные текстовые фрагменты в коллекцию
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();
    
    // Переберите фрагменты
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Обновите текст и другие свойства
        textFragment.setText("ファイル");
        textFragment.getTextState().setFont(FontRepository.findFont("MSGothic"));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
    }
    // Сохраните обновленный документ
    pdfDocument.save(_dataDir + "Japanese_Text.pdf");
}
```


## Замена текста должна автоматически переупорядочивать содержимое страницы

Aspose.PDF for Java поддерживает функцию поиска и замены текста внутри PDF файла. Однако недавно некоторые клиенты столкнулись с проблемами при замене текста, когда конкретный TextFragment заменяется на более короткое содержимое, и в результирующем PDF отображаются лишние пробелы, или в случае, если TextFragment заменяется на более длинную строку, слова накладываются на существующее содержимое страницы. Поэтому возникла необходимость ввести механизм, который, когда текст внутри PDF документа заменяется, содержимое должно быть переупорядочено.

Для решения вышеуказанных сценариев, Aspose.PDF for Java был улучшен так, чтобы такие проблемы не возникали при замене текста внутри PDF файла. Следующий фрагмент кода показывает, как заменить текст внутри PDF файла, и содержимое страницы должно быть автоматически переупорядочено.

```java
public static void RearrangeContent() {
    // Загрузить исходный PDF файл
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Создать объект TextFragment Absorber с регулярным выражением
    TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[PDF,Web]");

    TextSearchOptions textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber.setTextSearchOptions(textSearchOptions);
    
    //Вы также можете указать опцию ReplaceAdjustment.WholeWordsHyphenation для переноса текста на следующую или текущую строку
    //если текущая строка становится слишком длинной или короткой после замены:
    //textFragmentAbsorber.getTextReplaceOptions().setReplaceAdjustmentAction(TextReplaceOptions.ReplaceAdjustment.WholeWordsHyphenation);

    // Применить абсорбер для всех страниц документа
    pdfDocument.getPages().accept(textFragmentAbsorber);

    // Получить извлеченные фрагменты текста в коллекцию
    TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

    // Заменить каждый TextFragment
    for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
        // Установить шрифт заменяемого фрагмента текста
        textFragment.getTextState().setFont(FontRepository.findFont("Arial"));
        // Установить размер шрифта
        textFragment.getTextState().setFontSize(10);
        textFragment.getTextState().setForegroundColor(Color.getBlue());
        textFragment.getTextState().setBackgroundColor(Color.getGray());
        // Заменить текст на более длинную строку, чем заполнитель
        textFragment.setText("Это более длинная строка для тестирования этой функции");
    }
    // Сохранить результирующий PDF
    pdfDocument.save(_dataDir + "RearrangeContentsUsingTextReplacement_out.pdf");
}
```


## Отображение заменяемых символов при создании PDF

Заменяемые символы — это специальные символы в строке текста, которые могут быть заменены соответствующим содержимым во время выполнения. Заменяемые символы, которые в настоящее время поддерживаются новой моделью объектов документа из пространства имен Aspose.PDF, это `$P`, `$p,` `\n`, `\r`. Символы `$p` и `$P` используются для работы с нумерацией страниц во время выполнения. `$p` заменяется на номер страницы, на которой находится текущий класс Paragraph. `$P` заменяется на общее количество страниц в документе. При добавлении [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) в коллекцию параграфов PDF-документов, он не поддерживает перевод строки внутри текста. Однако, чтобы добавить текст с переводом строки, пожалуйста, используйте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TeXFragment) с [TextParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextParagraph):

- используйте "\r\n" или Environment.NewLine в TextFragment вместо одиночного "\n";
- создайте объект TextParagraph.
 Он добавит текст с разбивкой на строки;
- добавьте TextFragment с помощью TextParagraph.AppendLine;
- добавьте TextParagraph с помощью TextBuilder.AppendParagraph.

```java
public static void RenderingReplaceableSymbols() {
    // загрузить PDF файл
    Document pdfDocument = new Document(_dataDir + "sample.pdf");
    Page page = pdfDocument.getPages().add();

    // Инициализировать новый TextFragment с текстом, содержащим необходимые маркеры новой строки
    TextFragment textFragment = new TextFragment("Имя заявителя: " + System.lineSeparator() + " Джо Смо");

    // Установить свойства текстового фрагмента, если необходимо
    textFragment.getTextState().setFontSize(12);
    textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
    textFragment.getTextState().setBackgroundColor(Color.getLightGray());
    textFragment.getTextState().setForegroundColor(Color.getRed());

    // Создать объект TextParagraph
    TextParagraph par = new TextParagraph();

    // Добавить новый TextFragment в параграф
    par.appendLine(textFragment);

    // Установить позицию параграфа
    par.setPosition (new Position(100, 600));

    // Создать объект TextBuilder
    TextBuilder textBuilder = new TextBuilder(page);
    // Добавить TextParagraph с использованием TextBuilder
    textBuilder.appendParagraph(par);

    _dataDir = _dataDir + "RenderingReplaceableSymbols_out.pdf";
    pdfDocument.save(_dataDir);
}
```

## Заменяемые символы в области заголовка/подвала

Заменяемые символы также могут быть размещены в разделе Заголовок/Подвал файла PDF. Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода для получения подробной информации о том, как добавить заменяемый символ в секцию подвала.

```java
public static void ReplaceableSymbolsInHeaderFooterArea() {
    Document doc = new Document();
    Page page = doc.getPages().add();

    MarginInfo marginInfo = new MarginInfo();
    marginInfo.setTop(90);
    marginInfo.setBottom(50);
    marginInfo.setLeft(50);
    marginInfo.setRight(50);

    // Назначьте экземпляр marginInfo свойству Margin секции sec1.PageInfo
    page.getPageInfo().setMargin(marginInfo);

    HeaderFooter hfFirst = new HeaderFooter();
    page.setHeader(hfFirst);
    hfFirst.getMargin().setLeft(50);
    hfFirst.getMargin().setRight(50);

    // Создайте объект TextFragment, который будет хранить содержимое для отображения в качестве заголовка
    TextFragment t1 = new TextFragment("название отчета");
    t1.getTextState().setFont(FontRepository.findFont("Arial"));
    t1.getTextState().setFontSize(16);
    t1.getTextState().setForegroundColor(Color.getBlack());
    t1.getTextState().setFontStyle(FontStyles.Bold);
    t1.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t1.getTextState().setLineSpacing(5f);
    hfFirst.getParagraphs().add(t1);

    TextFragment t2 = new TextFragment("Имя_Отчета");
    t2.getTextState().setFont(FontRepository.findFont("Arial"));
    t2.getTextState().setForegroundColor(Color.getBlack());
    t2.getTextState().setHorizontalAlignment(HorizontalAlignment.Center);
    t2.getTextState().setLineSpacing(5f);
    t2.getTextState().setFontSize(12);
    hfFirst.getParagraphs().add(t2);

    // Создайте объект HeaderFooter для секции
    HeaderFooter hfFoot = new HeaderFooter();

    // Установите объект HeaderFooter для нечетного и четного подвала
    page.setFooter(hfFoot);
    hfFoot.getMargin().setLeft(50);
    hfFoot.getMargin().setRight(50);

    // Добавьте текстовый фрагмент, содержащий номер текущей страницы из общего числа страниц
    TextFragment t3 = new TextFragment("Сформировано на тестовую дату");
    TextFragment t4 = new TextFragment("название отчета ");
    TextFragment t5 = new TextFragment("Страница $p из $P");

    // Создайте объект таблицы
    Table tab2 = new Table();

    // Добавьте таблицу в коллекцию параграфов нужной секции
    hfFoot.getParagraphs().add(tab2);

    // Установите ширины колонок таблицы
    tab2.setColumnWidths("165 172 165");

    // Создайте строки в таблице, а затем ячейки в строках
    Row row3 = tab2.getRows().add();

    row3.getCells().add();
    row3.getCells().add();
    row3.getCells().add();

    // Установите вертикальное выравнивание текста по центру
    row3.getCells().get_Item(0).setAlignment(HorizontalAlignment.Left);
    row3.getCells().get_Item(1).setAlignment(HorizontalAlignment.Center);
    row3.getCells().get_Item(2).setAlignment(HorizontalAlignment.Right);

    row3.getCells().get_Item(0).getParagraphs().add(t3);
    row3.getCells().get_Item(1).getParagraphs().add(t4);
    row3.getCells().get_Item(2).getParagraphs().add(t5);

    Table table = new Table();

    table.setColumnWidths("33% 33% 34%");
    table.setDefaultCellPadding(new MarginInfo());
    table.getDefaultCellPadding().setTop(10);
    table.getDefaultCellPadding().setBottom(10);

    // Добавьте таблицу в коллекцию параграфов нужной секции
    page.getParagraphs().add(table);

    // Установите границу ячейки по умолчанию, используя объект BorderInfo
    table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));

    // Установите границу таблицы, используя другой настраиваемый объект BorderInfo
    table.setBorder(new BorderInfo(BorderSide.All, 1f));

    table.setRepeatingRowsCount(1);

    // Создайте строки в таблице, а затем ячейки в строках
    Row row1 = table.getRows().add();

    row1.getCells().add("col1");
    row1.getCells().add("col2");
    row1.getCells().add("col3");
    String CRLF = "\r\n";

    for (int i = 0; i <= 10; i++) {
        Row row = table.getRows().add();
        row.setRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            Cell c1;
            if (c == 2)
                c1 = row.getCells().add(
                        "Aspose.Total for Java - это компиляция всех компонентов Java, предлагаемых Aspose. Она компилируется на "
                                + CRLF
                                + "ежедневной основе, чтобы обеспечить наличие самых последних версий каждого из наших компонентов Java. "
                                + CRLF
                                + "ежедневной основе, чтобы обеспечить наличие самых последних версий каждого из наших компонентов Java. "
                                + CRLF
                                + "С использованием Aspose.Total for Java разработчики могут создавать широкий спектр приложений.");
            else
                c1 = row.getCells().add("item1" + c);
            c1.setMargin(new MarginInfo());
            c1.getMargin().setLeft(30);
            c1.getMargin().setTop(10);
            c1.getMargin().setBottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```


## Удалить весь текст из PDF документа

### Удалить весь текст с использованием операторов

В некоторых операциях с текстом необходимо удалить весь текст из PDF документа, и для этого обычно нужно установить найденный текст как пустую строку. Дело в том, что изменение текста для множества текстовых фрагментов вызывает ряд проверок и операций по корректировке позиции текста. Они необходимы в сценариях редактирования текста. Сложность заключается в том, что нельзя определить, сколько текстовых фрагментов будет удалено в сценарии, где они обрабатываются в цикле.

Поэтому мы рекомендуем использовать другой подход для сценария удаления всего текста со страниц PDF. Рассмотрите следующий фрагмент кода, который работает очень быстро.

```java
public static void RemoveAllTextUsingOperators() {
    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Перебрать все страницы PDF документа
    for (int i = 1; i <= pdfDocument.getPages().size(); i++) {
        Page page = pdfDocument.getPages().get_Item(i);
        OperatorSelector operatorSelector = new OperatorSelector(new com.aspose.pdf.operators.TextShowOperator());
        // Выбрать весь текст на странице
        page.getContents().accept(operatorSelector);
        // Удалить весь текст
        page.getContents().delete(operatorSelector.getSelected());
    }
    // Сохранить документ
    pdfDocument.save(_dataDir + "RemoveAllText_out.pdf");
}
```