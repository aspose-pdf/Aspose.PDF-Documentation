---
title: Работа с портфолио в PDF
linktitle: Портфолио
type: docs
weight: 40
url: ru/cpp/portfolio/
description: Создайте PDF-портфолио с помощью Aspose.PDF для C++. Вы должны использовать файл Microsoft Excel, документ Word и файл изображения для создания PDF-портфолио.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Как создать PDF-портфолио

Aspose.PDF позволяет создавать документы PDF-портфолио, используя класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Добавьте файл в объект Document.Collection после его получения с помощью класса [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Когда файлы добавлены, используйте метод Save класса Document, чтобы сохранить документ портфолио.

Следующий пример использует файл Microsoft Excel, документ Word и файл изображения для создания PDF-портфолио.

Код ниже приводит к следующему портфолио.

### PDF-портфолио, созданное с помощью Aspose.PDF


![PDF-портфолио, созданное с помощью Aspose.PDF для C++](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // Создать объект документа
    auto pdfDocument = MakeObject<Document>();

    // Создать объект коллекции документов
    pdfDocument->set_Collection(MakeObject<Collection>());

    // Получить файлы для добавления в портфолио
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // Указать описание файлов
    excel->set_Description(u"Файл Excel");
    word->set_Description(u"Файл Word");
    image->set_Description(u"Файл изображения");

    // Добавить файлы в коллекцию документов
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // Сохранить документ портфолио
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```

## Извлечение файлов из PDF портфолио

PDF Портфолио позволяет объединить контент из различных источников (например, PDF, Word, Excel, JPEG файлы) в один унифицированный контейнер. Оригинальные файлы сохраняют свою индивидуальность, но собираются в файл PDF Портфолио. Пользователи могут открывать, читать, редактировать и форматировать каждый компонентный файл независимо от других компонентных файлов.

Aspose.PDF позволяет создавать документы PDF Портфолио с использованием класса [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Он также предлагает возможность извлечения файлов из PDF портфолио.

Следующий фрагмент кода показывает вам шаги для извлечения файлов из PDF портфолио.

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // Получить коллекцию встроенных файлов
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // Перебор каждого файла в Портфолио
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // Сохранить извлеченный файл в какое-либо место
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // Закрыть объект потока
    fileStream->Close();
    }
}
```

![Извлечение файлов из PDF-портфолио](working-with-pdf-portfolio_2.jpg)

## Удаление файлов из PDF-портфолио

Чтобы удалить файлы из PDF-портфолио, попробуйте использовать следующие строки кода.

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Загрузить исходное PDF-портфолио
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```