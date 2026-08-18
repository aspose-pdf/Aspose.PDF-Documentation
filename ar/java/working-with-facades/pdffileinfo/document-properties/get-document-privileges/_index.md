---
title: الحصول على امتيازات المستند
linktitle: الحصول على امتيازات المستند
type: docs
weight: 10
url: /java/get-document-privileges/
description: تعرف على كيفية فحص امتيازات مستند PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرجع امتيازات مستند PDF باستخدام Aspose.PDF لـ Java
Abstract: تعرف على كيفية استرداد امتيازات المستند باستخدام Aspose.PDF لـ Java. يقوم مثال Java بإنشاء كائن PdfFileInfo، وقراءة إعدادات DocumentPrivilege الخاصة به، وطباعة علامات الأذونات للطباعة والنسخ والتعديل والتعليقات التوضيحية وملء النماذج وبرامج قراءة الشاشة والتجميع.
---
## الحصول على امتيازات الوثيقة

استخدم `PdfFileInfo.getDocumentPrivilege()` لفحص العمليات التي يسمح بها ملف PDF الحالي.

### خطوات

1. قم بإنشاء كائن `PdfFileInfo` لمدخل PDF.
2. اتصل `getDocumentPrivilege()` لاسترداد مجموعة الامتيازات.
3. اقرأ العلامات المنطقية ذات الصلة من الكائن `DocumentPrivilege` الذي تم إرجاعه.
4. أغلق المثيل `PdfFileInfo` عند الانتهاء.

### مثال جافا

```java
public static void getDocumentPrivileges(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    DocumentPrivilege privileges = pdfInfo.getDocumentPrivilege();

    System.out.println("Document Privileges:");
    System.out.println("  Can Print: " + privileges.isAllowPrint());
    System.out.println("  Can Degraded Print: " + privileges.isAllowDegradedPrinting());
    System.out.println("  Can Copy: " + privileges.isAllowCopy());
    System.out.println("  Can Modify Contents: " + privileges.isAllowModifyContents());
    System.out.println("  Can Modify Annotations: " + privileges.isAllowModifyAnnotations());
    System.out.println("  Can Fill In: " + privileges.isAllowFillIn());
    System.out.println("  Can Screen Readers: " + privileges.isAllowScreenReaders());
    System.out.println("  Can Assembly: " + privileges.isAllowAssembly());
    pdfInfo.close();
}
```
