---
title: Copiere Câmp Interior și Exterior
type: docs
weight: 40
url: /es/java/copy-inner-and-outer-field/
description: Această secțiune explică cum să copiați câmpul interior și exterior folosind com.aspose.pdf.facades cu clasa FormEditor.
lastmod: "2021-06-05"
draft: false
---

Metoda [copyInnerField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) vă permite să copiați un câmp în același fișier, la aceleași coordonate, pe pagina specificată. Această metodă necesită numele câmpului pe care doriți să îl copiați, noul nume al câmpului și numărul paginii pe care trebuie să fie copiat câmpul. Clasa [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) oferă această metodă. Fragmentul de cod următor vă arată cum să copiați câmpul în aceeași locație în același fișier.

```java
    public static void CopyInnerField() {
        FormEditor editor = new FormEditor();
        Document document = new Document(_dataDir + "Sample-Form-01.pdf");
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyInnerField("Last Name", "Last Name 2", 2);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## Copierea unui Câmp Extern într-un Fișier PDF Existent

Metoda [copyOuterField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) îți permite să copiezi un câmp de formular dintr-un fișier PDF extern și apoi să-l adaugi în fișierul PDF de intrare la aceeași locație și numărul de pagină specificat. Această metodă necesită fișierul PDF din care trebuie copiat câmpul, numele câmpului și numărul paginii la care trebuie copiat câmpul. Această metodă este oferită de clasa [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). Fragmentul de cod următor îți arată cum să copiezi un câmp dintr-un fișier PDF extern.

```java
  public static void CopyOuterField() {
        FormEditor editor = new FormEditor();
        Document document = new Document();
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
        editor.save(_dataDir + "Sample-Form-02-mod.pdf");
    }
```