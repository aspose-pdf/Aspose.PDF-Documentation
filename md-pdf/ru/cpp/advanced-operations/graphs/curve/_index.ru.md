---
title: Добавление объекта кривой в PDF файл
linktitle: Добавить кривую
type: docs
weight: 30
url: /cpp/add-curve/
description: В этой статье объясняется, как создать объект кривой в вашем PDF с использованием Aspose.PDF для C++.
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавление объекта кривой

График [Кривая](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/) представляет собой соединение проективных линий, каждая из которых встречается с тремя другими в обычных двойных точках.

Кривые Безье широко используются в компьютерной графике для моделирования гладких кривых. Кривая полностью содержится в выпуклой оболочке своих контрольных точек, точки могут быть отображены графически и использованы для интуитивного управления кривой.
Вся кривая содержится в четырехугольнике, углы которого образованы четырьмя заданными точками (их выпуклой оболочкой).

В этой статье мы рассмотрим простые графические кривые и заполненные кривые, которые вы можете создать в вашем PDF документе.

Следуйте шагам ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)

1. Создайте [Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing) с определенными размерами

1. Установите [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) для объекта Drawing

1. Добавьте объект [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) в коллекцию параграфов страницы

1. Сохраните наш PDF файл

```cpp
void ExampleCurve() {

    // Создайте экземпляр Document
    String _dataDir("C:\\Samples\\");
    // Создайте экземпляр Document
    auto document = MakeObject<Document>();

    // Добавьте страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    // Создайте объект Drawing с определенными размерами
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Установите границу для объекта Drawing
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Добавьте объект Graph в коллекцию параграфов страницы
    page->get_Paragraphs()->Add(graph);

    // Сохраните PDF файл
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```
Следующее изображение показывает результат, выполненный с нашим кодовым фрагментом:

![Drawing Curve](drawing_curve.png)

## Создание объекта Закрашенная Кривая

Этот пример показывает, как добавить объект Кривая, закрашенный цветом.

```cpp
void ExampleFilledCurve() {

    // Создание экземпляра Document
    String _dataDir("C:\\Samples\\");
    // Создание экземпляра Document
    auto document = MakeObject<Document>();

    // Добавление страницы в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();

    // Создание объекта Рисование с определенными размерами
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Установка границы для объекта Рисование
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Добавление объекта Graph в коллекцию абзацев страницы
    page->get_Paragraphs()->Add(graph);

    // Сохранение PDF файла
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```


Посмотрите на результат добавления залитой кривой:

![Filled Curve](filled_curve.png)
```