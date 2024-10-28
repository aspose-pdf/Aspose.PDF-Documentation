---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /cpp/posting-acroform-data/
description: Вы можете импортировать и экспортировать данные формы в XML файл с использованием пространства имен Aspose.Pdf.Facades в Aspose.PDF для C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm - это важный тип PDF документа. Вы можете не только создавать и редактировать AcroForm, используя [Aspose.Pdf.Facades namepsace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades), но также импортировать и экспортировать данные формы в XML файл. Пространство имен Aspose.Pdf.Facades в Aspose.PDF для C++ позволяет вам реализовать другую функцию AcroForm, которая помогает отправить данные AcroForm на внешнюю веб-страницу. Эта веб-страница затем считывает переменные поста и использует эти данные для дальнейшей обработки. Эта функция полезна в случаях, когда вы не хотите просто сохранять данные в PDF-файле, а хотите отправить их на ваш сервер и затем сохранить в базе данных и т.д.

{{% /alert %}}

## Детали реализации

В этой статье мы попытались создать AcroForm, используя [Aspose.Pdf.Facades namepsace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) и класс [FormEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form_editor/). Мы также добавили кнопку отправки и установили для нее целевой URL.

Следующие фрагменты кода показывают, как создать форму и затем получить отправленные данные на веб-странице.
```cpp
используя пространство имен System;
используя пространство имен Aspose::Pdf;

void ПримерОтправки() {

    // Строка _dataDir("C:\\Samples\\");
    // Создать экземпляр класса FormEditor и привязать входные и выходные pdf файлы
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // Создать поля AcroForm - я создал только два поля для простоты
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // Добавить кнопку отправки и установить целевой URL
    editor->AddSubmitBtn(u"submitbutton", 1, u"Submit", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // Сохранить выходной pdf файл
    editor->Save();
}
```