---
title: إنشاء ملف PDF من XML باستخدام XSLT 
linktitle: إنشاء ملف PDF من XML باستخدام XSLT
type: docs
weight: 10
url: /cpp/create-a-hello-world-pdf-document-through-xml-and-xslt/
description: توفر مكتبة C++ القدرة على تحويل ملف XML إلى مستند PDF بشرط أن يتبع ملف XML المدخل مخطط Aspose.PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

قد يكون لديك أحيانًا ملفات XML موجودة تحتوي على بيانات التطبيق وتريد إنشاء تقرير PDF باستخدام هذه الملفات. يمكنك استخدام XSLT لتحويل مستند XML الموجود لديك إلى مستند XML متوافق مع Aspose.Pdf ثم إنشاء ملف PDF. هناك 3 خطوات لإنشاء PDF باستخدام XML وXSLT.

يرجى اتباع هذه الخطوات لتحويل ملف XML إلى مستند PDF باستخدام XSLT:

* إنشاء مثيل لفئة PDF التي تمثل مستند PDF
* إذا كنت قد اشتريت ترخيصًا، فيجب عليك أيضًا تضمين الكود لاستخدام ذلك الترخيص بمساعدة فئة License في مساحة الأسماء Aspose.Pdf

* ربط ملفات XML وXSLT المدخلة بمثيل فئة PDF عن طريق استدعاء طريقة BindXML الخاصة بها
 * احفظ XML المرتبط مع مثيل PDF كوثيقة PDF

## ملف XML المدخل

```xml
<?xml version="1.0" encoding="utf-8" ?>
<Contents>
  <Content>مرحبا بالعالم!</Content>
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

```cpp
using namespace System;
using namespace Aspose::Pdf;

static System::SharedPtr<System::IO::MemoryStream> TransformXmltoHtml(String inputXml, String xsltString);

void WorkingWithXML::CreatingPDFfromXMLusingXSLT()
{
 String _dataDir("C:\\Samples\\");
 //Create pdf document
 auto pdf = MakeObject<Aspose::Pdf::Document>();
 //Bind XML and XSLT files to the document
 try
 {
  pdf->BindXml(_dataDir + u"\\HelloWorld.xml", _dataDir + u"\\HelloWorld.xslt");
 }
 catch (System::Exception ex)
 {
  std::cerr << ex.what();
  throw;
 }

 //Save the document
 pdf->Save(_dataDir + u"HelloWorldUsingXmlAndXslt.pdf");
}

```