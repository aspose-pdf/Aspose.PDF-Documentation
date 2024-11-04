---

title: العمل مع JasperServer

type: docs

weight: 20

url: /jasperreports/working-with-jasperserver/

lastmod: "2021-06-05"

---



#### <ins>**تعيين معلمة Exporter الخاصة بـ licenseFile في applicationContext.xml**

{{% alert color="primary" %}}



تُستخدم هذه الطريقة مع JasperServer.



{{% /alert %}}



1. قم بتنزيل الترخيص على جهاز الكمبيوتر الخاص بك ونسخه إلى مجلد ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF``` حيث يشير ```<InstallDir>``` إلى دليل تثبيت JasperServer.

2. حدد موقع الملف ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` وأضف الأسطر التالية:



```

 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  

    INF/Aspose.Total.JasperReports.lic"/>

</bean>

```

{{% alert color="primary" %}}


ملاحظة: يرجى ملاحظة أن مسار التثبيت يجب ألا يحتوي على أي مسافات، على سبيل المثال C:/Program Files/JasperServer… لأن ذلك يسبب مشاكل عند الوصول إلى ملف الترخيص.

{{% /alert %}}



#### **تحقق من أن الرخصة تعمل**

قم بتصدير أي تقرير إلى صيغة PDF وتحقق مما إذا كان التقرير يحتوي على رسالة تقييم. إذا لم تكن هناك رسالة تقييم، فهذا يعني أن الرخصة تعمل بشكل صحيح.



**يقوم Aspose.PDF for JasperReports بإضافة علامة مائية عند العمل في وضع التقييم**



![todo:image_alt_text](working-with-jasperserver_1.png)







**يقوم Aspose.PDF for JasperReports بإضافة علامة مائية عند العمل في وضع التقييم**



![todo:image_alt_text](working-with-jasperserver_2.png)