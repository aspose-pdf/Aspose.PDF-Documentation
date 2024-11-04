---
title: استخراج الصور من ملف PDF
linktitle: استخراج الصور
type: docs
weight: 20
url: /java/extract-images-from-the-pdf-file/
description: كيفية استخراج جزء من الصورة من ملف PDF باستخدام Aspose.PDF for Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يحتوي كل صفحة في مستند PDF على موارد (صور، نماذج وخطوط). يمكننا الوصول إلى هذه الموارد عن طريق استدعاء طريقة [getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--). تحتوي فئة [Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources) على [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection) ويمكننا الحصول على قائمة بالصور عن طريق استدعاء طريقة [getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--).

لذلك، لاستخراج صورة من الصفحة، نحتاج إلى الحصول على مرجع إلى الصفحة، ثم إلى موارد الصفحة وأخيرًا إلى مجموعة الصور.
يمكننا استخراج صورة معينة على سبيل المثال عن طريق الفهرس.

يعيد فهرس الصورة كائن [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage).
This object provides a [Save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

```java
public static void Extract_Images(){
       // المسار إلى دليل المستندات.
       String _dataDir = "/home/admin1/pdf-examples/Samples/";
       String filePath = _dataDir + "ExtractImages.pdf";

       // تحميل مستند PDF
       com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

       com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);
       com.aspose.pdf.XImageCollection xImageCollection = page.getResources().getImages();
       // استخراج صورة معينة
       com.aspose.pdf.XImage xImage = xImageCollection.get_Item(1);

       try {
           java.io.FileOutputStream outputImage = new java.io.FileOutputStream(_dataDir + "output.jpg");
           // حفظ الصورة المستخرجة
           xImage.save(outputImage);
           outputImage.close();
       } catch (java.io.FileNotFoundException e) {
           // TODO: التعامل مع الاستثناء
           e.printStackTrace();
       } catch (java.io.IOException e) {
           // TODO: التعامل مع الاستثناء
           e.printStackTrace();
       }
   }
```