---
title: Downloads and Configure Aspose.Pdf in Struts 1.3
type: docs
weight: 10
url: /ar/java/downloads-and-configure-aspose-pdf-in-struts-1-3/
lastmod: "2021-06-05"
---

## تنزيل Aspose.PDF Java لـ Struts 1.3

يمكنك تنزيل / التحقق من أكواد مصدر المشروع من المواقع التالية:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_for_Struts)

## بناء Aspose.PDF Java لـ Struts 1.3 من أكواد المصدر

بعد التحقق من أكواد المصدر من أي من المستودعات المذكورة أعلاه، قم بتطبيق أوامر mvn التالية:

{{< highlight java >}}

 $ mvn -U clean package

{{< /highlight >}}

سيقوم هذا ببناء "Strutsbookapp.war" في مجلد الهدف.

لنشر ملف .war فقط قم بنسخه إلى دليل webapp الخاص بخادم Apache tomcat الذي يعمل.