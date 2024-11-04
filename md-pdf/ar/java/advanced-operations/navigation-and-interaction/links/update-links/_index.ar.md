---
title: تحديث الروابط في ملف PDF
linktitle: تحديث الروابط
type: docs
weight: 20
url: /java/update-links/
description: تحديث الروابط في ملف PDF برمجياً. يتناول هذا الدليل كيفية تحديث الروابط في ملف PDF باستخدام لغة Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تحديث الروابط في ملف PDF

كما نوقش في إضافة رابط تشعبي في ملف PDF، تجعل فئة [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) من الممكن إضافة روابط في ملف PDF. هناك أيضًا فئة مشابهة تُستخدم للحصول على الروابط الموجودة داخل ملفات PDF. استخدم هذا إذا كنت بحاجة إلى تحديث رابط موجود. لتحديث رابط موجود:

1. قم بتحميل ملف PDF.
1. انتقل إلى صفحة محددة في ملف PDF.
1. حدد وجهة الرابط باستخدام خاصية Destination لكائن [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction).

1. يتم تحديد صفحة الوجهة باستخدام منشئ [XYZExplicitDestination](https://reference.aspose.com/pdf/java/com.aspose.pdf/XYZExplicitDestination).

### تعيين هدف الرابط إلى صفحة في نفس المستند

يظهر لك مقتطف الشفرة التالي كيفية تحديث رابط في ملف PDF وتعيين هدفه إلى الصفحة الثانية من المستند.

```java
    public static void SetLinkTargetToAPageInTheSameDocument() {
        
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
        // الحصول على أول تعليق توضيحي للرابط من الصفحة الأولى للمستند
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // تعديل الرابط: تغيير وجهة الرابط
        GoToAction goToAction = (GoToAction)linkAnnot.getAction();
        // تحديد الوجهة لكائن الرابط
        // تمثل الوجهة الصريحة التي تعرض الصفحة بالإحداثيات (left, top) الموضوعة في الزاوية العلوية اليسرى من 
        // النافذة ومحتويات الصفحة مكبرة بمعامل التكبير zoom.
        // المعامل الأول هو رقم صفحة الوجهة. 
        // المعامل الثاني هو الإحداثي الأيسر
        // المعامل الثالث هو الإحداثي العلوي
        // المعامل الرابع هو معامل التكبير عند عرض الصفحة المعنية. استخدام 2 يعني أن الصفحة سيتم عرضها بنسبة تكبير 200%
        goToAction.setDestination(new XYZExplicitDestination(1, 1, 2, 2 ));
        
        // حفظ المستند مع الرابط المحدث
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### تعيين وجهة الرابط إلى عنوان ويب

لتحديث الارتباط التشعبي بحيث يشير إلى عنوان ويب، قم بإنشاء كائن [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction) ومرره إلى خاصية Action الخاصة بـ LinkAnnotation. يُظهر مقتطف الشيفرة التالي كيفية تحديث رابط في ملف PDF وتعيين هدفه إلى عنوان ويب.

```java
    public static void SetLinkDestinationToWebAddress() {        
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        // الحصول على أول توضيح رابط من الصفحة الأولى للمستند
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        // تعديل الرابط: تغيير إجراء الرابط وتعيين الهدف كعنوان ويب
        linkAnnot.setAction(new GoToURIAction("www.aspose.com"));
        
        // حفظ المستند بالرابط المحدث
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```


### تعيين هدف الرابط إلى ملف PDF آخر

يُظهر مقتطف الشفرة التالي كيفية تحديث رابط في ملف PDF وتعيين هدفه إلى ملف PDF آخر.

```java
    public static void SetLinkTargetToAnotherPDFFile() {        
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
    
        LinkAnnotation linkAnnot = (LinkAnnotation)page.getAnnotations().get_Item(1);

        GoToRemoteAction goToR = (GoToRemoteAction)linkAnnot.getAction();
        // السطر التالي يحدث الوجهة، لا يحدث الملف
        goToR.setDestination(new XYZExplicitDestination(2, 0, 0, 1.5));
        // السطر التالي يحدث الملف
        goToR.setFile (new FileSpecification(_dataDir +  "input.pdf"));

        // حفظ المستند بالرابط المحدث
        document.save(_dataDir + "PDFLINK_Modified_UpdateLinks_out.pdf");        
    }
```

### تحديث لون نص LinkAnnotation

لا يحتوي التعليق التوضيحي للرابط على نص.
 بدلاً من ذلك، يتم وضع النص في محتويات الصفحة تحت التعليق التوضيحي. لذلك، لتغيير لون النص، قم بتغيير لون نص الصفحة بدلاً من محاولة تغيير لون التعليق التوضيحي. يوضح مقتطف الشيفرة التالي كيفية تحديث لون التعليق التوضيحي للرابط في ملف PDF.

```java
    public static void UpdateLinkAnnotationTextColor () {        
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        for (Annotation annotation : page.getAnnotations())
        {
            if (annotation.getAnnotationType() == AnnotationType.Link)
            {
                // البحث عن النص تحت التعليق التوضيحي
                TextFragmentAbsorber ta = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX()-10);
                rect.setLLY(rect.getLLY()-10);
                rect.setURX(rect.getURX()+ 10);
                rect.setURY(rect.getURY()+ 10);

                ta.setTextSearchOptions(new TextSearchOptions(rect));
                ta.visit(page);
                // تغيير لون النص.
                for (TextFragment tf : ta.getTextFragments())
                {
                    tf.getTextState().setForegroundColor(Color.getRed());
                }
            }
        
        }                       
        // حفظ المستند مع الرابط المحدث
        document.save(_dataDir + "UpdateLinkTextColor_out.pdf");        
    }
```