---
title: Оглавление, список таблиц и рисунков
linktitle: Оглавление, список таблиц и рисунков
type: docs
weight: 10
url: /ru/reportingservices/table-of-contents-list-of-tables-or-figures/
description: Узнайте, как добавить оглавление, список таблиц или список рисунков в PDF‑отчеты с помощью Aspose.PDF for Reporting Services.
lastmod: "2021-06-05"
---
{{% alert color="primary" %}}

Report Designer не поддерживает добавление оглавления для отчетных документов. С помощью Aspose.PDF for Reporting Services вы можете легко указать рендереру PDF создавать PDF‑документы с оглавлением, списком таблиц или рисунков. Сделать это можно следующими шагами:

{{% /alert %}}

Убедитесь, что файл **Aspose.Pdf.ListSectionStyle.xml** существует в каталоге ```<Instance>```/bin, где ```<Instance>``` обозначает каталог Report Server. Если файл отсутствует, создайте его в каталоге ```<Instance>```/bin и поместите в него следующую разметку.

## Оглавление

### Пример

```xml
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

## Список таблиц

### Пример

```xml
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Список рисунков

### Пример

```xml
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Пожалуйста, обратитесь к разделу **'Working with TOC'** онлайн‑документации Aspose.Pdf.

**2-** Добавьте параметр отчёта `IsListSectionSupported` и установите значение **True**, как показано в абзаце `List Section`.  
**3-** Добавьте пользовательское свойство для элемента отчёта, который вы хотите включить в **Table of Contents**, **List of Tables** или **Figures**.

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

Помечает текущий элемент отчёта как указанный в индексе в содержании, или в списке таблиц или рисунков.

```text
Custom Property Name: Title
Custom Property Type: String
```

Заголовок элемента, отображаемый в оглавлении, списке таблиц или рисунков.

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

Уровень пунктов списка, отображаемых в таблице содержимого.

