---
title: استخراج الجداول من PDF في Java
linktitle: استخراج جدول
type: docs
weight: 20
url: /ar/java/extracting-table/
description: تعلم كيفية استخراج بيانات الجدول من مستندات PDF الموجودة باستخدام Java.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج بيانات الجدول من ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية استخراج الجداول من مستندات PDF باستخدام Aspose.PDF for Java. تُظهر كيفية استخدام TableAbsorber لاكتشاف الجداول حسب الصفحة، وتكرار الصفوف والخلايا، وجمع نص الخلية للمعالجة اللاحقة.
---
استخدام `TableAbsorber` عند الحاجة إلى اكتشاف هياكل الجداول في ملف PDF موجود وقراءة محتواها.

## استخراج النص من الجداول المكتشفة

استخدم هذا المثال عندما تحتاج إلى تحديد مواقع الجداول في كل صفحة وجمع نص الخلايا الخاصة بها.

1. فتح ملف PDF المصدر [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. زيارة كل صفحة باستخدام [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. تصفح الجداول والصفوف والخلايا التي تم امتصاصها، ثم قم بإخراج النص المستخرج.

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    System.out.println("Row:");
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            for (TextSegment segment : fragment.getSegments()) {
                                cellText.append(segment.getText());
                            }
                        }
                        rowText.append(" | ").append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```
