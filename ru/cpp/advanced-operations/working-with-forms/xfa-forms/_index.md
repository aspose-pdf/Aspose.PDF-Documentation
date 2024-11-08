---
title: Работа с XFA Формами с использованием C++
linktitle: XFA Формы
type: docs
weight: 20
url: /ru/cpp/xfa-forms/
description: Aspose.PDF for C++ API позволяет работать с полями XFA и XFA Acroform в PDF документе. Aspose.PDF.Facades.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA Forms — это XML Forms Architecture, семейство проприетарных XML спецификаций, которые были предложены и разработаны компанией JetForm для улучшения обработки веб-форм. Они также могут использоваться в PDF файлах, начиная со спецификации PDF 1.5.

Заполните поля XFA с помощью класса [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/) из [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades).

## Заполнение полей XFA

Следующий фрагмент кода показывает, как заполнить поля в форме XFA.

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // Get names of XFA form fields
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Set field values

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Field 1");

    // Save the updated document
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```

## Convert XFA to AcroForm

{{% alert color="primary" %}}

Попробуйте онлайн
Вы можете проверить качество преобразования Aspose.PDF и просмотреть результаты онлайн по этой ссылке: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Динамические формы основаны на XML-спецификации, известной как XFA, «Архитектура XML-форм». Информация о форме (что касается PDF) очень расплывчата – указывается, что поля существуют, с определенными свойствами и событиями JavaScript, но не указывается никакое отображение.

В настоящее время PDF поддерживает два различных метода интеграции данных и PDF-форм:

- AcroForms (также известные как формы Acrobat), введенные и включенные в спецификацию формата PDF 1.2.
- Формы Adobe XML Forms Architecture (XFA), введенные в спецификации формата PDF 1.5 как необязательная функция (спецификация XFA не включена в спецификацию PDF, она только упоминается).

Мы не можем извлекать или манипулировать страницами форм XFA, потому что содержание формы генерируется во время выполнения (во время просмотра формы XFA) в приложении, пытающемся отобразить или визуализировать форму XFA. Aspose.PDF имеет функцию, которая позволяет разработчикам преобразовывать формы XFA в стандартные AcroForms.

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // Загрузить форму XFA
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // Установить тип полей формы как стандартный AcroForm
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // Сохранить полученный PDF
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## Получить свойства поля XFA

Чтобы получить доступ к свойствам полей, сначала используйте Document.Form.XFA.Teamplate для доступа к шаблону поля. Следующий фрагмент кода показывает шаги получения координат X и Y поля формы XFA.

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // Загрузить форму XFA
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Установить значения полей
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 1");

    // Получить позицию поля
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // Получить позицию поля
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // Сохранить обновленный документ
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```