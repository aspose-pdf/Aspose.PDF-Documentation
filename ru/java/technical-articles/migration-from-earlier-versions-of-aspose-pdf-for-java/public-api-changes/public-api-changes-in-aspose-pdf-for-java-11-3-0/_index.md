---
title: Public API changes in Aspose.PDF for Java 11.3.0
type: docs
weight: 130
url: ru/java/public-api-changes-in-aspose-pdf-for-java-11-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

На этой странице перечислены изменения в публичном API, введенные в Aspose.PDF для Java 11.3.0. Это включает не только новые и устаревшие публичные методы, но и описание любых изменений в поведении за кулисами в Aspose.PDF для Java, которые могут повлиять на существующий код. Любое поведение, введенное, которое может быть воспринято как регрессия и изменяет существующее поведение, особенно важно и документируется здесь.

{{% /alert %}}

**Изменения в классе com.aspose.pdf.Annotation:**

Добавленные методы:

- public boolean isUpdateAppearanceOnConvert()
- public void setUpdateAppearanceOnConvert(boolean value)

**Изменения в классе com.aspose.pdf.BaseParagraph:**

Добавленные методы:

- public int getZIndex()
- public void setZIndex(int)

**Изменения в классе com.aspose.pdf.MemoryCleaner:**

Добавленные методы:

- public void clearAllTempFiles()

**Изменения в классе com.aspose.pdf.Page:**

Methods added:

- public byte[] asByteArray(com.aspose.pdf.devices.Resolution)

**Изменения в классе com.aspose.pdf.Table:**

Методы добавлены:

- public com.aspose.pdf.Table getParentTable()
- public void setParentTable(com.aspose.pdf.Table)

**Изменения в классе com.aspose.pdf.TextSearchOptions:**

Методы добавлены:

- public boolean isIgnoreShadowText()
- public void setIgnoreShadowText(boolean value)