---
title: Заполнение AcroForm
linktitle: Заполнение AcroForm
type: docs
weight: 20
url: /ru/cpp/fill-form/
description: Этот раздел объясняет, как заполнить поле формы в PDF документе с помощью Aspose.PDF для C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF документы являются лучшим и действительно предпочтительным типом файлов для создания форм.

В этой теме объясняется, как заполнять PDF формы с помощью Aspose.PDF для C++.

Aspose.PDF для C++ позволяет заполнить поле формы, получить поле из коллекции Form объекта Document.

Давайте рассмотрим следующий пример, как решить эту задачу:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // Получить поле
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Изменить значение поля
    textBoxField->set_Value(u"Значение для заполнения в поле");

    // Сохранить обновленный документ
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```