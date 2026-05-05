---
title: Заменить текст в PDF с помощью Python
linktitle: Заменить текст в PDF
type: docs
weight: 40
url: /ru/python-net/replace-text-in-pdf/
description: Узнайте, как заменять, переупорядочивать и удалять текст в PDF‑документах с использованием Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Как заменить текст в PDF с помощью Python
Abstract: Статья представляет собой исчерпывающее руководство по различным техникам манипуляции текстом в PDF‑документах с использованием Aspose.PDF for Python via .NET. В ней рассматриваются несколько стратегий замены текста, включая замену текста на всех страницах, в определённых регионах страниц и с использованием регулярных выражений. Статья также объясняет, как заменить Font в PDF, гарантируя удаление неиспользуемых Font, и как управлять заменой текста для автоматической перестановки содержимого страниц. Кроме того, она рассматривает рендеринг заменяемых символов при создании PDF, включая их использование в областях заголовка/подвала, для улучшения кастомизации документа. Наконец, описаны методы удаления всего текста из PDF‑документа, оптимизирующие операции для сценариев, требующих полного удаления текста. Каждый раздел дополнен фрагментами кода на Python и других поддерживаемых языках для демонстрации практической реализации.
---

Эти примеры демонстрируют, как **изменять или удалять текст в существующем PDF**.

Используйте эту страницу, когда вам нужно обновить значения текста, удалить нежелательный контент или применить правила замены текста на страницах PDF.

## Заменить существующий текст

### Заменить текст на всех страницах PDF‑документа

{{% alert color="primary" %}}

Вы можете попытаться найти и заменить текст в документе с помощью Aspose.PDF и получить результаты онлайн здесь [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Замена текста — распространённая необходимость при обновлении или исправлении содержимого существующих PDF‑документов, например, при изменении названий продуктов, исправлении опечаток или обновлении терминологии на нескольких страницах.

Aspose.PDF for Python via .NET предлагает мощный и эффективный метод программного поиска и замены текста через [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) класс.

Этот пример демонстрирует, как найти все вхождения конкретной фразы (в этом случае "Black cat") и заменить их новой фразой ("White dog") во всём PDF-документе.

1. Укажите фразы поиска и замены. Установите текст, который вы хотите найти, и текст, которым его заменить.
1. Загрузите PDF Document.
1. Создайте Text Absorber. TextFragmentAbsorber инициализируется поисковой фразой. Он сканирует документ, находя все вхождения заданной фразы.
1. Примените Absorber ко всем страницам. Это перебирает все страницы и собирает фрагменты текста, соответствующие фразе.
1. Замените каждый найденный фрагмент. Каждое вхождение "Black cat" должно быть изменено на "White dog".
1. Сохраните обновленный PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Заменить текст в определённой области страницы

Иногда вам может понадобиться заменять текст только в определённой области страницы PDF, а не искать по всему документу — например, обновлять заголовок, нижний колонтитул или ячейку таблицы в известной позиции.

Библиотека Aspose.PDF for Python via .NET обеспечивает эту функциональность, используя [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) в сочетании с региональным поиском текста.

Этот пример демонстрирует, как найти и заменить все вхождения целевой фразы в заданной прямоугольной области на конкретной странице.

1. Укажите фразы поиска и замены.
1. Загрузите PDF Document.
1. Создайте Text Absorber для поиска. Инициализируйте TextFragmentAbsorber, чтобы найти нужный текст.
1. Ограничьте область поиска. Прямоугольник задаёт пределы координат x и y на странице.
1. Примените Absorber к определённой странице. Это выполняет поиск и собирает соответствующие фрагменты текста в указанной области.
1. Заменить найденный текст. Каждое вхождение 'doc' в определённой области становится 'DOC'.
1. Сохраните обновленный PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Изменить размер и сдвинуть текст без изменения размера шрифта

При замене текста в PDF иногда требуется вписать или переместить новый текст в определённую область, не изменяя размер шрифта.
Aspose.PDF for Python via .NET предоставляет варианты настройки размещения текста и интервалов, при этом сохраняя исходный размер шрифта без изменений.

1. Загрузите PDF Document.
1. Соберите все фрагменты текста на странице, используя 'TextFragmentAbsorber'.
1. Выберите фрагмент для изменения.
1. Сдвиньте и измените размер текстового прямоугольника.
1. Настройка интервала текста. Включите регулировку интервала, чтобы разместить текст внутри изменённого прямоугольника.
1. {"trans­latedText":"Заменить текст фрагмента."}
1. Сохраните обновленный PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Изменить размер и сдвинуть абзац в PDF

При работе с PDF иногда нужно заменить или расширить абзац, при этом визуально выровнять его с макетом страницы. Aspose.PDF позволяет изменить размер ограничивающего прямоугольника абзаца и отрегулировать интервал, чтобы разместить новый текст, всё это без изменения размера шрифта.

1. Загрузите PDF Document.
1. Используйте 'TextFragmentAbsorber' для сбора всех текстовых фрагментов на странице.
1. Выберите фрагмент для изменения.
1. Изменить размер и сместить абзац. Использовать медиакоробку страницы для определения границ и корректировать прямоугольник.
1. Настроить интервал. Это изменяет интервал между словами/буквами вместо изменения размера шрифта.
1. Заменить текст фрагмента.
1. Сохранить изменённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Заменить текст и автоматически расширить шрифт, чтобы заполнить целевую область

Замените текст в PDF, автоматически изменяя размер и расширяя шрифт, чтобы заполнить конкретную прямоугольную область. С помощью библиотеки Aspose.PDF for Python via .NET код динамически регулирует размер шрифта и интервалы, так чтобы новое текстовое содержимое идеально вписалось в определённый ограничивающий прямоугольник — без ручных вычислений шрифта.

1. Загрузите PDF.
1. Захватить фрагменты текста.
1. Выберите конкретный фрагмент.
1. Определить целевой прямоугольник.
1. Включить параметры корректировки текста.
1. Заменить текст.
1. Сохранить Document.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Заменить текст и вписать его в прямоугольник

Замените текст в PDF‑документе, при этом гарантируя, что новое содержание помещается в прямоугольную область оригинального текста, автоматически уменьшая размер шрифта при необходимости.

Используя библиотеку Aspose.PDF for Python via .NET, эта функция динамически регулирует как макет текста, так и размер Font, сохраняя структуру Document и предотвращая переполнение.

1. Создайте объект TextFragmentAbsorber, чтобы извлечь все текстовые фрагменты с первой страницы.
1. Получить доступ к конкретному фрагменту текста.
1. Установите область замены.
1. Настройте параметры регулировки текста. Установите два основных варианта замены:
    - Регулировка размера шрифта - ‘SHRINK_TO_FIT’ автоматически уменьшает размер шрифта, если новый текст слишком длинный.
    - Регулировка интервала - 'ADJUST_SPACE_WIDTH' сохраняет пропорциональность интервала.
1. Заменить Текст.
1. Сохранить изменённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Автоматически заменять текст‑заполнитель и перестраивать макет PDF

Замените заполнительный текст внутри PDF (например, шаблоны или формы) фактическими данными, такими как имена или информация о компании.
Он автоматически регулирует макет страницы, чтобы разместить новый текст, одновременно применяя пользовательское форматирование (шрифт, цвет, размер).

1. Импортировать и загрузить PDF.
1. Создайте Text Absorber для Placeholder.
1. Применить Absorber ко всем страницам.
1. Перебрать найденные фрагменты текста.
1. Применить пользовательское форматирование текста.
1. Сохранить обновлённый документ.

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Заменить текст на основе регулярного выражения

При работе с PDF‑документами может потребоваться заменить текст, соответствующий шаблону, а не конкретной фразе — например, номера телефонов, коды или форматы, похожие на даты.

Aspose.PDF for Python via .NET позволяет выполнять такие замены, используя регулярные выражения (regex) с классом TextFragmentAbsorber.

Этот пример демонстрирует, как находить шаблоны текста (в данном случае любой текст, соответствующий формату ####-####, например 1234-5678) и заменять их на отформатированную строку ABC1-2XZY'. Также показано, как настроить шрифт, цвет и размер заменённого текста.

Следующий фрагмент кода показывает, как заменять текст на основе регулярного выражения.

1. Загрузите PDF Document.
1. Создайте Text Absorber, основанный на регулярных выражениях. Инициализируйте TextFragmentAbsorber шаблоном регулярного выражения.
1. Включите режим регулярных выражений. Параметр 'True' активирует режим поиска с использованием регулярных выражений.
1. Примените Absorber к странице. Это сканирует страницу на поиск всех текстовых фрагментов, соответствующих заданному шаблону regex.
1. Замените каждое совпадение новым текстом и примените пользовательское оформление.
1. Сохранить изменённый документ.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Заменить шрифты или удалить неиспользуемые шрифты

### Заменить шрифты в существующем PDF файле

Время от времени вам требуется стандартизировать или обновить шрифты в PDF — например, заменить устаревший или проприетарный шрифт на более доступный. Библиотека Aspose.PDF for Python via .NET позволяет программно обнаруживать и заменять шрифты, обеспечивая постоянство типографики и совместимость документа.

Этот пример демонстрирует, как заменить все вхождения конкретного шрифта (например, 'Arial-Bold') другим шрифтом (например, 'Verdana') во всём PDF‑документе.

Следующий фрагмент кода показывает, как заменить шрифт внутри PDF‑документа:

1. Откройте PDF Document.
1. Инициализировать TextFragmentAbsorber.
1. Используйте Absorber для извлечения фрагментов текста со всех страниц Document.
1. Определить и заменить шрифты. Скрипт проверяет, является ли текущий шрифт фрагмента 'Arial-BoldMT'. Если да, он заменяет его шрифтом 'Verdana' с помощью метода FontRepository.find_font().
1. Сохранить изменённый документ.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Удалить неиспользуемые шрифты

Со временем PDF‑документы могут накапливать неиспользуемые или встроенные шрифты, которые увеличивают размер файла и замедляют обработку. Эти неиспользуемые шрифты часто остаются даже после редактирования или замены текста, особенно при работе с большими или сложными PDF.

Библиотека Aspose.PDF for Python via .NET предоставляет эффективный способ удаления таких избыточных шрифтов с помощью класса TextEditOptions. Это не только оптимизирует ваш Document, но и гарантирует, что он использует только шрифты, действительно применённые к видимому тексту.

Метод 'remove_unused_fonts()' — простой, но мощный способ оптимизировать PDF‑файлы, удаляя избыточные данные шрифтов.

Этот пример демонстрирует, как:

- Сканировать PDF на неиспользуемые шрифты.
- Безопасно удалите их.
- Переприсвойте активные текстовые фрагменты единому шрифту (например, Times New Roman).

1. Откройте PDF Document.
1. Настройте параметры редактирования текста. Это указывает движку удалить все встроенные шрифты, которые в данный момент не используются в видимом тексте.
1. Создайте Text Absorber с параметрами. TextFragmentAbsorber извлекает фрагменты текста из Document для редактирования.
1. Переназначить стандартный шрифт. После того как поглотитель соберёт все фрагменты, пройдитесь по ним и примените единый шрифт.
1. Сохраните очищенный PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## Удалить весь текст

### Удалить текст из PDF

Удалите весь текстовый контент из PDF‑файла, сохранив изображения, фигуры и структуры макета нетронутыми.
Используя TextFragmentAbsorber, код эффективно сканирует весь документ и удаляет каждый найденный на каждой странице фрагмент текста.

1. Загрузите PDF Document.
1. Создается объект TextFragmentAbsorber для обнаружения и обработки текстовых фрагментов в PDF.
1. Удалить всё текстовое содержимое. Метод ‘absorber.remove_all_text()’ удаляет каждый текстовый элемент из загруженного документа, оставляя нетекстовые компоненты нетронутыми.
1. Сохранить обновлённый документ.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Удалить весь текст с конкретной страницы

Удалить весь текст с одной страницы PDF‑документа с использованием класса TextFragmentAbsorber в Aspose.PDF.
В отличие от полного удаления документа, этот метод выполняет очистку текста на уровне страниц, удаляя текст только с выбранной страницы, оставляя все остальные страницы нетронутыми.

1. Загрузите PDF‑файл.
1. Создать экземпляр TextFragmentAbsorber.
1. Удалить весь текст с первой страницы.
1. Сохранить изменённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Удалить весь текст из определённой области на странице PDF

Удалить весь текст из конкретного прямоугольного региона на странице с помощью TextFragmentAbsorber из Aspose.PDF.
Вместо того чтобы очищать всю страницу, этот метод выполняет целенаправленное удаление текста, позволяя точно контролировать, какая часть страницы будет затронута.

1. Загрузите PDF Document.
1. Создать TextFragmentAbsorber.
1. Определите целевую область (прямоугольник).
1. Удалить текст из указанного региона.
1. Сохранить остальную часть документа.
1. Сохранить изменённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### Удалить весь скрытый текст из PDF‑документа

Удалить весь текст из конкретного прямоугольного региона на странице с помощью TextFragmentAbsorber из Aspose.PDF.
Вместо того чтобы очищать всю страницу, этот метод выполняет целенаправленное удаление текста, позволяя точно контролировать, какая часть страницы будет затронута.

1. Загрузите PDF Document.
1. Создать TextFragmentAbsorber.
1. Определите целевую область (прямоугольник).
1. Удалить текст из указанного региона.
1. Сохранить остальную часть документа.
1. Сохранить изменённый PDF.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## Связанные темы текста

- [Работа с текстом в PDF с помощью Python](/pdf/ru/python-net/working-with-text/)
- [Добавление текста в PDF](/pdf/ru/python-net/add-text-to-pdf-file/)
- [Поиск и извлечение текста PDF в Python](/pdf/ru/python-net/search-and-get-text-from-pdf/)
- [Форматировать текст PDF с помощью Python](/pdf/ru/python-net/text-formatting-inside-pdf/)
