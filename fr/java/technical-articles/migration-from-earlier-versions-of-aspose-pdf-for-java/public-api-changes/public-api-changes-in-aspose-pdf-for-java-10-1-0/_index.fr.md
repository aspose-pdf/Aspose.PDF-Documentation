---

title: Changements de l'API Publique dans Aspose.PDF pour Java 10.1.0  
type: docs  
weight: 100  
url: /java/public-api-changes-in-aspose-pdf-for-java-10-1-0/  
lastmod: "2022-01-27"  

---

{{% alert color="primary" %}}

Cette page répertorie les modifications de l'API publique introduites dans [Aspose.PDF pour Java 10.1.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry615512.aspx). Elle inclut non seulement les nouvelles méthodes publiques et celles devenues obsolètes, mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.PDF pour Java qui pourrait affecter le code existant. Tout comportement introduit qui pourrait être considéré comme une régression et qui modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}


**Changements de l'API Publique et Incompatibilités Rétroactives**

## Ajout de nouvelles classes d'exception :

- com.aspose.pdf.exceptions.UnsupportedFontTypeException
- com.aspose.pdf.exceptions.InvalidFormTypeOperationException
- com.aspose.pdf.exceptions.InvalidCgmFileFormatException

**com.aspose.pdf.facades.PdfViewer**

Méthodes ajoutées :

- public boolean getUseIntermidiateImage()  
- public void setUseIntermidiateImage(boolean value)

**com.aspose.pdf.XForm**

Méthode ajoutée :

- public void freeMemory()

**com.aspose.pdf.TextSearchOptions**

Méthodes ajoutées :

- public boolean getUseFontEngineEncoding()  
- public void setUseFontEngineEncoding(boolean value)

**com.aspose.pdf.TextEditOptions**

Méthodes ajoutées :

- public TextEditOptions(boolean allowLanguageTransformation)  
- public boolean getAllowLanguageTransformation()  
- public void setAllowLanguageTransformation(boolean value)

**com.aspose.pdf.Page**

Méthodes ajoutées :

- public void processParagraphs()  
- public void dispose()

**com.aspose.pdf.IDocument**

Méthodes ajoutées :

- public void processParagraphs();

**com.aspose.pdf.Document**

Méthodes ajoutées :

- public void processParagraphs();

**com.aspose.pdf.DocSaveOptions**

Méthodes ajoutées :

- public boolean getAddReturnToLineEnd()  
- public void setAddReturnToLineEnd(boolean value)

**com.aspose.pdf.HtmlDocumentTypeInternal - supprimé.**