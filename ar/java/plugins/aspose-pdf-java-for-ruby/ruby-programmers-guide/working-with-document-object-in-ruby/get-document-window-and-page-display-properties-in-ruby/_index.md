---
title: الحصول على خصائص نافذة المستند وعرض الصفحة في روبي
type: docs
weight: 40
url: /ar/java/get-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - الحصول على خصائص نافذة المستند وعرض الصفحة

للحصول على خصائص نافذة المستند وعرض الصفحة لمستند PDF باستخدام **Aspose.PDF Java for Ruby**، قم ببساطة باستدعاء وحدة **GetDocumentWindow**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح مستند pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# الحصول على خصائص المستند المختلفة

# موضع نافذة المستند - الافتراضي: false

puts "CenterWindow :- " + doc.getCenterWindow().to_s

# ترتيب القراءة السائد؛ تحديد موضع الصفحة

# عند العرض جنبًا إلى جنب - الافتراضي: L2R

puts "Direction :- " + doc.getDirection().to_s

# ما إذا كان يجب على شريط عنوان النافذة عرض عنوان المستند.

# إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false

puts "DisplayDocTitle :- " + doc.getDisplayDocTitle().to_s

# ما إذا كان يجب تغيير حجم نافذة المستند لتناسب حجم

# الصفحة المعروضة الأولى - الافتراضي: false

puts "FitWindow :- " + doc.getFitWindow().to_s

# ما إذا كان يجب إخفاء شريط القوائم لتطبيق العارض - الافتراضي: false

puts "HideMenuBar :-" + doc.getHideMenubar().to_s

# ما إذا كان يجب إخفاء شريط الأدوات لتطبيق العارض - الافتراضي: false

puts "HideToolBar :-" + doc.getHideToolBar().to_s

# ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير

# وترك محتويات الصفحة فقط معروضة - الافتراضي: false

puts "HideWindowUI :-" + doc.getHideWindowUI().to_s

# وضع صفحة المستند. كيفية عرض المستند عند الخروج من وضع ملء الشاشة.

puts "NonFullScreenPageMode :-" + doc.getNonFullScreenPageMode().to_s

# تخطيط الصفحة أي صفحة واحدة، عمود واحد

puts "PageLayout :-" + doc.getPageLayout().to_s

# كيف يجب عرض المستند عند الفتح.

puts "pageMode :-" + doc.getPageMode().to_s
```


## تحميل كود التشغيل

قم بتحميل **احصل على خصائص نافذة المستند وعرض الصفحة (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/getdocumentwindow.rb)