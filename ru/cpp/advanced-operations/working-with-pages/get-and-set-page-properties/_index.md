---
title: Получение и Установка Свойств Страницы
type: docs
weight: 20
url: ru/cpp/get-and-set-page-properties/
description: Вы можете получить и установить свойства страниц вашего PDF файла, используя библиотеку C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** позволяет читать и устанавливать свойства страниц в PDF файле в ваших приложениях на C++. Этот раздел показывает, как получить количество страниц в PDF файле, получить информацию о свойствах страницы PDF, таких как цвет, установить свойства страницы, получить конкретную страницу PDF файла и т.д.

## Получение Количества Страниц в PDF Файле

При работе с документами часто хочется знать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

Чтобы получить количество страниц в PDF файле:

1. Откройте PDF файл, используя класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Затем используйте свойство Count коллекции [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) (из объекта Document), чтобы получить общее количество страниц в документе.

Следующий фрагмент кода показывает, как получить количество страниц PDF-файла.

```cpp
void GetNumberOfPages() {
    // Открыть документ
    String _dataDir("C:\\Samples\\");
    String srcFileName("GetNumberofPages.pdf");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);

    // Получить количество страниц
    std::cout << "Page Count : " << srcDocument->get_Pages()->get_Count() << std::endl;
}
```

### Получить количество страниц без сохранения документа

Иногда мы создаем PDF-файлы на лету и в процессе создания PDF-файла можем столкнуться с необходимостью (создание оглавления и т.д.) получить количество страниц PDF-файла без сохранения файла на системе или потоке. Итак, для удовлетворения этого требования в классе Document был введен метод [ProcessParagraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a1773e7b6a887eaddd602073e29939a6f). Пожалуйста, обратите внимание на следующий фрагмент кода, который показывает шаги для получения количества страниц без сохранения документа.

```cpp
void GetPageCountWithoutSavingTheDocument() {
    // Создать экземпляр Document
    auto document = MakeObject<Document>();

    // Добавить страницу в коллекцию страниц PDF файла
    auto page = document->get_Pages()->Add();
    // Создать экземпляр цикла
    for (int i = 0; i < 300; i++)
        // Добавить TextFragment в коллекцию параграфов объекта страницы
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Pages count test"));
    // Обработать параграфы в PDF файле для получения точного количества страниц
    document->ProcessParagraphs();
    // Вывести количество страниц в документе
    std::cout << "Number of pages in document = " << document->get_Pages()->get_Count();
}
```

## Получить свойства страницы
### Доступ к свойствам страницы

Класс [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) предоставляет все свойства, связанные с конкретной страницей PDF. Все страницы PDF-файлов содержатся в коллекции [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Оттуда можно получить доступ как к отдельным объектам Page, используя их индекс, так и пройтись по коллекции с помощью цикла foreach, чтобы получить все страницы. Как только доступ к отдельной странице получен, мы можем получить ее свойства. Следующий фрагмент кода показывает, как получить свойства страницы.

```cpp
void AccessingPageProperties() {

    String _dataDir("C:\\Samples\\");
    String pdfDocument("GetProperties.pdf");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + pdfDocument);

    // Получить конкретную страницу
    auto pdfPage = document->get_Pages()->idx_get(1);
    // Получить свойства страницы
    Console::WriteLine(u"ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_ArtBox()->get_Height(), pdfPage->get_ArtBox()->get_Width(),
        pdfPage->get_ArtBox()->get_LLX(), pdfPage->get_ArtBox()->get_LLY(),
        pdfPage->get_ArtBox()->get_URX(), pdfPage->get_ArtBox()->get_URY());

    Console::WriteLine(u"->get_BleedBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_BleedBox()->get_Height(), pdfPage->get_BleedBox()->get_Width(),
        pdfPage->get_BleedBox()->get_LLX(), pdfPage->get_BleedBox()->get_LLY(),
        pdfPage->get_BleedBox()->get_URX(), pdfPage->get_BleedBox()->get_URY());

    Console::WriteLine(u"get_CropBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_CropBox()->get_Height(), pdfPage->get_CropBox()->get_Width(),
        pdfPage->get_CropBox()->get_LLX(), pdfPage->get_CropBox()->get_LLY(),
        pdfPage->get_CropBox()->get_URX(), pdfPage->get_CropBox()->get_URY());

    Console::WriteLine(u"get_MediaBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_MediaBox()->get_Height(), pdfPage->get_MediaBox()->get_Width(),
        pdfPage->get_MediaBox()->get_LLX(), pdfPage->get_MediaBox()->get_LLY(),
        pdfPage->get_MediaBox()->get_URX(), pdfPage->get_MediaBox()->get_URY());

    Console::WriteLine(u"get_TrimBox() : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_TrimBox()->get_Height(), pdfPage->get_TrimBox()->get_Width(),
        pdfPage->get_TrimBox()->get_LLX(), pdfPage->get_TrimBox()->get_LLY(),
        pdfPage->get_TrimBox()->get_URX(), pdfPage->get_TrimBox()->get_URY());

    Console::WriteLine(u"Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}",
        pdfPage->get_Rect()->get_Height(), pdfPage->get_Rect()->get_Width(),
        pdfPage->get_Rect()->get_LLX(), pdfPage->get_Rect()->get_LLY(),
        pdfPage->get_Rect()->get_URX(), pdfPage->get_Rect()->get_URY());

    Console::WriteLine(u"Page Number : {0}", pdfPage->get_Number());
    Console::WriteLine(u"Rotate : {0}", pdfPage->get_Rotate());
}
```