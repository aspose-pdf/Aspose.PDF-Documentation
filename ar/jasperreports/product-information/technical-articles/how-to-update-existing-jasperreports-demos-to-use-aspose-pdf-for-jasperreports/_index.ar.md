---
title: كيفية - تحديث عروض JasperReports الحالية لاستخدام Aspose.Pdf لـ JasperReports
type: docs
weight: 20
url: /jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

يتضمن Aspose.PDF لـ JasperReports عددًا من مشاريع العروض التوضيحية لمساعدتك على البدء في تصدير التقارير إلى PDF. تستند هذه العروض إلى عروض JasperReports القياسية التي تم تعديلها لتوضيح كيفية استخدام المصدرين الجدد. يوضح هذا الدليل الخطوات المطلوبة لتحديث عروض JasperReports الحالية لاستخدام Aspose.PDF لـ JasperReports.

{{% /alert %}}
### **تحديث العروض لاستخدام Aspose.PDF**

{{% alert color="primary" %}}

توضح الخطوات التالية كيفية تحديث العروض الحالية لاستخدام امتداد تصدير Aspose.PDF لـ JasperReports بدلاً من استخدام ميزة تصدير PDF القياسية لـ JasperReport.

1. قم بتنزيل JasperReports من <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. تأكد من تنزيل المشروع المؤرشف بالكامل مع كود المصدر والعروض التوضيحية، وليس فقط ملف JAR واحد. هذا الدليل تم إعداده باستخدام JasperReports-3.5.2.  
2. قم بفك ضغط المشروع المؤرشف إلى موقع ما على القرص الصلب لديك، على سبيل المثال C:\.  
3. انسخ **aspose.pdf.jasperreports.jar** من المجلد \lib في **Aspose.PDF.JasperReports.zip** إلى ```<InstallDir>```\jasperreports\lib.  
4. افتح ```<InstallDir>```\jasperreports\demo\samples، (حيث ```<InstallDir>``` هو الموقع الذي قمت بفك ضغط JasperReports فيه) لتحديث عرض توضيحي موجود. إذا كنت قد اخترت عرض الخطوط التوضيحي، على سبيل المثال، لاستخدامه مع Aspose.PDF لـ JasperReports، قم بإنشاء نسخة منه بحيث يبقى العرض التوضيحي الأصلي كما هو. لغرض هذا المثال، قمنا بتسمية المجلد الجديد **fonts.ap**.  
ملاحظة: ستعمل العروض التوضيحية من ```<InstallDir>``` \jasperreports\demo\samples لأن نصوص بناء العروض التوضيحية تعتمد على هيكل مجلد JasperReports. إذا قمت بتغيير مجلد العينة، يجب عليك تعديل نصوص البناء.  
5. افتح ملف **FontsApp.java** من المجلد src وأضف مرجعًا لـ Aspose.PDF لـ JasperReports:  

   import com.aspose.pdf.jr3_7_0.jasperreports.*;  (نحن نستخدم jr3_7_0 لأن هذا الشرح تم إعداده باستخدام JasperReports 3.5.2.)
6. أضف سلسلة جديدة:
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; جنبًا إلى جنب مع المتغيرات الموجودة كخيار تصدير عبر Aspose.PDF لـ JasperReports.
7. حدد موقع مقطع الكود else if (TASK_PDF.equals(taskName)) ونسخ المقطع بأكمله.
8. الصق جزء الكود تحت نفس المقطع.

```
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
```java
exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
exporter.exportReport();
System.err.println("PDF creation time : " + (System.currentTimeMillis() - start));
}
```

```
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
9. قم بفتح ملف **build.xml**.
10. قم بعمل نسخة من المقطع التالي وضعه داخل نفس الملف:

```
<target name="pdf" description="Generat PDF via Aspose.PDF for JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. لتشغيل العرض التوضيحي:

   - قم بتنزيل أداة ANT من <http://ant.apache.org/bindownload.cgi>.
```
    - قم بفك ضغط أداة ANT وقم بإعداد متغيرات البيئة كما هو موضح في دليل الأداة.
    - قم بتغيير الدليل الحالي إلى <InstallDir>\demo\hsqldb وقم بتشغيل سطر الأوامر التالي:
      ant runServer
12. افتح نافذة موجه أوامر جديدة وقم بتغيير الدليل الحالي إلى <InstallDir>\demo\samples\fonts.ap وقم بتشغيل الأوامر التالية في سطر الأوامر:
13. ant javac – لترجمة ملفات مصدر Java لتطبيق الاختبار
14. ant compile – لترجمة تصميم تقرير XML وإنتاج ملف .jasper
15. ant fill – لملء تصميم التقرير المترجم بالبيانات وإنتاج ملف .jrprint
16. ant aspose_ pdf – لإنتاج ملف PDF باستخدام Aspose.PDF لـ JasperReports.
17. افتح ملف PDF الناتج (**FontsReport.pdf**) من المجلد <InstallDir>\demo\samples\ fonts.ap\build\reports\.

{{% /alert %}}