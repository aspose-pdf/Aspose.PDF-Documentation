---
title: جدول المحتويات قائمة الجداول أو الأشكال
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يدعم مصمم التقارير إضافة جدول محتويات لوثائق التقرير. مع Aspose.Pdf لـ Reporting Services يمكنك بسهولة توجيه محول PDF لإنتاج مستندات PDF بجدول محتويات، أو قائمة بالجداول أو الأشكال. يمكنك القيام بذلك عبر الخطوات التالية:

{{% /alert %}}

{{% alert color="primary" %}}
تأكد من وجود ملف Aspose.Pdf.ListSectionStyle.xml في ```<Instance>```/bin، حيث ```<Instance>``` هو دليل خادم التقارير. إذا لم يكن الملف موجودًا، قم بإنشائه في دليل ```<Instance>```/bin وضع العلامات التالية بداخله.

## جدول المحتويات

**مثال**

```cs
<ListSection ListType="TableOfContents">
              <Title Alignment="Center">
            <Segment IsTrueTypeFontBold="true" FontSize="30">TableOfContents</Segment>
              </Title>
              <ListLevelFormat Level="1" LeftMargin="0">
            <TextInfo IsTrueTypeFontBold="true" IsTrueTypeFontItalic="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="2" LeftMargin="10">
            <TextInfo IsUnderline="true" FontSize="10"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="3" LeftMargin="20">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
              <ListLevelFormat Level="4" LeftMargin="30">
            <TextInfo IsTrueTypeFontBold="true"></TextInfo>
              </ListLevelFormat>
</ListSection>
```

## قائمة الجداول

**مثال**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## قائمة الأشكال

**مثال**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

يرجى الرجوع إلى قسم 'العمل مع TOC' في وثائق Aspose.Pdf عبر الإنترنت.

**2-** أضف معلمة تقرير 'IsListSectionSupported' واضبط القيمة لتكون True كما هو موضح في فقرة 'قسم القائمة'.
**3-** أضف خاصية مخصصة لبند التقرير الذي تريد إدراجه في جدول المحتويات، قائمة الجداول أو الأشكال.

{{% /alert %}}

{{% alert color="primary" %}}

**اسم الخاصية المخصصة** :IsInList
**قيمة الخاصية** :Boolean
**قيمة الخاصية المخصصة** : True أو False

{{% alert color="primary" %}}


يحدد بند التقرير الحالي كمدرج بواسطة الفهرس في جدول المحتويات، أو قائمة الجداول أو الأشكال.

{{% /alert %}}

**Custom Property Name** : Title  
**Custom Property Type** : String

{{% alert color="primary" %}}

العنوان المعروض في جدول المحتويات أو قائمة الجداول أو الأشكال.  
{{% /alert %}}

**Custom Property Name** : ListLevel  
**Custom Property Type** : Integer

{{% alert color="primary" %}}

مستوى العناصر المدرجة المعروضة في جدول المحتويات.

{{% /alert %}}

{{% /alert %}}