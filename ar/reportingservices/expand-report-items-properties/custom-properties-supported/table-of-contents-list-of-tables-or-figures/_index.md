---
title: فهرس قائمة الجداول أو الأشكال
linktitle: فهرس قائمة الجداول أو الأشكال
type: docs
weight: 10
url: /ar/reportingservices/table-of-contents-list-of-tables-or-figures/
description: تعلم كيفية إضافة فهرس، قائمة الجداول، أو الأشكال في تقارير PDF باستخدام Aspose.PDF for Reporting Services.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

لا يدعم Report Designer إضافة فهرس للمستندات التقريرية. باستخدام Aspose.Pdf for Reporting Services يمكنك بسهولة إرشاد مُعرض PDF لإنتاج مستندات PDF تحتوي على فهرس، أو قائمة الجداول أو الأشكال. يمكنك القيام بذلك في الخطوات التالية:

{{% /alert %}}

{{% alert color="primary" %}}
تأكد من وجود ملف Aspose.Pdf.ListSectionStyle.xml في ```<Instance>```/bin، أين ```<Instance>``` هو دليل خادم التقارير. إذا لم يكن الملف موجودًا، أنشئه في ```<Instance>```دليل /bin وضع العلامة التالية داخله.

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

##  قائمة الجداول

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

يرجى الرجوع إلى قسم 'Working with TOC' في توثيق Aspose.Pdf على الويب.

**2-** أضف معلمة التقرير 'IsListSectionSupported' وقم بتعيين القيمة لتكون True كما هو موضح في الفقرة 'List Section'.
**3-** أضف خاصية مخصصة لعنصر التقرير الذي تريد أن يُدرج في جدول المحتويات أو قائمة الجداول أو الأشكال.

{{% /alert %}}

{{% alert color="primary" %}}

**اسم الخاصية المخصصة** :IsInList
**قيمة الخاصية** :Boolean
**قيمة الخاصية المخصصة** : True or False

{{% alert color="primary" %}}

يُعلِّم العنصر الحالي في التقرير بأنه مدرج حسب الفهرس في جدول المحتويات، أو قائمة الجداول أو الأشكال.

{{% /alert %}}

**اسم الخاصية المخصصة** : العنوان
**نوع الخاصية المخصصة** : سلسلة

{{% alert color="primary" %}}

عنوان العنصر المعروض في جدول المحتويات، قائمة الجداول أو الأشكال.
{{% /alert %}}

**اسم الخاصية المخصصة** : ListLevel
**نوع الخاصية المخصصة** : عدد صالح

{{% alert color="primary" %}}

المستوى للعناصر المدرجة المعروضة في جدول المحتويات.

{{% /alert %}}

{{% /alert %}}

