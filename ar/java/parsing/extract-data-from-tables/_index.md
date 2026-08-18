---
title: استخراج البيانات من الجدول في PDF باستخدام Java
linktitle: استخراج البيانات من الجدول
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: تعرف على كيفية استخراج بيانات الجدول من ملفات PDF باستخدام Aspose.PDF لـ Java وتصدير الجداول المكتشفة لمزيد من المعالجة.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج البيانات من الجدول في PDF عبر جافا
Abstract: تشرح هذه المقالة كيفية استخراج بيانات الجدول ومعالجتها من مستندات PDF باستخدام Aspose.PDF لـ Java. فهو يوضح كيفية مسح الصفحات ضوئيًا باستخدام `TableAbsorber`، وقراءة الصفوف والخلايا من الجداول المكتشفة، وقصر الاستخراج على منطقة مشروحة معينة، وتصدير النتيجة إلى Excel.
---
## استخراج الجداول من PDF

استخدم `TableAbsorber` للعثور على الجداول في كل صفحة والتكرار عبر الصفوف والخلايا وأجزاء النص ومقاطع النص.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بالتكرار عبر كائنات المستند [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) لأنه يتم اكتشاف الجداول صفحة تلو الأخرى.
1. أنشئ [TableAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) لكل صفحة واتصل بـ`visit(page)` لملء قائمة الجداول المكتشفة.
1. قم بالتكرار من خلال الكائنات [AbsortedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) و[AbsortedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) و[AbsortedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) و[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) و`TextSegment` التي تم اكتشافها.
1. أنشئ نص الصف المستخرج من محتوى الجزء واطبع بيانات الجدول.

```java
public static void extractTablesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);

            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## استخراج جدول من منطقة محددة محددة

يبحث هذا المثال عن تعليق توضيحي مربع، ويقارن مستطيله بكل جدول تم اكتشافه، ويخرج الجداول فقط داخل المنطقة المحددة.

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. احصل على الهدف [الصفحة](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وحدد المربع [التعليق التوضيحي](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) الذي يمثل منطقة الاستخراج.
1. أنشئ [TableAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) واتصل بـ`visit(page)` لاكتشاف الجداول الموجودة في تلك الصفحة.
1. قارن كل [AbsortedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [مستطيل](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) المكتشف مع حدود مستطيل التعليقات التوضيحية.
1. قم بالمراجعة من خلال كائنات [AbsortedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) و[AbsortedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) المتطابقة وأعد إنشاء نص الصف.
1. اطبع بيانات الجدول للمنطقة المحددة فقط.

```java
public static void extractTableFromSpecificArea(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Annotation squareAnnotation = null;
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                squareAnnotation = annotation;
                break;
            }
        }

        if (squareAnnotation == null) {
            System.out.println("No square annotation found.");
            return;
        }

        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(page);

        for (AbsorbedTable table : absorber.getTableList()) {
            Rectangle tableRect = table.getRectangle();
            Rectangle annotationRect = squareAnnotation.getRect();

            boolean isInRegion = annotationRect.getLLX() < tableRect.getLLX()
                    && annotationRect.getLLY() < tableRect.getLLY()
                    && annotationRect.getURX() > tableRect.getURX()
                    && annotationRect.getURY() > tableRect.getURY();

            if (isInRegion) {
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## تصدير الجداول إلى Excel

1. افتح ملف PDF المصدر في مثيل [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بإنشاء [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) للتصدير.
1. قم بتعيين تنسيق إخراج Excel على `XLSX` بحيث تتم كتابة تخطيط الجدول المكتشف كمصنف Excel.
1. اتصل بـ `document.save(outputFile.toString(), excelSave)` لتصدير المستند بتنسيق Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
