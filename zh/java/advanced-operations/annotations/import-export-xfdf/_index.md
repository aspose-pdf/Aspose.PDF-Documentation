---
title: 导入和导出注释到XFDF格式
linktitle: 导入和导出注释到XFDF格式
type: docs
weight: 40
url: zh/java/import-export-xfdf/
description: 您可以使用Aspose.PDF for Java库导入和导出XFDF格式的注释。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF代表XML Forms Data Format。这是一种基于XML的文件格式。该文件格式用于表示PDF表单中包含的表单数据或注释。XFDF可以用于许多不同的目的，但在我们的例子中，它可以用于发送或接收表单数据或注释到其他计算机或服务器等，或者用于存档表单数据或注释。在本文中，我们将看到Aspose.Pdf.Facades如何考虑这一概念，以及我们如何将注释数据导入和导出到XFDF文件。

{{% /alert %}}

**Aspose.PDF for Java** 是一个功能丰富的组件，用于编辑PDF文档。
 As we know XFDF 是 PDF 表单操作的重要方面，Aspose.PDF for Java 中的 Aspose.Pdf.Facades 命名空间对此考虑得很好，并提供了将注释数据导入和导出到 XFDF 文件的方法。

[PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 类包含两个方法，用于处理注释到 XFDF 文件的导入和导出。 [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 方法提供了将 PDF 文档中的注释导出到 XFDF 文件的功能，而 [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) 方法允许您从现有的 XFDF 文件导入注释。为了导入或导出注释，我们需要指定注释类型。我们可以以枚举的形式指定这些类型，然后将该枚举作为参数传递给这些方法中的任何一个。这样，只有指定类型的注释才会被导入或导出到 XFDF 文件。

以下代码片段展示了如何将注释导出到 XFDF 文件：

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * 从 XFDF 文件导入注释 XML Forms Data Format (XFDF) 文件
     * 由 Adobe Acrobat 创建的 PDF 制作应用程序；存储页面表单元素及其值的描述，例如文本字段的名称和值；
     * 用于保存可以导入到 PDF 文档中的表单数据。
     * 您可以使用 PdfAnnotationEditor 类中的 ImportAnnotationsFromXfdf 方法从 XFDF 文件导入注释数据。
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // 创建 PdfAnnotationEditor 对象
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // 将 PDF 文档绑定到注释编辑器
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // 导出注释
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

下面的代码片段描述了如何将注释导入到XFDF文件中：

```java
public static void ImportAnnotationXFDF()
{
    // 创建 PdfAnnotationEditor 对象
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // 创建一个新的 PDF 文档
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // 导入注释
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // 保存输出 PDF
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## 另一种一次性导出/导入注释的方法

在下面的代码中，ImportAnnotations 方法允许直接从另一个 PDF 文档导入注释。

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // 创建 PdfAnnotationEditor 对象
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // 创建一个新的 PDF 文档
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // 注释编辑器允许从多个 PDF 文档导入注释，
        // 但在此示例中，我们只使用一个。
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // 保存输出 PDF
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```