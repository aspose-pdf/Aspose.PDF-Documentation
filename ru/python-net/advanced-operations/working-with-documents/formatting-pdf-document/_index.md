---
title: Форматирование PDF‑документа с использованием Python
linktitle: Форматирование PDF‑документа
type: docs
weight: 11
url: /ru/python-net/formatting-pdf-document/
description: Создайте и отформатируйте PDF‑документ с помощью Aspose.PDF for Python via .NET. Используйте следующий фрагмент кода для решения ваших задач.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Форматирование PDF‑документов с использованием Python
Abstract: Статья предоставляет всестороннее руководство по работе с PDF‑документами и их форматированию с использованием библиотеки Aspose.PDF в Python. В ней рассматриваются различные аспекты настройки PDF, включая установку свойств окна документа и отображения страниц, таких как центрирование окна, направление чтения и скрытие элементов пользовательского интерфейса. В статье объясняется, как программно получать и задавать эти свойства с помощью класса `Document`. Кроме того, рассматривается управление шрифтами, детально описывается встраивание стандартных шрифтов Type 1 и других шрифтов в PDF, обеспечивая переносимость документа и визуальную согласованность на разных системах. Также освещаются приемы установки имени шрифта по умолчанию, получения всех шрифтов из PDF и улучшения встраивания шрифтов с использованием `FontSubsetStrategy`. Далее статья раскрывает настройку коэффициента масштабирования PDF‑документов с помощью класса `GoToAction` и конфигурирование предустановленных свойств диалогового окна печати, включая опции дуплексной печати. Для каждого раздела приведены фрагменты кода, предоставляющие практические примеры реализации этих функций.
---

## Форматирование PDF‑документа

### Получить свойства окна документа и отображения страниц

Эта тема поможет вам понять, как получать свойства окна документа, приложения‑просмотрщика и как отображаются страницы. Чтобы установить эти свойства:

Откройте PDF‑файл с помощью класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Теперь вы можете задавать свойства объекта Document, такие как

- CenterWindow – Центрировать окно документа на экране. По умолчанию: false.
- Direction – Порядок чтения. Определяет, как страницы размещаются при отображении рядом. По умолчанию: слева направо.
- DisplayDocTitle – Отображать заголовок документа в строке заголовка окна документа. По умолчанию: false (заголовок отображается).
- HideMenuBar – Скрывать или отображать строку меню окна документа. По умолчанию: false (строка меню отображается).
- HideToolBar – Скрывать или отображать панель инструментов окна документа. По умолчанию: false (панель инструментов отображается).
- HideWindowUI – Скрывать или отображать элементы пользовательского интерфейса окна документа, такие как полосы прокрутки. По умолчанию: false (элементы UI отображаются).
- NonFullScreenPageMode – Как документ отображается, когда он не в полноэкранном режиме.
- PageLayout – Макет страницы.
- PageMode – Как документ отображается при первом открытии. Варианты: показать миниатюры, полноэкранный режим, показать панель вложений.

Следующий фрагмент кода показывает, как получить свойства с помощью класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get different document properties
    # Position of document's window - Default: false
    print("CenterWindow :", document.center_window)

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    print("Direction :", document.direction)

    # Whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    print("FitWindow :", document.fit_window)

    # Whether to hide menu bar of the viewer application - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Whether to hide tool bar of the viewer application - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Document's page mode. How to display document on exiting full-screen mode.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # The page layout i.e. single page, one column
    print("PageLayout :", document.page_layout)

    # How the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    print("pageMode :", document.page_mode)

```

### Установить свойства окна документа и отображения страниц

Эта тема объясняет, как задавать свойства окна документа, приложения‑просмотрщика и отображения страниц. Чтобы установить эти различные свойства:

1. Откройте PDF‑файл с помощью класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Задайте свойства объекта Document.
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

Каждый из них используется и описывается в коде ниже. Следующий фрагмент кода показывает, как задать свойства с помощью класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set different document properties
    # Sepcify to position document's window - Default: false
    document.center_window = True

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    document.direction = ap.Direction.R2L

    # Specify whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    document.display_doc_title = True

    # Specify whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    document.fit_window = True

    # Specify whether to hide menu bar of the viewer application - Default: false
    document.hide_menubar = True

    # Specify whether to hide tool bar of the viewer application - Default: false
    document.hide_tool_bar = True

    # Specify whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    document.hide_window_ui = True

    # Document's page mode. specify how to display document on exiting full-screen mode.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Specify the page layout i.e. single page, one column
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Specify how the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_THUMBS

    # Save updated PDF file
    document.save(output_pdf)
```

### Встраивание стандартных шрифтов Type 1

Некоторые PDF‑документы используют шрифты из специального набора шрифтов Adobe. Шрифты из этого набора называются «Standard Type 1 Fonts». Набор включает 14 шрифтов, и встраивание такого типа шрифтов требует использования специальных флагов, например [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Ниже приведён фрагмент кода, который можно использовать для получения документа со всеми шрифтами, включая стандартные шрифты Type 1:

```python

    import aspose.pdf as ap

    # Load an existing PDF Document
    document = ap.Document(input_pdf)
    # Set EmbedStandardFonts property of document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Check if font is already embedded
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Встраивание шрифтов при создании PDF

Если вам необходимо использовать любой шрифт, кроме 14 базовых шрифтов, поддерживаемых Adobe Reader, вы должны встроить описание шрифта при генерации PDF‑файла. Если информация о шрифте не встроена, Adobe Reader возьмёт её из операционной системы, если шрифт установлен, либо создаст заменяющий шрифт согласно дескриптору шрифта в PDF.

>Обратите внимание, что встроенный шрифт должен быть установлен на хост‑машине, т.е. в случае следующего кода шрифт ‘Univers Condensed’ установлен в системе.

Мы используем свойство 'is_embedded' для встраивания информации о шрифте в PDF‑файл. Установка значения этого свойства в 'True' внедрит полностью файл шрифта в PDF, при этом увеличив размер PDF‑файла. Ниже приведён фрагмент кода, который можно использовать для встраивания информации о шрифте в PDF.

```python

    import aspose.pdf as ap

    # Instantiate Pdf object by calling its empty constructor
    doc = ap.Document()

    # Create a section in the Pdf object
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Save PDF Document
    doc.save(output_pdf)
```

### Установить имя шрифта по умолчанию при сохранении PDF

Когда PDF‑документ содержит шрифты, которые недоступны в самом документе и на устройстве, API заменяет эти шрифты шрифтом по умолчанию. Если шрифт доступен (установлен на устройстве или внедрён в документ), выходной PDF должен содержать тот же шрифт (не должен заменяться шрифтом по умолчанию). Значение шрифта по умолчанию должно содержать имя шрифта (а не путь к файлам шрифта). Мы реализовали функцию установки имени шрифта по умолчанию при сохранении документа в PDF. Ниже приведён фрагмент кода, который можно использовать для установки шрифта по умолчанию:

```python

    import aspose.pdf as ap

    # Load an existing PDF document with missing font
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Specify Default Font Name
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Получить все шрифты из PDF‑документа

Если вы хотите получить все шрифты из PDF‑документа, вы можете использовать метод [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties), предоставленный в классе [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Пожалуйста, посмотрите следующий фрагмент кода, чтобы получить все шрифты из существующего PDF‑документа:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Улучшить внедрение шрифтов с помощью FontSubsetStrategy

Следующий фрагмент кода показывает, как установить свойство [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/), используемое в [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties):

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # All fonts will be embedded as subset into document in case of SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Получить/установить коэффициент масштабирования PDF‑файла

Иногда вам нужно определить текущий коэффициент масштабирования PDF‑документа. С Aspose.Pdf вы можете узнать текущое значение, а также установить его.

Свойство Destination класса [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) позволяет получить значение масштабирования, связанное с PDF‑файлом. Аналогично, его можно использовать для установки коэффициента масштабирования файла.

#### Установить коэффициент масштабирования

Следующий фрагмент кода показывает, как установить коэффициент масштабирования PDF‑файла.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Save the document
    doc.save(output_pdf)
```

#### Получить коэффициент масштабирования

Следующий фрагмент кода показывает, как получить коэффициент масштабирования PDF‑файла.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    # Create GoToAction object
    action = doc.open_action

    # Get the Zoom factor of PDF file
    print(action.destination.zoom)
```

### Настройка предустановленных свойств диалогового окна печати

Aspose.PDF позволяет задавать члены [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) PDF‑документа. Это позволяет изменить свойство DuplexMode для PDF‑документа, которое по умолчанию установлено в simplex. Это можно выполнить двумя различными методологиями, как показано ниже.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Настройка предустановленных свойств диалогового окна печати с помощью PDF Content Editor

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("The file has duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```


