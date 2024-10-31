---
title: Форматирование PDF документа с использованием Python
linktitle: Форматирование PDF документа
type: docs
weight: 11
url: /python-net/formatting-pdf-document/
description: Создание и форматирование PDF документа с помощью Aspose.PDF для Python через .NET. Используйте следующий фрагмент кода для решения ваших задач.
lastmod: "2023-04-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Форматирование PDF документа с использованием Python",
    "alternativeHeadline": "Как форматировать PDF документ в Python через .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, dotnet, python, форматирование PDF документа",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/formatting-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/formatting-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Создание и форматирование PDF документа с помощью Aspose.PDF для Python через .NET. Используйте следующий фрагмент кода для решения ваших задач."
}
</script>


## Форматирование PDF-документа

### Получение свойств окна документа и отображения страниц

Эта тема поможет вам понять, как получить свойства окна документа, приложения просмотра и как отображаются страницы. Чтобы установить эти свойства:

Откройте PDF-файл, используя класс [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Теперь вы можете установить свойства объекта Document, такие как

- CenterWindow – Центрировать окно документа на экране. По умолчанию: false.
- Direction – Порядок чтения. Это определяет, как страницы располагаются при отображении бок о бок. По умолчанию: слева направо.
- DisplayDocTitle – Отображать заголовок документа в строке заголовка окна документа. По умолчанию: false (заголовок отображается).
- HideMenuBar – Скрыть или отобразить строку меню окна документа. По умолчанию: false (строка меню отображается).
- HideToolBar – Скрыть или отобразить панель инструментов окна документа. По умолчанию: false (панель инструментов отображается).
- HideWindowUI – Скрыть или отобразить элементы окна документа, такие как полосы прокрутки.
 Default: false (элементы интерфейса отображаются).
- NonFullScreenPageMode – Как документ отображается, когда он не в полноэкранном режиме.
- PageLayout – Макет страницы.
- PageMode – Как документ отображается при первом открытии. Опции: отображать эскизы, полноэкранный режим, показывать панель вложений.

Следующий фрагмент кода показывает, как получить свойства с использованием класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Получить различные свойства документа
    # Позиция окна документа - По умолчанию: false
    print("CenterWindow :", document.center_window)

    # Преобладающий порядок чтения; определяет позицию страницы
    # При отображении рядом - По умолчанию: L2R
    print("Direction :", document.direction)

    # Должна ли строка заголовка окна отображать заголовок документа
    # Если false, строка заголовка отображает имя файла PDF - По умолчанию: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Должно ли изменяться размер окна документа, чтобы соответствовать размеру
    # Первой отображаемой страницы - По умолчанию: false
    print("FitWindow :", document.fit_window)

    # Должно ли скрываться строка меню приложения просмотра - По умолчанию: false
    print("HideMenuBar :", document.hide_menubar)

    # Должно ли скрываться панель инструментов приложения просмотра - По умолчанию: false
    print("HideToolBar :", document.hide_tool_bar)

    # Должны ли скрываться элементы интерфейса, такие как полосы прокрутки
    # И оставлять только содержимое страницы - По умолчанию: false
    print("HideWindowUI :", document.hide_window_ui)

    # Режим страницы документа. Как отображать документ при выходе из полноэкранного режима.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # Макет страницы, т.е. одиночная страница, одна колонка
    print("PageLayout :", document.page_layout)

    # Как документ должен отображаться при открытии
    # Т.е. отображать эскизы, полноэкранный режим, показывать панель вложений
    print("pageMode :", document.page_mode)

```

### Установите свойства окна документа и отображения страницы

Эта тема объясняет, как установить свойства окна документа, программы просмотра и отображения страницы. Чтобы установить эти различные свойства:

1. Откройте PDF-файл с помощью класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Установите свойства объекта Document.
1. Сохраните обновленный PDF-файл, используя метод save.

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

Каждое из них используется и описано в коде ниже. Следующий фрагмент кода показывает, как установить свойства с использованием класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Установить различные свойства документа
    # Указать позиционирование окна документа - По умолчанию: false
    document.center_window = True

    # Преобладающий порядок чтения; определяет позицию страницы
    # При отображении рядом друг с другом - По умолчанию: L2R
    document.direction = ap.Direction.R2L

    # Указать, должна ли строка заголовка окна отображать заголовок документа
    # Если false, строка заголовка отображает имя PDF-файла - По умолчанию: false
    document.display_doc_title = True

    # Указать, следует ли изменить размер окна документа по размеру
    # Первой отображаемой страницы - По умолчанию: false
    document.fit_window = True

    # Указать, следует ли скрыть строку меню программы просмотра - По умолчанию: false
    document.hide_menubar = True

    # Указать, следует ли скрыть панель инструментов программы просмотра - По умолчанию: false
    document.hide_tool_bar = True

    # Указать, следует ли скрыть элементы UI, такие как полосы прокрутки
    # И оставить отображенными только содержимое страницы - По умолчанию: false
    document.hide_window_ui = True

    # Режим страницы документа. указать, как отображать документ при выходе из полноэкранного режима.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Указать макет страницы, т.е. одна страница, одна колонка
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Указать, как документ должен отображаться при открытии
    # Т.е. показывать миниатюры, полноэкранный режим, показывать панель вложений
    document.page_mode = ap.PageMode.USE_THUMBS

    # Сохранить обновленный PDF-файл
    document.save(output_pdf)
```


### Встраивание стандартных шрифтов Type 1

Некоторые PDF-документы содержат шрифты из специального набора шрифтов Adobe. Шрифты из этого набора называются «Стандартные шрифты Type 1». Этот набор включает 14 шрифтов, и встраивание такого типа шрифтов требует использования специальных флагов, например [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Ниже приведен фрагмент кода, который можно использовать для получения документа со всеми встроенными шрифтами, включая стандартные шрифты Type 1:

```python

    import aspose.pdf as ap

    # Загрузить существующий PDF-документ
    document = ap.Document(input_pdf)
    # Установить свойство EmbedStandardFonts для документа
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Проверить, встроен ли шрифт
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Встраивание шрифтов при создании PDF

Если вам нужно использовать любой шрифт, кроме 14 основных шрифтов, поддерживаемых Adobe Reader, вы должны встроить описание шрифта при создании файла PDF. Если информация о шрифте не встроена, Adobe Reader возьмет её из операционной системы, если она установлена в системе, или создаст заменяющий шрифт в соответствии с дескриптором шрифта в PDF.

>Обратите внимание, что встроенный шрифт должен быть установлен на хост-машине, т.е. в случае следующего кода шрифт ‘Univers Condensed’ установлен в системе.

Мы используем свойство 'is_embedded', чтобы встроить информацию о шрифте в файл PDF. Установка значения этого свойства в 'True' встраивает весь файл шрифта в PDF, зная, что это увеличит размер PDF-файла. Ниже приведен фрагмент кода, который можно использовать для встраивания информации о шрифте в PDF.

```python

    import aspose.pdf as ap

    # Создать объект Pdf, вызвав его пустой конструктор
    doc = ap.Document()

    # Создать секцию в объекте Pdf
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" Это образец текста с использованием пользовательского шрифта.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Сохранить PDF-документ
    doc.save(output_pdf)
```


### Установить имя шрифта по умолчанию при сохранении PDF

Когда PDF-документ содержит шрифты, которые недоступны в самом документе и на устройстве, API заменяет эти шрифты на шрифт по умолчанию. Если шрифт доступен (установлен на устройстве или встроен в документ), итоговый PDF должен иметь тот же шрифт (не должен быть заменен на шрифт по умолчанию). Значение шрифта по умолчанию должно содержать имя шрифта (не путь к файлам шрифта). Мы реализовали функцию установки имени шрифта по умолчанию при сохранении документа как PDF. Следующий фрагмент кода можно использовать для установки шрифта по умолчанию:

```python

    import aspose.pdf as ap

    # Загрузить существующий PDF-документ с отсутствующим шрифтом
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Указать имя шрифта по умолчанию
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Получить все шрифты из PDF-документа

Если вы хотите получить все шрифты из PDF-документа, вы можете использовать метод [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties), предоставленный в классе [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
 Пожалуйста, проверьте следующий фрагмент кода, чтобы получить все шрифты из существующего PDF документа:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Улучшение встраивания шрифтов с использованием FontSubsetStrategy

Следующий фрагмент кода показывает, как установить [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) использованную в свойстве [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties):

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # Все шрифты будут встроены как подмножество в документ в случае SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Подмножество шрифта будет встроено для полностью встроенных шрифтов, но шрифты, которые не встроены в документ, не будут затронуты.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Установка и получение коэффициента масштабирования PDF-файла

Иногда необходимо определить текущий коэффициент масштабирования PDF-документа. С помощью Aspose.Pdf вы можете узнать текущее значение, а также установить его.

Свойство Destination класса [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) позволяет получить значение масштабирования, связанное с PDF-файлом. Аналогично, его можно использовать для установки коэффициента масштабирования файла.

#### Установка коэффициента масштабирования

Следующий фрагмент кода показывает, как установить коэффициент масштабирования PDF-файла.

```python

    import aspose.pdf as ap

    # Создать новый объект Document
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Сохранить документ
    doc.save(output_pdf)
```

#### Получение коэффициента масштабирования

Следующий фрагмент кода показывает, как получить коэффициент масштабирования PDF-файла.

```python

    import aspose.pdf as ap

    # Создать новый объект Document
    doc = ap.Document(input_pdf)

    # Создать объект GoToAction
    action = doc.open_action

    # Получить коэффициент масштабирования PDF-файла
    print(action.destination.zoom)
```


### Установка свойств предварительной настройки диалогового окна печати

Aspose.PDF позволяет установить [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) для членов PDF-документа. Это позволяет изменить свойство DuplexMode для PDF-документа, которое по умолчанию установлено на simplex. Это можно сделать, используя две разные методологии, как показано ниже.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Установка свойств предварительной настройки диалогового окна печати с использованием редактора содержимого PDF

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("Файл имеет двустороннюю печать с коротким переворотом")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```