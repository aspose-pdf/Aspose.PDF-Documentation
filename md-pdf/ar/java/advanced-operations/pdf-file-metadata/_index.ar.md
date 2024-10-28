---
title: العمل مع بيانات وصفية لملف PDF
linktitle: بيانات وصفية لملف PDF
type: docs
weight: 140
url: /java/pdf-file-metadata/
description: تشرح هذه القسم كيفية الحصول على معلومات ملف PDF، وكيفية الحصول على بيانات XMP الوصفية من ملف PDF، وتعيين معلومات ملف PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على معلومات ملف PDF

للحصول على معلومات محددة عن ملف PDF، أولاً احصل على كائن [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). بمجرد استرجاع كائن [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo)، يمكنك الحصول على قيم الخصائص الفردية.

يوضح لك مقتطف الشيفرة التالي كيفية تعيين معلومات ملف PDF.

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // إنشاء مستند PDF جديد
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // الحصول على معلومات المستند
        DocumentInfo docInfo = pdfDocument.getInfo();
        // عرض معلومات المستند
        System.out.println("المؤلف: " + docInfo.getAuthor());
        System.out.println("تاريخ الإنشاء: " + docInfo.getCreationDate());
        System.out.println("الكلمات المفتاحية: " + docInfo.getKeywords());
        System.out.println("تاريخ التعديل: " + docInfo.getModDate());
        System.out.println("الموضوع: " + docInfo.getSubject());
        System.out.println("العنوان: " + docInfo.getTitle());
    }
```


## إعداد معلومات ملف PDF

تسمح Aspose.PDF لـ Java لك بإعداد معلومات خاصة بالملف لملف PDF، مثل المؤلف، وتاريخ الإنشاء، والموضوع، والعنوان.

لإعداد هذه المعلومات:

1. أنشئ كائن [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo).
2. قم بتعيين قيم الخصائص.
3. احفظ المستند المحدث باستخدام طريقة [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) الخاصة بفئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

{{% alert color="primary" %}}

يرجى ملاحظة أنه لا يمكنك تعيين قيم مقابل الحقول **المنتج** و **المنشئ**، لأن Aspose.PDF لـ Java x.x.x سيتم عرضها مقابل هذه الحقول.

{{% /alert %}}

يوضح لك مقطع الشيفرة التالي كيفية إعداد معلومات ملف PDF.

```java
 public static void SetPDFFileInformation() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // تحديد معلومات المستند
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");

        // حفظ المستند الناتج
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```


## الحصول على بيانات XMP الوصفية من ملف PDF

تتيح لك Aspose.PDF for Java الوصول إلى بيانات XMP الوصفية لملف PDF.

للحصول على بيانات وصفية لملف PDF،

1. أنشئ كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) وافتح ملف PDF المدخل.
1. استخدم خاصية [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) للحصول على البيانات الوصفية.

يوضح جزء الشيفرة التالي كيفية الحصول على البيانات الوصفية من ملف PDF.

```java
   public static void GetXMPMetadata() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## تعيين بيانات XMP الوصفية في ملف PDF

تتيح لك Aspose.PDF for Java تعيين البيانات الوصفية في ملف PDF.
 لتعيين البيانات الوصفية:

1. أنشئ كائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. قم بتعيين قيم البيانات الوصفية باستخدام خاصية [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--).
1. احفظ المستند المحدث باستخدام طريقة [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) الخاصة بكائن [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

يوضح لك مقتطف الشيفرة التالي كيفية تعيين البيانات الوصفية في ملف PDF.

```java
    public static void SetXMPMetadata() {

        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // تعيين الخصائص
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // حفظ المستند
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## إدراج البيانات الوصفية مع البادئة

بعض المطورين يحتاجون إلى إنشاء مساحة أسماء جديدة للبيانات الوصفية مع بادئة. يوضح مقتطف الشيفرة التالي كيفية إدراج البيانات الوصفية مع البادئة.

```java
    public static void InsertMetadataWithPrefix() {
        // فتح المستند
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("alternative title"));        
        // حفظ المستند
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```