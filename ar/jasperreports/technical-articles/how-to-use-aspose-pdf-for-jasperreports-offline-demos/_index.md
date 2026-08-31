---
title: كيفية - استخدام Aspose.PDF للعروض التوضيحية غير المتصلة بالإنترنت لـ JasperReports
linktitle: كيفية - استخدام Aspose.PDF للعروض التوضيحية غير المتصلة بالإنترنت لـ JasperReports
type: docs
weight: 10
url: /ar/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
description: استكشف العروض التوضيحية غير المتصلة بالإنترنت لـ Aspose.PDF for JasperReports. تعلم التطبيقات والميزات العملية بطريقة عملية.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

يتضمن Aspose.PDF for JasperReports عددًا من المشاريع التجريبية لمساعدتك على البدء في تصدير التقارير إلى تنسيقات PDF من تطبيقك. العروض التوضيحية هي عروض توضيحية قياسية لـ JasperReports تم تعديلها لتوضيح كيفية استخدام المصدرين الجدد.

{{% /alert %}}

## تشغيل العروض التوضيحية لـ Aspose.PDF for JasperReports

لتشغيل Aspose.PDF للعروض التوضيحية لـ JasperReports:

{{% alert color="primary" %}}

1. قم بتنزيل JasperReports من <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. وتأكد من تنزيل المشروع المؤرشف بالكامل باستخدام الكود المصدري والعروض التوضيحية، وليس مجرد JAR واحد.
2. قم بفك ضغط المشروع المؤرشف في موقع ما على القرص الثابت لديك، على سبيل المثال C:\.
3. انسخ جميع المجلدات التجريبية من المجلد \demo في **Aspose.PDF.JasperReports.zip** إلى ```<InstallDir>```\jasperreports\demo\samples، حيث يشير ```<InstallDir>``` إلى الموقع الذي قمت بفك ضغط JasperReports إليه. هذه الخطوة مطلوبة لأن البرامج النصية للبناء التجريبي تعتمد على بنية مجلد JasperReports، وإلا فسيتعين عليك تعديل البرامج النصية للبناء.
4. انسخ الملف **aspose.pdf.jasperreports.jar** من المجلد \lib في **Aspose.PDF.JasperReports.zip** إلى ```<InstallDir>```\jasperreports\lib.
5. قم بتنزيل أداة ANT من <http://ant.apache.org/bindownload.cgi>.
6. قم بفك أداة ANT وإعداد متغيرات البيئة كما هو موضح في دليل الأداة.
7. غيّر الدليل الحالي إلى ```<InstallDir>```\demo\hsqldb ثم شغّل الأمر التالي:
   ant runServer
8. افتح مثيل موجه الأوامر الجديد وقم بتغيير الدليل الحالي إلى أحد ملفات Aspose.PDF للعروض التوضيحية لـ JasperReports، على سبيل المثال ```<InstallDir>```\demo\samples\charts.ap.
9. قم بتشغيل الأوامر التالية في سطر الأوامر:
10. ant javac – لتجميع ملفات Java المصدرية لتطبيق الاختبار.
11. ترجمة النمل – لتجميع تصميم تقرير XML وإنتاج ملف .jasper
12. تعبئة النمل - لملء تصميم التقرير المجمع بالبيانات وإنتاج ملف .jrprint
13. قم بتشغيل الأمر التالي في سطر الأوامر:
   ant pdf – لإنتاج ملف PDF من التقرير التجريبي.
14. افتح أحد المستندات الناتجة لعرضها، على سبيل المثال ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf في Adobe Reader أو أي تطبيق آخر.

{{% /alert %}}


