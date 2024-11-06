---
title: استخراج بيانات الجدول من PDF 
linktitle: استخراج بيانات الجدول 
type: docs
weight: 40
url: ar/java/extract-data-from-table-in-pdf/
description: تعلم كيفية استخراج البيانات الجدولية من PDF باستخدام Aspose.PDF for Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج الجداول من PDF برمجياً

استخراج الجداول من ملفات PDF ليس مهمة سهلة لأن الجدول يمكن أن يُنشأ بطرق مختلفة.

Aspose.PDF for Java لديه أداة لتسهيل استرجاع الجداول. لاستخراج بيانات الجدول، يجب عليك تنفيذ الخطوات التالية:

1. افتح المستند - أنشئ كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document);
1. أنشئ كائن [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber).

1. قرر أي الصفحات التي سيتم تحليلها وطبق [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) على الصفحات المطلوبة. سيتم فحص البيانات الجدولية، وسيتم حفظ النتيجة في قائمة من [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). يمكننا الحصول على هذه القائمة من خلال طريقة [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--).

2. للحصول على البيانات قم بالتكرار عبر `TableList` وتعامل مع قائمة [absorbed rows](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) وقائمة الخلايا المدمجة. يمكننا الوصول إلى القائمة الأولى عن طريق استدعاء طريقة [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) وإلى القائمة الثانية عن طريق استدعاء طريقة [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. يحتوي كل [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) على [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). يمكنك معالجته لأغراضك الخاصة.

يظهر المثال التالي استخراج جدول من جميع الصفحات:

```java
public static void Extract_Table() {
    // تحميل مستند PDF المصدر
    String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

    // فحص الصفحات
    for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
        absorber.visit(page);
        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            System.out.println("جدول");
            // التكرار على قائمة الصفوف
            for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                // التكرار على قائمة الخلايا
                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                    for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                        StringBuilder sb = new StringBuilder();
                        for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                            sb.append(seg.getText());
                        System.out.print(sb.toString() + "|");
                    }
                }
                System.out.println();
            }
        }
    }
}
```


## استخراج الجدول في منطقة محددة من صفحة PDF

كل جدول مستوعب يحتوي على خاصية [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable#getRectangle--) التي تصف موقع الجدول على الصفحة.

لذلك، إذا كنت بحاجة إلى استخراج الجداول الموجودة في منطقة معينة، يجب أن تعمل مع إحداثيات محددة.

المثال التالي يوضح كيفية استخراج جدول محدد بتعليق مربع:

```java
public static void Extract_Marked_Table() {
    // تحميل مستند PDF المصدر
    String filePath = "<... أدخل مسار ملف pdf هنا ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("الجداول المحددة غير موجودة..");
        return;
    }

    com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();
    absorber.visit(page);

    for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
        {
            boolean isInRegion = (squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                    && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                    && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                    && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

            if (isInRegion) {
                for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                    {
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb = new StringBuilder();
                                for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                                    sb.append(seg.getText());
                                System.out.print(sb.toString() + "|");
                            }
                        }
                        System.out.println();
                    }
                }
            }
        }
    }
}
```


## استخراج بيانات الجدول من PDF وتخزينها في ملف CSV

يوضح المثال التالي كيفية استخراج الجدول وتخزينه كملف CSV.
لرؤية كيفية تحويل PDF إلى جدول بيانات Excel، يرجى الرجوع إلى مقال [تحويل PDF إلى Excel](/pdf/java/convert-pdf-to-excel/).

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // تحميل مستند PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // إنشاء كائن خيار حفظ Excel
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // حفظ الخرج بتنسيق XLS
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```