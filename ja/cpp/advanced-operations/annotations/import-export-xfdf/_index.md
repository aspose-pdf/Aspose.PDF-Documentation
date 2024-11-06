---
title: XFDF形式の注釈をインポートおよびエクスポートする方法 | Aspose.PDF for C++
linktitle: XFDF形式の注釈をインポートおよびエクスポートする
type: docs
weight: 40
url: ja/cpp/import-export-xfdf/
description: C++とAspose.PDF for C++ライブラリを使用してXFDF形式で注釈をインポートおよびエクスポートできます。
lastmod: "2021-12-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDFはPDFリーダーと互換性のあるファイル形式です。XFDFファイルはXML形式を使用してデータを保存し、フォームのエンコードや注釈などを保存し、PDFにインポート/エクスポートして表示できます。

XFDFはさらに多くの異なるタスクに使用できますが、私たちの場合、それはフォームデータや注釈を他のコンピュータやサーバーなどに送信または受信するために使用することができます。また、フォームデータや注釈をアーカイブするためにも使用できます。

{{% /alert %}}

**Aspose.PDF for C++**は、PDFドキュメントを編集する際に豊富な機能を備えたコンポーネントです。 ```
As we know XFDF is an important aspect of PDF forms manipulation, Aspose.Pdf.Facades namespace in Aspose.PDF for C++ has considered this very well, and have provided methods to import and export annotations data to XFDF files.

XFDFはPDFフォーム操作の重要な側面であることはご存知の通りですが、Aspose.PDF for C++のAspose.Pdf.Facades名前空間はこれを非常によく考慮しており、XFDFファイルへの注釈データのインポートおよびエクスポートの方法を提供しています。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) class contains two methods to work with import and export of annotations to XFDF file.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) クラスには、XFDFファイルへの注釈のインポートとエクスポートを扱うための2つのメソッドが含まれています。
``` [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a533c7c17dfd25a2a192617492bbb561c) メソッドは、PDF ドキュメントから XFDF ファイルに注釈をエクスポートする機能を提供します。一方、[ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a17902042e1b48f5a85c0cfb8c428af0a) メソッドは、既存の XFDF ファイルから注釈をインポートすることを可能にします。注釈をインポートまたはエクスポートするためには、注釈の種類を指定する必要があります。これらの種類を列挙型の形で指定し、この列挙型をこれらのメソッドの引数として渡すことができます。

次のコードスニペットは、注釈を XFDF ファイルにエクスポートする方法を示しています:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Facades;

void AnnotationImportExport::ExportAnnotationXFDF() {

    String _dataDir("C:\\Samples\\");

    // PdfAnnotationEditor オブジェクトを作成
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // PDF ドキュメントを注釈エディターにバインド
    annotationEditor->BindPdf(_dataDir + u"AnnotationDemo1.pdf");

    // 注釈をエクスポート
    auto fileStream = System::IO::File::OpenWrite(_dataDir +u"exportannotations.xfdf");
    auto annotType = MakeArray<AnnotationType>({ AnnotationType::Line, AnnotationType::Square });
    annotationEditor->ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
    fileStream->Flush();
    fileStream->Close();
}
```
XFDFファイルに注釈をインポートする方法を示す次のコードスニペットです:

```cpp
void AnnotationImportExport::ImportAnnotationXFDF() {

    // PdfAnnotationEditorオブジェクトを作成
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // 新しいPDFドキュメントを作成
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);

    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // 注釈をインポート
    annotationEditor->ImportAnnotationsFromXfdf(exportFileName);

    // 出力PDFを保存
    document->Save(_dataDir + u"AnnotationDemo2.pdf");
}
```

## 一度に注釈をエクスポート/インポートする別の方法

以下のコードでは、ImportAnnotationsメソッドが別のPDFドキュメントから直接注釈をインポートすることを可能にします。

```cpp
void AnnotationImportExport::ImportAnnotationFromPDF() {

    // PdfAnnotationEditorオブジェクトを作成
    auto annotationEditor = MakeObject<PdfAnnotationEditor>();

    // 新しいPDFドキュメントを作成
    auto document = new Document();
    document->get_Pages()->Add();

    annotationEditor->BindPdf(document);
    String _dataDir("C:\\Samples\\");
    String exportFileName = _dataDir + u"exportannotations.xfdf";

    if (!System::IO::File::Exists(exportFileName))
        ExportAnnotationXFDF();

    // 注釈エディタは複数のPDFドキュメントから注釈をインポートすることを許可しますが、
    // この例では1つだけ使用します。
    auto fileStreams = MakeArray<String>({ _dataDir + u"AnnotationDemo1.pdf" });
    annotationEditor->ImportAnnotations(fileStreams);

    // 出力PDFを保存
    document->Save(_dataDir + u"AnnotationDemo3.pdf");
}
```