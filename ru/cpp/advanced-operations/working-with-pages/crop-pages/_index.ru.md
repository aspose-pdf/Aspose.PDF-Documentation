---
title: Программное обрезание страниц PDF на C++
linktitle: Обрезание Страниц
type: docs
weight: 80
url: /cpp/crop-pages/
description: Вы можете получить свойства страницы, такие как ширина, высота, bleed-, crop- и trimbox, используя Aspose.PDF для C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение Свойств Страницы

Каждая страница в PDF файле имеет ряд свойств, таких как ширина, высота, bleed-, crop- и trimbox. Aspose.PDF позволяет получить доступ к этим свойствам.

- **Медиабокс**: Медиабокс - это самая большая коробка страницы. Он соответствует размеру страницы (например, A4, A5, US Letter и т.д.), выбранному при печати документа в PostScript или PDF. Иными словами, медиабокс определяет физический размер носителя, на котором отображается или печатается PDF документ.
- **Bleed box**: Если документ имеет вылет, PDF также будет иметь вылетную коробку. Bleed - это количество цвета (или изображения), которое выходит за пределы края страницы. Оно используется, чтобы гарантировать, что при печати и обрезке документа ("подрезка") чернила будут доходить до самого края страницы. Даже если страница будет неправильно обрезана - слегка срезана за пределами меток обрезки - на странице не появятся белые края.
- **Trim box**: Trim box указывает окончательный размер документа после печати и обрезки.
- **Art box**: Art box - это рамка, нарисованная вокруг фактического содержимого страниц в ваших документах. Эта рамка страницы используется при импорте PDF-документов в другие приложения.
- **Crop box**: Crop box - это размер "страницы", при котором ваш PDF-документ отображается в Adobe Acrobat. В обычном режиме отображаются только содержимое crop box в Adobe Acrobat. Для подробных описаний этих свойств читайте Adobe.Pdf спецификацию, особенно раздел 10.10.1 Границы страницы.
- **Page.Rect**: пересечение (обычно видимый прямоугольник) MediaBox и DropBox. Изображение ниже иллюстрирует эти свойства.  
Для получения дополнительной информации, пожалуйста, посетите [эту страницу](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

Пример ниже показывает, как обрезать страницу:

```cpp
void CropPagesPDF()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("crop_page.pdf");
    String outputFileName("crop_page_out.pdf");

    // Открыть исходный документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    Console::WriteLine(document->get_Pages()->idx_get(1)->get_CropBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_TrimBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_ArtBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_BleedBox());
    Console::WriteLine(document->get_Pages()->idx_get(1)->get_MediaBox());

    // Создать новый прямоугольник Box
    auto newBox = MakeObject<Rectangle>(200, 220, 2170, 1520);
    document->get_Pages()->idx_get(1)->set_CropBox(newBox);
    document->get_Pages()->idx_get(1)->set_TrimBox(newBox);
    document->get_Pages()->idx_get(1)->set_ArtBox (newBox);
    document->get_Pages()->idx_get(1)->set_BleedBox (newBox);

    // Сохранить обновленный документ
    document->Save(_dataDir + outputFileName);
}
```
In this example we used a sample file [here](crop_page.pdf). Initially our page looks like shown on the Figure 1.
![Figure 1. Cropped Page](crop_page.png)

После изменения страница будет выглядеть как на Рисунке 2.
![Figure 2. Cropped Page](crop_page2.png)