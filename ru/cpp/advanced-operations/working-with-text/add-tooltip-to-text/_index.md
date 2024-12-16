---
title: PDF Tooltip использование C++
linktitle: PDF Tooltip
type: docs
weight: 20
url: /ru/cpp/pdf-tooltip/
description: Узнайте, как добавить всплывающую подсказку к фрагменту текста в PDF с использованием C++ и Aspose.PDF
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление всплывающей подсказки к найденному тексту, добавляя невидимую кнопку

Эта статья демонстрирует, как добавить всплывающую подсказку к тексту в существующем PDF документе с использованием C++. Aspose.PDF поддерживает создание всплывающих подсказок путем добавления невидимой кнопки над найденным текстом из PDF файла.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("Tooltip_out.pdf");

    // Create sample document with text
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Наведите курсор мыши сюда, чтобы отобразить всплывающую подсказку"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("Наведите курсор мыши сюда, чтобы отобразить очень длинную всплывающую подсказку"));

    document->Save(outputFileName);

    // Open document with text
    auto document = MakeObject<Document>(outputFileName);
    // Create TextAbsorber object to find all the phrases matching the regular expression
    auto absorber = MakeObject<TextFragmentAbsorber>("Наведите курсор мыши сюда, чтобы отобразить всплывающую подсказку");
    // Accept the absorber for the document pages
    document->get_Pages()->Accept(absorber);

    // Get the extracted text fragments
    auto textFragments = absorber->get_TextFragments();

    // Loop through the fragments
    for(auto fragment : textFragments)
    {
        // Create invisible button on text fragment position
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // AlternateName value will be displayed as tooltip by a viewer application
        field->set_AlternateName (u"Подсказка для текста.");
        // Add button field to the document
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Next will be sapmle of very long tooltip
    absorber = MakeObject<TextFragmentAbsorber>("Наведите курсор мыши сюда, чтобы отобразить очень длинную всплывающую подсказку");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // Set very long text
        field->set_AlternateName(String("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.\
            Duis aute irure dolor in reprehenderit in voluptate velit\
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
            occaecat cupidatat non proident, sunt in culpa qui officia\
            deserunt mollit anim id est laborum."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Save document
    document->Save(outputFileName);

}
```

## Создание скрытого текстового блока и его отображение при наведении мыши

Aspose.PDF для C++ реализует функцию скрытия действий, с помощью которой вы можете показывать/скрывать текстовое поле (или любой другой тип аннотации) при входе/выходе курсора мыши на невидимую кнопку. Для этого используйте класс Aspose.Pdf.Annotations.HideAction, чтобы назначить действие скрытия/показа текстовому блоку. Используйте следующий фрагмент кода для отображения/скрытия текстового блока при вводе/выводе мыши.

Также обратите внимание, что действия PDF в документах работают корректно в их соответствующих программах для чтения (таких как Adobe Reader), но не дают никаких гарантий для других программ для чтения PDF (таких как плагины браузера). Мы провели небольшое исследование и обнаружили:

- Все реализации скрытого действия в PDF-документах работают корректно в Internet Explorer v.11.0.
- Все реализации скрытого действия также работают в Opera v.12.14, но мы заметили некоторую задержку отклика при первом открытии документа.

- Только реализация, использующая конструктор HideAction, принимающий имя поля, работает, если Google Chrome v.61.0 просматривает документ; Пожалуйста, используйте соответствующие конструкторы, если просмотр в Google Chrome имеет значимость:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // Строка для имени выходного файла
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // Создаем пример документа с текстом
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Переместите курсор мыши сюда, чтобы отобразить плавающий текст"));
    document->Save(outputFileName);

    // Открываем документ с текстом
    auto document = MakeObject<Document>(outputFileName);

    // Создаем объект TextAbsorber для поиска всех фраз, соответствующих регулярному выражению
    auto absorber = MakeObject<TextFragmentAbsorber>("Переместите курсор мыши сюда, чтобы отобразить плавающий текст");
    // Принимаем абсорбер для страниц документа
    document->get_Pages()->Accept(absorber);
    // Получаем первый извлеченный фрагмент текста
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // Создаем скрытое текстовое поле для плавающего текста в указанном прямоугольнике страницы
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // Устанавливаем текст, который будет отображаться в качестве значения поля
    floatingField->set_Value(u"Это \"плавающее текстовое поле\".");
    // Мы рекомендуем сделать поле 'только для чтения' для этого сценария
    floatingField->set_ReadOnly(true);
    // Устанавливаем флаг 'скрытый', чтобы поле было невидимым при открытии документа
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // Уникальное имя поля устанавливать не обязательно, но разрешено
    floatingField->set_PartialName (u"FloatingField_1");

    // Установка характеристик внешнего вида поля не обязательна, но улучшает его
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // Добавляем текстовое поле в документ
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // Создаем невидимую кнопку на позиции текстового фрагмента
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // Создаем новое действие скрытия для указанного поля (аннотации) и флага невидимости.
    // (Вы также можете ссылаться на плавающее поле по имени, если указали его выше.)
    // Добавляем действия на вход/выход мыши в невидимое поле кнопки
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // Добавляем кнопку в документ
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // Сохраняем документ
    document->Save(outputFileName);
}
```