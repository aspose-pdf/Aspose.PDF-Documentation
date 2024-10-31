---
title: استخراج الصور من PDF 
linktitle: استخراج الصور
type: docs
weight: 20
url: /androidjava/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من PDF باستخدام Aspose.PDF لنظام Android عبر Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

كل صفحة في مستند PDF تحتوي على موارد (صور، نماذج وخطوط). يمكننا الوصول إلى هذه الموارد عن طريق استدعاء [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--) الطريقة. تحتوي فئة [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) على [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) ويمكننا الحصول على قائمة الصور عن طريق استدعاء [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--) الطريقة.

لذلك لاستخراج صورة من الصفحة، نحتاج إلى الحصول على مرجع للصفحة، ثم موارد الصفحة وأخيرًا إلى مجموعة الصور.

يمكننا استخراج صورة معينة على سبيل المثال بواسطة الفهرس.

فهرس الصورة يعيد كائن [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
يوفر هذا الكائن طريقة [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) التي يمكن استخدامها لحفظ الصورة المستخرجة. يوضح مقتطف الشيفرة التالي كيفية استخراج الصور من ملف PDF.

```java
public void extractImage () {
    // فتح المستند
    try {
        document=new Document(inputStream);
    } catch (Exception e) {
        resultMessage.setText(e.getMessage());
        return;
    }

    com.aspose.pdf.Page page=document.getPages().get_Item(1);
    com.aspose.pdf.XImageCollection xImageCollection=page.getResources().getImages();
    // استخراج صورة معينة
    com.aspose.pdf.XImage xImage=xImageCollection.get_Item(1);
    File file=new File(fileStorage, "extracted-image.jpeg");
    try {
        java.io.FileOutputStream outputImage=new java.io.FileOutputStream(file.toString());
        // حفظ الصورة الناتجة
        xImage.save(outputImage, ImageType.getJpeg());
        outputImage.close();
    } catch (java.io.IOException e) {
        resultMessage.setText(e.getMessage());
        return;
    }
    resultMessage.
  }
```