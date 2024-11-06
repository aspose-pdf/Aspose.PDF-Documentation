---
title: Aspose.PDF Java for PHP
type: docs
weight: 50
url: ar/java/aspose-pdf-java-for-php/
lastmod: "2021-06-05"
---

## مقدمة إلى Aspose.PDF Java for PHP

### جسر PHP / Java

جسر PHP/Java هو تنفيذ لبروتوكول شبكة مبني على XML يعتمد على التدفق، والذي يمكن استخدامه لربط محرك نصوص أصلي، على سبيل المثال PHP أو Scheme أو Python، مع آلة جافا الافتراضية. إنه أسرع بما يصل إلى 50 مرة من RPC المحلي عبر SOAP، ويتطلب موارد أقل على جانب خادم الويب. إنه أسرع وأكثر موثوقية من التواصل المباشر عبر واجهة Java الأصلية، ولا يتطلب أي مكونات إضافية لاستدعاء إجراءات جافا من PHP أو إجراءات PHP من جافا.

اقرأ المزيد في [sourceforge.net](http://php-java-bridge.sourceforge.net/pjb/)

### Aspose.PDF لجافا

Aspose.PDF لجافا هو مكون إنشاء مستندات PDF يمكنه تمكين تطبيقات جافا الخاصة بك من قراءة وكتابة ومعالجة مستندات PDF دون استخدام Adobe Acrobat.

Aspose.PDF for Java هو مكون بسعر معقول يقدم ثروة مذهلة من الميزات، تشمل هذه الميزات: خيارات ضغط PDF، إنشاء الجداول والتلاعب بها، دعم الرسوم البيانية، وظائف الصور، وظائف الروابط التشعبية الواسعة، ضوابط الأمان الموسعة ومعالجة الخطوط المخصصة.

يسمح لك Aspose.PDF for Java بإنشاء ملفات PDF مباشرة من خلال الـ API والنماذج XML المقدمة. ستتيح لك استخدام Aspose.PDF for Java إضافة قدرات PDF إلى تطبيقاتك في وقت قصير.

### Aspose.PDF Java for PHP

يظهر مشروع Aspose.PDF for PHP كيف يمكن تنفيذ مهام مختلفة باستخدام Aspose.PDF Java APIs في PHP. يهدف هذا المشروع إلى توفير أمثلة مفيدة لمطوري PHP الذين يرغبون في استخدام Aspose.PDF for Java في مشاريع PHP الخاصة بهم باستخدام [PHP/Java Bridge](http://php-java-bridge.sourceforge.net/pjb/).

## متطلبات النظام والمنصات المدعومة

### متطلبات النظام

فيما يلي متطلبات النظام لاستخدام Aspose.PDF لـ PHP عبر Java:

- تم تثبيت خادم Tomcat 8.0 أو أعلى.
- تم تكوين PHP/JavaBridge.
- تم تثبيت FastCGI.
- تم تنزيل مكون Aspose.PDF.

### الأنظمة المدعومة

الأنظمة المدعومة هي كالتالي:

- PHP 5.3 أو أعلى
- Java 1.8 أو أعلى

## التنزيل والتكوين

### تحميل المكتبات المطلوبة

قم بتنزيل المكتبات المطلوبة المذكورة أدناه. هذه مطلوبة لتنفيذ أمثلة Aspose.PDF Java لـ PHP.

- **Aspose:** [مكون Aspose.PDF لJava](https://downloads.aspose.com/pdf/java)
- جسر PHP/Java

### تنزيل الأمثلة من مواقع البرمجة الاجتماعية

الإصدارات التالية من الأمثلة التشغيلية متاحة للتنزيل على مواقع البرمجة الاجتماعية المذكورة أدناه:

### GitHub

- أمثلة Aspose.PDF Java لـ PHP
  - [Aspose.PDF Java لـ PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)

### كيفية تكوين الكود المصدري على نظام Linux

يرجى اتباع هذه الخطوات البسيطة من أجل فتح وتوسيع الكود المصدري أثناء الاستخدام:

### 1. تثبيت خادم Tomcat

لتثبيت خادم tomcat، قم بإصدار الأمر التالي على وحدة التحكم linux. سيتم تثبيت خادم tomcat بنجاح.

{{< highlight actionscript3 >}}

 sudo apt-get install tomcat8

{{< /highlight >}}

### 2. تحميل وتكوين PHP/JavaBridge

من أجل تحميل ملفات PHP/JavaBridge الثنائية، نفذ الأمر التالي على وحدة التحكم في لينكس.

{{< highlight actionscript3 >}}

  wget http://citylan.dl.sourceforge.net/project/php-java-bridge/Binary%20package/php-java-bridge_6.2.1/php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

قم بفك ضغط ملفات PHP/JavaBridge الثنائية عن طريق تنفيذ الأمر التالي على وحدة التحكم في لينكس.

{{< highlight actionscript3 >}}

  unzip -d php-java-bridge_6.2.1_documentation.zip

{{< /highlight >}}

سيؤدي هذا إلى استخراج ملف **JavaBridge.war**. قم بنسخه إلى مجلد **webapps** في tomcat8 عن طريق تنفيذ الأمر التالي على وحدة التحكم في لينكس.

{{< highlight actionscript3 >}}

  sudo cp JavaBridge.war /var/lib/tomcat8/webapps/JavaBridge.war

{{< /highlight >}}

عن طريق النسخ، سيقوم tomcat8 تلقائيًا بإنشاء مجلد جديد "**JavaBridge**" في **webapps**.

إذا ظهرت أي رسالة خطأ، قم بتثبيت **FastCGI** عن طريق تنفيذ الأمر التالي على وحدة التحكم في لينكس.

{{< highlight actionscript3 >}}

  sudo apt-get install php55-cgi

{{< /highlight >}}

إذا تم عرض خطأ **JAVA_HOME**، قم بفتح ملف /etc/default/tomcat8 وقم بإلغاء تعليق السطر الذي يعيّن JAVA_HOME.

### 3. تكوين أمثلة Aspose.PDF Java لـ PHP

قم باستنساخ أمثلة PHP عبر إصدار الأوامر التالية داخل مجلد webapps/JavaBridge.

{{< highlight actionscript3 >}}

$ git init&nbsp;

$ git clone [https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose.PDF-for-Java_for_PHP]

{{< /highlight >}}

### كيفية تكوين الكود المصدري على منصة ويندوز

يرجى اتباع الخطوات البسيطة أدناه لتكوين PHP/Java Bridge على منصة ويندوز

1. قم بتثبيت PHP5 وتكوينه كما تفعل عادةً
2. قم بتثبيت JRE 6 (بيئة تشغيل Java) إذا لم يكن لديك بالفعل. يمكنك التحقق من ذلك في C:\Program Files إلخ. يمكنك تنزيله هنا. أنا أستخدم JRE 6 لأنه متوافق مع PHP Java Bridge (PJB).

3. قم بتثبيت Apache Tomcat 8.0. يمكنك تنزيله هنا

4. قم بتنزيل [JavaBridge.war](https://sourceforge.net/projects/php-java-bridge/files/Binary%20package/php-java-bridge_6.2.1/JavaBridgeTemplate621.war/download). انسخ هذا الملف إلى دليل تطبيقات الويب في tomcat.
(مثال: C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps)

5. أعد تشغيل خدمة apache tomcat.

6. اذهب إلى http://localhost:8080/JavaBridge/test.php للتحقق مما إذا كان php يعمل. يمكنك العثور على أمثلة أخرى هناك.

7. انسخ ملف jar الخاص بـ [Aspose.PDF Java](https://downloads.aspose.com/pdf/java) إلى C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\WEB-INF\lib

8. استنسخ أمثلة [Aspose.PDF Java for PHP](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP) داخل المجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\.

9. انسخ المجلد C:\Program Files\Apache Software Foundation\Tomcat 8.0\webapps\JavaBridge\java إلى مجلد أمثلة Aspose.PDF Java for PHP الخاص بك.

10. أعد تشغيل خدمة apache tomcat وابدأ في استخدام الأمثلة.

## الدعم، التوسيع والمساهمة

### الدعم

منذ الأيام الأولى لشركة Aspose، كنا نعرف أن مجرد تقديم منتجات جيدة لعملائنا لن يكون كافياً. كنا بحاجة أيضاً لتقديم خدمة جيدة. نحن مطورون بأنفسنا ونتفهم مدى الإحباط عندما تتسبب مشكلة تقنية أو خلل في البرنامج في إيقافك عن القيام بما تحتاج إلى القيام به. نحن هنا لحل المشاكل، وليس لإنشائها.

لهذا السبب نقدم الدعم المجاني. أي شخص يستخدم منتجنا، سواء قام بشرائه أو كان يستخدمه كتجربة، يستحق اهتمامنا الكامل واحترامنا.

يمكنك تسجيل أي قضايا أو اقتراحات متعلقة بـ Aspose.Cells Java for PHP باستخدام أي من المنصات التالية:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### التوسيع والمساهمة

Aspose.PDF Java for PHP هو مفتوح المصدر، وكود المصدر متاح على مواقع البرمجة الاجتماعية الكبرى المذكورة أدناه.
 يشجع المطورون على تنزيل الشيفرة المصدرية والمساهمة باقتراح أو إضافة ميزة جديدة أو تحسين الميزات الحالية، حتى يتمكن الآخرون أيضًا من الاستفادة منها.

### الشيفرة المصدرية

يمكنك الحصول على أحدث شيفرة مصدرية من أحد المواقع التالية

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_Java_for_PHP)