---
title: Cambios en la API Pública en Aspose.PDF para Java 9.3.1
type: docs
weight: 60
url: /java/public-api-changes-in-aspose-pdf-for-java-9-3-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página enumera los cambios en la API pública introducidos en **Aspose.PDF para Java 9.3.1.** Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.PDF para Java que pueda afectar el código existente. Cualquier comportamiento introducido que podría verse como una regresión y modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}}

## Los siguientes métodos han sido internalizados:

com.aspose.pdf.DocumentInfo.setCreator(String)<p> 
com.aspose.pdf.DocumentInfo.setProducer(String)<p> 
com.aspose.pdf.FileParams.getEngineDict()

## Las siguientes constantes obsoletas han sido internalizadas, es necesario usar métodos estáticos en su lugar:

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

## Se ha añadido el siguiente campo:

public static Rectangle com.aspose.pdf.Rectangle.getEmpty() - devuelve rectángulo vacío