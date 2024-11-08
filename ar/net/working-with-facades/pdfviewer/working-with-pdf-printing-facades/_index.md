---
title: العمل مع طباعة PDF - الواجهات
type: docs
weight: 10
url: /ar/net/working-with-pdf-printing-facades/
description: يشرح هذا القسم كيفية طباعة ملفات PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

## طباعة ملف PDF إلى الطابعة الافتراضية باستخدام إعدادات الطابعة والصفحة

أولاً يتم تحويل المستند إلى صورة ثم يتم طباعته على الطابعة. نقوم بإنشاء مثيل لفئة [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) التي تسمح لك بطباعة ملف PDF إلى الطابعة الافتراضية، باستخدام طريقة BindPdf للمستند عليها، وإجراء بعض الإعدادات. في مثالنا، نستخدم تنسيق A4، توجيه عمودي. في إعدادات الطابعة، أولاً وقبل كل شيء، نشير إلى اسم الطابعة التي نطبع عليها. أو سيتم الطباعة إلى الطابعة الافتراضية. بعد ذلك، نحدد عدد النسخ التي نحتاجها.

```csharp
 public static void PrintingPDFFile()
        {
            // إنشاء كائن PdfViewer
            PdfViewer viewer = new PdfViewer();

            // فتح ملف PDF المدخل
            viewer.BindPdf(_dataDir + "sample.pdf");

            // تعيين السمات للطباعة
            viewer.AutoResize = true;         // طباعة الملف بحجم معدل
            viewer.AutoRotate = true;         // طباعة الملف بتدوير معدل
            viewer.PrintPageDialog = false;   // عدم إنتاج حوار رقم الصفحة عند الطباعة

            // إنشاء كائنات لإعدادات الطابعة والصفحة وPrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
            System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

            // تعيين اسم الطابعة
            ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

            // تعيين حجم الصفحة (إذا لزم الأمر)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // تعيين هوامش الصفحة (إذا لزم الأمر)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // طباعة المستند باستخدام إعدادات الطابعة والصفحة
            viewer.PrintDocumentWithSettings(pgs, ps);

            // إغلاق ملف PDF بعد الطباعة
            viewer.Close();
        }
```

لعرض مربع حوار الطباعة، حاول استخدام مقتطف الشفرة التالي:

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // إنشاء كائن PdfViewer
            PdfViewer viewer = new PdfViewer();

            // فتح ملف PDF المدخل
            viewer.BindPdf(_dataDir + "sample.pdf");

            // تعيين الخصائص للطباعة
            viewer.AutoResize = true;         // طباعة الملف مع ضبط الحجم
            viewer.AutoRotate = true;         // طباعة الملف مع ضبط الدوران

            // إنشاء كائنات لإعدادات الطابعة والصفحة و PrintDocument

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // تعيين حجم الصفحة (إذا لزم الأمر)
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // تعيين هوامش الصفحة (إذا لزم الأمر)
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // كود طباعة المستند هنا
                // طباعة المستند باستخدام إعدادات الطابعة والصفحة
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // إغلاق ملف PDF بعد الطباعة
            viewer.Close();
        }
```

## طباعة PDF إلى طابعة افتراضية

هناك طابعات تطبع إلى ملف. نقوم بتعيين اسم الطابعة الافتراضية، وعن طريق القياس مع المثال السابق، نقوم بإجراء الإعدادات.

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // Create PdfViewer object
            PdfViewer viewer = new PdfViewer();

            // Open input PDF file
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Set attributes for printing
            viewer.AutoResize = true;         // Print the file with adjusted size
            viewer.AutoRotate = true;         // Print the file with adjusted rotation
            viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

            viewer.PrintAsImage = false;

            // Create objects for printer and page settings and PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Set printer name
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Or set the PDF printer
            //ps.PrinterName = "Adobe PDF";

            // Set PageSize (if required)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Set PageMargins (if required)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Print document using printer and page settings
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Close the PDF file after priting
            viewer.Close();
        }
```

## إخفاء مربع حوار الطباعة

يسمح لك Aspose.PDF for .NET بإخفاء مربع حوار الطباعة. لاستخدام ذلك، استخدم طريقة [PrintPageDialog](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog).

يوضح لك مقتطف الشيفرة التالي كيفية إخفاء مربع حوار الطباعة.

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // إنشاء كائن PdfViewer
            PdfViewer viewer = new PdfViewer();

            // فتح ملف PDF المدخل
            viewer.BindPdf(_dataDir + "sample.pdf");

            // تعيين الخصائص للطباعة
            viewer.AutoResize = true;         // طباعة الملف بالحجم المعدل
            viewer.AutoRotate = true;         // طباعة الملف بالتدوير المعدل


            viewer.PrintPageDialog = false;   // عدم إنتاج مربع حوار أرقام الصفحات عند الطباعة

            // إنشاء كائنات لإعدادات الطابعة والصفحة و PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // تعيين اسم طابعة XPS/PDF
            ps.PrinterName = "OneNote for Windows 10";

            // تعيين حجم الصفحة (إذا لزم الأمر)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // تعيين هوامش الصفحة (إذا لزم الأمر)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // طباعة المستند باستخدام إعدادات الطابعة والصفحة
            viewer.PrintDocumentWithSettings(pgs, ps);

            // إغلاق ملف PDF بعد الطباعة
            viewer.Close();
        }
```

## طباعة ملف PDF ملون إلى ملف XPS بتدرج الرمادي

يمكن طباعة مستند PDF ملون إلى طابعة XPS كتدرج رمادي باستخدام [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). لتحقيق ذلك تحتاج إلى استخدام خاصية PdfViewer.PrintAsGrayscale وتعيينها إلى *true*. يوضح مقتطف الشيفرة التالي تنفيذ خاصية PdfViewer.PrintAsGrayscale.

```csharp
public static void PrintingPDFasGrayscale()
        {
            // إنشاء كائن PdfViewer
            PdfViewer viewer = new PdfViewer();

            // فتح ملف PDF المدخل
            viewer.BindPdf(_dataDir + "sample.pdf");

            // تعيين السمات للطباعة
            viewer.AutoResize = true;         // طباعة الملف بحجم معدل
            viewer.AutoRotate = true;         // طباعة الملف بتدوير معدل

            viewer.PrintPageDialog = false;   // عدم إنتاج مربع حوار رقم الصفحة عند الطباعة
            viewer.PrintAsGrayscale = false;

            // إنشاء كائنات لإعدادات الطابعة والصفحة وPrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // تعيين اسم طابعة XPS/PDF
            ps.PrinterName = "OneNote for Windows 10";

            // تعيين حجم الصفحة (إذا لزم الأمر)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // تعيين هوامش الصفحة (إذا لزم الأمر)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // طباعة المستند باستخدام إعدادات الطابعة والصفحة
            viewer.PrintDocumentWithSettings(pgs, ps);

            // إغلاق ملف PDF بعد الطباعة
            viewer.Close();
        }
```

## تحويل PDF إلى PostScript

توفر فئة [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) القدرة على طباعة مستندات PDF وبمساعدة هذه الفئة، يمكننا أيضًا تحويل ملفات PDF إلى تنسيق PostScript. لتحويل ملف PDF إلى PostScript، قم أولاً بتثبيت أي طابعة PS واطبع الملف بمساعدة PdfViewer.

يظهر لك مقتطف التعليمات البرمجية التالي كيفية الطباعة والتحويل من PDF إلى تنسيق PostScript.

```csharp
public static void PrintingPDFToPostScript()
        {
            // إنشاء كائن PdfViewer
            PdfViewer viewer = new PdfViewer();

            // فتح ملف PDF المدخل
            viewer.BindPdf(_dataDir + "sample.pdf");

            // تعيين السمات للطباعة
            viewer.AutoResize = true;         // طباعة الملف بحجم معدل
            viewer.AutoRotate = true;         // طباعة الملف بتدوير معدل
            viewer.PrintPageDialog = false;   // عدم إنتاج مربع حوار رقم الصفحة عند الطباعة

            viewer.PrintAsImage = false;

            // إنشاء كائنات لإعدادات الطابعة والصفحة وPrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // تعيين اسم الطابعة XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // تعيين اسم الملف الناتج وميزة PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // تعيين PageSize (إذا لزم الأمر)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // تعيين PageMargins (إذا لزم الأمر)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // طباعة المستند باستخدام إعدادات الطابعة والصفحة
            viewer.PrintDocumentWithSettings(pgs, ps);

            // إغلاق ملف PDF بعد الطباعة
            viewer.Close();
        }
```

## التحقق من حالة وظيفة الطباعة

يمكن طباعة ملف PDF إلى طابعة مادية وكذلك إلى Microsoft XPS Document Writer، دون عرض مربع حوار الطباعة، باستخدام فئة [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). عند طباعة ملفات PDF كبيرة، قد تستغرق العملية وقتًا طويلًا لذلك قد لا يكون المستخدم متأكدًا مما إذا كانت عملية الطباعة قد اكتملت أو واجهت مشكلة. لتحديد حالة وظيفة الطباعة، استخدم خاصية PrintStatus. يُظهر لك مقطع الشيفرة التالي كيفية طباعة ملف PDF إلى ملف XPS والحصول على حالة الطباعة.

```csharp
public static void CheckingPrintJobStatus()
        {
            // إنشاء كائن PdfViewer
            PdfViewer viewer = new PdfViewer();

            // فتح ملف PDF المدخل
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // تعيين السمات للطباعة
            viewer.AutoResize = true;         // طباعة الملف بحجم معدل
            viewer.AutoRotate = true;         // طباعة الملف بتدوير معدل
            viewer.PrintPageDialog = false;   // عدم إنتاج مربع حوار رقم الصفحة عند الطباعة

            viewer.PrintAsImage = false;

            // إنشاء كائنات لإعدادات الطابعة والصفحة وPrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // تعيين اسم طابعة XPS/PDF
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // تعيين اسم الملف الناتج و خاصية PrintToFile
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // تعيين حجم الورق (إذا لزم الأمر)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // تعيين هوامش الصفحة (إذا لزم الأمر)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // طباعة المستند باستخدام إعدادات الطابعة والصفحة
            viewer.PrintDocumentWithSettings(pgs, ps);

            // التحقق من حالة الطباعة
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // لم يتم العثور على أخطاء. اكتملت وظيفة الطباعة بنجاح
                Console.WriteLine("اكتملت الطباعة دون أي مشكلة..");
            }

            // إغلاق ملف PDF بعد الطباعة
            viewer.Close();
        }

        struct PrintingJobSettings
        {
            public int ToPage { get; set; }
            public int FromPage { get; set; }
            public string OutputFile { get; set; }
            public System.Drawing.Printing.Duplex Mode { get; set; }
        }
```

## طباعة الصفحات في وضع Simplex وDuplex

في مهمة طباعة معينة، يمكن طباعة صفحات مستند PDF إما في وضع Duplex أو في وضع Simplex ولكن لا يمكنك طباعة بعض الصفحات كوضع simplex وبعض الصفحات كوضع duplex ضمن مهمة طباعة واحدة. ومع ذلك من أجل تحقيق المتطلبات، يمكن استخدام نطاقات صفحات مختلفة وكائن PrintingJobSettings. يوضح مقتطف الشيفرة التالي كيفية طباعة بعض صفحات ملف PDF في وضع Simplex وبعض الصفحات في وضع Duplex.

```csharp
 public static void PrintingPagesInSimplexAndDuplexMode()
        {
            int printingJobIndex = 0;
            string inPdf = _dataDir + "sample-8page.pdf";
            string output = _dataDir;
            IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

            PrintingJobSettings printingJob1 = new PrintingJobSettings
            {
                FromPage = 1,
                ToPage = 3,
                OutputFile = output + "sample_1_3.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob1);

            PrintingJobSettings printingJob2 = new PrintingJobSettings
            {
                FromPage = 4,
                ToPage = 6,
                OutputFile = output + "sample_4_6.xps",
                Mode = Duplex.Simplex
            };

            printingJobs.Add(printingJob2);

            PrintingJobSettings printingJob3 = new PrintingJobSettings
            {
                FromPage = 7,
                ToPage = 7,
                OutputFile = output + "sample_7.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob3);

            PdfViewer viewer = new PdfViewer();

            viewer.BindPdf(inPdf);
            viewer.AutoResize = true;
            viewer.AutoRotate = true;
            viewer.PrintPageDialog = false;

            PrinterSettings ps = new PrinterSettings();
            PageSettings pgs = new PageSettings();

            ps.PrinterName = "Microsoft XPS Document Writer";
            ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
            ps.PrintToFile = true;
            ps.FromPage = printingJobs[printingJobIndex].FromPage;
            ps.ToPage = printingJobs[printingJobIndex].ToPage;
            ps.Duplex = printingJobs[printingJobIndex].Mode;
            ps.PrintRange = PrintRange.SomePages;

            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
            ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            viewer.EndPrint += (sender, args) =>
            {
                if (++printingJobIndex < printingJobs.Count)
                {
                    ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                    ps.FromPage = printingJobs[printingJobIndex].FromPage;
                    ps.ToPage = printingJobs[printingJobIndex].ToPage;
                    ps.Duplex = printingJobs[printingJobIndex].Mode;
                    viewer.PrintDocumentWithSettings(pgs, ps);
                }
            };

            viewer.PrintDocumentWithSettings(pgs, ps);
        }
```