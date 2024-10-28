---
title: Impor dan Ekspor Anotasi ke format XFDF menggunakan Aspose.PDF untuk C++
linktitle: Impor dan Ekspor Anotasi ke format XFDF
type: docs
weight: 40
url: /cpp/import-export-xfdf/
description: Anda dapat mengimpor dan mengekspor anotasi dengan format XFDF menggunakan C++ dan pustaka Aspose.PDF untuk C++.
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF adalah format file yang kompatibel dengan pembaca PDF. File XFDF menggunakan format XML untuk menyimpan data seperti pengkodean formulir dan anotasi, yang dapat disimpan dan diimpor/ekspor ke PDF dan dilihat.

XFDF dapat digunakan untuk banyak tugas berbeda lainnya, tetapi dalam kasus kami, ini dapat digunakan baik untuk mengirim atau menerima data formulir atau anotasi ke komputer atau server lain, dll., atau dapat digunakan untuk mengarsipkan data formulir atau anotasi.

{{% /alert %}}

**Aspose.PDF untuk C++** adalah komponen yang kaya fitur dalam hal mengedit dokumen PDF. As we know XFDF adalah aspek penting dari manipulasi formulir PDF, namespace Aspose.Pdf.Facades di Aspose.PDF untuk C++ telah mempertimbangkan ini dengan sangat baik, dan telah menyediakan metode untuk mengimpor dan mengekspor data anotasi ke file XFDF.

Kelas [PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) berisi dua metode untuk bekerja dengan impor dan ekspor anotasi ke file XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) metode menyediakan fungsi untuk mengekspor anotasi dari dokumen PDF ke file XFDF, sedangkan metode [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) memungkinkan Anda untuk mengimpor anotasi dari file XFDF yang ada. Untuk mengimpor atau mengekspor anotasi, kita perlu menentukan jenis anotasi. Kita dapat menentukan jenis ini dalam bentuk enumerasi dan kemudian meneruskan enumerasi ini sebagai argumen ke salah satu metode ini.

Cuplikan kode berikut menunjukkan cara mengekspor anotasi ke file XFDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Facades;

void AnnotationImportExport::ExportAnnotationXFDF() {

    String _dataDir("C:\\Samples\\");

    // Buat objek PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Ikat dokumen PDF ke Editor Anotasi
    annotationEditor->BindPdf(_dataDir + u"AnnotationDemo1.pdf");

    // Ekspor anotasi
    auto fileStream = System::IO::File::OpenWrite(_dataDir +u"exportannotations.xfdf");
    auto annotType = MakeArray<AnnotationType>({ AnnotationType::Line, AnnotationType::Square });
    annotationEditor->ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
    fileStream->Flush();
    fileStream->Close();
}
```
The next code snippet describes how import annotations to an XFDF file:

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // Buat objek PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Buat dokumen PDF baru
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // Impor anotasi
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // Simpan PDF keluaran
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## Cara lain untuk mengekspor/mengimpor anotasi sekaligus

Dalam kode di bawah ini, metode ImportAnnotations memungkinkan impor anotasi langsung dari dokumen PDF lain.

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // Buat objek PdfAnnotationEditor
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // Buat dokumen PDF baru
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // Editor Anotasi memungkinkan impor anotasi dari beberapa dokumen PDF,
    // tetapi dalam contoh ini, kita hanya menggunakan satu.
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // Simpan PDF keluaran
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```