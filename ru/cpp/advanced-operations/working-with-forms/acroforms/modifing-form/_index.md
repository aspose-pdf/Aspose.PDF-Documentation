---
title: Изменение AcroForm
linktitle: Изменение AcroForm
type: docs
weight: 40
url: /ru/cpp/modifing-form/
description: Изменение формы в вашем PDF файле с помощью библиотеки Aspose.PDF для C++. Вы можете добавлять или удалять поля в существующей форме, получать и устанавливать ограничение поля и т.д.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получить или Установить Ограничение Поля

Метод SetFieldLimit(field, limit) класса FormEditor позволяет установить ограничение поля, максимальное количество символов, которые могут быть введены в поле.

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

Аналогично, Aspose.PDF имеет метод, который получает ограничение поля с использованием подхода DOM. Следующий фрагмент кода показывает шаги.

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"Limit: {0}", textBoxField->get_MaxLen());        
}
```

Вы также можете установить и получить то же значение, используя пространство имен *Aspose.PDF.Facades* с помощью следующего фрагмента кода.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Добавление поля с ограничением
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Добавление поля с ограничением
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"Limit: {0}", form->GetFieldLimit(u"textbox1"));
}
```
## Установка пользовательского шрифта для поля формы

Поля формы в файлах Adobe PDF могут быть настроены для использования определенных шрифтов по умолчанию. В ранних версиях Aspose.PDF поддерживались только 14 стандартных шрифтов. Поздние выпуски позволили разработчикам применять любой шрифт. Чтобы установить и обновить шрифт по умолчанию, используемый для полей формы, используйте класс DefaultAppearance (Font font, double size, Color color). Этот класс находится в пространстве имен Aspose.PDF.InteractiveFeatures. Чтобы использовать этот объект, используйте свойство DefaultAppearance класса Field.

Следующий фрагмент кода показывает, как установить шрифт по умолчанию для полей формы PDF.

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // Получить конкретное поле формы из документа
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Создать объект шрифта
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // Установить информацию о шрифте для поля формы

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // Сохранить обновленный документ
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## Удаление полей из существующей формы

Все поля формы содержатся в коллекции Form объекта Document. Эта коллекция предоставляет различные методы для управления полями формы, включая метод Delete. Если вы хотите удалить конкретное поле, передайте имя поля в качестве параметра методу Delete, а затем сохраните обновленный PDF-документ. Следующий фрагмент кода показывает, как удалить конкретное поле из PDF-документа.

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // Удалить конкретное поле по имени
    document->get_Form()->Delete(u"textbox1");
    
    // Сохранить измененный документ
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```