---
title: تحويل HTML إلى ملف PDF في Java
linktitle: تحويل HTML إلى ملف PDF
type: docs
weight: 40
url: /ar/java/convert-html-to-pdf/
lastmod: "2021-11-19"
description: يوضح هذا الموضوع كيف يتيح لك Aspose.PDF تحويل تنسيقات HTML وMHTML إلى ملف PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## نظرة عامة

تشرح هذه المقالة كيفية تحويل HTML إلى PDF باستخدام Java. الكود بسيط جدًا، فقط قم بتحميل HTML إلى فئة Document واحفظه كملف PDF ناتج. تحويل MHTML إلى PDF في Java مشابه أيضًا. وهي تغطي المواضيع التالية

- [جافا HTML إلى PDF](#convert-html-to-pdf)
- [جافا MHTML إلى PDF](#convert-mhtml-to-pdf)
- [جافا تحويل HTML إلى PDF](#convert-html-to-pdf)
- [جافا تحويل MHTML إلى PDF](#convert-mhtml-to-pdf)
- [جافا PDF من HTML](#convert-html-to-pdf)
- [جافا PDF من MHTML](#convert-mhtml-to-pdf)
- [محول HTML إلى PDF في جافا - كيفية تحويل صفحة ويب إلى PDF](#convert-html-to-pdf)

- [مكتبة HTML إلى PDF في جافا، API أو كود لعرض، حفظ، توليد أو إنشاء PDF برمجيًا من HTML](#convert-html-to-pdf)

## مكتبة تحويل Java HTML إلى PDF

**Aspose.PDF for Java** هو API للتعامل مع ملفات PDF يتيح لك تحويل أي مستندات HTML موجودة إلى PDF بسلاسة.
يمكن تخصيص عملية تحويل HTML إلى PDF بمرونة.

## تحويل HTML إلى PDF

يُظهر مثال كود Java التالي كيفية تحويل مستند HTML إلى PDF.

1. إنشاء مثيل لفئة [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. تهيئة كائن [Document](https://reference.aspose.com/page/java/com.aspose.page/document).
1. حفظ مستند PDF الناتج عن طريق استدعاء طريقة **Document.save(String)**.

```java
// افتح مستند PDF المصدر
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// إنشاء كائن HTML SaveOptions
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// احفظ المستند
document.save(DATA_DIR + "MultiPageHTML_out.html", htmlsaveOptions);
```

{{% alert color="success" %}}
**حاول تحويل HTML إلى PDF عبر الإنترنت**

تقدم لك Aspose تطبيقًا مجانيًا عبر الإنترنت ["HTML to PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf)، حيث يمكنك محاولة التحقيق في الوظيفة والجودة التي يعمل بها.

[![Aspose.PDF Convertion HTML to PDF using Free App](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## التحويل المتقدم من HTML إلى PDF

محرك تحويل HTML يحتوي على عدة خيارات تتيح لنا التحكم في عملية التحويل.

### دعم استعلامات الوسائط

1. قم بإنشاء [خيارات تحميل HTML](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. قم بتعيين وضع الطباعة أو الشاشة.
1. قم بتثبيت [كائن المستند](<https://reference.aspose.com/page/java/com.aspose.page/document>).
1. احفظ مستند PDF الناتج.

تعتبر استعلامات الوسائط تقنية شائعة لتقديم ورقة أنماط مخصصة لأجهزة مختلفة. يمكننا تعيين نوع الجهاز باستخدام خاصية [HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType).

```java
// قم بإنشاء خيارات تحميل HTML
HtmlLoadOptions options = new HtmlLoadOptions();

// قم بتعيين وضع الطباعة أو الشاشة
options.setHtmlMediaType(HtmlMediaType.Print);

// تثبيت كائن المستند
String htmlFileName = Paths.get(DATA_DIR.toString(), "test.html").toString();
Document document = new Document(htmlFileName, options);

// احفظ مستند PDF الناتج
document.save(Paths.get(DATA_DIR.toString(), "HTMLtoPDF.pdf").toString());
document.close();
```


### تمكين (تعطيل) تضمين الخطوط

1. إضافة خيارات تحميل HTML جديدة [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions).
1. تمكين/تعطيل تضمين الخطوط.
1. حفظ مستند جديد.

غالبًا ما تستخدم صفحات HTML الخطوط (على سبيل المثال، الخطوط من المجلد المحلي، خطوط جوجل، إلخ). يمكننا أيضًا التحكم في تضمين الخطوط في مستند باستخدام خاصية [IsEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#isEmbedFonts--).

```java
HtmlLoadOptions options = new HtmlLoadOptions();
// تمكين/تعطيل تضمين الخطوط
options.setEmbedFonts(true);

Document document = new Document(DATA_DIR + "test_fonts.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();
```

### إدارة تحميل الموارد الخارجية

يوفر محرك التحويل آلية تتيح لك التحكم في تحميل بعض الموارد المرتبطة بمستند HTML.

تحتوي فئة [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions) على خاصية [CustomLoaderOfExternalResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions#setCustomLoaderOfExternalResources-com.aspose.pdf.LoadOptions.ResourceLoadingStrategy-) التي يمكننا من خلالها تحديد سلوك محمل المورد.

```java
HtmlLoadOptions options = new HtmlLoadOptions();

options.setCustomLoaderOfExternalResources(
        new LoadOptions.ResourceLoadingStrategy() {
            public LoadOptions.ResourceLoadingResult invoke(String resourceURI) {
                // إنشاء قالب مورد نظيف للاستبدال:
                LoadOptions.ResourceLoadingResult res = new LoadOptions.ResourceLoadingResult(new byte[] {});
                // إرجاع مصفوفة بايت فارغة في حالة خادم i.imgur.com
                if (resourceURI.contains("i.imgur.com")) {
                    return res;
                } else {
                    // معالجة الموارد باستخدام محمل الموارد الافتراضي
                    res.setLoadingCancelled(true);
                    return res;
                }
            }   
});

Document document = new Document(DATA_DIR + "test.html", options);
document.save(DATA_DIR + "html_test.PDF");
document.close();    
```

## تحويل MHTML إلى PDF

{{% alert color="success" %}}
**حاول تحويل MHTML إلى PDF عبر الإنترنت**


Aspose.PDF for Java يقدم لك تطبيقًا مجانيًا على الإنترنت ["MHTML to PDF"](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF Convertion MHTML to PDF using Free App](mhtml.png)](https://products.aspose.app/pdf/conversion/mhtml-to-pdf)
{{% /alert %}}

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>، اختصار لـ MIME HTML، هو صيغة أرشيف لصفحات الويب تُستخدم لدمج الموارد التي تمثل عادةً بواسطة روابط خارجية (مثل الصور، الرسوم المتحركة الفلاش، تطبيقات Java الصغيرة، وملفات الصوت) مع كود HTML في ملف واحد. يتم ترميز محتوى ملف MHTML كما لو كان رسالة بريد إلكتروني HTML، باستخدام نوع MIME multipart/related.

يظهر رمز المثال التالي كيفية تحويل ملفات MHTML إلى صيغة PDF باستخدام Java:

```java
// قم بإنشاء مثيل لـ MhtLoadOptions لتحديد خيارات التحميل لـ
// ملف MHTML.
MhtLoadOptions options = new MhtLoadOptions();

// تعيين مسار ملف MHTML.
String mhtmlFileName = Paths.get(DATA_DIR.toString(), "samplefile.mhtml").toString();

// تحميل ملف MHTML في كائن Document.
Document document = new Document(mhtmlFileName, options);

// احفظ المستند كملف PDF.
document.save(Paths.get(DATA_DIR.toString(), "MarkdowntoPDF.pdf").toString());

// اغلق المستند.
document.close();
```