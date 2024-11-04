---
title: Mudanças na API Pública no Aspose.PDF para Java 9.3.1
type: docs
weight: 60
url: /java/public-api-changes-in-aspose-pdf-for-java-9-3-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as mudanças na API pública introduzidas no **Aspose.PDF para Java 9.3.1.** Inclui não apenas novos métodos públicos e métodos obsoletos, mas também uma descrição de quaisquer mudanças no comportamento nos bastidores no Aspose.PDF para Java que podem afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e modifique o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}

## Os seguintes métodos foram internalizados:

com.aspose.pdf.DocumentInfo.setCreator(String)<p>
com.aspose.pdf.DocumentInfo.setProducer(String)<p>
com.aspose.pdf.FileParams.getEngineDict()

## As seguintes constantes depreciadas foram internalizadas, é necessário usar getters estáticos em vez disso:

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

## O seguinte campo é adicionado:

public static Rectangle com.aspose.pdf.Rectangle.getEmpty() - retorna retângulo vazio