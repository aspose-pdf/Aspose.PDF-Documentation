---
title: الحصول على خواص نافذة المستند وعرض الصفحة في بايثون
type: docs
weight: 30
url: /python-java/get-document-window-and-page-display-properties-in-python/
---

<ins>للحصول على خصائص نافذة المستند وعرض الصفحة لوثيقة Pdf باستخدام **Aspose.PDF Java for Python**، يمكنك ببساطة استدعاء فئة **GetDocumentWindow**.

**كود بايثون**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# الحصول على خصائص الوثيقة المختلفة
# موضع نافذة الوثيقة - الافتراضي: false
print "CenterWindow :- " + str(doc.getCenterWindow())

# ترتيب القراءة الرئيسي؛ يحدد موضع الصفحة
# عند العرض جنبًا إلى جنب - الافتراضي: L2R
print "Direction :- " + str(doc.getDirection())

# ما إذا كان يجب على شريط عنوان النافذة عرض عنوان الوثيقة.
# إذا كان false، يعرض شريط العنوان اسم ملف PDF - الافتراضي: false
print "DisplayDocTitle :- " + str(doc.getDisplayDocTitle())

# ما إذا كان يجب تغيير حجم نافذة الوثيقة لتناسب حجم
# الصفحة الأولى المعروضة - الافتراضي: false

print "FitWindow :- " + str(doc.getFitWindow())


# ما إذا كان يجب إخفاء شريط القوائم في تطبيق العارض - الافتراضي: false
print "HideMenuBar :-" + str(doc.getHideMenubar())

# ما إذا كان يجب إخفاء شريط الأدوات في تطبيق العارض - الافتراضي: false
print "HideToolBar :-" + str(doc.getHideToolBar())

# ما إذا كان يجب إخفاء عناصر واجهة المستخدم مثل أشرطة التمرير
# وترك محتويات الصفحة فقط معروضة - الافتراضي: false
print "HideWindowUI :-" + str(doc.getHideWindowUI())

# وضع صفحة المستند. كيفية عرض المستند عند الخروج من وضع الشاشة الكاملة.
print "NonFullScreenPageMode :-" + str(doc.getNonFullScreenPageMode())

# تخطيط الصفحة أي صفحة واحدة، عمود واحد
print "PageLayout :-" + str(doc.getPageLayout())

# كيف يجب أن يعرض المستند عند فتحه.
print "pageMode :-" + str(doc.getPageMode())

**تحميل الشيفرة الجارية**

قم بتحميل **احصل على نافذة المستند وخصائص عرض الصفحة (Aspose.PDF)** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetDocumentWindow/GetDocumentWindow.py)