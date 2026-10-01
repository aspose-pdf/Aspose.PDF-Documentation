---
title: استخراج البيانات من جدول في PDF باستخدام Java
linktitle: استخراج البيانات من جدول
type: docs
weight: 40
url: /ar/java/extract-data-from-table-in-pdf/
description: تعلم كيفية استخراج بيانات الجداول من ملفات PDF باستخدام Aspose.PDF for Java وتصدير الجداول المكتشفة للمعالجة الإضافية.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج البيانات من جدول في PDF عبر Java
Abstract: تشرح هذه المقالة كيفية استخراج ومعالجة بيانات الجداول من مستندات PDF باستخدام Aspose.PDF for Java. تُظهر كيفية فحص الصفحات باستخدام `TableAbsorber`، وقراءة الصفوف والخلايا من الجداول المكتشفة، وتقييد الاستخراج إلى منطقة مشروحة محددة، وتصدير النتيجة إلى Excel.
---
## استخراج الجداول من PDF

استخدام `TableAbsorber` للعثور على الجداول في كل صفحة والتكرار عبر الصفوف والخلايا وقطاعات النص وقطعات النص.

1. افتح ملف PDF المصدر في a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. التكرار عبر المستند [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) الكائنات لأن الجداول تُكتشف صفحة بصفحة.
1. إنشاء [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) لكل صفحة واستدع `visit(page)` لتعبئة قائمة الجداول المكتشفة.
1. التنقل عبر المكتشف [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), و `TextSegment` الكائنات.
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

## استخراج جدول من منطقة محددة

هذا المثال يجد تعليقًا مربعًا، يقارن مستطيله بكل جدول مُكتشف، ويُخرج فقط الجداول داخل المنطقة المحددة.

1. افتح ملف PDF المصدر في a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. احصل على الهدف [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) وحدد المربع [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) الذي يحدد منطقة الاستخراج.
1. إنشاء [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) و استدع `visit(page)` لاكتشاف الجداول في تلك الصفحة.
1. قارن كل ما تم اكتشافه [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) مع حدود مستطيل التعليق التوضيحي.
1. التكرار عبر المطابقة [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) و [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) الكائنات وإعادة بناء نص الصف.
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

1. افتح ملف PDF المصدر في a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) مثال.
1. إنشاء [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) للتصدير.
1. ضبط تنسيق مخرجات Excel إلى `XLSX` لذا يتم كتابة تخطيط الجدول المكتشف كدفتر عمل Excel.
1. اتصال `document.save(outputFile.toString(), excelSave)` لتصدير المستند بصيغة Excel.

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
