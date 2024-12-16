---
title: تحميل وتكوين Aspose.PDF في PHP
type: docs
weight: 10
url: /ar/java/download-and-configure-aspose-pdf-in-php/
lastmod: "2021-06-05"
---

## تحميل المكتبات المطلوبة

قم بتنزيل المكتبات المطلوبة المذكورة أدناه. هذه هي المطلوبة لتنفيذ أمثلة Aspose.PDF Java لـ PHP.

- **Aspose:** [مكون Aspose.PDF لـ Java](https://downloads.aspose.com/pdf/java)
- جسر PHP/Java

## تنزيل الأمثلة من مواقع البرمجة الاجتماعية

الإصدارات التالية من الأمثلة الجارية متاحة للتنزيل على مواقع البرمجة الاجتماعية المذكورة أدناه:

### GitHub

- **أمثلة Aspose.PDF Java لـ PHP**
  - [Aspose.PDF Java لـ PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## كيفية تكوين الكود المصدري على منصة Linux

يرجى اتباع هذه الخطوات البسيطة من أجل فتح وتوسيع الكود المصدري أثناء الاستخدام:

## 1. تثبيت خادم Tomcat

لتثبيت خادم Tomcat، قم بإصدار الأمر التالي على وحدة تحكم Linux. سيؤدي ذلك إلى تثبيت خادم Tomcat بنجاح.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. قم بتنزيل وتكوين PHP/JavaBridge

من أجل تنزيل ملفات PHP/JavaBridge التنفيذية، قم بإصدار الأمر التالي في وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


قم بفك ضغط ملفات PHP/JavaBridge التنفيذية عن طريق إصدار الأمر التالي في وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}


سيؤدي هذا إلى استخراج ملف **JavaBridge.war**. انسخه إلى مجلد **webapps** في tomcat8 عن طريق إصدار الأمر التالي في وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}


عن طريق النسخ، سيقوم tomcat8 بإنشاء مجلد جديد تلقائيًا باسم "**JavaBridge**" في **webapps**.
 بمجرد إنشاء المجلد، تأكد من تشغيل tomcat8 ثم تحقق من  http://localhost:8080/JavaBridge  في المتصفح، يجب أن يفتح صفحة JavaBridge الافتراضية.

إذا ظهرت أي رسالة خطأ، قم بتثبيت **FastCGI** عن طريق إصدار الأمر التالي في وحدة تحكم لينكس.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

بعد تثبيت php5.5 CGI، أعد تشغيل خادم tomcat8 وتحقق من  http://localhost:8080/JavaBridge  مرة أخرى في المتصفح.

إذا ظهرت خطأ **JAVA_HOME**، افتح الملف /etc/default/tomcat8 وقم بإلغاء تعليق السطر الذي يحدد JAVA_HOME. تحقق من  http://localhost:8080/JavaBridge  في المتصفح مرة أخرى، يجب أن يظهر الصفحة مع أمثلة PHP/JavaBridge.

## 3. تكوين Aspose.PDF Java لأمثلة PHP

استنسخ أمثلة PHP عن طريق إصدار الأوامر التالية داخل مجلد webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;


$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]
{{< /highlight >}}

## كيفية تهيئة الشيفرة المصدرية على نظام ويندوز

يرجى اتباع الخطوات البسيطة أدناه لتهيئة PHP/Java Bridge على منصة ويندوز

1. قم بتثبيت PHP5 وقم بتكوينه كما تفعل عادةً
2. قم بتثبيت JRE 6 (بيئة تشغيل Java) إذا لم تكن مثبتة لديك بالفعل. يمكنك التحقق من ذلك في C:\Program Files وما إلى ذلك. يمكنك تنزيله من هنا. أنا أستخدم JRE 6 لأنه متوافق مع PHP Java Bridge (PJB).

3. قم بتثبيت Apache Tomcat 8.0. يمكنك تنزيله من هنا

4. قم بتنزيل JavaBridge.war.
5. انسخ هذا الملف إلى دليل webapps في tomcat.
(مثال: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

6. أعد تشغيل خدمة tomcat apache.

7. اذهب إلى http://localhost:8080/JavaBridge/test.php للتحقق مما إذا كان PHP يعمل. يمكنك العثور على أمثلة أخرى هناك

8. انسخ ملف jar الخاص بـ [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) إلى C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. استنساخ [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) الأمثلة داخل المجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. نسخ المجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java إلى مجلد أمثلة Aspose.PDF Java for PHP الخاص بك.

11. إعادة تشغيل خدمة apache tomcat وبدء استخدام الأمثلة.