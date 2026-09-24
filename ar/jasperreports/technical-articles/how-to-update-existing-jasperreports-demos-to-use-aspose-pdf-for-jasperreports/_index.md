---
title: كيفية - تحديث العروض التوضيحية الحالية لـ JasperReports لاستخدام Aspose.PDF for JasperReports
linktitle: كيفية - تحديث العروض التوضيحية الحالية لـ JasperReports لاستخدام Aspose.PDF for JasperReports
type: docs
weight: 20
url: /ar/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: تعرف على كيفية تحديث العروض التوضيحية الحالية لـ JasperReports للاستفادة من إمكانات Aspose.PDF for JasperReports.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

يتضمن Aspose.PDF for JasperReports عددًا من المشاريع التجريبية لمساعدتك على البدء في تصدير التقارير إلى PDF. تعتمد هذه العروض التوضيحية على عروض JasperReports التجريبية القياسية التي تم تعديلها لتوضيح كيفية استخدام المصدرين الجدد. يتناول هذا البرنامج التعليمي الخطوات المطلوبة لتحديث العروض التوضيحية الحالية لـ JasperReports لاستخدام Aspose.PDF for JasperReports.

{{% /alert %}}

## تحديث العروض التوضيحية لاستخدام Aspose.PDF

{{% alert color="primary" %}}

توضح الخطوات التالية كيفية تحديث العروض التوضيحية الموجودة لاستخدام Aspose.PDF لملحق التصدير JasperReports بدلاً من استخدام ميزة تصدير PDF القياسية الخاصة بـ JasperReport.

1. قم بتنزيل JasperReports من <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   تأكد من تنزيل المشروع المؤرشف بالكامل باستخدام الكود المصدري والعروض التوضيحية، وليس مجرد JAR واحد. تم إعداد هذا البرنامج التعليمي باستخدام JasperReports-3.5.2.
2. قم بفك ضغط المشروع المؤرشف في موقع ما على القرص الثابت لديك، على سبيل المثال C:\.
3. انسخ **aspose.pdf.jasperreports.jar** من المجلد \lib في **Aspose.PDF.JasperReports.zip** إلى ```<InstallDir>```\jasperreports\lib.
4. افتح ```<InstallDir>```\jasperreports\demo\samples، حيث يشير ```<InstallDir>``` إلى الموقع الذي قمت بفك ضغط JasperReports فيه، لتحديث العرض التوضيحي الموجود. إذا اخترت عرض الخطوط التوضيحي، على سبيل المثال، لاستخدامه مع Aspose.PDF for JasperReports، فأنشئ نسخة منه حتى يظل العرض التوضيحي الأصلي كما هو. ولأغراض هذا المثال، سمّينا المجلد الجديد **fonts.ap**.
ملاحظة: سيتم تشغيل العروض التوضيحية من ```<InstallDir>``` \jasperreports\demo\samples لأن البرامج النصية الخاصة ببناء العرض التوضيحي تعتمد على بنية مجلد JasperReports. إذا قمت بتغيير المجلد النموذجي، فيجب عليك تعديل البرامج النصية للإنشاء.
5. افتح الملف **FontsApp.java** من المجلد src وأضف مرجعًا إلى Aspose.PDF for JasperReports:
   import com.aspose.pdf.jr3_7_0.jasperreports.*;
   (نحن نستخدم jr3_7_0 لأنه تم إعداد هذا البرنامج التعليمي باستخدام JasperReports 3.5.2.)
6. إضافة سلسلة جديدة:
   السلسلة النهائية الثابتة الخاصة TASK_ASPOSE_PDF = "aspose_pdf"; إلى جانب المتغيرات الموجودة كخيار تصدير عبر Aspose.PDF for JasperReports.
7. حدد موقع مقطع التعليمات البرمجية لـ else if (TASK_PDF.equals(taskName)) وانسخ المقطع بأكمله.
8. الصق مقتطف الشفرة أسفل المقطع نفسه.

```java
 else if (TASK_PDF.equals(taskName))
{
  File sourceFile = new File(fileName);
  JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
  File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");
  JRPdfExporter exporter = new JRPdfExporter();
  HashMap fontMap = new HashMap();
  FontKey key = new FontKey("DejaVu Serif", true, false);
  PdfFont font = new PdfFont("DejaVuSerif-Bold.ttf", "Cp1252", true);
  fontMap.put(key, font);
  exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);
  exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());
  exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
  exporter.exportReport();
  System.err.println("PDF creation time : " + (System.currentTimeMillis() - start));
}
```

```text
update
else if (TASK_PDF.equals(taskName))
as
else if (TASK_ASPOSE_PDF.equals(taskName))
replace
JRPdfExporter exporter = new JRPdfExporter();
with
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
```

9. افتح الملف **build.xml**.
10. قم بعمل نسخة من المقطع التالي ووضعه داخل نفس الملف:

```xml
 <target name="pdf" description="Generat PDF via Aspose.PDF for JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```diff
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. لتشغيل العرض التوضيحي:
   -  Download the ANT tool from <http://ant.apache.org/bindownload.cgi>.
   - قم بفك أداة ANT وإعداد متغيرات البيئة كما هو موضح في دليل الأداة.
   -  قم بتغيير الدليل الحالي إلى <InstallDir>\demo\hsqldb وقم بتشغيل سطر الأوامر التالي:
      النمل runServer
12. افتح مثيل موجه أوامر جديد وغيّر الدليل الحالي إلى <InstallDir>\demo\samples\fonts.ap ثم شغّل الأوامر التالية في سطر الأوامر:
13. ant javac – لتجميع ملفات Java المصدرية لتطبيق الاختبار
14. ant compile – to compile the XML report design and produce the .jasper file
15. تعبئة النمل - لملء تصميم التقرير المجمع بالبيانات وإنتاج ملف .jrprint
16. ant aspose_pdf – to produce a PDF file using Aspose.PDF for JasperReports.
17. Open the resultant PDF (**FontsReport.pdf**) from the <InstallDir>\demo\samples\ fonts.ap\build\reports\ folder.

{{% /alert %}}


