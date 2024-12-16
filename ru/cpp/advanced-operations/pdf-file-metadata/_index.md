---
title: Метаданные PDF файла
type: docs
weight: 20
url: /ru/cpp/pdf-file-metadata/
---

## Получение/Установка информации о PDF файле

Чтобы получить специфическую информацию о PDF файле, сначала нужно вызвать метод **get_Info()** класса Document. После получения объекта DocumentInfo, вы можете получить значения отдельных свойств. Кроме того, вы можете установить свойства, используя соответствующие методы класса DocumentInfo. Следующий фрагмент кода демонстрирует, как получить/установить информацию о PDF файле, используя Aspose.PDF для C++:

{{% alert color="primary" %}}

Обратите внимание, что вы не можете установить значения для полей **Application** и **Producer**, потому что против этих полей будут отображаться Aspose Ltd. и Aspose.PDF for C++ x.x.x.

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // Получить информацию о документе
    auto docInfo = pdfDocument->get_Info();
    // Показать информацию о документе
    Console::WriteLine(u"Author: {0}", docInfo->get_Author());
    Console::WriteLine(u"Creation Date: {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Keywords: {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Modify Date: {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Subject: {0}", docInfo->get_Subject());
    Console::WriteLine(u"Title: {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // Указать информацию о документе
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"PDF Information");
    docInfo->set_Title (u"Setting PDF Document Information");

    // Сохранить выходной документ
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```

## Получение/Установка XMP Метаданных из PDF Файла

Aspose.PDF для C++ позволяет вам получить доступ к XMP метаданным PDF файла, а также установить их. Чтобы получить/установить метаданные PDF файла:

1. Создайте объект Document и откройте входной PDF файл.
2. Получите/установите метаданные файла, используя соответствующие методы.

Следующий фрагмент кода показывает, как получить/установить метаданные из PDF файла.

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // Получить свойства
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // Установить свойства
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // Сохранить документ
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // Открыть документ
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // xmlns prefix has been removed
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // Сохранить документ
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```