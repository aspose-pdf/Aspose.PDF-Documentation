---
title: Создание PDF документа
linktitle: Создать PDF
type: docs
weight: 10
url: ru/cpp/create-pdf-document/
description: Эта статья описывает, как создавать и форматировать PDF документ с использованием Aspose.PDF для C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Мы всегда ищем способы создания PDF документов и работы с ними в проектах на C++ более точно, аккуратно и эффективно. Наличие простых в использовании функций из библиотеки позволяет нам сосредоточиться больше на работе, и меньше на трудоемких деталях, связанных с созданием PDF, будь то на C++.

## Генерация PDF с использованием C++

Aspose.PDF для C++ API позволяет создавать и читать PDF файлы с использованием C++. API может использоваться в различных приложениях на C++, включая WinForms и другие. В этой статье мы покажем, как использовать Aspose.PDF для C++ API для простого создания и чтения PDF файлов в приложениях на C++.

### Как создать простой PDF файл

Чтобы создать PDF файл с использованием C++, можно использовать следующие шаги.

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)  
1. Добавьте объект [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) в коллекцию 'Pages' объекта Document  
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) в коллекцию [Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) на странице  
1. Сохраните полученный PDF документ  

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");

    // Строка для имени файла.
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Добавить текст на новую страницу
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Сохранить обновленный PDF
    document->Save(_dataDir + outputFileName);
}
```
## Создание PDF-документа с возможностью поиска

Aspose.PDF для C++ позволяет создавать PDF с нуля и изменять существующие. 
Когда вы добавляете текстовые элементы в PDF, полученный PDF можно искать. Однако, если мы преобразуем изображение, содержащее текст, в PDF-файл, содержимое внутри PDF не подлежит поиску. Однако, как обходной путь, мы можем использовать OCR на полученном файле, чтобы сделать его доступным для поиска. Таким образом, сначала вам нужно установить Tesseract-OCR на вашу систему, и у вас будет консольное приложение tesseract.

Ниже приведен полный код для выполнения этого требования:

```cpp
void CreateSearchableDocument() {
    // Строка для имени пути.
    String _dataDir("C:\\Samples\\");
    // Строка для имени файла.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();

    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;
}
```