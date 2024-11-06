---
title: استخراج المحتوى الموسوم من PDF 
linktitle: استخراج المحتوى الموسوم
type: docs
weight: 20
url: ar/java/extract-tagged-content-from-tagged-pdfs/
description: يشرح هذا المقال كيفية استخراج مستند PDF الموسوم باستخدام Aspose.PDF لـ Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## الحصول على محتوى PDF الموسوم

من أجل الحصول على محتوى مستند PDF مع النص الموسوم، تقدم Aspose.PDF طريقة [getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--) من فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). يوضح المقتطف البرمجي التالي كيفية الحصول على محتوى مستند PDF مع النص الموسوم:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String path = "pathTodir";

// إنشاء مستند PDF
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

//
// العمل مع محتوى PDF الموسوم
//

// تعيين العنوان واللغة للمستند
taggedContent.setTitle("Simple Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// حفظ مستند PDF الموسوم
document.save(path + "TaggedPDFContent.pdf");
```


## الحصول على الهيكل الجذري

من أجل الحصول على الهيكل الجذري لمستند PDF الموسوم، يوفر Aspose.PDF طرق [getStructTreeRootElement]()(https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) و **getStructureElement()** لواجهة [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). يوضح الكود التالي كيفية الحصول على الهيكل الجذري لمستند PDF الموسوم:

```java
// للحصول على أمثلة وملفات البيانات الكاملة، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-Java
// المسار إلى دليل المستندات.
String path = "pathTodir";
// إنشاء مستند PDF
Document document = new Document();

// الحصول على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// تعيين العنوان واللغة للمستند
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// يتم استخدام خصائص StructTreeRootElement و RootElement للوصول إلى
// كائن StructTreeRoot لمستند pdf وإلى عنصر هيكل الجذر (عنصر هيكل الوثيقة).
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```


## الوصول إلى عناصر الأطفال

من أجل الوصول إلى عناصر الأطفال في وثيقة PDF الموسومة، تقدم Aspose.PDF فئة **ElementList**. يوضح جزء الشيفرة التالي كيفية الوصول إلى عناصر الأطفال في وثيقة PDF الموسومة:

```java
// للحصول على أمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-Java
String path = "pathTodir";
// افتح وثيقة PDF
Document document = new Document( path +"StructureElements.pdf");

// احصل على المحتوى للعمل مع TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// الوصول إلى العنصر الجذري
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // احصل على الخصائص
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// الوصول إلى عناصر الأطفال لأول عنصر في العنصر الجذري
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // تعيين الخصائص
        structureElement.setTitle("title");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("actual text");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// احفظ وثيقة PDF الموسومة
document.save( path +"AccessChildrenElements.pdf");
```