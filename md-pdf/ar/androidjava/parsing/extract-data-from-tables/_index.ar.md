---
title: استخراج بيانات الجدول من PDF 
linktitle: استخراج بيانات الجدول
type: docs
weight: 40
url: /androidjava/extract-data-from-table-in-pdf/
description: تعلّم كيفية استخراج الجداول من PDF باستخدام Aspose.PDF لنظام Android عبر Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## استخراج الجداول من PDF برمجياً

استخراج الجداول من ملفات PDF ليس مهمة سهلة لأن الجدول يمكن أن يتم إنشاؤه بطرق مختلفة.

يحتوي Aspose.PDF لنظام Android عبر Java على أداة لتسهيل استرجاع الجداول. لاستخراج بيانات الجدول، يجب عليك تنفيذ الخطوات التالية:

1. فتح المستند - إنشاء كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document);
1. إنشاء كائن [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber).

1. قرر أي الصفحات سيتم تحليلها وتطبيق [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) على الصفحات المطلوبة. سيتم مسح البيانات الجدولية، وسيتم حفظ النتيجة في قائمة من [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). يمكننا الحصول على هذه القائمة من خلال طريقة [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--).

1. للحصول على البيانات قم بالتكرار عبر `TableList` وتعامل مع قائمة [absorbed rows](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) وقائمة من الخلايا الممتصة. يمكننا الوصول إلى القائمة الأولى عن طريق استدعاء طريقة [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) وإلى الثانية عن طريق استدعاء طريقة [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. تحتوي كل [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) على [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). يمكنك معالجته لأغراضك الخاصة.

المثال التالي يوضح استخراج الجدول من جميع الصفحات:

```java
public void extractTable () {
        // افتح المستند
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();

        File file=new File(fileStorage, "extracted-text.txt");
        FileOutputStream fileOutputStream;

        try {
            fileOutputStream=new FileOutputStream(file);

        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
        // مسح الصفحات
        for (Page page : (Iterable<? extends Page>) document.getPages()) {
            absorber.visit(page);
            for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
                try {
                    bw.write("Table");
                    bw.newLine();
                    // التكرار عبر قائمة الصفوف
                    for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                        // التكرار عبر قائمة الخلايا
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb=new StringBuilder();
                                for (TextSegment seg :
                                        (Iterable<? extends TextSegment>) fragment.getSegments())
                                    sb.append(seg.getText());
                                bw.write(sb.toString() + "|");
                            }
                        }
                        bw.newLine();
                    }
                } catch (IOException e) {
                    resultMessage.setText(e.getMessage());
                    return;
                }
            }
        }
        try {
            bw.close();
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## استخراج الجدول في منطقة محددة من صفحة PDF

كل جدول مستوعب يحتوي على خاصية [Rectangle](https://reference.aspose.com/pdf/java/aspose.pdf.text/absorbedtable/properties/rectangle) التي تصف موقع الجدول على الصفحة.

لذلك، إذا كنت بحاجة لاستخراج الجداول الموجودة في منطقة محددة، عليك العمل مع إحداثيات معينة.

المثال التالي يوضح كيفية استخراج جدول محدد بتعليق مربع:

```java
public void extractMarkedTable () {
        // فتح المستند
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        com.aspose.pdf.Page page=document.getPages().get_Item(1);

        com.aspose.pdf.AnnotationSelector annotationSelector=
                new com.aspose.pdf.AnnotationSelector(
                        new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

        List list=annotationSelector.getSelected();
        if (list.size() == 0) {
            resultMessage.setText("لم يتم العثور على الجداول المحددة..");
            return;
        }

        com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

        com.aspose.pdf.TableAbsorber absorber=new com.aspose.pdf.TableAbsorber();
        absorber.visit(page);

        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            {
                boolean isInRegion=(squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                        && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                        && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                        && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

                if (isInRegion) {
                    File file=new File(fileStorage, "extracted-text.txt");
                    FileOutputStream fileOutputStream;

                    try {
                        fileOutputStream=new FileOutputStream(file);

                    } catch (FileNotFoundException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }

                    BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(fileOutputStream));
                    try {
                        //تحليل الجدول
                        for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                            {
                                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                                    for (com.aspose.pdf.TextFragment fragment :
                                            cell.getTextFragments()) {
                                        bw.write(fragment.getText());
                                    }
                                    bw.write("|");
                                }
                                bw.newLine();
                            }
                        }
                        bw.close();
                        // -------------
                    } catch (IOException e) {
                        resultMessage.setText(e.getMessage());
                        return;
                    }
                    resultMessage.setText(R.string.success_message);
                }
            }
        }
    }
```


## استخراج بيانات الجدول من PDF وتخزينها في ملف CSV

يوضح المثال التالي كيفية استخراج الجدول وتخزينه كملف CSV. لرؤية كيفية تحويل PDF إلى جدول بيانات Excel يرجى الرجوع إلى مقالة [تحويل PDF إلى Excel](/pdf/java/convert-pdf-to-excel/).

```java
 public void extractTableSaveCSV () {
        // فتح المستند
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        File file=new File(fileStorage, "PDFToXLS_out.csv");
        // إنشاء كائن ExcelSave Option
        com.aspose.pdf.ExcelSaveOptions excelSave=new com.aspose.pdf.ExcelSaveOptions();
        excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);
        try {
            document.save(file.toString(), excelSave);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```