---
title: إنشاء ملفات PDF متوافقة مع PDF/3-A وإرفاق فاتورة ZUGFeRD في Java
linktitle: إرفاق ZUGFeRD إلى PDF
type: docs
weight: 10
url: ar/java/attach-zugferd/
description: تعلم كيفية إنشاء مستند PDF مع ZUGFeRD في Aspose.PDF for Java
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إرفاق ZUGFeRD إلى PDF

نوصي بالخطوات التالية لإرفاق ZUGFeRD إلى PDF:

* تعريف متغير مسار يشير إلى مجلد حيث توجد ملفات PDF المدخلة والمخرجة.
* تعريف متغير سلسلة path الذي يخزن المسار إلى ملف PDF الذي سيتم معالجته. استخدم `Paths.get` لدمج أجزاء من المسار الكامل.
* إنشاء عبارة try-with-resources التي تضمن أن يتم إغلاق كائن Document الذي تم إنشاؤه من المتغير path تلقائيًا بعد انتهاء العبارة. يمثل كائن Document مستند PDF الذي سيتم تعديله وحفظه.

* إنشاء كائن [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) عن طريق تقديم المسار والوصف لملف آخر يحتوي على بيانات الفاتورة الوصفية المتوافقة مع معيار ZUGFeRD.
* أضف خصائص إلى كائن مواصفات الملف، مثل الوصف، نوع MIME، وعلاقة AF. تشير علاقة AF إلى كيفية ارتباط الملف المضمن بمستند PDF. في هذه الحالة، يتم تعيينها إلى "بديل"، مما يعني أن الملف المضمن هو تمثيل بديل لمحتوى PDF.
* أضف كائن مواصفات الملف إلى مجموعة الملفات المدمجة للمستند. يجب تحديد اسم الملف وفقًا لمعيار ZUGFeRD، مثل "factor-x.xml".
* قم بتحويل المستند إلى تنسيق PDF/A-3U، وهو جزء من PDF يضمن الحفظ طويل الأمد للمستندات الإلكترونية. يسمح PDF/A-3U بتضمين ملفات من أي تنسيق في مستندات PDF.
* احفظ المستند المحول كملف PDF جديد (مثل "ZUGFeRD-res.pdf").
* أغلق عبارة try-with-resources وحرر كائن Document.

```java
String _dataDir = "/home/aspose/pdf-examples/Samples/";
String path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-test.pdf").toString();
try (Document document = new Document(path)) {
    String description = "بيانات الفاتورة المطابقة لمعيار ZUGFeRD";
    path = Paths.get(_dataDir, "ZUGFeRD", "factur-x.xml").toString();
    FileSpecification fileSpecification = new FileSpecification(path.toString(), description);
    fileSpecification.setMIMEType("text/xml");
    fileSpecification.setAFRelationship(com.aspose.pdf.AFRelationship.Alternative);

    // أضف المرفق إلى مجموعة المرفقات للمستند
    document.getEmbeddedFiles().add(fileSpecification);
    path = Paths.get(_dataDir, "ZUGFeRD", "log.xml").toString();
    document.convert(path, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
    path = Paths.get(_dataDir, "ZUGFeRD", "ZUGFeRD-res.pdf").toString();
    document.save(path);
}
```