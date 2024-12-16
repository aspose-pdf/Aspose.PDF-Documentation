---
title: Замена текста в PDF с использованием C++
linktitle: Замена текста в PDF
type: docs
weight: 40
url: /ru/cpp/replace-text-in-pdf/
description: Узнайте больше о различных способах замены и удаления текста из PDF. Aspose.PDF позволяет заменять текст в определенной области или с использованием регулярного выражения.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Иногда возникает задача исправить или заменить текст в PDF-документе. Попытка сделать это вручную будет трудной задачей, поэтому вот решение этой проблемы.

Честно говоря, редактирование PDF-файла — это непростая задача. Поэтому ситуация, когда вам нужно найти и заменить одно слово на другое при редактировании PDF-файла, будет очень сложной, так как это займет у вас много времени. Кроме того, вы можете столкнуться со многими проблемами с вашим выводом, такими как форматирование или сломанные шрифты. Если вы хотите легко находить и заменять текст в PDF-файлах, мы рекомендуем использовать программное обеспечение библиотеки Aspose.Pdf, так как оно выполнит эту задачу за считанные минуты.

В этой статье мы покажем вам, как успешно находить и заменять текст в ваших PDF-файлах с использованием Aspose.PDF для C++.

## Замена текста на всех страницах PDF-документа

{{% alert color="primary" %}}

Вы можете попробовать найти и заменить текст в документе, используя Aspose.PDF, и получить результаты онлайн по этой [ссылке](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Для того чтобы заменить текст на всех страницах PDF-документа, сначала нужно использовать TextFragmentAbsorber для поиска конкретной фразы, которую вы хотите заменить. После этого нужно пройти через все TextFragments, чтобы заменить текст и изменить любые другие атрибуты. После того как вы это сделаете, остается только сохранить выходной PDF, используя метод Save объекта Document. Следующий фрагмент кода показывает, как заменить текст на всех страницах PDF-документа.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTextOnAllPages() {

    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Создайте объект TextAbsorber для поиска всех экземпляров вводимой поисковой фразы
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("Web");

    // Примите абсорбер для первой страницы документа
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Получите извлеченные текстовые фрагменты в коллекцию
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Переберите фрагменты
    for (auto textFragment : textFragmentCollection) {
        // Обновите текст и другие свойства
        textFragment->set_Text(u"World Wide Web");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Сохраните обновленный PDF-файл
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Замена текста в определенной области страницы

Для замены текста в определенной области страницы сначала необходимо создать объект TextFragmentAbsorber, указать область страницы с помощью свойства TextSearchOptions.Rectangle, а затем пройтись по всем TextFragments для замены текста. После выполнения этих операций нам нужно только сохранить выходной PDF, используя метод Save объекта Document. Следующий фрагмент кода показывает, как заменить текст на всех страницах PDF-документа.

```cpp
void ReplaceTextInParticularRegion() {

    String _dataDir("C:\\Samples\\");

    // load PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // instantiate TextFragment Absorber object
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // search text within page bound
    textFragmentAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);

    // specify the page region for TextSearch Options
    textFragmentAbsorber->get_TextSearchOptions()->set_Rectangle(new Rectangle(100, 700, 400, 770));

    // search text from first page of PDF file
    document->get_Pages()->idx_get(1)->Accept(textFragmentAbsorber);

    // iterate through individual TextFragment
    for (auto tf : textFragmentAbsorber->get_TextFragments()) {
        // replace text with "---"
        tf->set_Text(u"---");
    }

    // Save the updated PDF file
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Заменить текст на основе регулярного выражения

Если вы хотите заменить некоторые фразы на основе регулярного выражения, вам сначала нужно найти все фразы, соответствующие этому регулярному выражению, используя TextFragmentAbsorber. Вам нужно передать регулярное выражение в качестве параметра конструктору TextFragmentAbsorber. Также необходимо создать объект TextSearchOptions, который указывает, используется ли регулярное выражение. Как только вы получите совпадающие фразы в TextFragments, вам нужно пройтись по всем из них и обновить по мере необходимости. Наконец, вам нужно сохранить обновленный PDF, используя метод Save объекта Document. Следующий фрагмент кода показывает, как заменить текст на основе регулярного выражения.

```cpp
void ReplaceTextWithRegularExpression() {

    String _dataDir("C:\\Samples\\");

    // загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"Sample.pdf");
    // Создать объект TextAbsorber, чтобы найти все экземпляры входной поисковой фразы
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("\\d{4}-\\d{4}");
    // например, 1999-2000

    // Установить опцию поиска текста для указания использования регулярного выражения
    auto textSearchOptions = new TextSearchOptions(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Принять абсорбер для первой страницы документа
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Получить извлеченные текстовые фрагменты в коллекцию
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Пройтись по фрагментам
    for (auto textFragment : textFragmentCollection) {
        // Обновить текст и другие свойства
        textFragment->set_Text(u"ABCD-EFGH");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }

    // Сохранить обновленный PDF файл
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

## Замена шрифтов в существующем PDF-файле

Aspose.PDF для C++ поддерживает возможность замены текста в PDF-документе. Однако иногда возникает необходимость заменить только шрифт, используемый в PDF-документе. Вместо замены текста заменяется только используемый шрифт. Один из перегруженных конструкторов TextFragmentAbsorber принимает объект TextEditOptions в качестве аргумента, и мы можем использовать значение RemoveUnusedFonts из перечисления TextEditOptions.FontReplace для выполнения наших требований. В следующем фрагменте кода показано, как заменить шрифт в PDF-документе.

```cpp
void ReplaceFonts() {
    String _dataDir("C:\\Samples\\");

    // Создание объекта Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Поиск текстовых фрагментов и установка параметра редактирования как удаление неиспользуемых шрифтов
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(
        MakeObject<TextEditOptions>(TextEditOptions::FontReplace::RemoveUnusedFonts));

    // Принятие абсорбера для всех страниц документа
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Перебор всех TextFragments
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();
    for (auto textFragment : textFragmentCollection) {
        String fontName = textFragment->get_TextState()->get_Font()->get_FontName();
        // если имя шрифта ArialMT, заменить имя шрифта на Arial
        if (fontName.Equals(u"ArialMT")) {
            textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        }
    }

    // Сохранение обновленного PDF-файла
    document->Save(_dataDir + u"Updated_Text.pdf");
}
```

В следующем фрагменте кода вы увидите, как использовать неанглийский шрифт при замене текста:

```cpp
void UseNonEnglishFontWhenReplacingText() {

    String _dataDir("C:\\Samples\\");

    // Создайте объект Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Давайте изменим каждое слово "PDF" на японский текст с определенным шрифтом
    // MSGothic, который может быть установлен в ОС
    // Также это может быть другой шрифт, поддерживающий иероглифы
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("PDF");

    // Создайте экземпляр параметров поиска текста
    auto searchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(searchOptions);

    // Примите поглотитель для всех страниц документа
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Получите извлеченные текстовые фрагменты в коллекцию
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Переберите фрагменты
    for (auto textFragment : textFragmentCollection) {
        // Обновите текст и другие свойства
        textFragment->set_Text(u"ファイル");
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TakaoMincho"));
        textFragment->get_TextState()->set_FontSize(12);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
    }
    // Сохраните обновленный документ
    document->Save(_dataDir + u"Japanese_Text.pdf");
}
```

## Замена текста должна автоматически переупорядочивать содержимое страницы

Aspose.PDF для C++ поддерживает поиск и замену текста в PDF-файле. Однако недавно некоторые клиенты столкнулись с проблемами при замене текста, когда конкретный TextFragment заменяется меньшим содержимым, и в результирующем PDF отображаются лишние пробелы, или если TextFragment заменяется более длинной строкой, то слова накладываются на существующее содержимое страницы. Таким образом, было необходимо ввести механизм, который после замены текста внутри PDF-документа переупорядочивал его содержимое.

Чтобы обслуживать вышеупомянутые сценарии, Aspose.PDF для C++ был улучшен так, чтобы такие проблемы не возникали при замене текста в PDF-файле. Следующий фрагмент кода демонстрирует, как заменить текст в PDF-файле, и содержимое страницы должно быть автоматически переупорядочено.

```cpp
void RearrangeContent() {
    String _dataDir("C:\\Samples\\");

    // Создать объект Document
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Создать объект TextFragment Absorber с использованием регулярного выражения
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("[PDF,Web]");

    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Вы также можете указать опцию ReplaceAdjustment.WholeWordsHyphenation для
    // переноса текста на следующую или текущую строку, если текущая строка становится слишком длинной или
    // короткой после замены:
    //textFragmentAbsorber->get_TextReplaceOptions()->set_ReplaceAdjustmentAction(TextReplaceOptions::ReplaceAdjustment::WholeWordsHyphenation);

    // Применить абсорбер для всех страниц документа
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Получить извлеченные текстовые фрагменты в коллекцию
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Заменить каждый TextFragment
    for (auto textFragment : textFragmentCollection) {
        // Установить шрифт заменяемого текстового фрагмента
        textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
        // Установить размер шрифта
        textFragment->get_TextState()->set_FontSize(10);
        textFragment->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment->get_TextState()->set_BackgroundColor(Color::get_Gray());
        // Заменить текст на более длинную строку, чем заполнитель
        textFragment->set_Text(u"This is a larger string for the testing of this feature");
    }
    // Сохранить результирующий PDF
    document->Save(_dataDir + u"RearrangeContentsUsingTextReplacement_out.pdf");
}
```

## Отображение заменяемых символов при создании PDF

Заменяемые символы — это специальные символы в текстовой строке, которые могут быть заменены соответствующим содержимым во время выполнения. Заменяемые символы, которые в настоящее время поддерживаются новой моделью объекта документа пространства имен Aspose.PDF, это `$P`, `$p`, `\n`, `\r`. `$p` и `$P` используются для работы с нумерацией страниц во время выполнения. `$p` заменяется на номер страницы, на которой находится текущий класс `Paragraph`. `$P` заменяется на общее количество страниц в документе. При добавлении `TextFragment` в коллекцию абзацев PDF-документов, он не поддерживает перенос строки внутри текста. Однако, чтобы добавить текст с переносом строки, используйте `TextFragment` с `TextParagraph`:

- используйте "\r\n" или Environment.NewLine в `TextFragment` вместо одиночного "\n";
- создайте объект `TextParagraph`. Он добавит текст с разделением строк;
- добавьте `TextFragment` с помощью `TextParagraph.AppendLine`;
- добавьте `TextParagraph` с помощью `TextBuilder.AppendParagraph`.

```cpp
void RenderingReplaceableSymbols() {

    String _dataDir("C:\\Samples\\");

    // загрузить PDF файл
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->Add();

    // Инициализировать новый TextFragment с текстом, содержащим необходимые маркеры новой строки
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // Установить свойства фрагмента текста, если необходимо
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // Создать объект TextParagraph
    auto par = MakeObject<TextParagraph>();

    // Добавить новый TextFragment в абзац
    par->AppendLine(textFragment);

    // Установить позицию абзаца
    par->set_Position(MakeObject<Position>(100, 600));

    // Создать объект TextBuilder
    auto textBuilder = MakeObject<TextBuilder>(page);

    // Добавить TextParagraph с использованием TextBuilder
    textBuilder->AppendParagraph(par);

    document->Save(_dataDir + u"RenderingReplaceableSymbols_out.pdf");
}
```

## Заменяемые символы в области заголовка/подвала

Заменяемый символ также может быть размещен внутри секции заголовка/подвала PDF файла. Ознакомьтесь с следующим примером кода, чтобы увидеть, как добавить заменяемый символ в секцию подвала.

```csharp
void ReplaceableSymbolsInHeaderFooterArea() {

    auto document = MakeObject<Document>();
    auto page = doc.getPages().add();

    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Top(90);
    marginInfo->set_Bottom(50);
    marginInfo->set_Left(50);
    marginInfo->set_Right(50);

    // Присвоить экземпляр marginInfo свойству Margin объекта PageInfo
    page.getPageInfo()->set_Margin(marginInfo);

    auto hfFirst = MakeObject<HeaderFooter>();
    page->set_Header(hfFirst);
    hfFirst->get_Margin()->set_Left(50);
    hfFirst->get_Margin()->set_Right(50);

    // Создать текстовый абзац, который будет хранить содержимое для отображения в качестве заголовка
    auto t1 = MakeObject<TextFragment>("название отчета");
    t1->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t1->get_TextState()->set_FontSize(16);
    t1->get_TextState()->set_ForegroundColor(Color::get_Black());
    t1->get_TextState()->set_FontStyle(FontStyles::Bold);
    t1->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t1->get_TextState()->set_LineSpacing(5.0f);
    hfFirst->get_Paragraphs()->Add(t1);

    auto t2 = MakeObject<TextFragment>("Название_Отчета");
    t2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    t2->get_TextState()->set_ForegroundColor(Color::get_Black());
    t2->get_TextState()->set_HorizontalAlignment(HorizontalAlignment::Center);
    t2->get_TextState()->set_LineSpacing(5.0f);
    t2->get_TextState()->set_FontSize(12);
    hfFirst->get_Paragraphs()->Add(t2);

    // Создать объект HeaderFooter для секции
    auto hfFoot = MakeObject<HeaderFooter>();

    // Установить объект HeaderFooter как для нечетного, так и для четного подвала
    page->set_Footer(hfFoot);
    hfFoot->get_Margin()->set_Left(50);
    hfFoot->get_Margin()->set_Right(50);

    // Добавить текстовый абзац, содержащий текущий номер страницы от общего числа страниц
    auto t3 = MakeObject<TextFragment>("Создано на тестовой дате");
    auto t4 = MakeObject<TextFragment>("название отчета ");
    auto t5 = MakeObject<TextFragment>("Страница $p из $P");

    // Создать объект таблицы
    auto tab2 = MakeObject<Table>();

    // Добавить таблицу в коллекцию абзацев нужной секции
    hfFoot->get_Paragraphs()->Add(tab2);

    // Установить ширину столбцов таблицы
    tab2->set_ColumnWidths(u"165 172 165");

    // Создать строки в таблице, а затем ячейки в строках
    auto row3 = tab2->get_Rows()->Add();

    row3->get_Cells()->Add();
    row3->get_Cells()->Add();
    row3->get_Cells()->Add();

    // Установить вертикальное выравнивание текста по центру
    row3->get_Cells()->idx_get(0)->set_Alignment(HorizontalAlignment::Left);
    row3->get_Cells()->idx_get(1)->set_Alignment(HorizontalAlignment::Center);
    row3->get_Cells()->idx_get(2)->set_Alignment(HorizontalAlignment::Right);

    row3->get_Cells()->idx_get(0)->get_Paragraphs()->Add(t3);
    row3->get_Cells()->idx_get(1)->get_Paragraphs()->Add(t4);
    row3->get_Cells()->idx_get(2)->get_Paragraphs()->Add(t5);

    auto table = MakeObject<Table>();

    table->set_ColumnWidths(u"33% 33% 34%");
    table->set_DefaultCellPadding(new MarginInfo());
    table->get_DefaultCellPadding()->set_Top(10);
    table->get_DefaultCellPadding()->set_Bottom(10);

    // Добавить таблицу в коллекцию абзацев нужной секции
    page.getParagraphs().add(table);

    // Установить границу ячеек по умолчанию, используя объект BorderInfo
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));

    // Установить границу таблицы, используя другой настраиваемый объект BorderInfo
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f));

    table->set_RepeatingRowsCount(1);

    // Создать строки в таблице, а затем ячейки в строках
    auto row1 = table->get_Rows()->Add();

    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");

    String CRLF ("\r\n");

    for (int i = 0; i <= 10; i++) {
        auto row = table->get_Rows()->Add();
        row->set_IsRowBroken(true);
        for (int c = 0; c <= 2; c++) {
            SharedPtr<Cell> c1;
            if (c == 2)
                c1 = row->get_Cells()->Add(
                    u"Aspose.Total for C++ это компиляция всех Java компонентов, предлагаемых Aspose. Она компилируется на"
                    + CRLF
                    + u"ежедневной основе, чтобы гарантировать наличие самых актуальных версий каждого из наших Java компонентов. "
                    + CRLF
                    + u"ежедневной основе, чтобы гарантировать наличие самых актуальных версий каждого из наших Java компонентов. "
                    + CRLF
                    + u"Используя Aspose.Total for C++, разработчики могут создавать широкий спектр приложений.");
            else
                c1 = row->get_Cells()->Add(u"item1" + c);
            c1->set_Margin(new MarginInfo());
            c1->get_Margin()->set_Left(30);
            c1->get_Margin()->set_Top(10);
            c1->get_Margin()->set_Bottom(10);
        }
    }

    _dataDir = _dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
    doc.save(_dataDir);
}
```

## Удалить весь текст из PDF-документа

### Удалить весь текст с использованием операторов

В некоторых текстовых операциях вам нужно удалить весь текст из PDF-документа, и для этого обычно нужно установить найденный текст как пустую строку. Дело в том, что изменение текста для набора фрагментов текста вызывает ряд операций по проверке и корректировке положения текста. Они необходимы в сценариях редактирования текста. Сложность заключается в том, что вы не можете определить, сколько фрагментов текста будет удалено в скрипте, где они обрабатываются в цикле.

Поэтому мы рекомендуем использовать другой подход для сценария удаления всего текста с PDF-страниц.

Следующий пример кода показывает, как быстро решить эту задачу.

```cpp
void RemoveAllTextUsingOperators() {

    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    // Перебрать все страницы PDF-документа
    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto page = document->get_Pages()->idx_get(i);
        auto operatorSelector = MakeObject<OperatorSelector>(MakeObject<Aspose::Pdf::Operators::TextShowOperator>());
        // Выбрать весь текст на странице
        page->get_Contents()->Accept(operatorSelector);
        // Удалить весь текст
        page->get_Contents()->Delete(operatorSelector->get_Selected());
    }
    // Сохранить документ
    document->Save(_dataDir + u"RemoveAllText_out.pdf");
}
```