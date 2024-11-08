---
title: الحصول على خصائص نافذة المستند وعرض الصفحة في بايثون
type: docs
weight: 30
url: /ar/java/get-document-window-and-page-display-properties-in-python/
lastmod: "2021-06-05"
---

للحصول على خصائص نافذة المستند وعرض الصفحة لوثيقة Pdf باستخدام **Aspose.PDF Java for Python**، قم ببساطة باستدعاء فئة **GetDocumentWindow**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الحصول على خصائص المستند المختلفة
# موضع نافذة المستند - الافتراضي: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# ترتيب القراءة الأساسي؛ يحدد موضع الصفحة
# عند العرض جنبًا إلى جنب - الافتراضي: L2R
print "Direction :- " + str(doc.getDirection())

# ما إذا كان شريط عنوان النافذة يجب أن يعرض عنوان المستند.
# إذا كانت false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# ما إذا كان يجب تغيير حجم نافذة المستند لتتناسب مع حجم
# الصفحة الأولى المعروضة - الافتراضي: false
print "FitWindow :- " + str(doc.getFitWindow())

# ما إذا كان يجب إخفاء شريط القائمة لتطبيق العارض - الافتراضي: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# ما إذا كان يجب إخفاء شريط الأدوات لتطبيق العارض - الافتراضي: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
# وترك محتويات الصفحة فقط معروضة - الافتراضي: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# وضع صفحة المستند. كيفية عرض المستند عند الخروج من وضع الشاشة الكاملة.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# تخطيط الصفحة أي صفحة واحدة، عمود واحد
print "PageLayout :-" + str(doc.getPageLayout())

# كيفية عرض المستند عند فتحه.
print "pageMode :-" + str(doc.getPageMode())
```


**تنزيل الشيفرة التنفيذية**

قم بتنزيل **احصل على خصائص نافذة المستند وعرض الصفحة (Aspose.PDF)** من أي من مواقع البرمجة الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)