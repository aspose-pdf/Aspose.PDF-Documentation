---
title: Mudanças na API pública no Aspose.PDF para Java 11.3.0
type: docs
weight: 130
url: /java/public-api-changes-in-aspose-pdf-for-java-11-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as mudanças na API pública introduzidas no Aspose.PDF para Java 11.3.0. Inclui não apenas métodos públicos novos e obsoletos, mas também uma descrição de quaisquer mudanças no comportamento por trás das cenas no Aspose.PDF para Java que podem afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e que modifica o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}

**Mudanças na classe com.aspose.pdf.Annotation:**

Métodos adicionados:

- public boolean isUpdateAppearanceOnConvert()
- public void setUpdateAppearanceOnConvert(boolean value)

**Mudanças na classe com.aspose.pdf.BaseParagraph:**

Métodos adicionados:

- public int getZIndex()
- public void setZIndex(int)

**Mudanças na classe com.aspose.pdf.MemoryCleaner:**

Métodos adicionados:

- public void clearAllTempFiles()


**Mudanças na classe com.aspose.pdf.Page:**

Methods added:

- public byte[] asByteArray(com.aspose.pdf.devices.Resolution)

**Alterações na classe com.aspose.pdf.Table:**

Métodos adicionados:

- public com.aspose.pdf.Table getParentTable()
- public void setParentTable(com.aspose.pdf.Table)

**Alterações na classe com.aspose.pdf.TextSearchOptions:**

Métodos adicionados:

- public boolean isIgnoreShadowText()
- public void setIgnoreShadowText(boolean value)