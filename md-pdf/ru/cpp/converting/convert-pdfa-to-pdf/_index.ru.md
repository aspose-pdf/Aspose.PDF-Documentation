---
title: Конвертировать PDF/A в формат PDF
linktitle: Конвертировать PDF/A в формат PDF
type: docs
weight: 110
url: /cpp/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать файл PDF/A в документ PDF с помощью библиотеки C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Конвертировать документ PDF/A в PDF

Конвертация документа PDF/A в PDF означает удаление ограничения <abbr title="Portable Document Format Archive
">PDF/A</abbr> из оригинального документа. Класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) имеет метод 'RemovePdfaCompliance', чтобы удалить информацию о соответствии PDF из входного/исходного файла. После чего [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) входной файл.

```cpp
void ConvertPDFAtoPDF()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);

    // Удалить информацию о соответствии PDF/A
    document->RemovePdfaCompliance();

    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```

Этот документ также удаляется, если вы вносите какие-либо изменения (например, добавляете страницы). В следующем примере выходной документ теряет соответствие PDF/A после добавления страницы.

```cpp
void ConvertPDFAtoPDFAdvanced()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    // Добавление новой (пустой) страницы удаляет информацию о соответствии PDF/A.

    document->get_Pages()->Add();
    // Сохранить обновленный документ
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```