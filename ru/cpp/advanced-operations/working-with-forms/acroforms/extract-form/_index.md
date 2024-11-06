---
title: Извлечение данных AcroForm с использованием C++
linktitle: Извлечение данных AcroForm
type: docs
weight: 30
url: ru/cpp/extract-form/
description: Этот раздел объясняет, как извлечь формы из вашего PDF-документа с помощью Aspose.PDF для C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение значений из всех полей PDF-документа

Чтобы получить значения из всех полей в PDF-документе, вам нужно пройтись по всем полям формы и затем получить значение, используя свойство Value. Получите каждое поле из коллекции Form, в базовом типе поля, называемом Field, и получите доступ к его свойству Value.

Следующие фрагменты кода показывают, как получить значения всех полей из PDF-документа.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // Получить значения из всех полей
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"Имя поля : {0} ", formField->get_PartialName());
        Console::WriteLine(u"Значение : {0} ", formField->get_Value());
    }
}
```

## Получение значения из отдельного поля PDF-документа

Свойство Value поля формы позволяет получить значение конкретного поля. Чтобы получить значение, получите поле формы из коллекции Form объекта Document. В этом примере выбирается [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field) и извлекается его значение с помощью свойства Value.

Следующий фрагмент кода показывает, как получить значения отдельных полей в PDF-документе.

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // Получить поле
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Получить значение поля
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

Чтобы получить URL кнопки отправки, используйте следующие строки кода.

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## Получение полей формы из определенной области PDF файла

Иногда вы можете знать, где в документе находится поле формы, но не знать его имени. Например, если у вас есть только схема печатной формы. С Aspose.PDF для C++ это не проблема. Вы можете узнать, какие поля находятся в заданной области PDF файла. Чтобы получить поля формы из определенной области PDF файла:

1. Откройте PDF файл, используя объект Document.
1. Создайте объект прямоугольника, чтобы получить поля в этой области
1. Получите форму из коллекции Forms документа.
1. Отобразите имена и значения полей

Следующий фрагмент кода показывает, как получить поля формы в определенной прямоугольной области PDF файла.
```

```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // Открыть PDF файл
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // Создать объект прямоугольника для получения полей в этой области
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // Получить поля в прямоугольной области
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // Отобразить имена и значения полей
    for(auto field : fields)
    {
        // Отобразить свойства размещения изображения для всех размещений
        Console::WriteLine(u"Имя поля: {0} - Значение поля: {1}", field->get_FullName(), field->get_Value());
    }
}
```