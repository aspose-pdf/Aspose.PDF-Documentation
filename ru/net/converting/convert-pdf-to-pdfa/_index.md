---
title: Конвертация PDF в форматы PDF/A
linktitle: Конвертация PDF в форматы PDF/A
type: docs
weight: 100
url: /ru/net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать PDF файл в соответствующий PDF/A PDF файл.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF для .NET** позволяет конвертировать PDF файл в соответствующий <abbr title="Portable Document Format / A">PDF/A</abbr> PDF файл. Перед этим файл должен быть проверен. Эта тема объясняет как.

{{% alert color="primary" %}}

Обратите внимание, что мы следуем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют своё "представление" о соответствии PDF/A. Пожалуйста, ознакомьтесь с этой статьей о инструментах проверки PDF/A для справки. Мы выбрали продукты Adobe для проверки производства PDF файлов Aspose.PDF, потому что Adobe находится в центре всего, что связано с PDF.

{{% /alert %}}

Конвертируйте файл с использованием метода Convert класса Document.
{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PDF/A онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["PDF в PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PDF/A с помощью бесплатного приложения](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Конвертировать PDF файл в PDF/A-1b

Следующий фрагмент кода показывает, как конвертировать PDF файлы в соответствие с PDF/A-1b.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Открыть документ
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// Конвертировать в соответствующий документ PDF/A
// В процессе конвертации также выполняется проверка
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// Сохранить выходной документ
pdfDocument.Save(dataDir);
```
Чтобы выполнить только проверку, используйте следующую строку кода:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Проверить PDF на соответствие PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## Конвертация PDF файла в формат PDF/A-3b

Aspose.PDF для .NET также поддерживает возможность конвертации PDF файла в формат PDF/A-3b.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Открыть документ
Document pdfDocument = new Document(dataDir + "input.pdf");           

pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// Сохранить выходной документ
pdfDocument.Save(dataDir);
```
## Преобразование PDF файла в формат PDF/A-2u

Aspose.PDF для .NET также поддерживает возможность преобразования PDF файла в формат PDF/A-2u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Преобразование PDF файла в формат PDF/A-3u

Aspose.PDF для .NET также поддерживает возможность преобразования PDF файла в формат PDF/A-3u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Добавление вложений в файл PDF/A

В случае необходимости прикрепления файлов к файлу, соответствующему формату PDF/A, рекомендуется использовать значение PDF_A_3A из перечисления Aspose.PDF.PdfFormat.
PDF/A_3a — это формат, который предоставляет возможность прикреплять файлы любого формата в качестве вложения к файлу, соответствующему PDF/A.

```csharp

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Создайте экземпляр документа для загрузки существующего файла
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// Настройте новый файл для добавления в виде вложения
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "Большой файл изображения");
// Добавьте вложение в коллекцию вложений документа
doc.EmbeddedFiles.Add(fileSpecification);
// Выполните конвертацию в PDF/A_3a, чтобы вложение было включено в итоговый файл
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// Сохраните итоговый файл
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```

## Замена отсутствующих шрифтов альтернативными

Согласно стандартам PDFA, шрифты должны быть встроены в документ PDFA.
Согласно стандартам PDFA, шрифты должны быть встроены в документ PDFA.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // Шрифт отсутствует на целевой машине
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert( dataDir +  "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```
