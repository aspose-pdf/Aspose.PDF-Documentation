---
title: جدول المحتويات قائمة الجداول أو الأشكال
linktitle: جدول المحتويات قائمة الجداول أو الأشكال
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
description: تعرف على كيفية إضافة جدول محتويات أو قائمة جداول أو أشكال في تقارير PDF باستخدام Aspose.PDF لخدمات التقارير.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

لا يدعم مصمم التقارير إضافة جدول محتويات لمستندات التقرير. باستخدام Aspose.PDF لخدمات التقارير، يمكنك بسهولة توجيه عرض PDF لإنتاج مستندات PDF مع جدول المحتويات، أو قائمة الجداول أو الأشكال. يمكنك القيام بذلك في الخطوات التالية:

{{% /alert %}}

تأكد من وجود الملف Aspose.Pdf.ListSectionStyle.xml في دليل ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin ثم ضع العلامة التالية بداخله.

## جدول المحتويات

### مثال

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

##  قائمة الجداول S

### مثال

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## قائمة الأرقام

### مثال

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Please refer to 'Working with TOC' section of the Aspose.Pdf online documentation.

**2-** أضف معلمة التقرير `IsListSectionSupported` وقم بتعيين القيمة لتكون True كما هو موضح في الفقرة `List Section`.
**3-** أضف خاصية مخصصة لعنصر التقرير الذي تريد إدراجه في جدول المحتويات أو قائمة الجداول أو الأشكال.

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

وضع علامة على عنصر التقرير الحالي كما هو مدرج حسب الفهرس في جدول المحتويات، أو قائمة الجداول أو الأشكال.

```text
Custom Property Name: Title
Custom Property Type: String
```

عنوان العنصر المعروض في جدول المحتويات أو قائمة الجداول أو الأشكال.

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

مستوى العناصر المدرجة المعروضة في جدول المحتويات.
