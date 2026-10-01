---
title: تنزيل وتكوين Aspose.PDF في PHP
linktitle: تنزيل وتكوين Aspose.PDF في PHP
type: docs
weight: 10
url: /ar/java/download-and-configure-aspose-pdf-in-php/
description: تعرف على كيفية تنزيل وتكوين Aspose.PDF في PHP لتسهيل التكامل ومعالجة ملفات PDF داخل مشاريع PHP الخاصة بك.
lastmod: "2026-10-01"
---
## تنزيل المكتبات المطلوبة

قم بتنزيل المكتبات المطلوبة المذكورة أدناه. هذه هي المطلوبة لتشغيل أمثلة Aspose.PDF Java لـ PHP.

- **Aspose:** [مكوّن Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)
- جسر PHP/Java

## تحميل الأمثلة من مواقع الترميز الاجتماعي

الإصدارات التالية من الأمثلة القابلة للتشغيل متاحة للتنزيل على مواقع الترميز الاجتماعي المذكورة أدناه:

### GitHub

- **Aspose.PDF Java for PHP أمثلة**
  - [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## كيفية تكوين شفرة المصدر على منصة Linux

يرجى اتباع هذه الخطوات البسيطةВ من أجل فتح وتوسيع شفرة المصدر أثناء الاستخدام:

## 1. تثبيت خادم Tomcat

لتثبيت خادم Tomcat، نفّذ الأمر التالي على وحدة تحكم Linux.В سيتم تثبيت خادم Tomcat بنجاح.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

## 2. تنزيل وتكوين PHP/JavaBridge

من أجل تنزيل ملفات PHP/JavaBridge الثنائية، نفّذ الأمر التالي على وحدة تحكم لينكس.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

افك ضغط ملفات PHP/JavaBridge الثنائية بتنفيذ الأمر التالي على وحدة تحكم لينكس.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

سيتم استخراجВ **JavaBridge.war**В ملف. انسخه إلى tomcat88В **webapps**В المجلد عن طريق تنفيذ الأمر التالي في وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

عن طريق النسخ، سيقوم tomcat8 بإنشاء مجلد جديد "**JavaBridge**" في **webapps**. بمجرد إنشاء المجلد، تأكد من تشغيل tomcat8 ثم قم بالتحقق  http://localhost:8080/JavaBridge  في المتصفح، يجب أن تفتح الصفحة الافتراضية لـ JavaBridge.

إذا ظهرت أي رسالة خطأ فقم بتثبيتВ  **FastCGI**В عن طريق تنفيذ الأمر التالي في وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

بعد تثبيت php5.5 CGI، أعد تشغيل خادم tomcat8 وتحققВ  http://localhost:8080/JavaBridge В مرة أخرى في المتصفح.

إذاВ **JAVA_HOME**В ظهر خطأ، فافتح ملف /etc/default/tomcat8 وألغي التعليق عن السطر الذي يحدد JAVA_HOME. تحققВ http://localhost:8080/JavaBridge В في المتصفح مرة أخرى، يجب أن تكون مع صفحة أمثلة PHP/JavaBridge.

## 3. تكوين Aspose.PDF Java لأمثلة PHP

استنساخ، أمثلة PHP عن طريق تنفيذ الأوامر التالية داخل مجلد webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## كيفية تكوين شفرة المصدر على نظام Windows

يرجى اتباع الخطوات البسيطة أدناه لتكوين PHP/Java Bridge على منصة Windows

1. قم بتثبيت PHP5 وقم بتكوينها كما تفعل عادةً
2. قم بتثبيت JRE 6 (بيئة تشغيل جافا) إذا لم تكن donвЂ™t لديك بالفعل. يمكنك التحقق من ذلك في C:\Program Files إلخ. يمكنك تحميله من هنا . أنا أستخدم JRE 6 لأنه متوافق مع PHP Java Bridge (PJB).

3. قم بتثبيت Apache Tomcat 8.0. يمكنك تحميله من هنا

4. قم بتنزيل JavaBridge.war.
5. انسخ هذا الملف إلى دليل webapps الخاص بـ tomcat.
(مثال: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. أعد تشغيل خدمة tomcat apache.

7. اذهب إلى  http://localhost:8080/JavaBridge/test.php  للتحقق مما إذا كانت PHP تعمل. يمكنك العثور على أمثلة أخرى هناك

8. انسخ الخاص بك [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) ملف jar إلى C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. استنساخ [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) الأمثلة داخل المجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. انسخ المجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java إلى مجلد أمثلة Aspose.PDF Java for PHP الخاص بك.

11. أعد تشغيل خدمة Apache Tomcat وابدأ في استخدام الأمثلة.
