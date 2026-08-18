---
title: استخراج الجداول من PDF في جافا
linktitle: استخراج الجدول
type: docs
weight: 20
url: /java/extracting-table/
description: تعرف على كيفية استخراج بيانات الجدول من مستندات PDF الموجودة في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج بيانات الجدول من ملفات PDF باستخدام Java
Abstract: تشرح هذه المقالة كيفية استخراج الجداول من مستندات PDF باستخدام Aspose.PDF لـ Java. ويوضح كيفية استخدام TableAbsorter لاكتشاف الجداول حسب الصفحة، وتكرار الصفوف والخلايا، وجمع نص الخلية للمعالجة النهائية.
---
استخدم `TableAbsorber` عندما تحتاج إلى اكتشاف بنيات الجدول في ملف PDF موجود وقراءة محتواها.

## استخراج النص من الجداول المكتشفة

استخدم هذا المثال عندما تحتاج إلى تحديد موقع الجداول في كل صفحة وجمع نص الخلية الخاص بها.

1. افتح ملف PDF المصدر [المستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. قم بزيارة كل صفحة باستخدام [TableAbsorter](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/).
1. قم بالتكرار عبر الجداول والصفوف والخلايا الممتصة، ثم قم بإخراج النص المستخرج.

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
