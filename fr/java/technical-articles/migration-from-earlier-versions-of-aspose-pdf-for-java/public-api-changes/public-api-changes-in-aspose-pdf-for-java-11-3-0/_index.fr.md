---
title: Changements de l'API publique dans Aspose.PDF pour Java 11.3.0
type: docs
weight: 130
url: /java/public-api-changes-in-aspose-pdf-for-java-11-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Cette page répertorie les changements d'API publique introduits dans Aspose.PDF pour Java 11.3.0. Elle inclut non seulement les méthodes publiques nouvelles et obsolètes, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.PDF pour Java qui pourrait affecter le code existant. Tout comportement introduit qui pourrait être considéré comme une régression et modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}

**Changements dans la classe com.aspose.pdf.Annotation :**

Méthodes ajoutées :

- public boolean isUpdateAppearanceOnConvert()
- public void setUpdateAppearanceOnConvert(boolean value)

**Changements dans la classe com.aspose.pdf.BaseParagraph :**

Méthodes ajoutées :

- public int getZIndex()
- public void setZIndex(int)

**Changements dans la classe com.aspose.pdf.MemoryCleaner :**

Méthodes ajoutées :

- public void clearAllTempFiles()


**Changements dans la classe com.aspose.pdf.Page :**

Methods ajoutés :

- public byte[] asByteArray(com.aspose.pdf.devices.Resolution)

**Modifications dans la classe com.aspose.pdf.Table :**

Méthodes ajoutées :

- public com.aspose.pdf.Table getParentTable()
- public void setParentTable(com.aspose.pdf.Table)

**Modifications dans la classe com.aspose.pdf.TextSearchOptions :**

Méthodes ajoutées :

- public boolean isIgnoreShadowText()
- public void setIgnoreShadowText(boolean value)