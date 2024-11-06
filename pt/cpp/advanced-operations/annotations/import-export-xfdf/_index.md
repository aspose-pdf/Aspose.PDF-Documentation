---
title: Importar e Exportar Anotações para o formato XFDF usando Aspose.PDF para C++
linktitle: Importar e Exportar Anotações para o formato XFDF
type: docs
weight: 40
url: pt/cpp/import-export-xfdf/
description: Você pode importar e exportar anotações com o formato XFDF usando C++ e a biblioteca Aspose.PDF para C++.
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF é um formato de arquivo compatível com leitores de PDF. Arquivos XFDF usam o formato XML para armazenar dados como codificação de formulários e anotações, que podem ser salvos e importados/exportados para PDF e visualizados.

XFDF pode ser usado para muitas outras tarefas diferentes, mas no nosso caso, ele pode ser usado para enviar ou receber dados de formulários ou anotações para outros computadores ou servidores, etc., ou pode ser usado para arquivar dados de formulários ou anotações.

{{% /alert %}}

**Aspose.PDF para C++** é um componente rico em recursos quando se trata de editar documentos PDF. Como sabemos, XFDF é um aspecto importante da manipulação de formulários PDF, o namespace Aspose.Pdf.Facades no Aspose.PDF para C++ considerou isso muito bem e forneceu métodos para importar e exportar dados de anotações para arquivos XFDF.

A classe [PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) contém dois métodos para trabalhar com a importação e exportação de anotações para o arquivo XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) método fornece a funcionalidade para exportar anotações de um documento PDF para um arquivo XFDF, enquanto o método [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) permite importar anotações de um arquivo XFDF existente. Para importar ou exportar anotações, precisamos especificar os tipos de anotação. Podemos especificar esses tipos na forma de uma enumeração e, em seguida, passar essa enumeração como um argumento para qualquer um desses métodos.

O trecho de código a seguir mostra como exportar anotações para um arquivo XFDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Facades;

void AnnotationImportExport::ExportAnnotationXFDF() {

    String _dataDir("C:\\Samples\\");

    // Criar objeto PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Vincular documento PDF ao Editor de Anotações
    annotationEditor->BindPdf(_dataDir + u"AnnotationDemo1.pdf");

    // Exportar anotações
    auto fileStream = System::IO::File::OpenWrite(_dataDir +u"exportannotations.xfdf");
    auto annotType = MakeArray<AnnotationType>({ AnnotationType::Line, AnnotationType::Square });
    annotationEditor->ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
    fileStream->Flush();
    fileStream->Close();
}
```
O próximo trecho de código descreve como importar anotações para um arquivo XFDF:

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // Criar objeto PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Criar um novo documento PDF
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // Importar anotação
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // Salvar PDF de saída
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## Outra maneira de exportar/importar anotações de uma vez

No código abaixo, um método ImportAnnotations permite importar anotações diretamente de outro documento PDF.

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // Criar objeto PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Criar um novo documento PDF
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // O Editor de Anotações permite importar anotações de vários documentos PDF,
    // mas neste exemplo, usamos apenas um.
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // Salvar PDF de saída
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```