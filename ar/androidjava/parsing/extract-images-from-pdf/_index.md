---
title: استخراج الصور من PDF
linktitle: استخراج الصور
type: docs
weight: 20
url: /ar/androidjava/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من PDF باستخدام Aspose.PDF for Android via Java
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

كل صفحة في مستند PDF تحتوي على موارد (الصور والنماذج والخطوط). يمكننا الوصول إلى هذه الموارد من خلال استدعاء [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) طريقة. الفئة [الموارد](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) يحتوي [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) ويمكننا الحصول على قائمة الصور عن طريق استدعاء [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) طريقة.

لذا لاستخراج الصورة من الصفحة، نحتاج إلى الحصول على مرجع للصفحة، ثم موارد الصفحة وأخيرًا مجموعة الصور.
يمكننا استخراج صورة معينة على سبيل المثال عن طريق الفهرس.

فهرس الصورة يُعيد [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage) كائن.
هذا الكائن يوفر [حفظ](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) طريقة يمكن استخدامها لحفظ الصورة المستخرجة. يظهر المقتطف البرمجي التالي كيفية استخراج الصور من ملف PDF.

 ```java
 public void extractImage () {
        // Open document
        try {
            document=new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        com.aspose.pdf.Page page=document.getPages().get_Item(1);
        com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
        // Extract a particular image
        com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
        File file=new File(fileStorage, "extracted-image.jpeg");
        try {
            java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
            // Save output image
            xImage.save(outputImage, ImageType.getJpeg());
            outputImage.close();
        } catch (java.io.IOException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.
          }
```

