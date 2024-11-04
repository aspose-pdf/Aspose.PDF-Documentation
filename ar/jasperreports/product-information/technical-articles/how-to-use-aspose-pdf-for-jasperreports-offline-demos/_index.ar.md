---
title: كيفية - استخدام Aspose.Pdf لعروض JasperReports غير المتصلة بالإنترنت
type: docs
weight: 10
url: /jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

يتضمن Aspose.PDF لـ JasperReports عددًا من مشاريع العرض التوضيحي لمساعدتك على البدء في تصدير التقارير إلى تنسيقات PDF من تطبيقك. العروض التوضيحية هي عروض JasperReports القياسية التي تم تعديلها لإظهار كيفية استخدام المصدّرين الجدد.

{{% /alert %}}
### **تشغيل عروض Aspose.PDF لـ JasperReports التوضيحية**
لتشغيل عروض Aspose.PDF لـ JasperReports التوضيحية:

{{% alert color="primary" %}}

1. قم بتنزيل JasperReports من <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. تأكد من تنزيل المشروع المؤرشف بأكمله مع الشيفرة المصدرية والعروض التوضيحية، وليس مجرد ملف JAR واحد.
2. قم بفك المشروع المؤرشف إلى موقع ما على القرص الصلب، على سبيل المثال C:\.
3. 
انسخ جميع مجلدات العرض التوضيحي من مجلد \demo في **Aspose.PDF.JasperReports.zip** إلى ```<InstallDir>```\jasperreports\demo\samples، حيث أن ```<InstallDir>``` هو الموقع الذي قمت بفك ضغط JasperReports فيه. هذه الخطوة ضرورية لأن برامج بناء العرض التوضيحي تعتمد على هيكل مجلد JasperReports، وإلا يجب عليك تعديل برامج البناء.
4. انسخ ملف **aspose.pdf.jasperreports.jar** من مجلد \lib في **Aspose.PDF.JasperReports.zip** إلى ```<InstallDir>```\jasperreports\lib.
5. قم بتنزيل أداة ANT من <http://ant.apache.org/bindownload.cgi>.
6. فك ضغط أداة ANT وقم بإعداد متغيرات البيئة كما هو موضح في دليل الأداة.
7. قم بتغيير الدليل الحالي إلى ```<InstallDir>```\demo\hsqldb وقم بتشغيل الأمر التالي:
   ant runServer
8. افتح نافذة موجه أوامر جديدة وقم بتغيير الدليل الحالي إلى أحد عروض Aspose.PDF الخاصة بـ JasperReports التوضيحية، على سبيل المثال ```<InstallDir>```\demo\samples\charts.ap.
9. قم بتشغيل الأوامر التالية على سطر الأوامر:
10. 
``` ant javac – لتجميع ملفات مصدر Java لتطبيق الاختبار.  
11. ant compile – لتجميع تصميم تقرير XML وإنتاج ملف .jasper  
12. ant fill – لملء تصميم التقرير المجمع بالبيانات وإنتاج ملف .jrprint  
13. قم بتشغيل الأمر التالي في سطر الأوامر:  
    ant pdf – لإنتاج ملف PDF من تقرير العرض التوضيحي.  
14. افتح أحد المستندات الناتجة للعرض، على سبيل المثال ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf في Adobe Reader أو تطبيق آخر.  

{{% /alert %}}