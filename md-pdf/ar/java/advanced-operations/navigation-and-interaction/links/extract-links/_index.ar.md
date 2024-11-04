---
title: استخراج الروابط من ملف PDF
linktitle: استخراج الروابط
type: docs
weight: 30
url: /java/extract-links/
description: استخراج الروابط من PDF باستخدام Java. يشرح هذا الموضوع كيفية استخراج الروابط باستخدام فئة AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج الروابط من ملف PDF

تمثل الروابط تعليقات توضيحية في ملف PDF، لذا لاستخراج الروابط، قم باستخراج جميع كائنات [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).

1. أنشئ كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. احصل على [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) التي ترغب في استخراج الروابط منها.
3. استخدم فئة [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) لاستخراج جميع كائنات [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/LinkAnnotation) من الصفحة المحددة.

1. مرر كائن [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector) إلى طريقة Accept لكائن الصفحة.
1. احصل على جميع التعليقات التوضيحية للرابط المحدد في كائن IList باستخدام طريقة [getSelected](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationSelector#getSelected--) لكائن [AnnotationSelector](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationselector).

يعرض لك مقطع الشيفرة التالي كيفية استخراج الروابط من ملف PDF.

```java
    public static void ExtractLinksFromThePDFFile() {        
        // تحميل ملف PDF
        Document document = new Document(_dataDir + "UpdateLinks.pdf");
        Page page = document.getPages().get_Item(1);
           
        AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Rectangle.getTrivial()));
        page.accept(selector);
        java.util.List<Annotation> list = selector.getSelected();
        for(Annotation annot : list)
        {
            System.out.println("الملاحظة الموجودة: " + annot.getRect());
        }
                
        // احفظ المستند مع تحديث الرابط
        //document.save(_dataDir + "ExtractLinks_out.pdf");
    }
```