---
title: تعيين خصائص نافذة الوثيقة وعرض الصفحة في لغة روبي
type: docs
weight: 100
url: ar/java/set-document-window-and-page-display-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - تعيين خصائص نافذة الوثيقة وعرض الصفحة

لتعيين خصائص نافذة الوثيقة وعرض الصفحة لوثيقة PDF باستخدام **Aspose.PDF Java for Ruby**، ببساطة قم باستدعاء وحدة **SetDocumentWindow**.

كود روبي

```java
# المسار إلى دليل المستندات.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# افتح وثيقة pdf.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# تعيين خصائص الوثيقة المختلفة

# موضع نافذة الوثيقة - الافتراضي: false

doc.setCenterWindow(true)

# ترتيب القراءة السائد؛ تحديد موضع الصفحة

# عند العرض جنبًا إلى جنب - الافتراضي: L2R

#doc.setDirection(Rjb::import('com.aspose.pdf.Direction.L2R'))

# ما إذا كان شريط عنوان النافذة يجب أن يعرض عنوان الوثيقة.

# إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false

doc.setDisplayDocTitle(true)

# ما إذا كان يجب تغيير حجم نافذة الوثيقة لتناسب حجم

# الصفحة المعروضة أولاً - الافتراضي: false

doc.setFitWindow(true)

# ما إذا كان يجب إخفاء شريط القوائم لتطبيق العارض - الافتراضي: false

doc.setHideMenubar(true)

# ما إذا كان يجب إخفاء شريط الأدوات لتطبيق العارض - الافتراضي: false

doc.setHideToolBar(true)

# ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير

# وترك محتويات الصفحة فقط معروضة - الافتراضي: false

doc.setHideWindowUI(true)

# وضع صفحة الوثيقة. كيفية عرض الوثيقة عند الخروج من وضع الشاشة الكاملة.

doc.setNonFullScreenPageMode(Rjb::import('com.aspose.pdf.PageMode.UseOC'))

# تخطيط الصفحة أي صفحة واحدة، عمود واحد

doc.setPageLayout(Rjb::import('com.aspose.pdf.PageLayout.TwoColumnLeft'))

# كيفية عرض الوثيقة عند فتحها.

doc.setPageMode()

# حفظ ملف PDF المحدث

doc.save(data_dir + "Set Document Window.pdf")
```


## تنزيل الشيفرة الجاهزة

قم بتنزيل **تعيين نافذة المستند وخصائص عرض الصفحة (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/setdocumentwindow.rb)