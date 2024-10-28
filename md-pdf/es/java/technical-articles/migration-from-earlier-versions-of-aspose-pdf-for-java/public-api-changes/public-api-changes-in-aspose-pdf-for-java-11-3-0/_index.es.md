---
title: Cambios en la API Pública en Aspose.PDF para Java 11.3.0
type: docs
weight: 130
url: /java/public-api-changes-in-aspose-pdf-for-java-11-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista los cambios en la API pública introducidos en Aspose.PDF para Java 11.3.0. Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.PDF para Java que pueda afectar el código existente. Cualquier comportamiento introducido que pueda ser visto como una regresión y modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}}

**Cambios en la clase com.aspose.pdf.Annotation:**

Métodos añadidos:

- public boolean isUpdateAppearanceOnConvert()
- public void setUpdateAppearanceOnConvert(boolean value)

**Cambios en la clase com.aspose.pdf.BaseParagraph:**

Métodos añadidos:

- public int getZIndex()
- public void setZIndex(int)

**Cambios en la clase com.aspose.pdf.MemoryCleaner:**

Métodos añadidos:

- public void clearAllTempFiles()


**Cambios en la clase com.aspose.pdf.Page:**

Methods added:

- public byte[] asByteArray(com.aspose.pdf.devices.Resolution)

**Cambios en la clase com.aspose.pdf.Table:**

Métodos añadidos:

- public com.aspose.pdf.Table getParentTable()
- public void setParentTable(com.aspose.pdf.Table)

**Cambios en la clase com.aspose.pdf.TextSearchOptions:**

Métodos añadidos:

- public boolean isIgnoreShadowText()
- public void setIgnoreShadowText(boolean value)