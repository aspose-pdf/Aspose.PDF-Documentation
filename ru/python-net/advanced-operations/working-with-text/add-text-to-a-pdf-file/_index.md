---
title: Добавление текста в PDF с использованием Python
linktitle: Добавление текста в PDF
type: docs
weight: 10
url: /ru/python-net/add-text-to-pdf-file/
description: Эта статья описывает различные аспекты работы с текстом в Aspose.PDF. Узнайте, как добавить текст в PDF, добавить HTML-фрагменты или использовать пользовательские шрифты OTF.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Добавление текста в PDF с использованием Python",
    "alternativeHeadline": "Как добавить текст в PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, python, добавление текста в pdf",
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
    "url": "/python-net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-02-04",
    "description": "Эта статья описывает различные аспекты работы с текстом в Aspose.PDF для Python. Узнайте, как добавить текст в PDF, добавить HTML-фрагменты или использовать пользовательские шрифты OTF."
}
</script>


## Добавление текста

1. Откройте входной PDF-документ с помощью Aspose.PDF.
1. Выберите конкретную страницу, на которую вы хотите добавить текст.
1. Создайте объект TextFragment. Текстовый фрагмент создается с содержимым 'main text'. Этот фрагмент позиционируется на координатах (100, 600) на странице.
1. Установка свойств текста. Устанавливаются различные свойства текста, такие как размер шрифта, тип шрифта (Times New Roman), цвет фона (светло-серый) и цвет переднего плана (красный).
1. Создайте объект TextBuilder. Объект TextBuilder создается с выбранной страницей.
1. Добавьте текстовый фрагмент. Созданный ранее текстовый фрагмент добавляется на страницу PDF с использованием объекта TextBuilder.
1. Вызовите метод [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) и сохраните выходной PDF-файл.

Следующий фрагмент кода показывает, как добавить текст в существующий PDF-файл:

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Получить конкретную страницу
    page = document.pages[1]

    # Создать текстовый фрагмент
    text_fragment = ap.text.TextFragment("main text")
    text_fragment.position = ap.text.Position(100, 600)

    # Установить свойства текста
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Создать объект TextBuilder
    builder = ap.text.TextBuilder(page)

    # Добавить текстовый фрагмент на страницу PDF
    builder.append_text(text_fragment)

    # Сохранить результатирующий PDF-документ.
    document.save(output_pdf)             
```


## Загрузка шрифта из потока

Следующий фрагмент кода показывает, как загрузить шрифт из объектного потока при добавлении текста в PDF-документ.

```python

    import aspose.pdf as ap

    # Загрузить входной PDF файл
    document = ap.Document()
    document.pages.add()
    # Создать объект построителя текста для первой страницы документа
    text_builder = ap.text.TextBuilder(document.pages[1])
    # Создать фрагмент текста с примером строки
    text_fragment = ap.text.TextFragment("Hello world")

    if input_ttf != "":
        # Загрузить шрифт TrueType в объект потока
        font_stream = open(input_ttf, "rb")
        # Установить имя шрифта для текстовой строки
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # Указать позицию для текстового фрагмента
        text_fragment.position = ap.text.Position(10, 10)
        # Добавить текст в TextBuilder, чтобы он мог быть размещен на PDF файле
        text_builder.append_text(text_fragment)
        # Сохранить полученный PDF-документ.
        document.save(output_pdf)
```


## Добавить текст с использованием TextParagraph

Следующий фрагмент кода показывает, как добавить текст в PDF-документ с использованием класса [TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/).

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document()
    # Добавить страницу в коллекцию страниц объекта Document
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # Создать текстовый абзац
    paragraph = ap.text.TextParagraph()
    # Установить отступ последующих строк
    paragraph.subsequent_lines_indent = 20
    # Указать местоположение для добавления TextParagraph
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # Указать режим переноса слов
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # Создать текстовый фрагмент
    fragment1 = ap.text.TextFragment("the quick brown fox jumps over the lazy dog")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # Добавить фрагмент в абзац
    paragraph.append_line(fragment1)
    # Добавить абзац
    builder.append_paragraph(paragraph)

    # Сохранить полученный PDF-документ.
    document.save(output_pdf)
```


## Добавить гиперссылку к TextSegment

Этот код демонстрирует, как создать динамический и интерактивный контент в PDF-документе, включая гиперссылки на внешние ресурсы.

Страница PDF может состоять из одного или нескольких объектов TextFragment, где каждый объект TextFragment может иметь один или несколько экземпляров [TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/).

Пожалуйста, попробуйте использовать следующий фрагмент кода для выполнения этого требования:

```python

    import aspose.pdf as ap

    # Создать экземпляр документа
    document = ap.Document()
    # Добавить страницу в коллекцию страниц PDF файла
    page1 = document.pages.add()
    # Создать экземпляр TextFragment
    tf = ap.text.TextFragment("Пример текстового фрагмента")
    # Установить горизонтальное выравнивание для TextFragment
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # Создать текстовый сегмент с примером текста
    segment = ap.text.TextSegment(" ... Текстовый сегмент 1...")
    # Добавить сегмент в коллекцию сегментов TextFragment
    tf.segments.append(segment)
    # Создать новый TextSegment
    segment = ap.text.TextSegment("Ссылка на Google")
    # Добавить сегмент в коллекцию сегментов TextFragment
    tf.segments.append(segment)
    # Установить гиперссылку для TextSegment
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # Установить цвет переднего плана для текстового сегмента
    segment.text_state.foreground_color = ap.Color.blue
    # Установить форматирование текста как курсив
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # Создать другой объект TextSegment
    segment = ap.text.TextSegment("TextSegment без гиперссылки")
    # Добавить сегмент в коллекцию сегментов TextFragment
    tf.segments.append(segment)
    # Добавить TextFragment в коллекцию абзацев объекта страницы
    page1.paragraphs.add(tf)
    # Сохранить итоговый PDF-документ.
    document.save(output_pdf)
```


## Использование шрифта OTF

Aspose.PDF для Python через .NET предлагает возможность использовать пользовательские/TrueType шрифты при создании/манипуляции содержимым PDF файла, чтобы содержимое файла отображалось с использованием шрифтов, отличных от стандартных системных шрифтов.

```python

    import aspose.pdf as ap

    # Создать новый экземпляр документа
    document = ap.Document()
    # Добавить страницу в коллекцию страниц PDF файла
    page = document.pages.add()
    # Создать экземпляр TextFragment с примером текста
    fragment = ap.text.TextFragment("Пример текста в шрифте OTF")
    # Или вы можете даже указать путь к OTF шрифту в системном каталоге
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # Указать внедрение шрифта в PDF файл, чтобы он отображался правильно,
    # Даже если конкретный шрифт не установлен/отсутствует на целевой машине
    fragment.text_state.font.is_embedded = True
    # Добавить TextFragment в коллекцию абзацев экземпляра страницы
    page.paragraphs.add(fragment)
    # Сохранить результирующий PDF документ.
    document.save(output_pdf)
```


## Добавление HTML строки с использованием DOM

Следующий код на Python использует библиотеку Aspose.PDF для создания PDF-документа с HTML-фрагментом.

1. Создайте экземпляр Document. Создается экземпляр класса Document, представляющий PDF-документ.
1. Добавьте страницу в PDF-документ.
1. Создайте объект HtmlFragment с содержимым HTML.
1. Установите отступы для HTML-фрагмента. В этом случае нижний отступ установлен на 10 пунктов, а верхний отступ — на 200 пунктов.
1. Добавьте HTML-фрагмент на страницу.
1. Сохраните PDF-файл.

```python

    import aspose.pdf as ap

    # Создать объект Document
    doc = ap.Document()
    # Добавить страницу в коллекцию страниц PDF-файла
    page = doc.pages.add()
    # Создать HtmlFragment с HTML содержимым
    title = ap.HtmlFragment("<fontsize=10><b><i>Таблица</i></b></fontsize>")
    # Установить информацию о нижнем отступе
    title.margin.bottom = 10
    # Установить информацию о верхнем отступе
    title.margin.top = 200
    # Добавить HTML-фрагмент в коллекцию абзацев страницы
    page.paragraphs.add(title)
    # Сохранить PDF-файл
    doc.save(output_pdf)
```


### Пользовательский стиль линии для FootNote

Следующий пример демонстрирует, как добавить сноски в нижнюю часть страницы PDF и определить пользовательский стиль линии.

```python

    import aspose.pdf as ap

    # Создать экземпляр Document
    doc = ap.Document()
    # Добавить страницу в коллекцию страниц PDF
    page = doc.pages.add()
    # Создать объект GraphInfo
    graph = ap.GraphInfo()
    # Установить ширину линии как 2
    graph.line_width = 2
    # Установить цвет для объекта graph
    graph.color = ap.Color.red
    # Установить значение dash array как 3
    graph.dash_array = [3]
    # Установить значение dash phase как 1
    graph.dash_phase = 1
    # Установить стиль линии сноски для страницы как graph
    page.note_line_style = graph
    # Создать экземпляр TextFragment
    text = ap.text.TextFragment("Hello World")
    # Установить значение FootNote для TextFragment
    text.foot_note = ap.Note("сноска для тестового текста 1")
    # Добавить TextFragment в коллекцию абзацев первой страницы документа
    page.paragraphs.add(text)
    # Создать второй TextFragment
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # Установить FootNote для второго текстового фрагмента
    text.foot_note = ap.Note("сноска для тестового текста 2")
    # Добавить второй текстовый фрагмент в коллекцию абзацев PDF-файла
    page.paragraphs.add(text)
    # Сохранить результирующий PDF-документ.
    doc.save(output_pdf)
```


### Настроить метку сноски

Следующий фрагмент кода показывает, как создать PDF-документ с текстовым фрагментом, содержащим сноску.

По умолчанию номер сноски увеличивается, начиная с 1. Однако может возникнуть необходимость установить пользовательскую метку сноски. Чтобы выполнить это требование, попробуйте использовать следующий фрагмент кода

```python

    import aspose.pdf as ap

    # Создать экземпляр документа
    document = ap.Document()
    # Добавить страницу в коллекцию страниц PDF
    page = document.pages.add()
    # Создать объект GraphInfo
    graph = ap.GraphInfo()
    # Установить ширину линии равной 2
    graph.line_width = 2
    # Установить цвет для объекта графика
    graph.color = ap.Color.red
    # Установить значение массива тире как 3
    graph.dash_array = [3]
    # Установить значение фазы тире как 1
    graph.dash_phase = 1
    # Установить стиль линии сноски для страницы как график
    page.note_line_style = graph
    # Создать экземпляр TextFragment
    text = ap.text.TextFragment("Hello World")
    # Установить значение сноски для TextFragment
    text.foot_note = ap.Note("сноска для тестового текста 1")
    # Указать пользовательскую метку для сноски
    text.foot_note.text = " Aspose"
    # Добавить TextFragment в коллекцию абзацев первой страницы документа
    page.paragraphs.add(text)
    # Сохранить результирующий PDF-документ.
    document.save(output_pdf)
```


## Добавление изображения и таблицы в сноску

Этот код демонстрирует, как создать PDF-документ с текстовым фрагментом, содержащим сложную сноску, которая включает изображение, текст и таблицу, используя Aspose.PDF для Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("some text")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("footnote text")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Row 1 Cell 1"))
    text.foot_note.paragraphs.add(table)

    # Сохранить результирующий PDF-документ.
    document.save(output_pdf)
```

## Как создать концевые сноски

Концевая сноска — это ссылка на источник, которая отсылает читателя к определённому месту в конце документа, где он может узнать источник информации или слов, цитируемых или упомянутых в документе.
 При использовании сносок, за вашей цитатой или перефразированным предложением или резюмированным материалом следует номер в верхнем регистре.

Этот код демонстрирует, как добавить фрагмент текста со сноской в PDF-документ с использованием Aspose.PDF для Python:

```python

    import aspose.pdf as ap

    # Создать экземпляр Document
    document = ap.Document()
    # Добавить страницу в коллекцию страниц PDF
    page = document.pages.add()
    # Создать экземпляр TextFragment
    text = ap.text.TextFragment("Hello World")
    # Установить значение EndNote для TextFragment
    text.end_note = ap.Note("sample End note")
    # Указать пользовательскую метку для FootNote
    text.end_note.text = " Aspose"
    # Добавить TextFragment в коллекцию абзацев первой страницы документа
    page.paragraphs.add(text)
    # Сохранить результирующий PDF-документ.
    document.save(output_pdf)
```

## Текст и изображение как встроенный абзац

Макет PDF-файла по умолчанию - это потоковый макет (сверху-слева направо-вниз). Следовательно, каждый новый элемент, добавляемый в PDF файл, добавляется в нижний правый поток. Однако, может возникнуть необходимость отображать различные элементы страницы, такие как изображение и текст, на одном уровне (один за другим). Один из подходов может заключаться в создании экземпляра таблицы и добавлении обоих элементов в отдельные ячейки. Однако, другой подход может быть использованием встроенного параграфа. Установив свойство IsInLineParagraph для изображения и текста в значение true, эти параграфы будут отображаться как встроенные с другими элементами страницы.

Следующий фрагмент кода показывает, как добавить текст и изображение как встроенные параграфы в PDF файл.

```python

    import aspose.pdf as ap

    # Создать экземпляр Document
    document = ap.Document()
    # Добавить страницу в коллекцию страниц экземпляра Document
    page = document.pages.add()
    # Создать TextFragment
    text = ap.text.TextFragment("Hello World.. ")
    # Добавить фрагмент текста в коллекцию параграфов объекта Page
    page.paragraphs.add(text)
    # Создать экземпляр изображения
    image = ap.Image()
    # Установить изображение как встроенный параграф, чтобы оно появилось сразу после
    # предыдущего объекта параграфа (TextFragment)
    image.is_in_line_paragraph = True
    # Указать путь к файлу изображения
    image.file = input_jpg
    # Установить высоту изображения (необязательно)
    image.fix_height = 30
    # Установить ширину изображения (необязательно)
    image.fix_width = 100
    # Добавить изображение в коллекцию параграфов объекта страницы
    page.paragraphs.add(image)
    # Повторно инициализировать объект TextFragment с другим содержимым
    text = ap.text.TextFragment(" Hello Again..")
    # Установить TextFragment как встроенный параграф
    text.is_in_line_paragraph = True
    # Добавить вновь созданный TextFragment в коллекцию параграфов страницы
    page.paragraphs.add(text)
    # Сохранить полученный PDF документ.
    document.save(output_pdf)
```

## Указание интервала между символами при добавлении текста

Следующий фрагмент кода показывает, как создать PDF-документ, содержащий текстовый фрагмент с увеличенным интервалом между символами.

Текст можно добавить внутри коллекции абзацев PDF-файлов, используя экземпляр TextFragment, или с помощью объекта TextParagraph, и даже можно вставить текст внутри PDF с помощью класса TextStamp.

### Использование TextBuilder и TextFragment

```python

    import aspose.pdf as ap

    # Создать экземпляр документа
    document = ap.Document()
    # Добавить страницу в коллекцию страниц документа
    document.pages.add()
    # Создать экземпляр TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Создать экземпляр текстового фрагмента с примерным содержимым
    wide_fragment = ap.text.TextFragment("Текст с увеличенным интервалом между символами")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # Указать интервал между символами для TextFragment
    wide_fragment.text_state.character_spacing = 2.0
    # Указать позицию TextFragment
    wide_fragment.position = ap.text.Position(100, 650)
    # Добавить TextFragment в экземпляр TextBuilder
    builder.append_text(wide_fragment)
    # Сохранить полученный PDF-документ.
    document.save(output_pdf)
```


### Использование TextParagraph

```python

    import aspose.pdf as ap

    # Создать экземпляр Document
    document = ap.Document()
    # Добавить страницу в коллекцию страниц Document
    document.pages.add()
    # Создать экземпляр TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # Создать экземпляр TextParagraph
    paragraph = ap.text.TextParagraph()
    # Создать экземпляр TextState для указания имени и размера шрифта
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # Указать интервал между символами
    state.character_spacing = 1.5
    # Добавить текст в объект TextParagraph
    tt = "Это абзац с интервалом между символами"
    paragraph.append_line(tt, state)
    # Указать позицию для TextParagraph
    paragraph.position = ap.text.Position(100, 550)
    # Добавить TextParagraph в экземпляр TextBuilder
    builder.append_paragraph(paragraph)
    # Сохранить результирующий PDF-документ.
    document.save(output_pdf)
```

### Использование TextStamp

```python

    import aspose.pdf as ap

    # Создать экземпляр Document
    document = ap.Document()
    # Добавить страницу в коллекцию страниц Document
    page = document.pages.add()
    # Создать экземпляр TextStamp с примерным текстом
    stamp = ap.TextStamp("Это текстовый штамп с интервалом между символами")
    # Указать имя шрифта для объекта Stamp
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # Указать размер шрифта для TextStamp
    stamp.text_state.font_size = 12
    # Указать интервал между символами как 1
    stamp.text_state.character_spacing = 1
    # Установить x_indent для штампа
    stamp.x_indent = 100
    # Установить y_indent для штампа
    stamp.y_indent = 500
    # Добавить текстовый штамп на страницу
    stamp.put(page)
    # Сохранить результирующий PDF-документ.
    document.save(output_pdf)
```


## Создание PDF-документа с несколькими колонками

[Aspose.PDF для Python через .NET](https://docs.aspose.com/pdf/python-net/) также предлагает возможность создания нескольких колонок внутри страниц PDF-документов. Для того чтобы создать PDF-файл с несколькими колонками, мы можем использовать класс FloatingBox, так как он предоставляет свойство column_info для указания количества колонок внутри FloatingBox, а также мы можем указать расстояние между колонками и ширину колонок, используя свойства column_spacing и width соответственно.

Расстояние между колонками означает пространство между колонками, и по умолчанию расстояние между колонками составляет 1,25 см. Если ширина колонки не указана, то [Aspose.PDF для Python через .NET](https://docs.aspose.com/pdf/python-net/) автоматически рассчитывает ширину для каждой колонки в соответствии с размером страницы и расстоянием между колонками.

Ниже приведен пример, демонстрирующий создание двух колонок с объектами графиков (Линия), которые добавляются в коллекцию параграфов FloatingBox, а затем добавляются в коллекцию параграфов экземпляра Page.

```python

    import aspose.pdf as ap

    document = ap.Document()
    # Укажите информацию о левом поле для PDF файла
    document.page_info.margin.left = 40
    # Укажите информацию о правом поле для PDF файла
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # Добавьте линию в коллекцию параграфов объекта секции
    page.paragraphs.add(graph1)

    # Укажите координаты для линии
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # Создайте строковые переменные с текстом, содержащим html теги
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> Как избежать денежных афер</<strong> "
        + "</font>"
    )
    # Создайте текстовые параграфы, содержащие HTML текст
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # Добавьте четыре колонки в секцию
    box.column_info.column_count = 2
    # Установите расстояние между колонками
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("От сотрудника Google (Официальный блог Google)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # Создайте объект графиков для рисования линии
    graph2 = ap.drawing.Graph(50, 10)
    # Укажите координаты для линии
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # Добавьте линию в коллекцию параграфов объекта секции
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "Сед augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # Сохраните PDF файл
    document.save(output_pdf)
```


## Работа с пользовательскими табуляциями

Этот фрагмент кода на Python показывает, как создать PDF-документ, содержащий текстовые фрагменты, расположенные с использованием табуляций для имитации структуры таблицы.

Вот пример того, как установить пользовательские табуляции.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "Это пример формирования таблицы с использованием табуляций", ts
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts)

    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts)
    text2 = ap.text.TextFragment("#$TABdata21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```


## Как добавить прозрачный текст в PDF

Файл PDF содержит объекты Image, Text, Graph, attachment, Annotations, и при создании TextFragment вы можете установить информацию о переднем, заднем фоне, а также форматирование текста. Aspose.PDF для Python через .NET поддерживает возможность добавления текста с альфа-каналом цвета.

Следующий фрагмент кода показывает, как добавить текст с прозрачным цветом.

```python

    import aspose.pdf as ap

    # Создать экземпляр документа
    document = ap.Document()
    # Создать страницу для коллекции страниц PDF-файла
    page = document.pages.add()

    # Создать экземпляр TextFragment с примерным значением
    text = ap.text.TextFragment(
        "прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст прозрачный текст "
    )
    # Создать объект цвета из альфа-канала
    color = ap.Color.from_argb(30, 0, 255, 0)
    # Установить информацию о цвете для экземпляра текста
    text.text_state.foreground_color = color
    # Добавить текст в коллекцию абзацев экземпляра страницы
    page.paragraphs.add(text)

    document.save(output_pdf)
```


## Указать межстрочный интервал для шрифтов

Каждый шрифт имеет абстрактный квадрат, высота которого является предполагаемым расстоянием между строками текста в одном и том же размере шрифта. Этот квадрат называется em-квадрат и является конструкционной сеткой, на которой определены контуры глифов. Многие буквы входного шрифта имеют точки, которые расположены за пределами em-квадрата шрифта, поэтому для правильного отображения шрифта необходимо использование специальной настройки.

Следующий фрагмент кода загружает PDF, добавляет текстовый фрагмент с определенным межстрочным интервалом, используя шрифт TrueType, и сохраняет измененный PDF-документ:

```python

    import aspose.pdf as ap

    # Загрузить входной PDF файл
    document = ap.Document()
    # Создать TextFormattingOptions с LineSpacingMode.FULL_SIZE
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # Создать текстовый фрагмент с примерной строкой
    text_fragment = ap.text.TextFragment("Hello world")

    # Загрузить шрифт TrueType в объект потока
    font_stream = open(input_ttf, "rb")
    # Установить имя шрифта для текстовой строки
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # Указать позицию для текстового фрагмента
    text_fragment.position = ap.text.Position(100, 600)
    # Установить TextFormattingOptions текущего фрагмента на предопределенный (который указывает на LineSpacingMode.FULL_SIZE)
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # Сохранить результирующий PDF документ
    document.save(output_pdf)
```


## Получение ширины текста динамически

Этот фрагмент кода на Python выполняет сравнение между измерениями строк, полученных из объекта шрифта и объекта состояния текста в Aspose.PDF:

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Неожиданное измерение строки шрифта!")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Неожиданное измерение строки состояния!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("Измерение строки шрифта и состояния не совпадает!")

        c_code += 1
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>