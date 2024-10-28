---
title: XFDF形式への注釈のインポートとエクスポート
linktitle: XFDF形式への注釈のインポートとエクスポート
type: docs
weight: 40
url: /java/import-export-xfdf/
description: Aspose.PDF for Javaライブラリを使用して、XFDF形式で注釈をインポートおよびエクスポートできます。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDFはXML Forms Data Formatの略です。これはXMLベースのファイル形式です。このファイル形式は、PDFフォームに含まれるフォームデータまたは注釈を表すために使用されます。XFDFはさまざまな目的で使用できますが、私たちの場合、フォームデータまたは注釈を他のコンピュータやサーバーに送信または受信するために使用することもできますし、フォームデータまたは注釈をアーカイブするために使用することもできます。この記事では、Aspose.Pdf.Facadesがこの概念をどのように考慮し、注釈データをXFDFファイルにインポートおよびエクスポートできるかを見ていきます。

{{% /alert %}}

**Aspose.PDF for Java**は、PDFドキュメントの編集に関して多機能なコンポーネントです。
 As we know XFDFはPDFフォーム操作の重要な側面であり、Aspose.PDF for JavaのAspose.Pdf.Facades名前空間ではこれを非常によく考慮しており、注釈データをXFDFファイルにインポートおよびエクスポートするためのメソッドを提供しています。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor)クラスには、XFDFファイルへの注釈のインポートとエクスポートを扱うための2つのメソッドが含まれています。 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) メソッドは、PDF ドキュメントから XFDF ファイルに注釈をエクスポートする機能を提供します。一方、[ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) メソッドは、既存の XFDF ファイルから注釈をインポートすることを可能にします。注釈をインポートまたはエクスポートするためには、注釈の種類を指定する必要があります。これらの種類は列挙の形で指定し、その列挙をこれらのメソッドのいずれかに引数として渡します。このようにして、指定された種類の注釈のみが XFDF ファイルにインポートまたはエクスポートされます。

次のコードスニペットは、注釈を XFDF ファイルにエクスポートする方法を示しています:

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // ドキュメントディレクトリへのパス
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * XFDF ファイル XML Forms Data Format (XFDF) ファイルから注釈をインポート
     * Adobe Acrobat によって作成された、PDF オーサリングアプリケーション; ページフォーム要素とその値の説明を保存します。
     * テキストフィールドの名前と値など。PDF ドキュメントにインポートできるフォームデータを保存するために使用されます。
     * PdfAnnotationEditor クラスの ImportAnnotationsFromXfdf メソッドを使用して、XFDF ファイルから PDF へ注釈データをインポートできます。
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // PdfAnnotationEditor オブジェクトを作成
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // 注釈エディタに PDF ドキュメントをバインド
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // 注釈をエクスポート
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

次のコードスニペットは、XFDFファイルに注釈をインポートする方法を説明しています。

```java
public static void ImportAnnotationXFDF()
{
    // PdfAnnotationEditorオブジェクトを作成
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // 新しいPDFドキュメントを作成
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // 注釈をインポート
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // 出力PDFを保存
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## 注釈を一度にエクスポート/インポートする別の方法

以下のコードでは、ImportAnnotationsメソッドにより、別のPDFドキュメントから直接注釈をインポートできます。

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // PdfAnnotationEditorオブジェクトを作成
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // 新しいPDFドキュメントを作成
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // Annotation Editorは複数のPDFドキュメントから注釈をインポートできますが、
        // この例では1つのみを使用します。
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // 出力PDFを保存
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```