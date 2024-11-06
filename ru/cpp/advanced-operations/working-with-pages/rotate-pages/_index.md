---
title: Поворот страниц PDF с использованием C++
linktitle: Поворот страниц PDF
type: docs
weight: 50
url: ru/cpp/rotate-pages/
description: В этой теме описано, как программно изменить ориентацию страниц в существующем PDF-файле с помощью C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

В этой теме описано, как программно обновить или изменить ориентацию страниц в существующем PDF-файле с помощью C++.

## Изменение ориентации страницы

Aspose.PDF for C++ позволяет изменить ориентацию страницы с альбомной на портретную и наоборот. Чтобы изменить ориентацию страницы, установите MediaBox страницы, используя следующий фрагмент кода. Вы также можете изменить ориентацию страницы, установив угол поворота с помощью метода Rotate().

```cpp
void ChangePageOrientation() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {

        auto r = page->get_MediaBox();
        double newHeight = r->get_Width();
        double newWidth = r->get_Height();
        double newLLX = r->get_LLX();

        // Мы должны переместить страницу вверх, чтобы компенсировать изменение размера страницы
        // (нижний край страницы 0,0 и информация обычно размещается сверху страницы.
        // Поэтому мы перемещаем нижний край вверх на разницу между старой и новой высотой.

        double newLLY = r->get_LLY() + (r->get_Height() - newHeight);
        page->set_MediaBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));
        // Иногда нужно также установить CropBox (если он был установлен в исходном файле)
        page->set_CropBox(MakeObject<Rectangle>(newLLX, newLLY, newLLX + newWidth, newLLY + newHeight));

        // Установка угла поворота страницы
        page->set_Rotate(Rotation::on90);
    }

    // Сохранить выходной файл
    document->Save(_dataDir + outputFileName);
}
```

## Подгонка содержимого страницы к новой ориентации страницы

Пожалуйста, обратите внимание, что при использовании приведенного выше фрагмента кода, часть содержимого документа может быть обрезана, поскольку высота страницы уменьшена. Чтобы избежать этого, увеличьте ширину пропорционально и оставьте высоту без изменений. Пример расчетов:

```cpp
void FittingPageContentToNewPageOrientation()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("ChangeOrientation.pdf");
    String outputFileName("ChangeOrientation_out.pdf");
    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    for (auto page : document->get_Pages())
    {
        auto r = page->get_MediaBox();
        // Новая высота та же
        double newHeight = r->get_Height();
        // Новая ширина увеличивается пропорционально, чтобы сделать ориентацию альбомной
        // (мы предполагаем, что предыдущая ориентация - портретная)
        double newWidth = r->get_Height() * r->get_Height() / r->get_Width();

        // ...

    }
}
```

Кроме вышеуказанного подхода, рассмотрите возможность использования фасада PdfPageEditor, который может применять масштабирование к содержимому страницы.

```cpp
void ZoomPageContent()
{

    String _dataDir("C:\\Samples\\");
    String inputFileName("ZoomToPageContents.pdf");
    String outputFileName("ZoomToPageContents_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Получить прямоугольную область первой страницы PDF
    auto rect = document->get_Pages()->idx_get(1)->get_Rect();

    // Создать экземпляр PdfPageEditor
    auto ppe = MakeObject<Aspose::Pdf::Facades::PdfPageEditor>();
    // Привязать исходный PDF
    ppe->BindPdf(_dataDir + inputFileName);
    // Установить коэффициент увеличения
    ppe->set_Zoom ((float)(rect->get_Width() / rect->get_Height()));
    // Обновить размер страницы
    ppe->set_PageSize(MakeObject<PageSize>((float)rect->get_Height(), (float)rect->get_Width()));

    // Сохранить выходной файл
    document->Save(_dataDir + outputFileName);
}
```