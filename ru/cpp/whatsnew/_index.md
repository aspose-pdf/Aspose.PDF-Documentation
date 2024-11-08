---
title: Новое в C++
linktitle: Новое
type: docs
weight: 10
url: /ru/cpp/whatsnew/
description: На этой странице представлены самые популярные новые функции в Aspose.PDF для C++, которые были введены в последних выпусках.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## Что нового в Aspose.PDF 24.8

Возможность добавлять SVG изображения на страницу.

## Что нового в Aspose.PDF 24.4

Исправлена проблема с загрузкой SVG изображений.

## Что нового в Aspose.PDF 24.3

Исправлены утечки памяти при конвертации PDF документов в другие форматы.

## Что нового в Aspose.PDF 24.2

С версии 24.2 была реализована:

- Производительность JPXDecoder была улучшена.

- Исправлено чтение документов с нарушенной структурой.

## Что нового в Aspose.PDF 23.7

- Введено сохранение PDF документов в формате EPUB:

```cpp

    void ConvertPDFtoEPUB()
    {
        std::clog << __func__ << ": Start" << std::endl;
        // Строка для имени пути
        String _dataDir("C:\\Samples\\Conversion\\");

        // Строка для имени входного файла
        String infilename("sample.pdf");
        // Строка для имени выходного файла
        String outfilename("PDFToEPUB_out.epub");

        // Открыть документ
        auto document = MakeObject<Document>(_dataDir + infilename);

        // Сохранить PDF файл в формате EPUB
        document->Save(_dataDir + outfilename, SaveFormat::Epub);
        std::clog << __func__ << ": Finish" << std::endl;
    }
```

- Загрузка файлов формата PCL была реализована:

```cpp

    int main(int argc, char** argv)
    {
        try
        {
            auto options = System::MakeObject<PclLoadOptions>();
            options->ConversionEngine = Aspose::Pdf::PclLoadOptions::ConversionEngines::NewEngine;
            options->SupressErrors = false;

            auto doc = System::MakeObject<Document>(u"c:/aspose.pcl", options);
            doc->Save(u"e:/37432.pdf");
        }
        catch (const System::Exception& error)
        {
            Console::WriteLine(u"Ошибка: {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "Ошибка: " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```

## Что нового в Aspose.PDF 23.1

С версии 23.1 была добавлена поддержка изображений формата Dicom:

```cpp

    int main()
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Dicom);
        image->set_ImageStream(MakeObject<FileStream>(u"c:/aspose.pdf/Aspose.dcm", FileMode::Open, FileAccess::Read));
        page->get_Paragraphs()->Add(image);
        document->Save(u"e:/document.pdf");
    }
```

## Что нового в Aspose.PDF 22.11

С версии 22.11 был анонсирован первый публичный релиз **Aspose.PDF для C++ macOS**.

Мы рады объявить о первом публичном релизе Aspose.PDF для C++ macOS. Aspose.PDF для C++ macOS — это проприетарная библиотека C++, которая позволяет разработчикам создавать и обрабатывать PDF-документы без использования Adobe Acrobat. Aspose.PDF для C++ macOS позволяет разработчикам создавать формы, добавлять/редактировать текст, обрабатывать страницы PDF, добавлять аннотации, обрабатывать пользовательские шрифты и многое другое.

## Что нового в Aspose.PDF 22.5

Была реализована поддержка XFA-форм в PDF-документах.

## Что нового в Aspose.PDF 22.4

Новая версия Aspose.PDF для C++ имеет кодовую базу Aspose.PDF для .Net 22.4 и Aspose.Imaging 22.4.

- был реализован метод System::Drawing::GetThumbnailImage();
- был оптимизирован конструктор RegionDataNodeRect;
- была исправлена загрузка черно-белого изображения с 1 битом на пиксель.

## Что нового в Aspose.PDF 22.3

Были добавлены перегрузки методов в многочисленные классы. Эти параметры поддерживают тип ArrayView, где ранее поддерживался только ArrayPtr.

## Что нового в Aspose.PDF 22.1

Новая версия Aspose.PDF для C++ имеет кодовую базу Aspose.PDF для .Net 22.1:

- была предоставлена новая реализация для System::Xml. Ранее у нас была собственная реализация, основанная на библиотеках libxml2 и libxslt. Новая версия основана на портированном коде CoreFX

- библиотека double-conversion была обновлена до версии 3.1.7

- файлы Dll подписаны сертификатом Aspose

## Что нового в Aspose.PDF 21.10

### Aspose.PDF для C++ поддерживает функцию преобразования SVG в формат PDF

Следующий фрагмент кода показывает процесс преобразования файла SVG в формат PDF с использованием Aspose.PDF для C++.

```cpp

    void ConvertSVGtoPDF()
    {
        std::clog << "SVG to PDF convert: Start" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("sample.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }
        std::clog << "SVG to PDF convert: Finish" << std::endl;
    }
```
Рассмотрим пример с расширенными функциями:

```cpp

    void ConvertSVGtoPDF_Advanced()
    {
        std::clog << "SVG to PDF convert: Start" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("Aspose.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        options->set_AdjustPageSize(true);
        options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }

        std::clog << "SVG to PDF convert: Finish" << std::endl;
    }
```

## Что нового в Aspose.PDF 21.4

### Реализовано сохранение PDF документов в формате HTML

Aspose.PDF для C++ поддерживает функции для преобразования PDF файла в HTML.

```cpp

    int main()
    {
        auto doc = MakeObject<Document>(u"e:\\sample.pdf");
        doc->Save(u"e:\\sample.html", SaveFormat::Html);
    }
```