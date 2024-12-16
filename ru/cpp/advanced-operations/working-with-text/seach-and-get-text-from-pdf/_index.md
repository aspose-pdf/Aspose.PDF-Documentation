---
title: Поиск и Извлечение Текста со Страниц PDF Документа
linktitle: Поиск и Извлечение Текста
type: docs
weight: 60
url: /ru/cpp/search-and-get-text-from-pdf/
description: Эта статья объясняет, как использовать различные инструменты для поиска и извлечения текста из PDF документов. Мы можем искать с использованием регулярных выражений на отдельных или всех страницах.
lastmod: "2021-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Поиск и Извлечение Текста со Всех Страниц PDF Документа

Класс [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) позволяет находить текст, совпадающий с определенной фразой, на всех страницах PDF документа. Чтобы искать текст по всему документу, необходимо вызвать метод Accept коллекции [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Метод 'Accept' принимает объект TextFragmentAbsorber в качестве параметра, который возвращает коллекцию объектов TextFragment.

Следующий фрагмент кода показывает, как искать текст на всех страницах.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void SearchAndGetTextFromAllThePagesOfPDFDocument() {
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Создать объект TextAbsorber для поиска всех экземпляров входной поисковой фразы
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>("document");

    // Принять абсорбер для всех страниц
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Получить извлеченные текстовые фрагменты в коллекцию
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Перебрать фрагменты
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Текст :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Позиция :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Шрифт - Имя :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Шрифт - IsAccessible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Шрифт - Встроенный - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Шрифт - Подмножество :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Размер шрифта :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Цвет переднего плана :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```

## Search and Get Text from all pages using Regular Expression

TextFragmentAbsorber помогает вам искать и извлекать текст со всех страниц на основе регулярного выражения. Сначала вам нужно передать регулярное выражение в конструктор [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) в качестве фразы. После этого необходимо установить свойство [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/) объекта TextFragmentAbsorber. Это свойство требует объект TextSearchOptions, и вам нужно передать true в качестве параметра его конструктору при создании новых объектов. Поскольку вы хотите извлечь совпадающий текст со всех страниц, вам нужно вызвать метод Accept коллекции Pages. [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment_absorber/) возвращает TextFragmentCollection, содержащий все фрагменты, соответствующие критериям, указанным в регулярном выражении. Следующий фрагмент кода показывает, как искать и извлекать текст со всех страниц на основе регулярного выражения.

```cpp
void SearchAndGetTextFromPagesUsingRegularExpression()
{
    String _dataDir("C:\\Samples\\");

    auto document = new Document(_dataDir + u"sample.pdf");

    // Создать объект TextAbsorber для поиска всех экземпляров входной поисковой фразы
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>(u"\\d{4}-\\d{4}"); // например, 1999-2000

    // Установить опцию поиска текста для указания использования регулярного выражения
    auto textSearchOptions = MakeObject<TextSearchOptions>(true);
    textFragmentAbsorber->set_TextSearchOptions(textSearchOptions);

    // Принять абсорбер для первой страницы документа
    document->get_Pages()->Accept(textFragmentAbsorber);

    // Получить извлеченные фрагменты текста в коллекцию
    auto textFragmentCollection = textFragmentAbsorber->get_TextFragments();

    // Перебрать фрагменты
    for (auto textFragment : textFragmentCollection) {
        Console::WriteLine(u"Text :- {0}", textFragment->get_Text());
        Console::WriteLine(u"Position :- {0}", textFragment->get_Position());
        Console::WriteLine(u"XIndent :- {0}", textFragment->get_Position()->get_XIndent());
        Console::WriteLine(u"YIndent :- {0}", textFragment->get_Position()->get_YIndent());
        Console::WriteLine(u"Font - Name :- {0}", textFragment->get_TextState()->get_Font()->get_FontName());
        Console::WriteLine(u"Font - IsAccessible :- {0}", textFragment->get_TextState()->get_Font()->get_IsAccessible());
        Console::WriteLine(u"Font - IsEmbedded - {0}", textFragment->get_TextState()->get_Font()->get_IsEmbedded());
        Console::WriteLine(u"Font - IsSubset :- {0}", textFragment->get_TextState()->get_Font()->get_IsSubset());
        Console::WriteLine(u"Font Size :- {0}", textFragment->get_TextState()->get_FontSize());
        Console::WriteLine(u"Foreground Color :- {0}", textFragment->get_TextState()->get_ForegroundColor());
    }
}
```