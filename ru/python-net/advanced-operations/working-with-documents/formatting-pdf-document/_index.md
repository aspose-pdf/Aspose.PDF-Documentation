---
title: Форматировать PDF-документы в Python
linktitle: Форматирование PDF-документа
type: docs
weight: 11
url: /ru/python-net/formatting-pdf-document/
description: Узнайте, как форматировать PDF‑документы, встраивать шрифты, управлять настройками просмотрщика и настраивать параметры отображения в Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Форматирование PDF‑документов с использованием Python
Abstract: Статья предоставляет исчерпывающее руководство по манипулированию и форматированию PDF‑документов с использованием библиотеки Aspose.PDF в Python. Она охватывает различные аспекты настройки PDF, включая установку свойств окна документа и отображения страниц, таких как центрирование окна, направление чтения и скрытие элементов интерфейса. В статье объясняется, как программно получать и задавать эти свойства с помощью класса `Document`. Кроме того, рассматривается управление шрифтами, подробно описывается, как встраивать стандартные шрифты Type 1 и другие шрифты в PDF, обеспечивая переносимость документа и визуальную согласованность между системами. Также выделяются техники установки имени шрифта по умолчанию, получения всех шрифтов из PDF и улучшения встраивания шрифтов с использованием `FontSubsetStrategy`. Далее статья раскрывает настройку коэффициента масштабирования PDF‑документов с помощью класса `GoToAction` и конфигурацию предустановок диалогового окна печати, включая варианты двусторонней печати. Для каждого раздела приведены фрагменты кода, предоставляющие практические примеры реализации этих функций.
---

Это руководство полезно, когда вам необходимо управлять поведением PDF‑просмотрщика, встраиванием шрифтов, настройками отображения по умолчанию или параметрами печати в генерируемых Python документах.

## Форматирование PDF-документа

### Получить свойства окна документа и отображения страниц

Эта тема поможет вам понять, как получить свойства окна документа, приложения‑просмотрщика и как отображаются страницы. Чтобы установить эти свойства:

Откройте PDF-файл с помощью [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс. Теперь вы можете установить свойства объекта Document, такие как

- CenterWindow – Центрировать окно документа на экране. По умолчанию: false.
- Direction – Порядок чтения. Это определяет, как страницы располагаются при отображении рядом. По умолчанию: слева направо.
- DisplayDocTitle – Отобразить заголовок документа в строке заголовка окна документа. По умолчанию: false (заголовок отображается).
- HideMenuBar – Скрыть или отобразить панель меню окна документа. По умолчанию: false (панель меню отображается).
- HideToolBar – Скрыть или отобразить панель инструментов окна документа. По умолчанию: false (панель инструментов отображается).
- HideWindowUI – Скрыть или отобразить элементы окна документа, такие как полосы прокрутки. По умолчанию: false (элементы интерфейса отображаются).
- NonFullScreenPageMode – Как отображается документ, когда он не в полноэкранном режиме.
- PageLayout – макет страницы.
- PageMode – Как документ отображается при первом открытии. Варианты: показать миниатюры, полноэкранный режим, показать панель вложений.

Следующий фрагмент кода показывает, как получить свойства, используя [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### Установить свойства окна документа и отображения страницы

Эта тема объясняет, как задать свойства окна документа, приложения‑просмотрщика и отображения страницы. Чтобы задать эти разные свойства:

1. Откройте PDF-файл с помощью [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.
1. Установите свойства объекта Document.
1. Сохраните обновлённый PDF‑файл, используя метод save.

Доступные свойства:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Каждый используется и описан в коде ниже. Следующий - фрагмент кода показывает, как установить свойства, используя [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### Встраивание стандартных шрифтов Type 1

Некоторые PDF‑документы используют шрифты из специального набора шрифтов Adobe. Шрифты из этого набора называются “Standard Type 1 Fonts”. Этот набор включает 14 шрифтов, и встраивание такого типа шрифтов требует использования специальных флагов, т. е [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Следующий фрагмент кода, который можно использовать, чтобы получить документ со всеми встроенными шрифтами, включая стандартные шрифты Type 1:

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Встраивание Fonts при создании PDF

Если вам требуется использовать любой шрифт, отличный от 14 основных шрифтов, поддерживаемых Adobe Reader, вы должны внедрить описание шрифта при создании PDF‑файла. Если информация о шрифте не внедрена, Adobe Reader возьмёт её из операционной системы, если шрифт установлен в системе, либо построит заменяющий шрифт в соответствии с дескриптором шрифта в PDF.

>Обратите внимание, встроенный шрифт должен быть установлен на хост‑машине, т.е. в случае следующего кода шрифт ‘Univers Condensed’ установлен в системе.

Мы используем свойство 'is_embedded' для встраивания информации о шрифте в файл PDF. Установка значения этого свойства в 'True' встроит полный файл шрифта в PDF, учитывая тот факт, что это увеличит размер файла PDF. Ниже приведён фрагмент кода, который можно использовать для встраивания информации о шрифте в PDF.

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### Установить имя шрифта по умолчанию при сохранении PDF

Когда PDF‑документ содержит шрифты, которые недоступны ни в самом документе, ни на устройстве, API заменяет эти шрифты шрифтом по умолчанию. Если шрифт доступен (установлен на устройстве или встроен в документ), результирующий PDF должен использовать тот же шрифт (не должен заменяться шрифтом по умолчанию). Значение шрифта по умолчанию должно содержать название шрифта (а не путь к файлам шрифтов). Мы реализовали возможность задавать название шрифта по умолчанию при сохранении документа в PDF. Ниже приведён фрагмент кода, который можно использовать для установки шрифта по умолчанию:

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### Получить все шрифты из PDF Document

Если вы хотите получить все шрифты из PDF‑документа, вы можете использовать [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) метод, предоставленный в [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс. Пожалуйста, проверьте следующий фрагмент кода, чтобы получить все шрифты из существующего PDF‑документа:

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### Улучшить встраивание шрифтов с использованием FontSubsetStrategy

Следующий фрагмент кода показывает, как установить [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) использовано [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) свойство:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### Получить/установить коэффициент масштабирования PDF‑файла

Иногда вам нужно определить текущий коэффициент масштабирования PDF‑документа. С помощью Aspose.Pdf вы можете узнать текущее значение, а также установить его.

Эта [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) class Destination property позволяет получить значение масштабирования, связанное с PDF‑файлом. Аналогично, его можно использовать для установки коэффициента масштабирования файла.

#### Установить коэффициент масштабирования

Следующий фрагмент кода демонстрирует, как установить коэффициент масштабирования PDF-файла.

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### Получить коэффициент масштабирования

В следующем фрагменте кода показано, как получить коэффициент масштабирования PDF‑файла.

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## Связанные темы Document

- [Работа с PDF документами в Python](/pdf/ru/python-net/working-with-documents/)
- [Создайте PDF-файлы в Python](/pdf/ru/python-net/create-pdf-document/)
- [Манипулировать PDF документами в Python](/pdf/ru/python-net/manipulate-pdf-document/)
- [Оптимизировать PDF файлы в Python](/pdf/ru/python-net/optimize-pdf/)
