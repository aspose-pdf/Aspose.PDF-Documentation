---
title: دمج جداول PDF مع مصادر البيانات في Java
linktitle: دمج الجدول
type: docs
weight: 30
url: /java/integrate-table/
description: تعرف على كيفية دمج جداول PDF مع مصادر البيانات المنظمة مثل ملفات CSV في Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أنشئ جداول PDF من بيانات منظمة باستخدام Java
Abstract: تشرح هذه المقالة كيفية دمج جداول PDF مع البيانات الخارجية باستخدام Aspose.PDF لـ Java. وهو يغطي قراءة بيانات CSV، واختيار أعمدة معينة، وإنشاء كائن جدول منسق من الصفوف التي تم تحليلها، وتقديم النتيجة إلى مستند PDF.
---
يقوم مثال Java بإنشاء جداول PDF من بيانات CSV دون الاعتماد على مكتبات إطار البيانات الخارجية.

## إنشاء جدول من صفوف CSV

استخدم هذا المثال عندما يجب تحويل أعمدة CSV المحددة إلى جدول PDF ذو نمط.

1. قم بإنشاء [جدول](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) وقم بتكوين حدوده.
1. اكتشف فهارس الأعمدة المطلوبة من صف رأس CSV.
1. قم بإضافة صف الرأس والعدد المطلوب من صفوف البيانات، ثم قم بإرجاع الجدول.

```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    headerRow.setRowBroken(false);
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    int limit = Math.min(maxRows, rows.size() - 1);
    for (int rowIndex = 1; rowIndex <= limit; rowIndex++) {
        Row row = table.getRows().add();
        String[] rowData = rows.get(rowIndex);
        for (int columnIndex : selectedColumns) {
            row.getCells().add(columnIndex < rowData.length ? rowData[columnIndex] : "");
        }
    }

    return table;
}
```

## إنشاء ملف PDF من بيانات CSV

استخدم هذا المثال عندما يجب أن يتم عرض إدخال CSV كمستند جدول PDF.

1. اقرأ صفوف CSV من ملف الإدخال.
1. قم بمعاينة مجموعة فرعية من الصفوف التي تم تحليلها في وحدة التحكم.
1. أنشئ ملف PDF [مستند](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)، وأضف الجدول الذي تم إنشاؤه، واحفظ ملف الإخراج.

```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);
    for (int i = 0; i < Math.min(20, rows.size()); i++) {
        System.out.println(String.join(" | ", rows.get(i)));
    }

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```

## ابحث عن فهارس أعمدة CSV بالاسم

استخدم هذا المساعد عندما يجب أن تكون هناك أعمدة محددة محددة في صف رأس CSV.

1. قم بالتكرار من خلال أسماء الأعمدة المطلوبة.
1. ابحث في صف الرأس عن الفهارس المطابقة.
1. قم بإرجاع مواضع الأعمدة المجمعة.

```java
private static int[] findColumns(String[] header, String... names) {
    int[] indexes = new int[names.length];
    for (int i = 0; i < names.length; i++) {
        indexes[i] = 0;
        for (int j = 0; j < header.length; j++) {
            if (names[i].equals(header[j])) {
                indexes[i] = j;
                break;
            }
        }
    }
    return indexes;
}
```

## قراءة صفوف CSV من ملف

استخدم هذا المساعد عندما يجب تحميل مصدر CSV في الذاكرة قبل إنشاء الجدول.

1. قراءة كافة الأسطر من ملف الإدخال.
1. قم بتقسيم كل سطر باستخدام مساعد محلل CSV.
1. إرجاع قيم الصف المجمعة.

```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## قم بتقسيم سطر CSV واحد إلى قيم

استخدم هذا المساعد عندما قد يحتوي صف CSV على قيم بين علامات الاقتباس وأحرف الاقتباس التي تم تجاوزها.

1. التكرار من خلال الأحرف الموجودة في السطر.
1. تتبع ما إذا كان المحلل اللغوي موجودًا حاليًا داخل النص المقتبس.
1. أنشئ قائمة القيم النهائية وأعدها كمصفوفة.

```java
private static String[] splitCsvLine(String line) {
    List<String> values = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    boolean inQuotes = false;
    for (int i = 0; i < line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '"') {
            if (inQuotes && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                current.append('"');
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (ch == ',' && !inQuotes) {
            values.add(current.toString());
            current.setLength(0);
        } else {
            current.append(ch);
        }
    }
    values.add(current.toString());
    return values.toArray(String[]::new);
}
```
