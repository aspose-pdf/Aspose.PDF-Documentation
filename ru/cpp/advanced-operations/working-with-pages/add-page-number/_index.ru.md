---
title: Добавить Номер Страницы в PDF с помощью C++
linktitle: Добавить Номер Страницы
type: docs
weight: 100
url: /cpp/add-page-number/
description: Aspose.PDF для C++ позволяет добавить штамп с номером страницы в ваш PDF файл, используя класс PageNumberStamp.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Как Добавить Номера Страниц в Существующий PDF

Все документы должны иметь номера страниц. Номер страницы облегчает читателю поиск различных частей документа.
**Aspose.PDF для C++** позволяет добавить номера страниц с помощью PageNumberStamp.

Следующие шаги и пример кода иллюстрируют, как добавить метки нумерации страниц в существующий PDF документ, используя элемент страницы [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) для автоматического добавления номеров страниц в PDF.

Шаги для добавления номеров страниц в существующий PDF документ:

Для добавления штампа с номером страницы, вам нужно создать объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) и объект [PageNumberStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_number_stamp) с использованием необходимых свойств.

После этого вы можете вызвать метод [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) класса [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page), чтобы добавить штамп в PDF.

Вы также можете установить атрибуты шрифта штампа номера страницы.

Следующий фрагмент кода показывает, как добавить номера страниц в PDF файл.

```cpp
void AddPageNumberToPDF() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("PageNumberStamp.pdf");
    String outputFileName("PageNumberStamp_out.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Создать штамп номера страницы
    auto pageNumberStamp = MakeObject<PageNumberStamp>();
    //// Является ли штамп фоном
    //pageNumberStamp.Background = false;
    //pageNumberStamp.Format = "Page # of " + pdfDocument.Pages.Count;
    //pageNumberStamp.BottomMargin = 10;
    //pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
    //pageNumberStamp.StartingNumber = 1;

    //// Установить свойства текста
    //pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
    //pageNumberStamp.TextState.FontSize = 14.0F;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
    //pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
    //pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

    // Добавить штамп на конкретную страницу
    document->get_Pages()->idx_get(1)->AddStamp(pageNumberStamp);

    // Сохранить выходной документ
    document->Save(_dataDir+ outputFileName);
}
```

## Пример в реальном времени

[Добавить номера страниц в PDF](https://products.aspose.app/pdf/page-number) — это бесплатное веб-приложение, которое позволяет исследовать, как работает функциональность добавления номеров страниц.

[![Как добавить номер страницы в PDF с использованием C++](page_number.png)](https://products.aspose.app/pdf/page-number)

## Добавить/Удалить нумерацию Бейтса

**Нумерация Бейтса** (также известная как штамп Бейтса) используется в юридической, медицинской и бизнес-сферах для размещения идентификационных номеров и/или отметок даты/времени на изображениях и документах при их сканировании или обработке, например, на этапе раскрытия информации в процессе подготовки к судебному разбирательству или идентификации бизнес-чеки. Этот процесс обеспечивает идентификацию, защиту и автоматическую последовательную нумерацию изображений или документов.

Aspose.PDF пока что имеет ограниченную поддержку нумерации Бейтса. Эта функциональность будет обновлена в соответствии с запросами клиентов.

### Как удалить нумерацию Бейтса

```cpp
void WorkingWithPages::RemoveBatesNubmering()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("BatesNumbering.pdf");
    String outputFileName("BatesNumbering_out.pdf");
    String customSubtype("BatesN");
    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    for (auto page : document->get_Pages())
    {
        auto coll = page->get_Artifacts();
        for (auto batesNum : coll)
        {
        if (batesNum->get_CustomSubtype() == customSubtype)
            page->get_Artifacts()->Delete(batesNum);
        }
    }

    // Сохранить выходной документ
    document->Save(_dataDir + outputFileName);
}
```