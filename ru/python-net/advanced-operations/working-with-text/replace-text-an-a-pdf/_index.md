---
title: Заменить текст в PDF с помощью Python
linktitle: Заменить текст в PDF
type: docs
weight: 40
url: /ru/python-net/replace-text-in-pdf/
description: Узнайте, как заменять текст в PDF-файлах с помощью Python, включая замену текста на разных страницах, ограничение изменений области страницы, использование регулярных выражений и удаление текста.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Заменяйте и удаляйте текст в PDF-файлах с помощью Python
Abstract: В этой статье показано, как заменять текст в PDF‑документах с помощью Aspose.PDF for Python via .NET. Описывается замена текста на всех страницах, замена в пределах регионов страниц, использование регулярных выражений, замена шрифтов, настройка расположения текста и удаление видимого или скрытого текста.
---

Эта страница показывает, как **заменить текст в PDF с помощью Python** с использованием Aspose.PDF for Python via .NET.

Используйте эти примеры, когда вам необходимо обновить значения текста, удалить нежелательный контент, заменить текст в определённой области страницы или применить правила замены текста на нескольких страницах PDF.

## Заменить текст в PDF с помощью Python

### Заменить текст на всех страницах PDF‑документа

{{% alert color="primary" %}}

Вы можете попробовать поиск и замену текста онлайн с помощью Aspose.PDF [приложение для редактирования](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

Замена текста является распространённой задачей при обновлении или исправлении содержимого в существующих PDF‑документах — например, при изменении названий продуктов, исправлении опечаток или обновлении терминологии на нескольких страницах.

Aspose.PDF for Python via .NET предлагает мощный и эффективный метод программного поиска и замены текста через [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) класс.

Этот пример демонстрирует, как найти все вхождения конкретной фразы (в данном случае "Black cat") и заменить их новой фразой ("White dog") во всём PDF‑документе.

1. Укажите фразы поиска и замены. Установите текст, который вы хотите найти, и текст, на который его нужно заменить.
1. Загрузите PDF-документ.
1. Создайте Text Absorber. TextFragmentAbsorber инициализируется поисковой фразой. Он сканирует документ для поиска всех вхождений данной фразы.
1. Применить поглотитель ко всем страницам. Это проходит по всем страницам и собирает текстовые фрагменты, соответствующие фразе.
1. Замените каждый найденный фрагмент. Каждое вхождение "Black cat" должно быть изменено на "White dog".
1. Сохраните обновлённый PDF.

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

### Заменить текст в конкретном участке страницы

Иногда может потребоваться заменить текст только в определённой области страницы PDF, а не искать по всему документу — например, обновить заголовок, нижний колонтитул или ячейку таблицы в известном положении.

Библиотека Aspose.PDF for Python via .NET обеспечивает эту функциональность, используя [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) в сочетании с поиском текста по регионам.

Этот пример демонстрирует, как найти и заменить все вхождения целевой фразы в определённом прямоугольном регионе на конкретной странице.

1. Укажите фразы поиска и замены.
1. Загрузите PDF-документ.
1. Создайте TextAbsorber для поиска. Инициализируйте TextFragmentAbsorber, чтобы найти нужный текст.
1. Ограничьте область поиска. Прямоугольник указывает пределы координат x и y на странице.
1. Примените Absorber к конкретной странице. Это выполняет поиск и собирает соответствующие текстовые фрагменты в указанной области.
1. Заменить найденный текст. Каждое вхождение 'doc' в определённой области становится 'DOC'.
1. Сохраните обновлённый PDF.

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

При замене текста в PDF иногда требуется разместить или переместить новый текст в определённой области, не меняя размер шрифта.
Aspose.PDF for Python via .NET предоставляет возможности настройки макета текста и интервала, сохраняя исходный размер Font.

1. Загрузите PDF-документ.
1. Соберите все текстовые фрагменты на странице, используя 'TextFragmentAbsorber'.
1. Выберите фрагмент для изменения.
1. Сдвиньте и измените размер прямоугольника текста.
1. Регулировать межбуквенный интервал. Включить регулировку интервала, чтобы разместить текст внутри изменённого прямоугольника.
1. Заменить текст фрагмента.
1. Сохраните обновлённый PDF.

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

### Изменить размер и переместить абзац в PDF

Работая с PDF, иногда требуется заменить или расширить абзац, при этом сохранять его визуальное выравнивание с макетом страницы. Aspose.PDF позволяет изменить размер ограничивающего прямоугольника абзаца и настроить интервал, чтобы вместить новый текст, всё без изменения размера шрифта.

1. Загрузите PDF-документ.
1. Используйте 'TextFragmentAbsorber' для сбора всех текстовых фрагментов на странице.
1. Выберите фрагмент для изменения.
1. Измените размер и переместите абзац. Используйте медиакоробку страницы, чтобы определить границы и скорректировать прямоугольник.
1. Настройте интервал. Это изменяет расстояние между словами/буквами вместо изменения размера шрифта.
1. Заменить текст фрагмента.
1. Сохраните изменённый PDF.

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

Замените текст в PDF, автоматически изменяя размер и расширяя шрифт, чтобы заполнить конкретную прямоугольную область. С помощью библиотеки Aspose.PDF for Python via .NET код динамически регулирует размер шрифта и интервалы, так что новое текстовое содержимое идеально вписывается в определённый ограничивающий прямоугольник — без ручных расчётов шрифта.

1. Загрузите PDF.
1. Захватить фрагменты текста.
1. Выберите конкретный фрагмент.
1. Определить целевой прямоугольник.
1. Включить параметры регулировки текста.
1. Заменить текст.
1. Сохраните документ.

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

Заменить текст в PDF‑документе, гарантируя, что новый контент помещается в прямоугольную область оригинального текста, автоматически уменьшая размер шрифта при необходимости.

Используя библиотеку Aspose.PDF for Python via .NET, эта функция динамически регулирует как раскладку текста, так и размер шрифта, сохраняя структуру документа и предотвращая переполнение.

1. Создайте объект TextFragmentAbsorber, чтобы извлечь все фрагменты текста с первой страницы.
1. Получите доступ к конкретному фрагменту текста.
1. Задайте область замены.
1. Настройте параметры коррекции текста. Установите два ключевых параметра замены:
    - Регулировка размера шрифта - 'SHRINK_TO_FIT' автоматически уменьшает размер шрифта, если новый текст слишком длинный.
    - Регулировка интервала - 'ADJUST_SPACE_WIDTH' сохраняет пропорциональность интервала.
1. Заменить текст.
1. Сохраните изменённый PDF.

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

Замените заполняемый текст внутри PDF (например, шаблоны или формы) на фактические данные, такие как имена или информацию о компании.
Он автоматически регулирует макет страницы, чтобы разместить новый текст, одновременно применяя пользовательское форматирование (шрифт, цвет, размер).

1. Импортировать и загрузить PDF.
1. Создайте Text Absorber для Placeholder.
1. Применить Absorber ко всем страницам.
1. Перебрать найденные фрагменты текста.
1. Применить пользовательское форматирование текста.
1. Сохраните обновлённый документ.

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

При работе с PDF‑документами вам может потребоваться заменять текст, соответствующий шаблону, а не конкретной фразе — например, номера телефонов, коды или форматы, похожие на даты.

Aspose.PDF for Python via .NET позволяет выполнять такие замены, используя регулярные выражения (regex) и класс TextFragmentAbsorber.

В этом примере демонстрируется, как находить текстовые шаблоны (в данном случае любой текст, соответствующий формату ####-####, например 1234-5678) и заменять их форматированной строкой 'ABC1-2XZY'. Также показывается, как настроить шрифт, цвет и размер заменяемого текста.

Следующий фрагмент кода показывает, как заменить текст, используя регулярное выражение.

1. Загрузите PDF-документ.
1. Создайте Text Absorber, основанный на регулярных выражениях. Инициализируйте TextFragmentAbsorber с шаблоном регулярного выражения.
1. Включите режим регулярных выражений. Параметр ’True’ активирует режим поиска с использованием регулярных выражений.
1. Примените Absorber к странице. Это сканирует страницу на предмет всех текстовых фрагментов, соответствующих заданному шаблону regex.
1. Замените каждое совпадение новым текстом и примените пользовательское оформление.
1. Сохраните изменённый документ.

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

### Заменить шрифты в существующем PDF‑файле

Иногда требуется стандартизировать или обновить шрифты в PDF — например, заменить устаревший или проприетарный шрифт на более доступный. Библиотека Aspose.PDF for Python via .NET позволяет программно обнаруживать и заменять шрифты, обеспечивая согласованную типографику и совместимость документа.

Этот пример демонстрирует, как заменить все вхождения определённого шрифта (например, 'Arial-BoldMT') другим шрифтом (например, 'Verdana') во всём PDF документе.

Следующий фрагмент кода показывает, как заменить шрифт внутри PDF‑документа:

1. Откройте PDF-документ.
1. Инициализировать TextFragmentAbsorber.
1. Используйте Absorber для извлечения фрагментов текста со каждой страницы документа.
1. Определить и заменить шрифты. Скрипт проверяет, является ли текущий шрифт фрагмента 'Arial-BoldMT'. Если да, он заменяет его шрифтом 'Verdana' с помощью метода FontRepository.find_font().
1. Сохраните изменённый документ.

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

Со временем PDF‑документы могут накапливать неиспользуемые или встроенные шрифты, которые увеличивают размер файла и замедляют обработку. Эти неиспользуемые шрифты часто остаются даже после редактирования или замены текста, особенно при работе с большими или сложными PDF‑файлами.

Библиотека Aspose.PDF for Python via .NET предоставляет эффективный способ удалить такие избыточные шрифты с помощью класса TextEditOptions. Это не только оптимизирует ваш документ, но и гарантирует, что он использует только те шрифты, которые действительно применяются к видимому тексту.

Метод 'remove_unused_fonts()' — простой, но мощный способ оптимизировать PDF‑файлы, удаляя избыточные данные шрифтов.

Этот пример демонстрирует, как:

- Просканировать PDF на неиспользуемые шрифты.
- Удалите их безопасно.
- Переназначить активные фрагменты текста на единый шрифт (например, Times New Roman).

1. Откройте PDF-документ.
1. Настройте параметры редактирования текста. Это указывает движку удалить все встроенные шрифты, которые в данный момент не используются в видимом тексте.
1. Создайте Text Absorber с параметрами. TextFragmentAbsorber извлекает фрагменты текста из документа для редактирования.
1. Переприсвоить стандартный Font. Как только absorber соберёт все фрагменты, пройдитесь по ним и примените единый Font.
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

Удалить весь текстовый контент из PDF‑файла, сохранив при этом изображения, фигуры и структуры макета нетронутыми.
Используя TextFragmentAbsorber, код эффективно сканирует весь документ и удаляет каждый найденный фрагмент текста на каждой странице.

1. Загрузите PDF-документ.
1. Создается объект TextFragmentAbsorber для обнаружения и обработки текстовых фрагментов в PDF.
1. Удалите весь текстовый контент. Метод 'absorber.remove_all_text()' удаляет каждый текстовый элемент из загруженного документа, оставляя нетекстовые компоненты нетронутыми.
1. Сохраните обновлённый документ.

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

### Удалить весь текст с определённой страницы

Удалите весь текст с одной страницы PDF‑документа, используя класс TextFragmentAbsorber в Aspose.PDF.
В отличие от удаления всего документа, этот метод выполняет очистку текста на уровне страницы, удаляя текст только с выбранной страницы, оставляя все остальные страницы нетронутыми.

1. Загрузите PDF-файл.
1. Создайте экземпляр TextFragmentAbsorber.
1. Удалите весь текст с первой страницы.
1. Сохраните изменённый PDF.

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

Удалите весь текст из конкретного прямоугольного региона на странице, используя Aspose.PDF TextFragmentAbsorber.
Вместо полной очистки страницы этот метод выполняет целенаправленное удаление текста, позволяя точно контролировать, какая часть страницы будет затронута.

1. Загрузите PDF-документ.
1. Создайте TextFragmentAbsorber.
1. Определите целевую область (прямоугольник).
1. Удалите текст из указанной области.
1. Сохраните остальную часть документа.
1. Сохраните изменённый PDF.

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

### Удалить весь скрытый текст из PDF-документа

Удалите весь текст из конкретного прямоугольного региона на странице, используя Aspose.PDF TextFragmentAbsorber.
Вместо полной очистки страницы этот метод выполняет целенаправленное удаление текста, позволяя точно контролировать, какая часть страницы будет затронута.

1. Загрузите PDF-документ.
1. Создайте TextFragmentAbsorber.
1. Определите целевую область (прямоугольник).
1. Удалите текст из указанной области.
1. Сохраните остальную часть документа.
1. Сохраните изменённый PDF.

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
- [Форматировать текст PDF в Python](/pdf/ru/python-net/text-formatting-inside-pdf/)
