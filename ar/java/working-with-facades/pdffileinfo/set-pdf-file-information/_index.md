---
title: تعيين معلومات ملف PDF - الواجهات
type: docs
weight: 20
url: /ar/java/set-pdf-information/
description: تشرح هذه القسم كيفية تعيين معلومات ملف PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

تسمح لك فئة [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) بتعيين معلومات محددة للملف في مستند PDF. تحتاج إلى إنشاء كائن من فئة [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) ثم تعيين خصائص محددة للملف مثل المؤلف، العنوان، الكلمات الدالة، والمنشئ إلخ. أخيرًا، احفظ ملف PDF المحدث باستخدام طريقة [saveNewInfo(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) للكائن [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo).

يوضح لك مقتطف الشيفرة التالي كيفية تعيين معلومات ملف PDF.

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // تعيين معلومات PDF
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Hello World!");
        fileInfo.setKeywords("Peace and Development");
        fileInfo.setCreator ("Aspose");
        
        // حفظ الملف المحدث
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```


## إعداد معلومات الميتا

تتيح لك طريقة [setMetaInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) إضافة أي معلومات. في مثالنا، أضفنا حقلًا. تحقق من مقتطف الشيفرة التالي:

```java
   public static void SetMetaInfo()
    {
        // إنشاء مثيل لكائن PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // تعيين سمة عميل جديدة كمعلومات ميتا
        fInfo.setMetaInfo("Reviewer", "Aspose.PDF user");

        // حفظ الملف المحدث
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```