---
title: Конвертация PDF в форматы PDF/A
linktitle: Конвертация PDF в форматы PDF/A
type: docs
weight: 100
url: /ru/cpp/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать PDF файл в PDF файл, соответствующий стандарту PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF для C++** позволяет конвертировать PDF файл в PDF файл, соответствующий стандарту <abbr title="Portable Document Format / A">PDF/A</abbr>. Перед этим файл должен быть проверен. Эта тема объясняет, как это сделать.

{{% alert color="primary" %}}

Обратите внимание, что мы следуем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют свою собственную «репрезентацию» соответствия PDF/A. Пожалуйста, ознакомьтесь с этой статьей о инструментах проверки PDF/A для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создает PDF файлы, потому что Adobe находится в центре всего, что связано с PDF.

{{% /alert %}}

Конвертируйте файл, используя метод Convert класса Document. Перед преобразованием PDF в файл, соответствующий стандарту PDF/A, проверьте PDF, используя метод Validate. Результат проверки сохраняется в XML-файл, и затем этот результат также передается в метод Convert. Вы также можете указать действие для элементов, которые не могут быть преобразованы, используя перечисление ConvertErrorAction.
## Преобразование PDF-файла в PDF/A-1b

Следующий фрагмент кода показывает, как преобразовать PDF-файлы в PDF, соответствующий стандарту PDF/A-1b.

```cpp
void ConverttoPDFA_1b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени файла журнала
    String logfilename("log.xml");
    // Строка для имени выходного файла
    String outfilename("PDFToPDFA_out.pdf");

    // Открыть документ
    auto document = new Document(_dataDir + infilename);

    // Преобразовать в документ, соответствующий стандарту PDF/A
    // В процессе преобразования также выполняется проверка
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

    // Сохранить выходной документ
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
Для выполнения только проверки используйте следующую строку кода:

```cpp
void ConverttoPDFA_1b_Validation()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени файла журнала
    String logfilename("log.xml");

    // Открыть документ
    auto document = new Document(_dataDir + infilename);

    // Преобразовать в документ, соответствующий PDF/A
    // Во время процесса преобразования также выполняется проверка
    document->Validate(_dataDir + logfilename, PdfFormat::PDF_A_1B);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Преобразование PDF файла в PDF/A-3b

Aspose.PDF для C++ также поддерживает возможность преобразования PDF файла в формат PDF/A-3b.

```cpp
void ConverttoPDFA_3b()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени файла журнала
    String logfilename("log.xml");
    // Строка для имени выходного файла
    String outfilename("PDFToPDFA3b_out.pdf");

    // Открыть документ
    auto document = new Document(_dataDir + infilename);

    // Преобразовать в документ, соответствующий PDF/A
    // Во время процесса преобразования также выполняется проверка
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3B, ConvertErrorAction::Delete);

    // Сохранить выходной документ
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert PDF file to PDF/A-2u

Aspose.PDF для C++ также поддерживает функцию преобразования PDF-файла в формат PDF/A-2u.

```cpp
void ConverttoPDFA_2u()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
     String infilename("sample.pdf");
    // String for log file name
    String logfilename("log.xml");
    // String for input file name
    String outfilename("PDFToPDFA3b_out.pdf");

    // Open document
    auto document = new Document(_dataDir + infilename);

    // Convert to PDF/A compliant document
    // During conversion process, the validation is also performed
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Save output document
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Convert PDF file to PDF/A-3u

Aspose.PDF для C++ также поддерживает функцию преобразования PDF-файла в формат PDF/A-3u.

```cpp
void ConverttoPDFA_3u()
{
    std::clog << __func__ << ": Начало" << std::endl;
    // Строка для имени пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени файла журнала
    String logfilename("log.xml");
    // Строка для имени выходного файла
    String outfilename("PDFToPDFA3b_out.pdf");

    // Открыть документ
    auto document = new Document(_dataDir + infilename);

    // Преобразовать в документ, соответствующий PDF/A
    // Во время процесса преобразования также выполняется валидация
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_2U, ConvertErrorAction::Delete);

    // Сохранить выходной документ
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Завершение" << std::endl;
}
```

## Добавить вложение в файл PDF/A

Если у вас есть требование прикрепить файлы к формату соответствия PDF/A, то мы рекомендуем использовать значение PDF_A_3A из перечисления Aspose.PDF.PdfFormat.

PDF/A_3a - это формат, который предоставляет возможность прикреплять любой формат файла в качестве вложения к файлу, соответствующему PDF/A.

```cpp
void ConverttoPDFA_AddAttachment()
{
    std::clog << __func__ << ": Начало" << std::endl;
    // Строка для пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени файла журнала
    String logfilename("log.xml");
    // Строка для имени выходного файла
    String outfilename("PDFToPDFA3b_out.pdf");

    // Открыть документ
    auto document = new Document(_dataDir + infilename);

    // Настройка нового файла для добавления в виде вложения
    auto fileSpecification = MakeObject<FileSpecification>(_dataDir + String("aspose-logo.jpg"), String("Большой файл изображения"));
    // Добавить вложение в коллекцию вложений документа
    document->get_EmbeddedFiles()->Add(fileSpecification);

    // Преобразовать в документ, соответствующий PDF/A
    // В процессе преобразования также выполняется проверка
    document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_3A, ConvertErrorAction::Delete);

    // Сохранить выходной документ
    document->Save(_dataDir + outfilename);
    std::clog << __func__ << ": Завершение" << std::endl;
}
```

## Замена отсутствующих шрифтов альтернативными шрифтами

Согласно стандартам PDFA, шрифты должны быть встроены в документ PDFA. Однако, если шрифты не встроены в исходный документ или отсутствуют на машине, то PDFA не проходит проверку. В этом случае требуется заменить отсутствующие шрифты на некоторые альтернативные шрифты с машины. Мы можем заменить отсутствующие шрифты, используя метод SimpleFontSubsituation следующим образом при конверсии PDF в PDFA.

```cpp
void ConverttoPDFA_ReplaceFont()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Строка для пути
    String _dataDir("C:\\Samples\\Conversion\\");

    // Строка для имени входного файла
    String infilename("sample.pdf");
    // Строка для имени файла журнала
    String logfilename("log.xml");
    // Строка для имени выходного файла
    String outfilename("PDFToPDFA3b_out.pdf");

    // Открыть документ
    auto document = new Document(_dataDir + infilename);

    System::SharedPtr<Aspose::Pdf::Text::Font> originalFont;
    try
    {
        originalFont = FontRepository::FindFont(String("AgencyFB"));
    }
    catch (Exception)
    {
        // Шрифт отсутствует на целевой машине
        auto substitutions = FontRepository::get_Substitutions();
        auto substitution = MakeObject<SimpleFontSubstitution>(String("AgencyFB"), String("Helvetica"));
        substitutions->Add(substitution);
    }

    // Конвертировать в документ, соответствующий PDF/A
    try {
        // Во время процесса конверсии также выполняется проверка
        document->Convert(_dataDir + logfilename, PdfFormat::PDF_A_1B, ConvertErrorAction::Delete);

        // Сохранить выходной документ
        document->Save(_dataDir + outfilename);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="primary" %}}
**Попробуйте конвертировать PDF в PDF/A онлайн**

Aspose.PDF for C++ представляет вам бесплатное онлайн-приложение ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Конвертация PDF в PDF/A с бесплатным приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}