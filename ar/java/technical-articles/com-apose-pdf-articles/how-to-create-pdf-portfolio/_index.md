---
title: كيفية إنشاء ملف PDF Portfolio
type: docs
weight: 10
url: ar/java/how-to-create-pdf-portfolio/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسمح لك ملفات PDF portfolios بتجميع المحتوى من مجموعة متنوعة من المصادر (على سبيل المثال، PDF، Word، Excel، ملفات JPEG) في حاوية موحدة واحدة. تحتفظ الملفات الأصلية بهوياتها الفردية ولكن يتم تجميعها في ملف PDF portfolio. يمكن للمستخدمين فتح وقراءة وتحرير وتنسيق كل ملف مكون بشكل مستقل عن الملفات المكونة الأخرى.

تتيح Aspose.PDF for Java إنشاء مستندات PDF Portfolio باستخدام فئة Document. قم بتحميل الملف الفردي في كائن FileSpecification وأضفها إلى كائن Document.Collection باستخدام الطريقة add(...). بمجرد إضافة الملفات، استخدم طريقة save(..) الخاصة بفئة Document لتوليد مستند portfolio.

{{% /alert %}}

## عينة كود

المثال التالي يستخدم ملف Microsoft XPS، مستند Word، ملف PDF وملف صورة لإنشاء PDF Portfolio.

**ملف PDF portfolio تم إنشاؤه باستخدام Aspose.PDF**

![todo:نص بديل للصورة](how-to-create-pdf-portfolio_1.png)

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "CreatePDFPortfolio.java" >}}