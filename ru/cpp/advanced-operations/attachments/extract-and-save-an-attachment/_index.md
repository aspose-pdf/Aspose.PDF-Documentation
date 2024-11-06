---
title: Извлечение и сохранение вложения
linktitle: Извлечение и сохранение вложения
type: docs
weight: 20
url: ru/cpp/extract-and-save-an-attachment/
description: Aspose.PDF для C++ позволяет получить все вложения из PDF-документа. Также можно получить отдельное вложение из вашего документа.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получить все вложения

С помощью Aspose.PDF можно получить все вложения из PDF-документа. Это полезно, когда вы хотите сохранить документы отдельно от PDF или если вам нужно удалить вложения из PDF.

Чтобы получить все вложения из PDF файла:

1. Loop через коллекцию [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Коллекция [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) содержит все вложения. Каждый элемент этой коллекции представляет собой объект [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Каждая итерация foreach цикла через коллекцию [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) возвращает объект [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification).  
1. Как только объект доступен, извлеките либо все свойства вложенного файла, либо сам файл.

Следующие фрагменты кода показывают, как получить все вложения из PDF документа.

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // Открыть документ
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // Получить коллекцию встроенных файлов
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // Получить количество встроенных файлов
 Console::WriteLine(u"Всего файлов : {0}", embeddedFiles->get_Count());

 int count = 1;

 // Цикл через коллекцию для получения всех вложений
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Имя: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Описание: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Тип MIME: {0}", fileSpecification->get_MIMEType());

  // Проверка, содержит ли объект параметров параметры
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"Контрольная сумма: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Дата создания: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Дата изменения: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Размер: {0}", fileSpecification->get_Params()->get_Size());
  }

  // Получить вложение и записать в файл или поток
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```
## Получение индивидуального вложения

Чтобы получить индивидуальное вложение, мы можем указать индекс вложения в объекте `EmbeddedFiles` экземпляра Document. Пожалуйста, попробуйте использовать следующий фрагмент кода.

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // Открыть документ
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // Получить конкретный встроенный файл
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // Получить свойства файла
    Console::WriteLine(u"Имя: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"Описание: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"Mime Тип: {0}", fileSpecification->get_MIMEType());

    // Проверить, содержит ли объект параметра параметры
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"Контрольная сумма: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"Дата создания: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"Дата изменения: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"Размер: {0}",
        fileSpecification->get_Params()->get_Size());
    }


    // Получить вложение и записать в файл или поток
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```