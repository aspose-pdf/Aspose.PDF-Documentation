---
title: استخراج الصور من PDF (الواجهات)
type: docs
weight: 30
url: /ar/java/extract-images/
description: يشرح هذا القسم كيفية استخراج الصور باستخدام Aspose.PDF Facades مع استخدام فئة PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تتيح لك فئة [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) استخراج الصور من ملف PDF.
 First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) class and bind input PDF file using bindPdf method. After that, call [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of hasNextImage and getNextImage methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the getNextImage method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.

أولاً، تحتاج إلى إنشاء كائن من فئة [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) وربط ملف PDF المدخل باستخدام طريقة bindPdf. بعد ذلك، استدعِ طريقة [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) لاستخراج جميع الصور في الذاكرة. بمجرد استخراج الصور، يمكنك الحصول على تلك الصور بمساعدة طريقتي hasNextImage وgetNextImage. تحتاج إلى التجول عبر جميع الصور المستخرجة باستخدام حلقة while. من أجل حفظ الصور على القرص، يمكنك استدعاء التحميل الزائد لطريقة getNextImage التي تأخذ مسار الملف كحجة. يوضح لك مقتطف الشيفرة التالي كيفية استخراج الصور من ملف PDF بالكامل إلى ملفات.

```java   
public static void ExtractImages()
 {
    //Create an extractor and bind it to the document
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    //Run the extractor
    extractor.extractImage();
    int imageNumber = 1;
    //Iterate througth extracted images collection
    while (extractor.hasNextImage())
    {
        //Retrieve image from collection and save it in a file 
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++),ImageType.getPng());
    }
}
```