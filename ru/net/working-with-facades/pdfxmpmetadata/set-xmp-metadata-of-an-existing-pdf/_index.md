---
title: Установка XMP Метаданных существующего PDF
type: docs
weight: 20
url: /ru/net/set-xmp-metadata-of-an-existing-pdf/
description: Этот раздел объясняет, как установить XMP метаданные существующего PDF с помощью Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Для установки XMP метаданных в PDF файле, необходимо создать объект [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) и связать PDF файл, используя метод [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Вы можете использовать метод [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) класса [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata), чтобы добавить различные свойства. Наконец, вызовите метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) класса [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata). Следующий фрагмент кода показывает, как добавить XMP метаданные в PDF файл.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Создать объект PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Связать PDF файл с объектом
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// Добавить дату создания
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// Изменить дату метаданных
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// Добавить инструмент создания
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Creator tool name");

// Удалить дату изменения
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// Добавить пользовательское свойство
// Шаг #1: зарегистрировать префикс пространства имен и URI
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// Шаг #2: добавить пользовательское свойство с префиксом
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// Изменить пользовательское свойство
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// Сохранить xmp метаданные в PDF файл
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// Закрыть объект
xmpMetaData.Close();
```