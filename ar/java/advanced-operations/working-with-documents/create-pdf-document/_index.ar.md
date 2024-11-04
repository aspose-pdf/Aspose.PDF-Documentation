---
title: إنشاء مستند
type: docs
weight: 10
url: /java/create-pdf-document/
description: يساعد Aspose.PDF for Java على إنشاء مستند PDF وملف PDF قابل للبحث في بضع خطوات سهلة.
lastmod: "2021-06-05"
---

في هذه المقالة، سنوضح كيفية استخدام Aspose.PDF for Java API لإنشاء وقراءة ملفات PDF بسهولة في تطبيقات Java.

تتيح Aspose.PDF for Java API لمطوري تطبيقات Java تضمين وظيفة معالجة مستندات PDF في تطبيقاتهم. يمكن استخدامها لإنشاء وقراءة ملفات PDF دون الحاجة إلى أي برامج أخرى مثبتة على الجهاز الأساسي. يمكن استخدام Aspose.PDF for Java في مجموعة متنوعة من أنواع تطبيقات Java مثل تطبيقات Desktop وJSP وJSF.

## كيفية إنشاء ملف PDF باستخدام Java

لإنشاء ملف PDF باستخدام Java، يمكن اتباع الخطوات التالية.

1. إنشاء كائن من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)

1. أضف كائن [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) إلى مجموعة Pages لكائن Document
1. أضف [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) إلى مجموعة [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) في الصفحة
1. احفظ مستند PDF الناتج

```java
package com.aspose.pdf.examples;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.Document.CallBackGetHocr;

public class ExampleCreate {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    
    public static void Create() {        
        Document document = new Document();
 
        //إضافة صفحة
        Page page = document.getPages().add();
         
        // إضافة نص إلى الصفحة الجديدة
        page.getParagraphs().add(new TextFragment("Hello World!"));
         
        // حفظ ملف PDF المحدث
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```


في هذه الحالة، نقوم بإنشاء مستند PDF من صفحة واحدة بحجم الصفحة A4، وتوجه عمودي. ستحتوي صفحتنا على "مرحباً، أيها العالم" في الجزء العلوي الأيسر من الصفحة.

أيضًا، يوفر Aspose.PDF for Java القدرة على إنشاء كيفية إنشاء PDF قابل للبحث. دعونا نتعلم الشيفرة التالية:

```java
public static void CreateSearchablePDF() {                
        Document doc = new Document(_dataDir + "sample1.pdf");
        
        // إنشاء رد اتصال - منطق التعرف على النص لصور PDF. استخدم OCR خارجي يدعم معيار HOCR (http://en.wikipedia.org/wiki/HOCR).
        // لقد استخدمنا برنامج جوجل تيسيراكت OCR المجاني (http://en.wikipedia.org/wiki/Tesseract_%28software%29)
        
        CallBackGetHocr cbgh = new CallBackGetHocr() {
            @Override
            public String invoke(java.awt.image.BufferedImage img) {
                File outputfile = new File(_dataDir + "test.jpg");
                try {
                    ImageIO.write(img, "jpg", outputfile);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
        
                try {
                    java.lang.Process process = Runtime.getRuntime().exec("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    System.out.println("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    process.waitFor();
        
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
        
                // قراءة out.html إلى سلسلة
                File file = new File(_dataDir + "out.hocr");
                StringBuilder fileContents = new StringBuilder((int) file.length());
                Scanner scanner = null;
                try {
                    scanner = new Scanner(file);
                    String lineSeparator = System.getProperty("line.separator");
        
                    while (scanner.hasNextLine()) {
                        fileContents.append(scanner.nextLine() + lineSeparator);
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } finally {
                    if (scanner != null)
                        scanner.close();
                }
        
                // حذف الملفات المؤقتة
                File fileOut = new File(_dataDir + "out.hocr");
                if (fileOut.exists()) {
                    fileOut.delete();
                }
                File fileTest = new File(_dataDir + "test.jpg");
                if (fileTest.exists()) {
                    fileTest.delete();
                }
        
                return fileContents.toString();
            }
        };
        // نهاية رد الاتصال
        
        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");        
    }
}
```