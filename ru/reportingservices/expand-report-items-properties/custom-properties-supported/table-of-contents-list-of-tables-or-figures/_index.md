---
title: Оглавление Список таблиц или рисунков
linktitle: Оглавление Список таблиц или рисунков
type: docs
weight: 10
url: /ru/reportingservices/table-of-contents-list-of-tables-or-figures/
description: Узнайте, как добавить Оглавление, Список таблиц или рисунков в PDF‑отчеты, используя Aspose.PDF for Reporting Services.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Report Designer не поддерживает добавление оглавления для документов отчётов. С помощью Aspose.Pdf for Reporting Services вы можете легко указать PDF‑рендереру создавать PDF‑документы с Оглавлением, Список таблиц или рисунков. Вы можете сделать это в следующих шагах:

{{% /alert %}}

{{% alert color="primary" %}}
Убедитесь, что файл Aspose.Pdf.ListSectionStyle.xml существует в ```<Instance>```/bin, где ```<Instance>``` это каталог Report Server. Если файл не существует, создайте его в ```<Instance>```директорию /bin и разместите внутри следующую разметку.

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

##  Список таблиц

**Пример**

```cs
<ListSection ListType="ListOfTables">
              <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfTables</Segment>
              </Title>
</ListSection>
```

## Список рисунков

**Пример**

```cs
 <ListSection ListType="ListOfFigures">
    <Title>
            <Segment IsTrueTypeFontBold="true" FontSize="30">ListOfFigures</Segment>
    </Title>
</ListSection>

```

Пожалуйста, обратитесь к разделу 'Working with TOC' в онлайн-документации Aspose.Pdf.

**2-** Добавьте параметр отчёта 'IsListSectionSupported' и установите значение True, как показано в абзаце 'List Section'.
**3-** Добавьте пользовательское свойство для элемента вашего отчёта, которое вы хотите включить в Содержание, Список таблиц или Список рисунков.

{{% /alert %}}

{{% alert color="primary" %}}

**Имя пользовательского свойства** :IsInList
**Значение свойства** :Boolean
**Значение пользовательского свойства** : True or False

{{% alert color="primary" %}}

Отмечает текущий элемент отчета как включенный в список по индексу в оглавлении, списке таблиц или рисунков.

{{% /alert %}}

**Имя пользовательского свойства** : Заголовок
**Тип пользовательского свойства** : Строка

{{% alert color="primary" %}}

Заголовок элемента, отображаемый в оглавлении, списке таблиц или рисунков.
{{% /alert %}}

**Имя пользовательского свойства** : Уровень списка
**Тип пользовательского свойства** : Integer

{{% alert color="primary" %}}

Уровень перечисленных элементов, отображаемых в таблице содержимого.

{{% /alert %}}

{{% /alert %}}

