---
title: Импорт и экспорт аннотаций в формате XFDF
linktitle: Импорт и экспорт аннотаций в формате XFDF
type: docs
weight: 40
url: /ru/java/import-export-xfdf/
description: Вы можете импортировать и экспортировать аннотации в формате XFDF, используя библиотеку Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

XFDF означает XML Forms Data Format. Это формат файла на основе XML. Этот формат файла используется для представления данных формы или аннотаций, содержащихся в PDF-форме. XFDF может использоваться для многих различных целей, но в нашем случае он может использоваться для отправки или получения данных формы или аннотаций на другие компьютеры или серверы и т. д., или он может использоваться для архивирования данных формы или аннотаций. В этой статье мы рассмотрим, как Aspose.Pdf.Facades учел эту концепцию и как мы можем импортировать и экспортировать данные аннотаций в файл XFDF.

{{% /alert %}}

**Aspose.PDF для Java** — это компонент, богатый функциями редактирования PDF-документов.
 As we know XFDF является важным аспектом манипуляции с PDF-формами, пространство имен Aspose.Pdf.Facades в Aspose.PDF для Java учло это очень хорошо и предоставило методы для импорта и экспорта данных аннотаций в файлы XFDF.

Класс [PDFAnnotationEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) содержит два метода для работы с импортом и экспортом аннотаций в файл XFDF. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) метод предоставляет функциональность для экспорта аннотаций из PDF документа в файл XFDF, в то время как [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfAnnotationEditor) метод позволяет импортировать аннотации из существующего файла XFDF. Чтобы импортировать или экспортировать аннотации, нам необходимо указать типы аннотаций. Мы можем указать эти типы в виде перечисления, а затем передать это перечисление в качестве аргумента в любой из этих методов. Таким образом, аннотации указанных типов будут импортированы или экспортированы только в файл XFDF.

Следующий фрагмент кода показывает, как экспортировать аннотации в файл XFDF:

```java
package com.aspose.pdf.examples;

import java.io.FileOutputStream;
import java.io.IOException;
import com.aspose.pdf.*;
import com.aspose.pdf.facades.PdfAnnotationEditor;

public class ExampleAnnotationImportExport {
    // Путь к директории с документами.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    /*
     * Импорт аннотаций из файла XFDF XML Forms Data Format (XFDF) файл,
     * созданный с помощью Adobe Acrobat, приложения для создания PDF; хранит описания
     * элементов формы страницы и их значения, такие как имена и значения для текстовых
     * полей; используется для сохранения данных формы, которые могут быть импортированы в PDF документ.
     * Вы можете импортировать данные аннотаций из файла XFDF в PDF, используя
     * метод ImportAnnotationsFromXfdf в классе PdfAnnotationEditor.
     */

    public static void ExportAnnotationXFDF() throws IOException {
        // Создать объект PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

        // Привязать PDF документ к редактору аннотаций
        AnnotationEditor.bindPdf(_dataDir + "AnnotationDemo1.pdf");

        // Экспортировать аннотации
        FileOutputStream fileStream = new FileOutputStream(_dataDir + "exportannotations.xfdf");
        int[] annotType = { AnnotationType.Line, AnnotationType.Square };
        AnnotationEditor.exportAnnotationsXfdf(fileStream, 1, 1, annotType);
        fileStream.flush();
        fileStream.close();
    }
```

Следующий фрагмент кода описывает, как импортировать аннотации в файл XFDF:

```java
public static void ImportAnnotationXFDF()
{
    // Создать объект PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // Создать новый PDF документ
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // Импортировать аннотацию
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // Сохранить выходной PDF
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## Еще один способ экспортировать/импортировать аннотации сразу

В коде ниже метод ImportAnnotations позволяет импортировать аннотации непосредственно из другого PDF документа.

```java
    public static void ImportAnnotationFromPDF() throws IOException {
        // Создать объект PdfAnnotationEditor
        PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
        // Создать новый PDF документ
        Document document = new Document();

        document.getPages().add();
        AnnotationEditor.bindPdf(document);
        String exportFileName = _dataDir + "exportannotations.xfdf";
        java.io.File f = new java.io.File(exportFileName);
        if (!f.exists()) {
            ExportAnnotationXFDF();
        }

        // Редактор аннотаций позволяет импортировать аннотации из нескольких PDF документов,
        // но в этом примере мы используем только один.
        String[] fileNames = { _dataDir + "AnnotationDemo1.pdf" };
        AnnotationEditor.importAnnotations(fileNames);

        // Сохранить выходной PDF
        document.save(_dataDir + "AnnotationDemo3.pdf");
    }
}
```