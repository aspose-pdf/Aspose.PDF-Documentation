---
title: احصل على معلومات ملف PDF - الواجهات
type: docs
weight: 10
url: /java/get-pdf-information/
description: توضح هذه القسم كيفية الحصول على معلومات ملف PDF باستخدام Aspose.PDF Facades باستخدام فئة PdfFileInfo.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

من أجل الحصول على معلومات محددة لملف PDF، تحتاج إلى إنشاء كائن من فئة [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo). بعد ذلك، يمكنك الحصول على قيم الخصائص الفردية مثل الموضوع، العنوان، الكلمات الرئيسية، والمؤلف وما إلى ذلك.

يوضح لك مقطع الشفرة التالي كيفية الحصول على معلومات ملف PDF.

```java
public static void GetPdfInfo()
    {
        // فتح المستند
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // الحصول على معلومات PDF
        System.out.println("الموضوع: " + fileInfo.getSubject());
        System.out.println("العنوان: " + fileInfo.getTitle());
        System.out.println("الكلمات الرئيسية: " + fileInfo.getKeywords());
        System.out.println("المؤلف: " + fileInfo.getCreator());
        System.out.println("تاريخ الإنشاء: " + fileInfo.getCreationDate());
        System.out.println("تاريخ التعديل: " + fileInfo.getModDate());
        // التحقق مما إذا كان PDF صالحًا ومشفرًا أيضًا
        System.out.println("هل هو PDF صالح: " + fileInfo.isPdfFile());
        System.out.println("هل هو مشفر: " + fileInfo.isEncrypted());

        System.out.println("عرض الصفحة:" +fileInfo.getPageWidth(1));
    }
```


## الحصول على معلومات ميتا

من أجل الحصول على المعلومات، نستخدم طريقة [getHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#getHeader--). باستخدام 'Hashtable' نحصل على جميع القيم الممكنة.

```java
public static void GetMetaInfo()
    {        
        // إنشاء مثيل لكائن PdffileInfo
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "SetMetaInfo_out.pdf");

        // استرجاع جميع السمات المخصصة الموجودة
        Hashtable<String,String> hTable = new Hashtable<String,String>(fInfo.getHeader());

        Enumeration<String> enumerator = hTable.keys();
        while (enumerator.hasMoreElements()) { 
            // الحصول على المفتاح
            String key = enumerator.nextElement();  
            // طباعة المفتاح والقيمة المقابلة لذلك المفتاح
            System.out.println(key + ": " + hTable.get(key));
        }

        // استرجاع واحدة من السمات المخصصة
        System.out.println( fInfo.getMetaInfo("Reviewer"));
```