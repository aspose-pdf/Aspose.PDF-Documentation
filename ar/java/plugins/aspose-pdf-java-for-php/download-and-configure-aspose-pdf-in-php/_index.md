---
title: تنزيل وتكوين Aspose.PDF في PHP
linktitle: تنزيل وتكوين Aspose.PDF في PHP
type: docs
weight: 10
url: /java/download-and-configure-aspose-pdf-in-php/
description: تعرف على كيفية تنزيل Aspose.PDF وتكوينه بلغة PHP لسهولة التكامل ومعالجة ملفات PDF داخل مشاريع PHP الخاصة بك.
lastmod: "2026-06-09"
---
## تحميل المكتبات المطلوبة

قم بتنزيل المكتبات المطلوبة المذكورة أدناه. هذه هي العناصر المطلوبة لتنفيذ Aspose.PDF Java لأمثلة PHP.

- **Aspose:** [Aspose.PDF لمكون Java](https://downloads.aspose.com/pdf/java)
- PHP / جسر جافا

## قم بتنزيل أمثلة من مواقع الترميز الاجتماعي

الإصدارات التالية من الأمثلة الجارية متاحة للتنزيل على مواقع الترميز الاجتماعي المذكورة أدناه:

### جيثب

- **Aspose.PDF Java لأمثلة PHP**
  - [Aspose.PDF Java لـ PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

## كيفية تكوين الكود المصدري على منصة Linux

يرجى اتباع هذه الخطوات البسيطة لفتح كود المصدر وتوسيعه أثناء الاستخدام:

## 1. قم بتثبيت خادم Tomcat

لتثبيت خادم Tomcat، أصدر الأمر التالي على وحدة تحكم Linux. سيؤدي هذا إلى تثبيت خادم Tomcat بنجاح.

{{< highlight actionscript3 >}}

 Sudo apt-get install tomcat8

{{< /highlight >}}

## 2. قم بتنزيل وتكوين PHP/JavaBridge

لتنزيل ثنائيات PHP/JavaBridge، قم بإصدار الأمر التالي على وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

قم بفك ضغط ثنائيات PHP/JavaBridge عن طريق إصدار الأمر التالي على وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  فك الضغط -d php-Java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

سيؤدي هذا إلى استخراج الملف **JavaBridge.war**В. انسخه إلى المجلد tomcat88В **webapps** В عن طريق إصدار الأمر التالي على وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

من خلال النسخ، سيقوم Tomcat8 تلقائيًا بإنشاء مجلد جديد "**JavaBridge**" في В **webapps**. بمجرد إنشاء المجلد، تأكد من تشغيل Tomcat8 ثم تحقق http://localhost:8080/JavaBridge في المتصفح، يجب أن يفتح صفحة JavaBridge الافتراضية.

إذا ظهرت أي رسالة خطأ، فقم بتثبيت **FastCGI**В عن طريق إصدار الأمر التالي على وحدة تحكم Linux.

{{< highlight actionscript3 >}}

  Sudo apt-get install php55-cgi

{{< /highlight >}}

بعد تثبيت php5.5 CGI، أعد تشغيل خادم Tomcat8 وتحقق من http://localhost:8080/JavaBridge مرة أخرى في المتصفح.

إذا تم عرض الخطأ **JAVA_HOME**В، فافتح الملف /etc/default/tomcat8 وقم بإلغاء التعليق على السطر الذي يقوم بتعيين JAVA_HOME. تحقق من В http://localhost:8080/JavaBridge В في المتصفح مرة أخرى، يجب أن يأتي مع صفحة أمثلة PHP/JavaBridge.

## 3. قم بتكوين Aspose.PDF Java لأمثلة PHP

استنساخ أمثلة PHP عن طريق إصدار الأوامر التالية داخل مجلد webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ جيت الحرف الأول&nbsp;

استنساخ $ git [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

## كيفية تكوين التعليمات البرمجية المصدر على نظام التشغيل Windows

يرجى اتباع الخطوات البسيطة أدناه لتكوين PHP/Java Bridge على نظام Windows الأساسي

1. قم بتثبيت PHP5 وقم بتكوينه كما تفعل عادةً
2. قم بتثبيت JRE 6 (Java Runtime Environment) إذا لم يكن لديك بالفعل. يمكنك التحقق من ذلك في C:\Program الملفات وما إلى ذلك. يمكنك تنزيله هنا. أنا أستخدم JRE 6 لأنه متوافق مع PHP Java Bridge (PJB).

3. تثبيت أباتشي Tomcat 8.0. يمكنك تنزيله هنا

4. تحميل JavaBridge.war.
5. انسخ هذا الملف إلى دليل Tomcat webapps.
(على سبيل المثال: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps )

6. أعد تشغيل خدمة Tomcat Apache.

7. انتقل إلى http://localhost:8080/JavaBridge/test.php للتحقق مما إذا كان PHP يعمل. يمكنك العثور على أمثلة أخرى هناك

8. انسخ ملف jar [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) إلى C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

9. استنساخ أمثلة [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) داخل مجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

10. انسخ المجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java إلى مجلد أمثلة Aspose.PDF Java for PHP.

11. أعد تشغيل خدمة Apache Tomcat وابدأ في استخدام الأمثلة.
