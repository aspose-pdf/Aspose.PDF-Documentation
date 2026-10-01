---
title: احصل على امتيازات المستند
linktitle: احصل على امتيازات المستند
type: docs
weight: 10
url: /ar/java/get-document-privileges/
description: تعرف على كيفية فحص امتيازات مستند PDF في Java باستخدام واجهة PdfFileInfo.
lastmod: "2026-10-01"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استرجاع امتيازات مستند PDF باستخدام Aspose.PDF for Java
Abstract: تعرف على كيفية استرجاع امتيازات المستند باستخدام Aspose.PDF for Java. ينشئ المثال في Java كائنًا من نوع PdfFileInfo، يقرأ إعدادات DocumentPrivilege الخاصة به، ويطبع علامات الأذونات للطباعة، والنسخ، والتعديل، والتعليقات التوضيحية، وتعبئة النماذج، وقارئات الشاشة، وتجميع المستند.
---
## احصل على امتيازات المستند

استخدام `PdfFileInfo.getDocumentPrivilege()` لتفحص ما العمليات التي يسمح بها ملف PDF الحالي.

### خطوات

1. إنشاء `PdfFileInfo` كائن لملف PDF الإدخال.
2. اتصال `getDocumentPrivilege()` لاسترجاع مجموعة الامتيازات.
3. اقرأ العلامات البوليانية ذات الصلة من القيم المسترجعة `DocumentPrivilege` كائن.
4. إغلاق الـ `PdfFileInfo` مثال عند الانتهاء.

### مثال Java

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
