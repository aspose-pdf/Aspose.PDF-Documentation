---
title: Оглавление Список таблиц или рисунков
type: docs
weight: 10
url: /ru/reportingservices/table-of-contents-list-of-tables-or-figures/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Конструктор отчетов не поддерживает добавление оглавления для документов отчетов. С помощью Aspose.Pdf для Reporting Services вы можете легко настроить вывод PDF-документов с оглавлением или списком таблиц или рисунков. Вы можете сделать это, следуя следующим шагам:

{{% /alert %}}

{{% alert color="primary" %}}
Убедитесь, что файл Aspose.Pdf.ListSectionStyle.xml существует в ```<Instance>```/bin, где ```<Instance>``` — это директория сервера отчетов. Если файл не существует, создайте его в директории ```<Instance>```/bin и поместите следующий разметку внутрь.

## Оглавление

**Пример**

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

## Список Таблиц

**Пример**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Список Иллюстраций

**Пример**

```cs
<ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Пожалуйста, обратитесь к разделу 'Работа с TOC' в онлайн-документации Aspose.Pdf.

**2-** Добавьте параметр отчета 'IsListSectionSupported' и установите значение True, как показано в абзаце 'List Section'.
**3-** Добавьте пользовательское свойство для элемента отчета, который вы хотите включить в Содержание, Список Таблиц или Иллюстраций.

{{% /alert %}}

{{% alert color="primary" %}}

**Имя пользовательского свойства**: IsInList
**Значение свойства**: Boolean
**Значение пользовательского свойства**: True или False

{{% alert color="primary" %}}

Отмечает текущий элемент отчета как включенный в содержание, или в список таблиц или иллюстраций.

{{% /alert %}}

**Custom Property Name** : Title  
**Custom Property Type** : String

{{% alert color="primary" %}}

Название элемента, отображаемое в оглавлении, списке таблиц или рисунков.  
{{% /alert %}}

**Custom Property Name** : ListLevel  
**Custom Property Type** : Integer

{{% alert color="primary" %}}

Уровень перечисленных элементов, отображаемых в оглавлении.

{{% /alert %}}

{{% /alert %}}