---
title: حذف صفحات PDF برمجياً
linktitle: حذف صفحات PDF
type: docs
weight: 40
url: /java/delete-pages/
description: يمكنك حذف صفحات من ملف PDF باستخدام مكتبة Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

يمكنك حذف الصفحات من ملف PDF باستخدام Aspose.PDF لـ Java. لحذف صفحة معينة من [PageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection) ببساطة قم باستدعاء دالة delete() وحدد فهرس الصفحة المعينة التي تريد حذفها. ثم قم باستدعاء دالة الحفظ لحفظ ملف PDF المحدث.

## حذف صفحة من ملف PDF

1. قم باستدعاء دالة Delete وحدد فهرس الصفحة
1. قم باستدعاء دالة Save لحفظ ملف PDF المحدث
يعرض مقطع الشيفرة التالي كيفية حذف صفحة معينة من ملف PDF باستخدام Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleDeletePage {

  private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

  public static void DeletePageFromPDFFile() {

    // افتح المستند
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // حذف صفحة معينة
    pdfDocument.getPages().delete(2);

    _dataDir = _dataDir + "DeleteParticularPage_out.pdf";
    // حفظ ملف PDF المحدث
    pdfDocument.save(_dataDir);    

  }
```