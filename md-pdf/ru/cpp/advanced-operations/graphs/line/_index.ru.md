---
title: Добавить объект линии в PDF файл
linktitle: Добавить линию
type: docs
weight: 40
url: /cpp/add-line/
description: Эта статья объясняет, как создать объект линии в вашем PDF с использованием Aspose.PDF для C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавить объект линии

Aspose.PDF для C++ поддерживает возможность добавления графических объектов (например, график, линия, прямоугольник и т.д.) в PDF документы. Вы также можете добавить объект [Line](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/), где вы можете указать шаблон штриховки, цвет и другие параметры форматирования для элемента линии.

Следуйте приведенным ниже шагам:

1. Создайте новый [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) PDF

1. Добавьте [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) в коллекцию страниц PDF файла

1. Создайте экземпляр [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/).

1. Добавьте объект Graph в коллекцию параграфов экземпляра страницы.

1. Создайте экземпляр [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/).

1. Установите ширину линии.

1. Добавьте объект [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) в коллекцию фигур объекта Graph.

1. Сохраните ваш PDF файл.

Следующий фрагмент кода показывает, как добавить объект [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/), заполненный цветом.

```cpp

void AddLineObjectToPDF()
{

String _dataDir("C:\\Samples\\");

// Создайте экземпляр Document

auto document = MakeObject<Document>();


// Добавьте страницу в коллекцию страниц PDF файла

auto page = document->get_Pages()->Add();


// Создайте экземпляр Graph

auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);


// Добавьте объект graph в коллекцию параграфов экземпляра страницы

page->get_Paragraphs()->Add(graph);


// Создайте экземпляр Rectangle

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });



// Укажите цвет заливки для объекта Graph

line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));

line->get_GraphInfo()->set_DashPhase (1);



// Добавьте объект rectangle в коллекцию фигур объекта Graph

graph->get_Shapes()->Add(line);



// Сохраните PDF файл

document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```
![Add Line](add_line.png)

## Как добавить пунктирную линию в ваш PDF-документ

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{

String _dataDir("C:\\Samples\\");

// Создайте экземпляр документа

auto document = MakeObject<Document>();


// Добавьте страницу в коллекцию страниц PDF-файла

auto page = document->get_Pages()->Add();


// Создайте объект рисования с определенными размерами

auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

// Добавьте объект рисования в коллекцию абзацев экземпляра страницы

page->get_Paragraphs()->Add(canvas);



// Создайте объект линии

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));

// Установите цвет для объекта линии

line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());

// Укажите массив штриха для объекта линии

line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));

// Установите фазу штриха для экземпляра линии

line->get_GraphInfo()->set_DashPhase(1);

// Добавьте линию в коллекцию фигур объекта рисования

canvas->get_Shapes()->Add(line);


// Сохраните PDF-файл

document->Save(_dataDir + u"DashLength_out.pdf");
}
```

Давайте проверим результат:

![Пунктирная линия](dash_line.png)

## Нарисовать линию через страницу

Мы также можем использовать объект линии, чтобы нарисовать крест, начиная с левого нижнего до правого верхнего угла и с левого верхнего до правого нижнего угла.

Пожалуйста, посмотрите на следующий фрагмент кода, чтобы выполнить это требование.

```cpp
void ExampleLineAcrossPage() {

    // Создать экземпляр документа
    String _dataDir("C:\\Samples\\");
    // Создать экземпляр документа
    auto document = MakeObject<Document>();
   
    // Добавить страницу в коллекцию страниц PDF-файла
    auto page = document->get_Pages()->Add();
    // Установить отступы страницы по всем сторонам в 0

    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // Создать объект графики с шириной и высотой, равными размерам страницы
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // Создать первый объект линии, начиная с нижнего левого до верхнего правого угла страницы
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // Добавить линию в коллекцию фигур объекта графики
    graph->get_Shapes()->Add(line);
    // Нарисовать линию с верхнего левого угла страницы до нижнего правого угла страницы
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // Добавить линию в коллекцию фигур объекта графики
    graph->get_Shapes()->Add(line2);
    // Добавить объект графики в коллекцию абзацев страницы
    page->get_Paragraphs()->Add(graph);

    // Сохранить PDF-файл
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```