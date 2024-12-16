---
title: دمج مستندات PDF
type: docs
weight: 10
url: /ar/java/concatenate-pdf-documents/
description: يشرح هذا القسم كيفية دمج مستندات PDF باستخدام com.aspose.pdf.facades باستخدام فئة PdfFileEditor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## دمج ملفات PDF باستخدام مسارات الملفات (Facades)

يمكن استخدام طريقة concatenate لفئة [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) لدمج ملفين PDF. تتيح لك طريقة concatenate تمرير ثلاثة معلمات: ملف PDF الأول المدخل، ملف PDF الثاني المدخل، وملف PDF الناتج. يحتوي ملف PDF النهائي على كلا ملفي PDF المدخلين.

يظهر لك مقتطف الشيفرة التالي كيفية دمج ملفات PDF باستخدام مسارات الملفات.

```java
    public static void ConcatenatePDFfilesUsingFilePaths01() {
        // إنشاء كائن PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // دمج الملفات
        pdfEditor.concatenate(_dataDir + "Sample-Document-01.pdf", _dataDir + "Sample-Document-02.pdf",
                _dataDir + "Concatenate_Result_01.pdf");
    }
```


في بعض الحالات، عندما يكون هناك الكثير من المخططات التفصيلية، قد يقوم المستخدمون بتعطيلها عن طريق ضبط **CopyOutlines** على false وتحسين أداء الدمج.

```java
  public static void ConcatenatePDFfilesUsingFilePaths02() {
        // إنشاء كائن PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // دمج الملفات
        String[] inputFiles = Directory.GetFiles(_dataDir, "Sample-Document-0?.pdf");
        pdfEditor.CopyOutlines = false;
        var res = pdfEditor.Concatenate(inputFiles, _dataDir + "Concatenate_Result_02.pdf");
        Console.WriteLine(res);
    }

```

## دمج ملفات PDF متعددة باستخدام MemoryStreams

[Concatenate]https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#concatenate-com.aspose.pdf.IDocument:A-com.aspose.pdf.IDocument-) طريقة [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) تأخذ ملفات PDF المصدر وملف PDF الوجهة كمعاملات.
 هذه المعاملات يمكن أن تكون إما مسارات لملفات PDF على القرص أو يمكن أن تكون MemoryStreams. الآن، في هذا المثال، سنقوم أولاً بإنشاء تدفقين للملفات لقراءة ملفات PDF من القرص. ثم سنقوم بتحويل هذه الملفات إلى مصفوفات بايت. سيتم تحويل مصفوفات البايت هذه لملفات PDF إلى MemoryStreams. بمجرد الحصول على MemoryStreams من ملفات PDF، سنكون قادرين على تمريرها إلى طريقة الدمج ودمجها في ملف إخراج واحد.

يظهر لك مقطع الشيفرة التالي كيفية دمج ملفات PDF متعددة باستخدام MemoryStreams:

```java
    public static void ConcatenateMultiplePDFfilesUsingMemoryStreams()
        {
            // إنشاء تدفقين للملفات لقراءة ملفات PDF
            FileInputStream fs1 = new FileInputStream(_dataDir + "Sample-Document-01.pdf");
            FileInputStream fs2 = new FileInputStream(_dataDir + "Sample-Document-02.pdf");

            // إنشاء مصفوفات بايت للاحتفاظ بمحتويات ملفات PDF
            byte[] buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            byte[] buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            // قراءة محتويات ملف PDF في مصفوفات بايت
            fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // الآن، أولاً تحويل مصفوفات البايت إلى MemoryStreams ومن ثم دمج تلك التدفقات
            using (MemoryStream pdfStream = new MemoryStream())
            {
                using (MemoryStream fileStream1 = new MemoryStream(buffer1))
                {
                    using (MemoryStream fileStream2 = new MemoryStream(buffer2))
                    {
                        // إنشاء مثيل لفئة PdfFileEditor لدمج التدفقات
                        PdfFileEditor pdfEditor = new PdfFileEditor();
                        // دمج كلا MemoryStreams المدخلات وحفظها في MemoryStream المخرجات
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // تحويل MemoryStream مرة أخرى إلى مصفوفة بايت
                        byte[] data = pdfStream.ToArray();
                        // إنشاء FileStream لحفظ ملف PDF الناتج
                        FileStream output = new FileStream(_dataDir + "Concatenate_Result_03.pdf", FileMode.Create,
                        FileAccess.Write);
                        // كتابة محتويات مصفوفة البايت في تدفق ملف الإخراج
                        output.Write(data, 0, data.Length);
                        // إغلاق ملف الخرج
                        output.Close();
                    }
                }
            }
            // إغلاق الملفات المدخلة
            fs1.Close();
            fs2.Close();
        }
```

## دمج مصفوفة من ملفات PDF باستخدام مسارات الملفات (الواجهات)

إذا كنت ترغب في دمج ملفات PDF متعددة، يمكنك استخدام التحميل الزائد لطريقة الدمج، التي تتيح لك تمرير مصفوفة من مسارات ملفات PDF. يتم حفظ النتيجة النهائية كملف مدمج تم إنشاؤه من جميع الملفات في المصفوفة.

يظهر لك مقتطف الشيفرة التالي كيفية دمج مصفوفة من ملفات PDF باستخدام مسارات الملفات.

```java
 public static void ConcatenateArrayOfPDFfilesUsingFilePaths() {
        // إنشاء كائن PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // مصفوفة من الملفات
        string[] filesArray = new string[2];
        filesArray[0] = _dataDir + "Sample-Document-01.pdf";
        filesArray[1] = _dataDir + "Sample-Document-02.pdf";
        // دمج الملفات
        pdfEditor.Concatenate(filesArray, _dataDir + "Concatenate_Result_04.pdf");
    }
```

## دمج مصفوفة من ملفات PDF باستخدام التدفقات (الواجهات)

دمج مصفوفة من ملفات PDF لا يقتصر فقط على الملفات الموجودة على القرص.
 يمكنك أيضًا دمج مجموعة من ملفات PDF من التدفقات. إذا كنت ترغب في دمج ملفات PDF متعددة، يمكنك استخدام التحميل الزائد المناسب لطريقة Concatenate. أولاً، تحتاج إلى إنشاء مصفوفة من تدفقات الإدخال وتدفق واحد لخروج ملف PDF ثم استدعاء طريقة Concatenate. سيتم حفظ الخرج في تدفق الخروج.

يظهر لك مقتطف الشيفرة التالي كيفية دمج مجموعة من ملفات PDF باستخدام التدفقات.

```java
   public static void ConcatenateArrayOfPDFfilesUsingStreams() {
        // إنشاء كائن PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        // مصفوفة من التدفقات
        FileStream[] inputStreams = new FileStream[2];
        inputStreams[0] = new FileStream(_dataDir + "Sample-Document-01.pdf", FileMode.Open);
        inputStreams[1] = new FileStream(_dataDir + "Sample-Document-02.pdf", FileMode.Open);
        // تدفق الخرج
        FileStream outputStream = new FileStream(_dataDir + "Concatenate_Result_05.pdf", FileMode.Create);
        // دمج الملف
        pdfEditor.Concatenate(inputStreams, outputStream);
    }
```

## دمج نماذج PDF والحفاظ على أسماء الحقول فريدة

فئة [PdfFileEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor) في مساحة الأسماء [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) تقدم القدرة على دمج ملفات PDF.
 الآن، إذا كانت ملفات الـ PDF التي سيتم دمجها تحتوي على حقول نموذج بأسماء مشابهة، يوفر Aspose.PDF ميزة الحفاظ على الحقول في ملف الـ PDF الناتج كحقول فريدة وأيضاً يمكنك تحديد اللاحقة لجعل أسماء الحقول فريدة. طريقة [KeepFieldsUnique](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getKeepFieldsUnique--) في PdfFileEditor كـ true ستجعل أسماء الحقول فريدة عند دمج نماذج الـ PDF. أيضاً، يمكن استخدام طريقة [UniqueSuffix](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileEditor#getUniqueSuffix--) في PdfFileEditor لتحديد تنسيق اللاحقة الذي يحدده المستخدم والذي يُضاف إلى اسم الحقل لجعله فريداً عند دمج النماذج. يجب أن تحتوي هذه السلسلة على %NUM% كجزء فرعي والذي سيتم استبداله بالأرقام في الملف الناتج.

يرجى الاطلاع على الكود البسيط التالي لتحقيق هذه الوظيفة.

```java
  public static void ConcatenatePDFformsAndKeepFieldsNamesUnique()
        {
            // تعيين مسارات ملفات الإدخال والإخراج

            string inputFile1 = _dataDir + "Sample-Form-01.pdf";
            string inputFile2 = _dataDir + "Sample-Form-02.pdf";
            string outFile = _dataDir + "ConcatenatePDFForms_out.pdf";

            // إنشاء كائن PdfFileEditor
            PdfFileEditor fileEditor = new PdfFileEditor
            {
                // للحفاظ على معرف حقل فريد لجميع الحقول
                KeepFieldsUnique = true,
                // تنسيق اللاحقة التي تضاف إلى اسم الحقل لجعله فريداً عند دمج النماذج.
                UniqueSuffix = "_%NUM%"
            };

            // دمج الملفات في ملف PDF الناتج
            fileEditor.Concatenate(inputFile1, inputFile2, outFile);
        }
```

## دمج إدراج صفحة فارغة

بمجرد دمج ملفات PDF، يمكننا إدراج صفحة فارغة في بداية المستند حيث يمكننا إنشاء جدول المحتويات. لتحقيق هذا المتطلب، يمكننا تحميل الملف المدمج في كائن Document ونحتاج إلى استدعاء طريقة Page.Insert(…) لإدراج صفحة فارغة.

```java
   public static void ConcatenatePDF_InsertBlankPage() {
        // إنشاء كائن PdfFileEditor
        PdfFileEditor pdfEditor = new PdfFileEditor();
        var documents = new Aspose.Pdf.Document[3];
        documents[0] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-01.pdf");
        documents[1] = new Aspose.Pdf.Document(_dataDir + "Sample-Document-02.pdf");
        var destinationDoc = new Aspose.Pdf.Document();
        destinationDoc.Pages.Add();
        // دمج الملفات
        pdfEditor.Concatenate(documents, destinationDoc);
        destinationDoc.Save(_dataDir + "Concatenate_Result_06.pdf");
    }
```