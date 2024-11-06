---
title: العمل مع الحافظة في مستندات PDF
linktitle: الحافظة
type: docs
weight: 40
url: ar/java/portfolio/
description: كيفية إنشاء حافظة PDF باستخدام جافا. يجب عليك استخدام ملف Microsoft Excel، ومستند Word، وملف صورة لإنشاء حافظة PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

أولاً، دعونا نكتشف **ما هو تنسيق ملف حافظة PDF؟**

على سبيل المثال، خذ ملف حافظة PDF يحتوي على مستند Word، وعرض تقديمي Excel، وPowerPoint وغيرها، كمرفقات. هنا يحتفظ كل ملف مرفق بتنسيق المستند الأصلي الخاص به، ولكنه مضمّن أو مجمع في ملف حافظة PDF واحد. يمكنك بالطبع فتح وقراءة أو تعديل كل ملف فردي من حافظة PDF كما لو كان على محرك أقراص أو مجلد. بالإضافة إلى ذلك، تمامًا مثل مستند PDF العادي، يمكنك أيضًا تطبيق العلامة المائية، وتعيين كلمات المرور وتصاريح الأمان مثل القدرة على العرض أو الطباعة أو إجراء تغييرات على مرفقات حافظة PDF.

يمكننا وضع أو تجميع الملفات الأصلية، في نوعها أو تنسيقاتها الأصلية كمرفقات، في ملف حافظة PDF.

## كيفية إنشاء محفظة PDF

تسمح Aspose.PDF بإنشاء مستندات محفظة PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). أضف ملفًا إلى كائن Document.Collection بعد الحصول عليه باستخدام فئة [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). عند إضافة الملفات، استخدم طريقة الحفظ لفئة Document لحفظ مستند المحفظة.

يستخدم المثال التالي ملف Microsoft Excel، ومستند Word، وملف صورة لإنشاء محفظة PDF.

النص البرمجي أدناه ينتج المحفظة التالية.

### محفظة PDF تم إنشاؤها باستخدام Aspose.PDF

![محفظة PDF تم إنشاؤها باستخدام Aspose.PDF for Java](working-with-pdf-portfolio_1.jpg)

```java
    public static void CreatePortfolio() throws IOException {
        // إنشاء كائن المستند
        Document pdfDocument = new Document();

        // إنشاء كائن مجموعة المستندات
        pdfDocument.setCollection(new Collection());

        // الحصول على الملفات لإضافتها إلى المحفظة
        FileSpecification excel = new FileSpecification(_dataDir + "HelloWorld.xlsx");
        FileSpecification word = new FileSpecification(_dataDir + "HelloWorld.docx");
        FileSpecification image = new FileSpecification(_dataDir + "aspose-logo.jpg");

        // توفير وصف للملفات
        excel.setDescription ("ملف Excel");
        word.setDescription ("ملف Word");
        image.setDescription ("ملف صورة");

        // إضافة الملفات إلى مجموعة المستندات
        pdfDocument.getCollection().add(excel);
        pdfDocument.getCollection().add(word);
        pdfDocument.getCollection().add(image);

        // حفظ مستند المحفظة
        pdfDocument.save(_dataDir + "CreatePDFPortfolio_out.pdf");
    }
```


## استخراج الملفات من PDF Portfolio

تسمح لك PDF Portfolios بتجميع المحتوى من مجموعة متنوعة من المصادر (على سبيل المثال، PDF، Word، Excel، ملفات JPEG) في حاوية موحدة واحدة. تحتفظ الملفات الأصلية بهوياتها الفردية ولكن يتم تجميعها في ملف PDF Portfolio. يمكن للمستخدمين فتح وقراءة وتحرير وتنسيق كل ملف مكون بشكل مستقل عن الملفات المكونة الأخرى.

يسمح Aspose.PDF بإنشاء مستندات PDF Portfolio باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). كما يوفر القدرة على استخراج الملفات من PDF Portfolio.

يعرض لك المقتطف البرمجي التالي الخطوات لاستخراج الملفات من PDF Portfolio.

![استخراج الملفات من PDF Portfolio](working-with-pdf-portfolio_2.jpg)

```java
    public static void ExtractPortfolio() throws IOException {
        // افتح مستند
        Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
        // احصل على مجموعة الملفات المضمنة
        EmbeddedFileCollection embeddedFiles = pdfDocument.getEmbeddedFiles();

        // التنقل عبر الملف الفردي للـ Portfolio
        for (FileSpecification fileSpecification : embeddedFiles) {
            InputStream initialStream = fileSpecification.getContents();
            byte[] buffer = new byte[fileSpecification.getContents().available()];
            initialStream.read(buffer);

            File targetFile = new File(_dataDir + fileSpecification.getName());
            OutputStream outStream = new FileOutputStream(targetFile);
            outStream.write(buffer);
            outStream.close();
        }
    }
```


## إزالة الملفات من محفظة PDF

لحذف/إزالة الملفات من محفظة PDF، حاول استخدام أسطر الكود التالية.

```java
public static void RemoveFilesFromPDFPortfolio() {
    // تحميل محفظة PDF المصدر
    Document pdfDocument = new Document(_dataDir + "PDFPortfolio.pdf");
    pdfDocument.getCollection().delete();
    pdfDocument.save(_dataDir + "No_PortFolio_out.pdf");
}
```