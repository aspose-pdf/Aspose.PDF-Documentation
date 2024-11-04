---
title: Импорт и экспорт аннотаций в формате XFDF с использованием Aspose.PDF для C++
linktitle: Импорт и экспорт аннотаций в формате XFDF
type: docs
weight: 40
url: /cpp/import-export-xfdf/
description: Вы можете импортировать и экспортировать аннотации в формате XFDF с помощью C++ и библиотеки Aspose.PDF для C++.
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF — это формат файла, совместимый с PDF-ридерами. Файлы XFDF используют формат XML для хранения данных, таких как кодировка форм и аннотации, которые могут быть сохранены и импортированы/экспортированы в PDF и просмотрены.

XFDF может использоваться для многих других различных задач, но в нашем случае он может использоваться либо для отправки или получения данных форм или аннотаций на другие компьютеры или серверы и т. д., либо для архивации данных форм или аннотаций.

{{% /alert %}}

**Aspose.PDF для C++** — это компонент, богатый функциями, когда дело касается редактирования PDF-документов. As we know XFDF является важным аспектом работы с PDF-формами, пространство имен Aspose.Pdf.Facades в Aspose.PDF для C++ учитывает это очень хорошо и предоставляет методы для импорта и экспорта данных аннотаций в файлы XFDF.

Класс [PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) содержит два метода для работы с импортом и экспортом аннотаций в файл XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) метод предоставляет функциональность для экспорта аннотаций из PDF документа в XFDF файл, в то время как метод [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) позволяет импортировать аннотации из существующего XFDF файла. Для того чтобы импортировать или экспортировать аннотации, нам необходимо указать типы аннотаций. Мы можем указать эти типы в виде перечисления и затем передать это перечисление в качестве аргумента любому из этих методов.

Следующий фрагмент кода показывает, как экспортировать аннотации в XFDF файл:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Facades;

void AnnotationImportExport::ExportAnnotationXFDF() {

    String _dataDir("C:\\Samples\\");

    // Создать объект PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Привязать PDF документ к редактору аннотаций
    annotationEditor->BindPdf(_dataDir + u"AnnotationDemo1.pdf");

    // Экспортировать аннотации
    auto fileStream = System::IO::File::OpenWrite(_dataDir +u"exportannotations.xfdf");
    auto annotType = MakeArray<AnnotationType>({ AnnotationType::Line, AnnotationType::Square });
    annotationEditor->ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
    fileStream->Flush();
    fileStream->Close();
}
```
Следующий фрагмент кода описывает, как импортировать аннотации в файл XFDF:

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // Создать объект PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Создать новый PDF документ
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // Импортировать аннотацию
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // Сохранить выходной PDF
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## Еще один способ экспортировать/импортировать аннотации сразу

В приведенном ниже коде метод ImportAnnotations позволяет импортировать аннотации непосредственно из другого PDF документа.

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // Создать объект PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Создать новый PDF документ
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // Редактор аннотаций позволяет импортировать аннотации из нескольких PDF документов,
    // но в этом примере мы используем только один.
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // Сохранить выходной PDF
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```