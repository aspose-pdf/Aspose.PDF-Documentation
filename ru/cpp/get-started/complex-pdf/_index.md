---
title: Создание сложного PDF 
linktitle: Создание сложного PDF
type: docs
weight: 60
url: ru/cpp/complex-pdf-example/
description: Aspose.PDF для C++ позволяет создавать более сложные документы, содержащие изображения, текстовые фрагменты и таблицы в одном документе.
lastmod: "2021-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Пример [Hello, World](/pdf/cpp/hello-world-example/) показал простые шаги для создания PDF-документа с использованием C++ и Aspose.PDF. В этой статье мы рассмотрим создание более сложного документа с помощью C++ и Aspose.PDF для C++. В качестве примера мы возьмем документ от вымышленной компании, которая занимается пассажирскими паромными перевозками. Наш документ будет содержать изображение, два текстовых фрагмента (заголовок и абзац) и таблицу. Для создания такого документа мы будем использовать подход на основе DOM. Подробнее вы можете прочитать в разделе [Основы DOM API](/pdf/cpp/basics-of-dom-api/).

Если мы создаем документ с нуля, нам нужно выполнить определенные шаги:

1. Создайте [String Class](https://reference.aspose.com/pdf/cpp/class/system.string) для имени пути и имени файла.
1. Создайте объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). На этом этапе мы создадим пустой PDF-документ с некоторыми метаданными, но без страниц.
1. Добавьте [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) к объекту документа. Теперь наш документ будет содержать одну страницу.
1. Добавьте [Image](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image) на страницу.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) для заголовка. Для заголовка мы будем использовать шрифт Arial с размером шрифта 24pt и выравниванием по центру.
1. Добавьте заголовок к [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) страницы. Создайте [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) для описания. Для описания мы будем использовать шрифт Arial с размером 24pt и выравниванием по центру.
1. Добавьте (описание) в абзацы страницы.
1. Создайте таблицу, добавьте свойства таблицы.
1. Добавьте (таблицу) в [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#ac5c48bedc9fe8a7e0800a1d9b2c28170) страницы.
1. Сохраните документ "Complex.pdf".

```cpp
void ExampleComplex()
{
    String outputFileName;

    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String filename("Complex.pdf");

    // Инициализировать объект документа
    auto document = MakeObject<Document>();
    // Добавить страницу
    auto page = document->get_Pages()->Add();

    // Добавить изображение
    String imageFileName = _dataDir + String(u"logo.png");

    // Добавить изображение в коллекцию изображений ресурсов страницы
    auto rectangle = MakeObject<Rectangle>(20, 730, 120, 830);
    page->AddImage(imageFileName, rectangle);

    // Добавить заголовок
    auto header = MakeObject<TextFragment>(u"Новые маршруты паромов осенью 2020");
    auto textFragementState = header->get_TextState();
    textFragementState->set_Font(FontRepository::FindFont(u"Arial"));
    textFragementState->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    auto position = MakeObject<Aspose::Pdf::Text::Position>(130, 720);
    header->set_Position(position);
    page->get_Paragraphs()->Add(header);

    // Добавить описание
    String descriptionText(u"Посетители должны покупать билеты онлайн, и количество билетов ограничено до 5,000 в день. Паромное сообщение работает на половину мощности и по сокращенному расписанию. Ожидайте очереди.");
    auto description = MakeObject<TextFragment>(descriptionText);
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);

    // Добавить таблицу
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200");

    table->set_Border(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, 1.0f, Aspose::Pdf::Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(Aspose::Pdf::BorderSide::Box, .5f, Aspose::Pdf::Color::get_Black()));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));

    auto headerRow = table->get_Rows()->Add();
    headerRow->get_Cells()->Add(u"Отправление из города");
    headerRow->get_Cells()->Add(u"Отправление с острова");

    for (auto headerRowCell : headerRow->get_Cells())
    {
        headerRowCell->set_BackgroundColor(Color::get_Gray());
        headerRowCell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }

    String arrivals[10] = { u"6:00",u"6:45", u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45" };
    String departures[10] = { u"7:00", u"7:45", u"8:00", u"8:45", u"9:00", u"9:45", u"10:00", u"10:45", u"11:00", u"11:45" };

    for (int i = 0; i < 10; i++)
    {
        auto dataRow = table->get_Rows()->Add();
        dataRow->get_Cells()->Add(arrivals[i]);
        dataRow->get_Cells()->Add(departures[i]);
    }

    page->get_Paragraphs()->Add(table);

    // Сохранить обновленный PDF
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```