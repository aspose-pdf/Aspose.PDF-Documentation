---
title: Table of Contents List of Tables or Figures
linktitle: Оглавление Список таблиц и рисунков
type: docs
weight: 10
url: /reportingservices/table-of-contents-list-of-tables-or-figures/
description: Узнайте, как добавить оглавление, список таблиц или рисунки в отчеты PDF с помощью Aspose.PDF для служб Reporting Services.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Дизайнер отчетов не поддерживает добавление оглавления для документов отчета. С помощью Aspose.PDF for Reporting Services вы можете легко настроить рендеринг PDF для создания PDF-документов с оглавлением, списком таблиц или рисунков. Вы можете сделать это, выполнив следующие шаги:

{{% /alert %}}

Make sure that Aspose.Pdf.ListSectionStyle.xml file exists in ```<Instance>```/bin, where ```<Instance>``` is the directory of the Report Server. If the file does not exist, create it in the ```<Instance>```/bin directory and place the following markup inside.

## Оглавление

### Пример

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

##  Список таблиц

### Пример

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Список фигур

### Пример

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Пожалуйста, обратитесь к разделу «Работа с TOC» онлайн-документации Aspose.Pdf.

**2-** Добавьте параметр отчета `IsListSectionSupported` и установите значение True, как показано в абзаце `List Section`.
**3-** Добавьте пользовательское свойство для элемента отчета, который вы хотите включить в оглавление, список таблиц или рисунков.

```text
Custom Property Name: IsInList
Property Value: Boolean
Custom Property Value: True or False
```

Отмечает текущий элемент отчета как указанный по индексу в оглавлении или списке таблиц или рисунков.

```text
Custom Property Name: Title
Custom Property Type: String
```

Название элемента отображается в оглавлении, списке таблиц или рисунков.

```text
Custom Property Name: ListLevel
Custom Property Type: Integer
```

Уровень перечисленных элементов отображается в оглавлении.
