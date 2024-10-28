---
title: Changements de l'API Publique dans Aspose.PDF pour Java 9.3.1
type: docs
weight: 60
url: /java/public-api-changes-in-aspose-pdf-for-java-9-3-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Cette page liste les changements de l'API publique introduits dans **Aspose.PDF pour Java 9.3.1.** Elle inclut non seulement de nouvelles méthodes publiques et obsolètes, mais aussi une description de tout changement dans le comportement en coulisse dans Aspose.PDF pour Java qui peut affecter le code existant. Tout comportement introduit qui pourrait être vu comme une régression et modifie le comportement existant est particulièrement important et est documenté ici.

{{% /alert %}}

## Les méthodes suivantes ont été internalisées :

com.aspose.pdf.DocumentInfo.setCreator(String)<p>
com.aspose.pdf.DocumentInfo.setProducer(String)<p>
com.aspose.pdf.FileParams.getEngineDict()

## Les constantes dépréciées suivantes ont été internalisées, il est nécessaire d'utiliser les getters statiques à la place :

com.aspose.pdf.ImageFormatInternal.Bmp<p>
com.aspose.pdf.ImageFormatInternal.Emf<p>

com.aspose.pdf.ImageFormatInternal.Exif<p>
com.aspose.pdf.ImageFormatInternal.Gif<p>
com.aspose.pdf.ImageFormatInternal.Jpeg<p>
com.aspose.pdf.ImageFormatInternal.Icon<p>
com.aspose.pdf.ImageFormatInternal.MemoryBmp<p>
com.aspose.pdf.ImageFormatInternal.Png<p>
com.aspose.pdf.ImageFormatInternal.Tiff<p>
com.aspose.pdf.ImageFormatInternal.Wmf<p>
com.aspose.pdf.TextEncodingInternal.ASCII<p>
com.aspose.pdf.TextEncodingInternal.BigEndianUnicode<p>
com.aspose.pdf.TextEncodingInternal.Default<p>
com.aspose.pdf.TextEncodingInternal.Unicode<p>
com.aspose.pdf.TextEncodingInternal.UTF32<p>
com.aspose.pdf.TextEncodingInternal.UTF32BE<p>
com.aspose.pdf.TextEncodingInternal.UTF7<p>
com.aspose.pdf.TextEncodingInternal.UTF8<p>
com.aspose.pdf.TextEncodingInternal.UTF8Unmarked

## Le champ suivant est ajouté :

public static Rectangle com.aspose.pdf.Rectangle.getEmpty() - retourne un rectangle vide