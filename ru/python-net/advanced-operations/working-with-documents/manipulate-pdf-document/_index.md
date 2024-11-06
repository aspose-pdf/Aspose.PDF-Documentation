---
title: Манипулировать PDF документом в Python через .NET
linktitle: Манипулировать PDF документом
type: docs
weight: 20
url: ru/python-net/manipulate-pdf-document/
description: Эта статья содержит информацию о том, как проверить PDF документ на соответствие стандарту PDF A с использованием Python, как работать с оглавлением, как установить срок действия PDF и т. д.
keywords: "манипулировать pdf python"
lastmod: "2023-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Манипулировать PDF документом через Python",
    "alternativeHeadline": "Как манипулировать PDF файлом с помощью Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, dotnet, python, манипулировать pdf файлом",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "url": "/python-net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Эта статья содержит информацию о том, как проверить PDF документ на соответствие стандарту PDF A с использованием Python, как работать с оглавлением, как установить срок действия PDF и т. д."
}
</script>


## Манипуляция с PDF-документом на Python

## Валидация PDF-документа на соответствие стандарту PDF/A (A 1A и A 1B)

Чтобы проверить PDF-документ на совместимость с PDF/A-1a или PDF/A-1b, используйте метод [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Этот метод позволяет указать имя файла, в который будет сохранён результат, и требуемый тип валидации из перечисления PdfFormat: PDF_A_1A или PDF_A_1B.

Следующий фрагмент кода показывает, как выполнить валидацию PDF-документа для PDF/A-1A.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Проверка PDF на соответствие PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

Следующий фрагмент кода показывает, как выполнить валидацию PDF-документа для PDF/A-1B.

```python

    import aspose.pdf as ap

    # Открыть документ
    document = ap.Document(input_pdf)

    # Проверка PDF на соответствие PDF/A-1b
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```


## Работа с Оглавлением

### Добавление Оглавления в Существующий PDF

Оглавление в PDF обозначает "Table of Contents" (Таблица Содержания). Это функция, которая позволяет пользователям быстро перемещаться по документу, предоставляя обзор его разделов и заголовков.

Чтобы добавить оглавление в существующий PDF файл, используйте класс Heading в пространстве имен [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). Пространство имен [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) может как создавать новые, так и обрабатывать существующие PDF файлы. Чтобы добавить оглавление в существующий PDF, используйте пространство имен Aspose.Pdf. Следующий фрагмент кода показывает, как создать таблицу содержания внутри существующего PDF файла с использованием Python через .NET.

```python

    import aspose.pdf as ap

    # Загрузите существующий PDF файл
    doc = ap.Document(input_pdf)

    # Получите доступ к первой странице PDF файла
    tocPage = doc.pages.insert(1)

    # Создайте объект для представления информации об оглавлении
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Установите заголовок для оглавления
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Создайте строковые объекты, которые будут использоваться как элементы оглавления
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Создайте объект Heading
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Укажите целевую страницу для объекта заголовка
        heading2.destination_page = doc.pages[i + 2]

        # Целевая страница
        heading2.top = doc.pages[i + 2].rect.height

        # Координата назначения
        segment2.text = titles[i]

        # Добавьте заголовок на страницу, содержащую оглавление
        tocPage.paragraphs.add(heading2)

    # Сохраните обновленный документ
    doc.save(output_pdf)
```


### Установить разные TabLeaderType для разных уровней Оглавления

Aspose.PDF для Python также позволяет устанавливать разные TabLeaderType для разных уровней оглавления. Вам нужно установить свойство [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) для [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # установить LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Содержание")
    title.text_state.font_size = 30
    toc_info.title = title

    # Добавить секцию списка в коллекцию секций документа Pdf
    tocPage.toc_info = toc_info
    # Определите формат списка из четырех уровней, установив отступы слева
    # и
    # настройки формата текста для каждого уровня

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Создать секцию в документе Pdf
    page = doc.pages.add()

    # Добавить четыре заголовка в секцию
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Пример Заголовка" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Добавить заголовок в Оглавление.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # сохранить Pdf
    doc.save(output_pdf)
```


### Скрыть номера страниц в ОГЛ

В случае, если вы не хотите отображать номера страниц вместе с заголовками в ОГЛ, вы можете использовать свойство [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) класса [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) как false. Пожалуйста, ознакомьтесь с следующим фрагментом кода, чтобы скрыть номера страниц в оглавлении:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Содержание")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Добавить секцию списка в коллекцию секций PDF документа
    toc_page.toc_info = toc_info
    # Определите формат списка из четырех уровней, установив отступы слева и
    # параметры форматирования текста для каждого уровня

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Добавить четыре заголовка в секцию
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "это заголовок уровня " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```


### Настройка номеров страниц при добавлении оглавления

Обычно при добавлении оглавления в PDF-документ настраиваются номера страниц. Например, может потребоваться добавить некоторый префикс перед номером страницы, например, P1, P2, P3 и так далее. В таком случае Aspose.PDF для Python предоставляет свойство [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) класса [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/), которое можно использовать для настройки номеров страниц, как показано в следующем примере кода.

```python

    import aspose.pdf as ap

    # Загрузить существующие PDF-файлы
    doc = ap.Document(input_pdf)
    # Получить доступ к первой странице PDF-файла
    toc_page = doc.pages.insert(1)
    # Создать объект для представления информации об оглавлении
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Установить заголовок для оглавления
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Создать объект заголовка
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Указать страницу назначения для объекта заголовка
        heading2.destination_page = doc.pages[i + 1]
        # Страница назначения
        heading2.top = doc.pages[i + 1].rect.height
        # Координата назначения
        segment2.text = "Page " + str(i)
        # Добавить заголовок на страницу, содержащую оглавление
        toc_page.paragraphs.add(heading2)

    # Сохранить обновленный документ
    doc.save(output_pdf)

```


## Как установить дату окончания срока действия PDF

Мы применяем привилегии доступа к PDF-файлам, чтобы определенная группа пользователей могла получить доступ к определенным функциям/объектам PDF-документов. Чтобы ограничить доступ к PDF-файлу, мы обычно применяем шифрование, и у нас может возникнуть необходимость установить срок действия PDF-файла, чтобы пользователь, получающий/просматривающий документ, получал действительное уведомление о сроке действия PDF-файла.

```python

    import aspose.pdf as ap

    # Создаем объект Document
    doc = ap.Document()
    # Добавляем страницу в коллекцию страниц PDF-файла
    doc.pages.add()
    # Добавляем текстовый фрагмент в коллекцию абзацев объекта страницы
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # Создаем объект JavaScript для установки даты окончания срока действия PDF
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # Устанавливаем JavaScript как действие открытия PDF
    doc.open_action = javaScript

    # Сохраняем PDF-документ
    doc.save(output_pdf)
```


## Уплощение Заполняемого PDF в Python

PDF-документы часто содержат формы с интерактивными заполняемыми элементами, такими как переключатели, флажки, текстовые поля, списки и т.д. Чтобы сделать их не редактируемыми для различных целей, необходимо уплощить PDF-файл.
Aspose.PDF предоставляет функцию для уплощения вашего PDF в Python всего несколькими строками кода:

```python

    import aspose.pdf as ap

    # Загрузить исходную PDF-форму
    doc = ap.Document(input_pdf)

    # Уплощение Заполняемого PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Сохранить обновленный документ
    doc.save(output_pdf)