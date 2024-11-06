---
title: Извлечение текста со всех страниц PDF с использованием C++
linktitle: Извлечение текста из PDF
type: docs
weight: 10
url: ru/cpp/extract-text-from-all-pdf/
description: В этой статье описываются различные способы извлечения текста из PDF-документов с использованием Aspose.PDF в C++. Извлечение с целых страниц, из конкретной части, на основе колонок и т. д.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Извлечение текста со всех страниц PDF-документа

Извлечение текста из PDF-документа является распространенной задачей. В этом примере вы увидите, как Aspose.PDF для C++ позволяет извлекать текст со всех страниц PDF документа. Вам нужно создать объект класса [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). После этого откройте PDF, используя класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), и вызовите метод 'Accept' коллекции [Pages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Класс [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) поглощает текст из документа и возвращает его в свойстве 'Text'. Следующий фрагмент кода показывает, как извлечь текст со всех страниц PDF документа.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages() {

    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Parsing\\");

    // String for file name
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Create TextAbsorber object to extract text
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Accept the absorber for all the pages
    document->get_Pages()->Accept(textAbsorber);
    // Get the extracted text
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Вызовите метод **Accept** на определенной странице объекта Document. Индекс - это номер страницы, с которой нужно извлечь текст.

```cpp
void ExtractTextFromParticularPage() {

    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект TextAbsorber для извлечения текста
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Принять абсорбер для всех страниц
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Получить извлеченный текст
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Извлечение текста со страниц с использованием Text Device

Вы можете использовать класс [TextDevice](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.devices.text_device/), чтобы извлечь текст из PDF файла. TextDevice использует TextAbsorber в своей реализации, таким образом, фактически, они делают одно и то же, но TextDevice просто реализован для унификации подхода "Device" для извлечения чего-либо со страницы: ImageDevice, PageDevice и т.д. TextAbsorber может извлекать текст из страницы, всего PDF или XForm, этот TextAbsorber более универсален

### Извлечение текста со всех страниц

Следующие шаги и фрагмент кода показывают, как извлечь текст из PDF с использованием текстового устройства.

1. Создайте объект класса Document с указанным входным PDF файлом
1. Создайте объект класса TextDevice
1. Используйте объект класса TextExtractOptions для указания параметров извлечения
1. Используйте метод Process класса TextDevice для преобразования содержимого в текст
1. Сохраните текст в выходной файл

```cpp
void ExtractTextUsingTextDevice() {

    std::clog << __func__ << ": Start" << std::endl;
    // Строка для пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto builder = MakeObject<System::Text::StringBuilder>();
    // Строка для хранения извлеченного текста
    String extractedText;

    for (auto page : document->get_Pages()) {
        auto textStream = MakeObject<System::IO::MemoryStream>();
        // Создать текстовое устройство
        auto textDevice = MakeObject<Aspose::Pdf::Devices::TextDevice>();

        // Установить параметры извлечения текста - установить режим извлечения текста (Raw или Pure)
        auto textExtOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);

        textDevice->set_ExtractionOptions(textExtOptions);

        // Преобразовать определенную страницу и сохранить текст в поток
        textDevice->Process(page, textStream);

        // Закрыть поток памяти
        textStream->Close();

        // Получить текст из потока памяти
        extractedText = System::Text::Encoding::get_Unicode()->GetString(textStream->ToArray());
        builder->Append(extractedText);

    }
    // Сохранить извлеченный текст в текстовый файл
    System::IO::File::WriteAllText(_dataDir + outfilename, builder->ToString());
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Извлечение текста из определенной области страницы

Класс [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) предоставляет возможность извлекать текст из определенной или всех страниц PDF документа. Этот класс возвращает извлеченный текст в свойстве 'Text'. Однако, если нам нужно извлечь текст из определенной области страницы, мы можем использовать свойство **Rectangle** из [TextSearchOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_search_options/). Свойство Rectangle принимает объект Rectangle в качестве значения, и с помощью этого свойства мы можем указать область страницы, из которой необходимо извлечь текст.

Метод **Accept** страницы вызывается для извлечения текста. Создайте объекты классов [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) и [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Вызовите метод 'Accept' на отдельной странице, как **Page** Index, объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/). **Index** — это конкретный номер страницы, с которой нужно извлечь текст. Вы можете получить текст из свойства 'Text' класса [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber). Следующий фрагмент кода показывает, как извлечь текст с отдельной страницы.

```cpp
void ExtractTextFromParticularPageRegion() {

    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект TextAbsorber для извлечения текста
    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
    textAbsorber->get_TextSearchOptions()->set_Rectangle(MakeObject<Rectangle>(100, 200, 250, 350));

    // Принять поглотитель для всех страниц
    document->get_Pages()->idx_get(1)->Accept(textAbsorber);
    // Получить извлеченный текст
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;

}
```
## Извлечение текста по столбцам

PDF — это очень популярный формат, и на то есть веская причина: с PDF вы можете быть практически уверены, что ваш документ будет отображаться и печататься одинаково на разных компьютерах.

Однако документы PDF имеют недостаток в том, что обычно в них отсутствует информация о содержимом в параграфах, таблицах, рисунках, заголовках/подвалах и так далее.

Aspose.PDf для C++ — это простой в использовании инструмент, который позволяет извлекать текст на основе столбцов.

```cpp
void ExtractTextBasedOnColumns() {

    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Создать объект TextAbsorber для извлечения текста
    auto textFragmentAbsorber = MakeObject<TextFragmentAbsorber>();


    // Применить абсорбер ко всем страницам
    document->get_Pages()->Accept(textFragmentAbsorber);

    auto tfc = textFragmentAbsorber->get_TextFragments();
    for (auto tf : tfc)
    {
        // Необходимо уменьшить размер шрифта как минимум на 70%
        auto size = tf->get_TextState()->get_FontSize() * 0.7f;
        tf->get_TextState()->set_FontSize(size);
    }
    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    document = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Второй подход - Использование ScaleFactor

В этом новом выпуске мы также внедрили несколько улучшений в TextAbsorber и во внутренний механизм форматирования текста. Теперь при извлечении текста в режиме «Pure» вы можете указать опцию [ScaleFactor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_extraction_options#a4f9a173765d483b493c31e416f8b035a), и это может быть еще одним подходом для извлечения текста из многостолбцового PDF-документа, помимо вышеупомянутого подхода. Этот коэффициент масштабирования может быть установлен для настройки сетки, которая используется во внутреннем механизме форматирования текста во время извлечения текста. Указание значений ScaleFactor между 1 и 0.1 (включая 0.1) оказывает тот же эффект, что и уменьшение шрифта.

Указание значений ScaleFactor между 0.1 и -0.1 рассматривается как нулевое значение, но это заставляет алгоритм автоматически рассчитывать необходимый коэффициент масштабирования во время извлечения текста. Расчет основан на средней ширине глифа самого популярного шрифта на странице, но мы не можем гарантировать, что в извлеченном тексте ни одна строка столбца не достигает начала следующего столбца. Обратите внимание, что если значение ScaleFactor не указано, будет использоваться значение по умолчанию 1.0. Это означает, что масштабирование выполняться не будет. Если указанное значение ScaleFactor больше 10 или меньше -0.1, будет использоваться значение по умолчанию 1.0.

Мы предлагаем использовать автоматическое масштабирование (ScaleFactor = 0) при обработке большого количества PDF файлов для извлечения текстового содержимого. Или вручную установить избыточное уменьшение ширины сетки (около ScaleFactor = 0.5). Тем не менее, вы не должны определять, необходимо ли масштабирование для конкретных документов или нет. Если вы установите избыточное уменьшение ширины сетки для документа (который в этом не нуждается), извлеченное текстовое содержимое останется полностью адекватным. Пожалуйста, посмотрите на следующий фрагмент кода.

```cpp
void ExtractTextUsingScaleFactor() {

    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-4pages.pdf");
    String outfilename("extracted-text.txt");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto textAbsorber = MakeObject<TextAbsorber>();
    textAbsorber->set_ExtractionOptions(MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure));
    // Установка коэффициента масштабирования на 0.5 достаточна для разделения столбцов в большинстве документов
    // Установка нуля позволяет алгоритму выбирать коэффициент масштабирования автоматически
    textAbsorber->get_ExtractionOptions()->set_ScaleFactor(0.5); /* 0; */
    document->get_Pages()->Accept(textAbsorber);
    String extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(_dataDir + outfilename, extractedText);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Извлечение выделенного текста из PDF-документа

В различных сценариях извлечения текста из PDF-документа может возникнуть необходимость извлечь только выделенный текст. Для реализации этой функциональности мы добавили методы TextMarkupAnnotation.GetMarkedText() и TextMarkupAnnotation.GetMarkedTextFragments() в API. Вы можете извлечь выделенный текст из PDF-документа, отфильтровав TextMarkupAnnotation и используя указанные методы. Следующий фрагмент кода показывает, как можно извлечь выделенный текст из PDF-документа.

```cpp
void ExtractHighlightedText() {

    std::clog << __func__ << ": Start" << std::endl;
    // Строка для пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-highlight.pdf");
    String outfilename("extracted-text.txt");

    // Открыть документ
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Перебрать все аннотации
    for (auto annotation : document->get_Pages()->idx_get(1)->get_Annotations())
    {
        // Фильтр TextMarkupAnnotation
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Highlight)
        {
        auto highlightedAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);

        // Извлечение выделенных фрагментов текста
        auto collection = highlightedAnnotation->GetMarkedTextFragments();
        for (auto tf : collection)
        {
            // Показать выделенный текст
            String s = tf->get_Text();
            std::cout << s << std::endl;
        }
        }
    }
}
```

## Доступ к элементам TextFragment и TextSegment из XML

Иногда необходимо получить доступ к элементам TextFragment или TextSegment при обработке PDF-документов, созданных из XML. Aspose.PDF для C++ предоставляет доступ к таким элементам по имени. Пример кода ниже показывает, как использовать эту функциональность.

```cpp
void AccessTextFragmentandSegmentElementsXML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Parsing\\");

    // Строка для имени файла
    String infilename("sample-doc.xml");
    String outfilename("sample-doc.pdf");

    auto document = MakeObject<Document>();
    document->BindXml(_dataDir + infilename);

    System::SharedPtr<Page> page = System::DynamicCast<Aspose::Pdf::Page>(document->GetObjectById(u"mainSection"));
    // Выполнение некоторых операций с страницей
    // ...

    System::SharedPtr<TextSegment> segment = System::DynamicCast<Aspose::Pdf::Text::TextSegment>(document->GetObjectById(u"product_description"));
    // Выполнение некоторых операций с сегментом
    // ...
    document->Save(_dataDir + outfilename);

    std::clog << __func__ << ": Finish" << std::endl;
}
```