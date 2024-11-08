---
title: Importar y Exportar Anotaciones al formato XFDF usando Aspose.PDF para C++
linktitle: Importar y Exportar Anotaciones al formato XFDF
type: docs
weight: 40
url: /es/cpp/import-export-xfdf/
description: Puede importar y exportar anotaciones con el formato XFDF con C++ y la biblioteca Aspose.PDF para C++.
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF es un formato de archivo compatible con los lectores de PDF. Los archivos XFDF utilizan el formato XML para almacenar datos como codificación de formularios y anotaciones, que se pueden guardar e importar/exportar a PDF y visualizar.

XFDF se puede usar para muchas más tareas diferentes, pero en nuestro caso, se puede usar para enviar o recibir datos de formularios o anotaciones a otras computadoras o servidores, etc., o se puede usar para archivar datos de formularios o anotaciones.

{{% /alert %}}

**Aspose.PDF para C++** es un componente rico en funciones cuando se trata de editar documentos PDF. Como sabemos, XFDF es un aspecto importante de la manipulación de formularios PDF, el espacio de nombres Aspose.Pdf.Facades en Aspose.PDF para C++ ha considerado esto muy bien y ha proporcionado métodos para importar y exportar datos de anotaciones a archivos XFDF.

La clase [PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) contiene dos métodos para trabajar con la importación y exportación de anotaciones a archivos XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) método proporciona la funcionalidad para exportar anotaciones de un documento PDF a un archivo XFDF, mientras que el método [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) le permite importar anotaciones de un archivo XFDF existente. Para importar o exportar anotaciones necesitamos especificar los tipos de anotación. Podemos especificar estos tipos en forma de una enumeración y luego pasar esta enumeración como un argumento a cualquiera de estos métodos.

El siguiente fragmento de código le muestra cómo exportar anotaciones a un archivo XFDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Facades;

void AnnotationImportExport::ExportAnnotationXFDF() {

    String _dataDir("C:\\Samples\\");

    // Crear objeto PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Vincular documento PDF al Editor de Anotaciones
    annotationEditor->BindPdf(_dataDir + u"AnnotationDemo1.pdf");

    // Exportar anotaciones
    auto fileStream = System::IO::File::OpenWrite(_dataDir +u"exportannotations.xfdf");
    auto annotType = MakeArray<AnnotationType>({ AnnotationType::Line, AnnotationType::Square });
    annotationEditor->ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
    fileStream->Flush();
    fileStream->Close();
}
```
El siguiente fragmento de código describe cómo importar anotaciones a un archivo XFDF:

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // Crear objeto PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Crear un nuevo documento PDF
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // Importar anotación
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // Guardar PDF de salida
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## Otra forma de exportar/importar anotaciones de una vez

En el código a continuación, un método ImportAnnotations permite importar anotaciones directamente desde otro documento PDF.

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // Crear objeto PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Crear un nuevo documento PDF
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // El Editor de anotaciones permite importar anotaciones de varios documentos PDF,
    // pero en este ejemplo, usamos solo uno.
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // Guardar PDF de salida
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```