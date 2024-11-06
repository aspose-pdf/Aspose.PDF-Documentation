---
title: إنشاء PDF من XML باستخدام XSLT
linktitle: إنشاء PDF من XML باستخدام XSLT
type: docs
weight: 10
url: ar/net/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: توفر مكتبة C# القدرة على تحويل ملف XML إلى مستند PDF بشرط أن يتبع ملف XML المدخل مخطط Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إنشاء PDF من XML باستخدام XSLT",
    "alternativeHeadline": "كيفية إنشاء PDF من XML باستخدام XSLT",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, create pdf xml, pdf with xslt",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-a-hello-world-pdf-document-through-xml-and-xslt/"
    },
    "dateModified": "2022-02-04",
    "description": "توفر مكتبة C# القدرة على تحويل ملف XML إلى مستند PDF بشرط أن يتبع ملف XML المدخل مخطط Aspose.PDF."
}
</script>

يعمل مقتطف الشيفرة التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

في بعض الأحيان قد يكون لديك ملفات XML موجودة تحتوي على بيانات تطبيقية وترغب في إنشاء تقرير PDF باستخدام هذه الملفات. يمكنك استخدام XSLT لتحويل مستند XML الموجود لديك إلى مستند XML متوافق مع Aspose.Pdf ثم إنشاء ملف PDF. هناك 3 خطوات لإنشاء PDF باستخدام XML وXSLT.

يرجى اتباع هذه الخطوات لتحويل ملف XML إلى مستند PDF باستخدام XSLT:

* إنشاء مثيل لفئة PDF التي تمثل مستند PDF
* إذا كنت قد اشتريت رخصة، فيجب عليك أيضًا تضمين الشيفرة لاستخدام هذه الرخصة بمساعدة فئة License في مساحة الأسماء Aspose.Pdf
* ربط ملفات XML وXSLT المدخلة بمثيل فئة PDF عن طريق استدعاء طريقة BindXML الخاصة بها
* حفظ XML المرتبط مع مثيل PDF كوثيقة PDF

## ملف XML المدخل

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>Hello World!</Content>
</Contents>
```

## ملف XSLT المدخل

```xml
<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="text()"/>
    <xsl:template match="/Contents">
    <html>
      <Document xmlns="Aspose.Pdf" IsAutoHyphenated="false">
        <PageInfo>
          <DefaultTextState
                            Font = "Helvetica" FontSize="8" LineSpacing="4"/>
          <Margin Left="5cm" Right="5cm" Top="3cm" Bottom="15cm" />
        </PageInfo>
        <Page id="mainSection">
          <TextFragment>
            <TextSegment>
              <xsl:value-of select="Content"/>
            </TextSegment>
          </TextFragment>
        </Page>
      </Document>
    </html>
</xsl:template>
</xsl:stylesheet>
```
```
{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Working-Document-HelloWorldPDFUsingXmlAndXslt-HelloWorldPDFUsingXmlAndXslt.cs" >}}

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "المبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "المبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "المبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "عرض",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "مكتبة معالجة ملفات PDF لـ .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "التقييم المجمع",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

# مقدمة

مرحبًا بكم في وثائق المشروع. يهدف هذا المستند إلى تقديم نظرة عامة شاملة على مشروعنا.

## الميزات

- **سهولة الاستخدام**: تم تصميم هذا المشروع ليكون سهل الاستخدام للمطورين من جميع المستويات.
- **أداء عالي**: يوفر المشروع أداءً عاليًا لضمان استجابة سريعة.
- **قابلية التوسع**: يمكن توسيع المشروع بسهولة ليناسب احتياجاتك.

## التثبيت

لتثبيت المشروع، اتبع الخطوات التالية:

1. استنساخ المستودع:
   ```bash
   git clone https://github.com/your-repo/project.git
   ```

2. الانتقال إلى دليل المشروع:
   ```bash
   cd project
   ```

3. تثبيت التبعيات:
   ```bash
   npm install
   ```

## الاستخدام

لتشغيل المشروع محليًا، استخدم الأمر التالي:

```bash
npm start
```

## المساهمة

نرحب بالمساهمات من الجميع. لبدء المساهمة، اتبع الخطوات التالية:

1. عمل فورك للمستودع.
2. إنشاء فرع جديد للتغييرات الخاصة بك.
3. إرسال طلب سحب بالمساهمات الخاصة بك.

## التراخيص

هذا المشروع مرخص بموجب رخصة MIT. لمزيد من المعلومات، يرجى قراءة ملف `LICENSE`.

## الاتصال

إذا كان لديك أي أسئلة أو استفسارات، يرجى فتح قضية في المستودع أو الاتصال بنا عبر البريد الإلكتروني.

changefreq: "monthly"

type: docs
```
