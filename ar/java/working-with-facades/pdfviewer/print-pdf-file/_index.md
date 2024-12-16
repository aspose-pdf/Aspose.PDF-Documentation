---
title: العمل مع طباعة PDF
type: docs
weight: 10
url: /ar/java/print-pdf-file/
description: يشرح هذا القسم كيفية طباعة ملف PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfViewer.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## طباعة ملف PDF إلى الطابعة الافتراضية باستخدام إعدادات الطابعة والصفحة

تسمح لك فئة [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) بطباعة ملف PDF إلى الطابعة الافتراضية. لذلك تحتاج إلى إنشاء كائن [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) وفتح ملف PDF باستخدام الطريقة openPdfFile(..).

قم باستدعاء الطريقة printDocument(..) لطباعة ملف PDF إلى الطابعة الافتراضية.

يظهر مقتطف الشيفرة التالي كيفية طباعة ملف PDF إلى الطابعة الافتراضية مع إعدادات الطابعة والصفحة.

```java
 public static void PrintingPDFFile() {
        // إنشاء كائن PdfViewer
        PdfViewer viewer = new PdfViewer();

        // فتح ملف PDF المدخل
        viewer.bindPdf(_dataDir + "sample.pdf");

        // تعيين السمات للطباعة
        viewer.setAutoResize(true); // طباعة الملف بحجم معدل
        viewer.setAutoRotate(true); // طباعة الملف بتدوير معدل
        viewer.setPrintPageDialog(false); // عدم إنتاج حوار رقم الصفحة عند الطباعة

        // إنشاء كائنات لإعدادات الطابعة والصفحة وPrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // تعيين اسم الطابعة
        printerSettings.setPrinterName("Microsoft Print to PDF");
        

        // تعيين حجم الصفحة (إذا لزم الأمر)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // تعيين هوامش الصفحة (إذا لزم الأمر)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // طباعة المستند باستخدام إعدادات الطابعة والصفحة
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // إغلاق ملف PDF بعد الطباعة
        viewer.close();
    }
```


من أجل عرض مربع حوار الطباعة، حاول استخدام شفرة الكود التالية:

```java
public static void PrintingPDFDisplayPrintDialog() {
        // إنشاء كائن PdfViewer
        PdfViewer viewer = new PdfViewer();

        // فتح ملف PDF المدخل
        viewer.bindPdf(_dataDir + "sample.pdf");

        // ضبط السمات للطباعة
        viewer.setAutoResize(true); // طباعة الملف بالحجم المعدل
        viewer.setAutoRotate(true); // طباعة الملف بالدوران المعدل
        viewer.setPrintPageDialog(true);

        // إنشاء كائنات لإعدادات الطابعة والصفحة وPrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // ضبط حجم الصفحة (إذا لزم الأمر)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // ضبط هوامش الصفحة (إذا لزم الأمر)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // طباعة المستند باستخدام إعدادات الطابعة والصفحة
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // إغلاق ملف PDF بعد الطباعة
        viewer.close();
    }
```


## طباعة PDF إلى طابعة افتراضية

هناك طابعات تطبع إلى ملف. نقوم بتعيين اسم الطابعة الافتراضية، وبالتشابه مع المثال السابق، نقوم بإجراء الإعدادات.

```java
public static void PrintingPDFToSoftPrinter() {
        // إنشاء كائن PdfViewer
        PdfViewer viewer = new PdfViewer();

        // فتح ملف PDF المدخل
        viewer.bindPdf(_dataDir + "sample.pdf");

        // تعيين السمات للطباعة
        viewer.setAutoResize(true); // طباعة الملف بالحجم المعدل
        viewer.setAutoRotate(true); // طباعة الملف بالتدوير المعدل
        viewer.setPrintPageDialog(false); // عدم إنتاج مربع حوار رقم الصفحة عند الطباعة

        // إنشاء كائنات للطابعة وإعدادات الصفحة وPrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // تعيين الطابعة Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // أو Adobe
        // printerSettings.setPrinterName("Adobe PDF");

        // تعيين حجم الصفحة (إذا لزم الأمر)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // تعيين هوامش الصفحة (إذا لزم الأمر)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // طباعة المستند باستخدام إعدادات الطابعة والصفحة
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // إغلاق ملف PDF بعد الطباعة
        viewer.close();
    }
```


## إخفاء مربع حوار الطباعة

تتيح لك Aspose.PDF for Java إخفاء مربع حوار الطباعة. لاستخدام هذه الميزة، استخدم طريقة [getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--).

يوضح لك مقطع الكود التالي كيفية إخفاء مربع حوار الطباعة.

```java
public static void PrintingPDFHidePrintDialog() {
        // إنشاء كائن PdfViewer
        PdfViewer viewer = new PdfViewer();

        // فتح ملف PDF المدخل
        viewer.bindPdf(_dataDir + "sample.pdf");

        // تعيين الخصائص للطباعة
        viewer.setAutoResize(true); // طباعة الملف بحجم معدل
        viewer.setAutoRotate(true); // طباعة الملف بتدوير معدل

        viewer.setPrintPageDialog(false); // عدم إنتاج مربع حوار رقم الصفحة عند الطباعة

        // إنشاء كائنات لإعدادات الطابعة والصفحة و PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // تعيين الطابعة Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // تعيين حجم الصفحة (إذا لزم الأمر)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // تعيين هوامش الصفحة (إذا لزم الأمر)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // طباعة المستند باستخدام إعدادات الطابعة والصفحة
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // إغلاق ملف PDF بعد الطباعة
        viewer.close();
    }
```


## طباعة ملف PDF ملون إلى ملف XPS كدرجات رمادية

يمكن طباعة مستند PDF ملون إلى طابعة XPS كدرجات رمادية، باستخدام [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). لتحقيق ذلك، تحتاج إلى استخدام الخاصية PdfViewer.PrintAsGrayscale وتعيينها إلى *true*.

يوضح مقطع الشيفرة التالي تنفيذ خاصية PdfViewer.PrintAsGrayscale.

```java
 public static void PrintingPDFasGrayscale() {
        // إنشاء كائن PdfViewer
        PdfViewer viewer = new PdfViewer();

        // فتح ملف PDF المدخل
        viewer.bindPdf(_dataDir + "sample.pdf");

        // تعيين السمات للطباعة
        viewer.setAutoResize(true); // طباعة الملف بحجم معدل
        viewer.setAutoRotate(true); // طباعة الملف بتدوير معدل

        viewer.setPrintAsGrayscale(true);

        // إنشاء كائنات لإعدادات الطابعة والصفحة و PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // تعيين الطابعة إلى Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // تعيين حجم الصفحة (إذا لزم الأمر)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // تعيين هوامش الصفحة (إذا لزم الأمر)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // طباعة المستند باستخدام إعدادات الطابعة والصفحة
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // إغلاق ملف PDF بعد الطباعة
        viewer.close();
    }
```


## تحويل PDF إلى PostScript

تتيح فئة [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) إمكانية طباعة مستندات PDF ومع مساعدة هذه الفئة، يمكننا أيضًا تحويل ملفات PDF إلى تنسيق PostScript. لتحويل ملف PDF إلى PostScript، قم أولاً بتثبيت أي طابعة PS واطبع الملف بمساعدة PdfViewer.

يوضح لك مقطع الشيفرة التالي كيفية الطباعة والتحويل من PDF إلى تنسيق PostScript.

```java
public static void PrintingPDFToPostScript() {
        // إنشاء كائن PdfViewer
        PdfViewer viewer = new PdfViewer();

        // فتح ملف PDF الإدخال
        viewer.bindPdf(_dataDir + "sample.pdf");

        // تعيين السمات للطباعة
        viewer.setAutoResize(true); // طباعة الملف بحجم معدل
        viewer.setAutoRotate(true); // طباعة الملف بتدوير معدل

        viewer.setPrintAsGrayscale(true);
        

        // إنشاء كائنات لإعدادات الطابعة والصفحة وPrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // تعيين طابعة PostSScript
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // تعيين حجم الصفحة (إذا لزم الأمر)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // تعيين هوامش الصفحة (إذا لزم الأمر)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // طباعة المستند باستخدام إعدادات الطابعة والصفحة
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // إغلاق ملف PDF بعد الطباعة
        viewer.close();
    }
```


## التحقق من حالة مهمة الطباعة

يمكن طباعة ملف PDF على طابعة فعلية وكذلك على كاتب مستندات Microsoft XPS، دون إظهار مربع حوار الطباعة، باستخدام فئة [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). عند طباعة ملفات PDF كبيرة، قد تستغرق العملية وقتًا طويلاً لذلك قد لا يكون المستخدم متأكدًا مما إذا كانت عملية الطباعة قد اكتملت أو واجهت مشكلة. لتحديد حالة مهمة الطباعة، استخدم خاصية PrintStatus. يوضح لك مقطع الشيفرة التالي كيفية طباعة ملف PDF إلى ملف XPS والحصول على حالة الطباعة.

```java
public static void CheckingPrintJobStatus() {
        // إنشاء كائن PdfViewer
        PdfViewer viewer = new PdfViewer();

        // فتح ملف PDF المدخل
        viewer.bindPdf(_dataDir + "sample.pdf");

        // تعيين السمات للطباعة
        viewer.setAutoResize(true); // طباعة الملف مع ضبط الحجم
        viewer.setAutoRotate(true); // طباعة الملف مع ضبط الدوران

        viewer.setPrintAsGrayscale(true);

        // إنشاء كائنات لإعدادات الطابعة والصفحة وPrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // تعيين طابعة Microsoft Soft Printer
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // تعيين حجم الصفحة (إذا لزم الأمر)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // تعيين هوامش الصفحة (إذا لزم الأمر)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // طباعة المستند باستخدام إعدادات الطابعة والصفحة
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // // التحقق من حالة الطباعة
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // لم يتم العثور على أي أخطاء. لقد اكتملت مهمة الطباعة بنجاح
            System.out.println("Everything went OK!");
        }
        // إغلاق ملف PDF بعد الطباعة
        viewer.close();
    }
```