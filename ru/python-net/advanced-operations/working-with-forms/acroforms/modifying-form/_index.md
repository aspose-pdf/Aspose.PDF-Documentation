---
title: Изменение AcroForm
linktitle: Изменение AcroForm
type: docs
weight: 45
url: /ru/python-net/modifying-form/
description: Изменение формы в вашем PDF-файле с помощью библиотеки Aspose.PDF для Python через .NET. Вы можете добавлять или удалять поля в существующей форме, получать и задавать ограничение поля и т.д.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управление и настройка полей PDF-формы
Abstract: Эта подборка примеров демонстрирует различные техники управления и настройки полей PDF-форм с использованием Aspose.PDF для Python через .NET. Она включает методы очистки текста из полей формы в стиле машинописного ввода с помощью TextFragmentAbsorber, установку и получение ограничений по количеству символов с помощью FormEditor, применение пользовательских шрифтов и стилей к полям текстовых ящиков, а также удаление конкретных полей формы по имени. Эти операции позволяют разработчикам очищать, форматировать и адаптировать PDF-формы для повторного распространения, брендинга или проверки данных, поддерживая как эстетическое, так и функциональное совершенствование в автоматизированных рабочих процессах с документами.
---

## Очистить текст в форме

Этот пример демонстрирует, как очистить текст из полей формы типа Typewriter в PDF с помощью Aspose.PDF для Python через .NET. Он сканирует первую страницу PDF, определяет формы Typewriter, удаляет их содержимое и сохраняет обновлённый документ. Такой подход полезен для сброса или очистки полей формы перед повторным распространением PDF.

1. Загрузите входной PDF‑документ.
1. Получите доступ к формам на первой странице.
1. Пройдитесь по каждой форме и проверьте, является ли она формой `Typewriter`.
1. Используйте TextFragmentAbsorber для поиска текстовых фрагментов в форме.
1. Очистите текст каждого фрагмента.
1. Сохраните изменённый PDF в выходной файл.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    dataDir = "path/to/your/data/dir/"
    path_infile = dataDir + infile
    path_outfile = dataDir + outfile
    document = ap.Document(path_infile)

    # Get the forms from the first page
    forms = document.pages[1].resources.forms

    for form in forms:
        # Check if the form is of type "Typewriter" and subtype "Form"
        if (form.it == "Typewriter" and form.subtype == "Form"):
            # Create a TextFragmentAbsorber to find text fragments
            absorber = ap.Text.TextFragmentAbsorber()
            absorber.visit(form)

            # Clear the text in each fragment
            for fragment in absorber.text_fragments:
                fragment.Text = ""

    # Save PDF document
    document.save(path_outfile)
```

## Получить или установить ограничение поля

Метод set_field_limit(field, limit) класса FormEditor позволяет установить ограничение поля — максимальное количество символов, которое может быть введено в поле.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Create FormEditor instance
    form = ap.facades.FormEditor()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Set field limit for "First Name"
    form.set_field_limit("First Name", 15)

    # Save PDF document
    form.save(path_outfile)
```

Аналогично, Aspose.PDF имеет метод, который получает ограничение поля.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {textBoxField.max_len}")
```

## Установить пользовательский шрифт для поля формы

Поля формы в файлах Adobe PDF можно настроить для использования конкретных шрифтов по умолчанию. В ранних версиях Aspose.PDF поддерживались только 14 стандартных шрифтов. Поздние релизы позволили разработчикам применять любой шрифт.

Этот код обновляет внешний вид поля текстового блока в PDF‑форме, устанавливая пользовательский шрифт, размер и цвет, а затем сохраняет изменённый документ с помощью Aspose.PDF для Python через .NET.

Ниже приведён фрагмент кода, показывающий, как установить шрифт по умолчанию для полей PDF‑формы.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        textBoxField.default_appearance = ap.annotations.DefaultAppearance(font, 10, ap.Color.black.to_rgb())

    document.save(path_outfile)
```

## Удалить поля в существующей форме

Этот код удаляет конкретное поле формы (по его имени) из PDF‑документа и сохраняет обновлённый файл с помощью Aspose.PDF для Python через .NET.

1. Загрузите PDF‑документ.
1. Удалите поле формы по имени.
1. Сохраните обновлённый PDF.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    # Delete a particular field by name
    document.form.delete("First Name")
    # Save PDF document
    document.save(path_outfile)
```

