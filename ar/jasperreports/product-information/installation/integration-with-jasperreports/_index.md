---

title: التكامل مع JasperReports

type: docs

weight: 20

url: ar/jasperreports/integration-with-jasperreports/

lastmod: "2021-06-05"

---



{{% alert color="primary" %}}



لاستخدام Aspose.PDF لـ JasperReports في تطبيقك، انسخ **aspose.pdf.jasperreports.jar** من المجلد \lib في **Aspose.PDF.JasperReports.zip** إلى دليل JasperReports\lib، أو إلى مجلد مكتبة في تطبيقك. بعد ذلك، يمكنك الوصول إلى المصدرين برمجيًا.



{{% /alert %}}



يوضح المثال التالي الكود النموذجي المطلوب لتصدير تقرير إلى تنسيق PDF باستخدام Aspose.PDF لـ JasperReports. يمكن العثور على المزيد من الأمثلة في تقارير العرض التوضيحي المضمنة في تحميل المنتج.



{{< highlight csharp >}}



   import com.aspose.pdf.jr3_7_0.jasperreports.*;



   com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf. jr3_7_0.jasperreports.JrPdfExporter();





   File sourceFile = new File(fileName);




   JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
```

```java
exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.exportReport();
```

{{< /highlight >}}

تم اختبار مقتطف الشيفرة أعلاه مع JasperReports 3.5.2. إذا كنت تستخدم JasperReports 3.1.0، يرجى محاولة استخدام import com.aspose.pdf.jr3_1_0.jasperreports.; واستبدال إصدار المنتج في بقية الشيفرة أيضًا.