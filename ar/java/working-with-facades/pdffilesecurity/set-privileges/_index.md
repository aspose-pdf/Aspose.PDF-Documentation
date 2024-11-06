---
title: تعيين الامتيازات على ملف PDF موجود
type: docs
weight: 50
url: ar/java/set-privileges/
description: يشرح هذا الموضوع كيفية تعيين الامتيازات على ملف PDF موجود باستخدام فئة PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---

## تعيين الامتيازات على ملف PDF موجود (الواجهات)

لتعيين امتيازات ملف PDF، قم بإنشاء كائن فئة [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSecurity) واربط ملف PDF المدخل باستخدام طريقة binPdf. ثم يجب عليك استدعاء طريقة setPrivilege لتعيين الامتيازات. يمكنك تحديد الامتيازات باستخدام كائن [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/DocumentPrivilege) ثم تمرير هذا الكائن إلى طريقة setPrivilege وحفظ ملف PDF الناتج باستخدام طريقة save.

يظهر مقطع الشيفرة التالي كيفية تعيين امتيازات ملف PDF.

```java
public static void SetPrivilege1() {
        // إنشاء كائن DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // إنشاء كائن PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege(privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```


See the following method with specifying a password:

```java
 public static void SetPrivilege2() {
        // إنشاء كائن DocumentPrivileges
        DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
        privilege.setChangeAllowLevel(1);
        privilege.setAllowPrint(true);
        privilege.setAllowCopy(true);

        // إنشاء كائن PdfFileSecurity
        PdfFileSecurity fileSecurity = new PdfFileSecurity();
        fileSecurity.bindPdf(_dataDir + "sample.pdf");
        fileSecurity.setPrivilege("", "P@ssw0rd", privilege);
        fileSecurity.save(_dataDir + "sample_privileges.pdf");
    }
```