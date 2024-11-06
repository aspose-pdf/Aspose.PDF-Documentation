---
title: إنشاء مستند PDF "مرحبا بالعالم" باستخدام XML وXSLT
linktitle: إنشاء مستند PDF "مرحبا بالعالم" باستخدام XML وXSLT
type: docs
weight: 10
url: ar/java/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: يوفر Aspose.PDF for Java الفرصة لتحويل ملف XML إلى مستند PDF بشرط أن يتبع ملف XML المدخل مخطط Aspose.PDF XSD Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

في بعض الأحيان قد يكون لديك ملفات XML موجودة تحتوي على بيانات التطبيق وترغب في إنشاء تقرير PDF باستخدام هذه الملفات. يمكنك استخدام XSLT لتحويل مستند XML الموجود لديك إلى مستند XML متوافق مع Aspose.Pdf ثم إنشاء ملف PDF. هناك 3 خطوات لإنشاء PDF باستخدام XML وXSLT.

يرجى اتباع هذه الخطوات لتحويل ملف XML إلى مستند PDF باستخدام XSLT:

* إنشاء مثيل لفئة PDF التي تمثل مستند PDF

* إذا كنت قد اشتريت ترخيصًا فيجب عليك أيضًا تضمين الكود لاستخدام هذا الترخيص بمساعدة فئة License في نطاق الأسماء Aspose.Pdf
* ربط ملفات XML و XSLT المدخلة إلى مثيل فئة PDF عن طريق استدعاء أسلوب BindXML الخاص بها
* حفظ XML المرتبط مع مثيل PDF كمستند PDF

## ملف XML المدخل

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>مرحباً بالعالم!</Content>
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
          <DefaultTextState Font = "Helvetica" FontSize="8" LineSpacing="4"/>
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


## إنشاء برنامج Hello World باستخدام XML و Java

```java
public static void Example_XML_to_PDF_02() {
      com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document();
      pdfDocument.bindXml(_dataDir + "XMLFile1.xml",_dataDir +  "XSLTFile1.xslt");
      pdfDocument.save(_dataDir + "data_xml.pdf");
}    
```