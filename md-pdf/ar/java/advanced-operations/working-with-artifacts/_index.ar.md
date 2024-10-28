---
title: العمل مع القطع الأثرية
linktitle: العمل مع القطع الأثرية
type: docs
weight: 110
url: /java/artifacts/
description: تصف هذه الصفحة كيفية العمل مع فئة Artifact باستخدام Aspose.PDF لـ Java. تعرض مقتطفات الكود كيفية إضافة صورة خلفية إلى صفحات PDF وكيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

القطع الأثرية هي عمومًا كائنات رسومية أو علامات أخرى ليست جزءًا من المحتوى المؤلف. في أمثلة PDF الخاصة بك تتضمن القطع الأثرية معلومات مختلفة، هناك ترويسة أو تذييل الصفحة، أو خطوط أو رسومات أخرى تفصل بين أقسام الصفحة، أو صور زخرفية.

تحتوي فئة [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) على:

- [Artifact.Type](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactType) – يحصل على نوع القطعة الأثرية (يدعم القيم لتعداد Artifact.ArtifactType حيث تشمل القيم الخلفية، والتخطيط، والصفحة، والترقيم، وغير محدد).
- [Artifact.Subtype](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact.ArtifactSubtype) – يحصل على النوع الفرعي للأداة (يدعم القيم في تعداد Artifact.ArtifactSubtype حيث تشمل القيم الخلفية، التذييل، الرأس، غير محدد، العلامة المائية).

يُطلق على العلامة المائية التي تم إنشاؤها باستخدام Adobe Acrobat اسم أداة (كما هو موضح في 14.8.2.2 المحتوى الحقيقي والأدوات في مواصفات PDF). للعمل مع الأدوات، يحتوي Aspose.PDF على فئتين: [Artifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/Artifact) و [ArtifactCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/ArtifactCollection).

من أجل الحصول على جميع الأدوات في صفحة معينة، تحتوي فئة [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) على خاصية Artifacts. يشرح هذا الموضوع كيفية العمل مع الأدوات في ملفات PDF.

يوضح مقتطف الشيفرة التالي كيفية تعيين العلامة المائية على الصفحة الأولى من ملف PDF.

```java

 public class ExamplesArtifacts {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Artifacts/";

    public static void SetWatermark(){
        Document doc = new Document(_dataDir + "sample.pdf");
        WatermarkArtifact artifact = new WatermarkArtifact();        
        artifact.setText(new FormattedText("WATERMARK", java.awt.Color.BLUE, 
                            FontStyle.Courier,
                            EncodingType.Identity_h, true, 72));
        artifact.setArtifactHorizontalAlignment (HorizontalAlignment.Center);
        artifact.setArtifactVerticalAlignment (VerticalAlignment.Center);
        artifact.setRotation (45);
        artifact.setOpacity (0.5);
        artifact.setBackground (true);
        doc.getPages().get_Item(1).getArtifacts().add(artifact);
        doc.save(_dataDir + "watermark.pdf");
    }
```


يمكن استخدام الصور الخلفية لإضافة علامة مائية أو تصميم آخر خفيف إلى المستندات. في Aspose.PDF لـ Java، كل مستند PDF هو مجموعة من الصفحات وكل صفحة تحتوي على مجموعة من العناصر. يمكن استخدام فئة [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) لإضافة صورة خلفية إلى كائن الصفحة.

يوضح مقطع الشفرة التالي كيفية إضافة صورة خلفية إلى صفحات PDF باستخدام كائن BackgroundArtifact.

```java

    public static void SetBackground() throws FileNotFoundException {

        // فتح المستند
        Document pdfDocument = new Document();
                
        // إضافة صفحة جديدة إلى كائن المستند
        Page page = pdfDocument.getPages().add();

        // إنشاء كائن خلفية
        BackgroundArtifact background = new BackgroundArtifact();

        // تحديد الصورة لكائن الخلفية
        background.setBackgroundImage(new java.io.FileInputStream(new java.io.File(_dataDir + "background.png")));
        
        // إضافة كائن الخلفية إلى مجموعة العناصر في الصفحة
        page.getArtifacts().add(background);

        // حفظ ملف PDF المعدل
        pdfDocument.save(_dataDir + "ImageAsBackground_out.pdf");

    }
```


## عينات البرمجة: الحصول على العلامة المائية

يوضح مقتطف الشفرة التالي كيفية الحصول على كل علامة مائية في الصفحة الأولى من ملف PDF.

```java
    public static void GettingWatermarks() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        // تكرار والحصول على النوع الفرعي والنص وموقع الأداة
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            System.out.println(artifact.getSubtype() + " " + artifact.getText() + " " + artifact.getRectangle().toString());
        }
```

## عينات البرمجة: حساب عدد الأدوات من نوع معين

لحساب العدد الإجمالي للأدوات من نوع معين (على سبيل المثال، العدد الإجمالي للعلامات المائية)، استخدم الشفرة التالية:

```java
    public static void CountingArtifacts() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir +  "watermark_new.pdf");
        int count = 0;
        for (Artifact artifact : pdfDocument.getPages().get_Item(1).getArtifacts())
        {
            // إذا كان نوع الأداة هو العلامة المائية، زد العداد
            if (artifact.getSubtype() == Artifact.ArtifactSubtype.Watermark) count++;
        }
        System.out.println("تحتوي الصفحة على " + count + " علامات مائية");
    }
```